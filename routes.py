from flask import render_template, request, redirect, request, session, url_for, jsonify
import requests

from app import *

# @app.route("/", methods=["GET", "POST"])
# def homePage():
#     if request.method == "POST":
#         return render_template("profile.html", username=request.form.get("username"))
#     else:
#         return render_template("index.html")
    
@app.route("/")
def home():
    return render_template("index.html")

# Redireciona para o GitHub para autenticação
@app.route("/login")
def login():
    github_auth_url = f"https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}&scope=user repo"
    return redirect(github_auth_url)

# Callback do GitHub (onde receberemos o token)
@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return render_template("callback.html", error="Erro ao autenticar!")

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
        return render_template("callback.html", error="Erro ao obter token!")

    session["github_token"] = token_json["access_token"]
    return redirect(url_for("profile"))

# Pega informações do usuário autenticado
@app.route("/profile")
def profile():
    token = session.get("github_token")
    if not token:
        return redirect(url_for("login"))

    headers = {"Authorization": f"token {token}"}
    user_response = requests.get("https://api.github.com/user", headers=headers)
    user_data = user_response.json()

    return jsonify(user_data)  # Retorna os dados do usuário como JSON

# Logout
@app.route("/logout")
def logout():
    session.pop("github_token", None)
    return redirect(url_for("home"))
