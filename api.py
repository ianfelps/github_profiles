import requests

GITHUB_API_URL = "https://api.github.com"

# dados do usuário pelo username
def get_user_data(username, token):
    headers = {"Authorization": f"token {token}"}
    response = requests.get(f"{GITHUB_API_URL}/users/{username}", headers=headers)
    return response.json() if response.status_code == 200 else None

# repositórios públicos do usuário
def get_repos(username, token):
    headers = {"Authorization": f"token {token}"}
    response = requests.get(f"{GITHUB_API_URL}/users/{username}/repos", headers=headers)
    return response.json() if response.status_code == 200 else []


# linguagens usadas em um repositórios
def get_repo_languages(username, repo_name, token):
    headers = {"Authorization": f"token {token}"}
    response = requests.get(f"{GITHUB_API_URL}/repos/{username}/{repo_name}/languages", headers=headers)
    return list(response.json().keys()) if response.status_code == 200 else []

# número total de commits de um repositório
def get_total_commits(username, repo_name, token):
    headers = {"Authorization": f"token {token}"}
    response = requests.get(f"{GITHUB_API_URL}/repos/{username}/{repo_name}/commits", headers=headers)
    return len(response.json()) if response.status_code == 200 else "N/A"

# número total de commits do usuário somando todos os repositórios pessoais
def get_user_total_commits(username, token):
    repos = get_repos(username, token)
    if not repos:
        return 0

    total_commits = 0
    for repo in repos:
        total_commits += get_total_commits(username, repo["name"], token)
    return total_commits