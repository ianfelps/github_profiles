from flask import render_template, request, redirect, request, session, url_for, jsonify
import requests

from app import *

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
        return redirect(url_for("login"))

    headers = {"Authorization": f"token {token}"}

    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            return render_template("error.html", error="Digite um nome de usuário!")

        # buscar dados do usuário
        user_response = requests.get(f"https://api.github.com/users/{username}", headers=headers)
        if user_response.status_code != 200:
            return render_template("error.html", error="Usuário não encontrado!")

        user_data = user_response.json()

        # buscar repositórios do usuário
        repos_response = requests.get(f"https://api.github.com/users/{username}/repos", headers=headers)
        if repos_response.status_code != 200:
            return render_template("error.html", error="Não foi possível obter os repositórios!")

        repos_data = repos_response.json()

        # buscar linguagens dos repositórios
        for repo in repos_data:
            lang_response = requests.get(f"https://api.github.com/repos/{username}/{repo['name']}/languages", headers=headers)
            if lang_response.status_code == 200:
                repo["languages"] = list(lang_response.json().keys())  # Lista de linguagens
            else:
                repo["languages"] = []

        return render_template("results.html", user=user_data, repos=repos_data)

    return render_template("search.html")

# Logout
@app.route("/logout")
def logout():
    session.pop("github_token", None)
    return redirect(url_for("home"))
