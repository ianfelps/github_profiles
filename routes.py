from flask import render_template, request, redirect, request, session, url_for, jsonify
import requests

from app import *
import api

# rota padrão
@app.route("/")
def home():
    return render_template("index.html")

# rota para eedirecionar para autenticação do github
@app.route("/login")
def login():
    github_auth_url = f"https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}&scope=user repo"
    return redirect(github_auth_url)

# rota para callback do github
@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return render_template("error.html", error="Erro ao autenticar!")

    # Troca o código pelo token de acesso
    token_url = "https://github.com/login/oauth/access_token"
    token_data = {
        "client_id": GITHUB_CLIENT_ID,
        "client_secret": GITHUB_CLIENT_SECRET,
        "code": code
    }
    headers = {"Accept": "application/json"}
    token_response = requests.post(token_url, data=token_data, headers=headers)
    token_json = token_response.json()

    if "access_token" not in token_json:
        return render_template("error.html", error="Erro ao obter token!")

    session["github_token"] = token_json["access_token"]
    return redirect(url_for("search"))

# rota para pesquisar por usario
@app.route("/search", methods=["GET", "POST"])
def search():
    token = session.get("github_token")
    if not token:
        return redirect(url_for("home"))

    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            return render_template("error.html", error="Digite um nome de usuário!")

        # buscar dados do usuário
        user_data = api.get_user_data(username, token)
        if not user_data:
            return render_template("error.html", error="Usuário não encontrado!")

        # buscar repositórios do usuário (se não houver, retorna lista vazia)
        repos_data = api.get_repos(username, token)

        # verifica se o usuário tem repositórios
        if not repos_data:
            return render_template("results.html", user=user_data, repos=[], total_commits=0)

        # adicionar linguagens e commits a cada repositório
        for repo in repos_data:
            repo["languages"] = api.get_repo_languages(username, repo["name"], token)
            repo["commits_count"] = api.get_total_commits(username, repo["name"], token)

        # calcular total de commits do usuário
        total_commits = api.get_user_total_commits(username, token)

        return render_template("results.html", user=user_data, repos=repos_data, total_commits=total_commits)

    return render_template("search.html")


# logout
@app.route("/logout")
def logout():
    session.pop("github_token", None)
    return redirect(url_for("home"))
