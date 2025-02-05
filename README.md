# GitHub Profiles

## Descrição do Projeto

Este projeto, desenvolvido com Python e Flask, tem como objetivo demonstrar o consumo de APIs externas de forma eficiente e dinâmica. Através dele, é possível buscar informações detalhadas sobre usuários do GitHub, listar seus repositórios públicos e visualizar estatísticas como número de estrelas, forks e linguagens utilizadas. Além disso, a aplicação conta com uma interface simples e intuitiva, tornando a navegação fácil e acessível.

## Funcionalidades

- **Segurança e Autenticação**: A aplicação utiliza o fluxo de autenticação OAuth do GitHub, garantindo que as informações acessadas sejam seguras.
- **Busca de Usuários**: Permite que os usuários pesquisem perfis do GitHub pelo nome de usuário.
- **Exibição de Repositórios**: Lista os repositórios públicos do usuário pesquisado, incluindo detalhes como descrição, número de estrelas e forks.
- **Estatísticas de Repositórios**: Mostra informações sobre as linguagens utilizadas em cada repositório e o número total de commits.
- **Interface Intuitiva**: A aplicação possui uma interface amigável, facilitando a navegação e a interação do usuário.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do backend.
- **Flask**: Framework web para Python que facilita a criação de aplicações web.
- **Requests**: Biblioteca para fazer requisições HTTP, utilizada para interagir com a API do GitHub.
- **HTML/CSS**: Para a construção da interface do usuário.
- **Bootstrap**: Framework CSS para estilização e responsividade da aplicação.

## Estrutura do Projeto

```
/github_profiles
│
├── .git/              # Diretório do Git
├── .gitignore         # Arquivo para ignorar arquivos e pastas no Git
├── api.py             # Módulo para interagir com a API do GitHub
├── app.py             # Arquivo principal da aplicação Flask
├── requirements.txt   # Dependências do projeto
├── routes.py          # Definição das rotas da aplicação
├── static/            # Arquivos estáticos (CSS, JS, imagens)
│   ├── favicon.ico
│   ├── script.js
│   └── style.css
└── templates/         # Templates HTML
    ├── error.html
    ├── index.html
    ├── layout.html
    ├── profile.html
    ├── results.html
    └── search.html
```

## Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/ianfelps/github_profiles.git
   ```

2. **Instale as dependências**: Certifique-se de ter o `Python` e o `pip` instalados. Em seguida, execute:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as variáveis de ambiente**: Crie um arquivo `.env` na raiz do projeto e adicione suas credenciais do GitHub:
   ```
   SECRET_KEY=sua_secret_key
   GITHUB_CLIENT_ID=sua_client_id
   GITHUB_CLIENT_SECRET=sua_client_secret
   ```

4. **Execute a aplicação**:
   ```bash
   python app.py
   ```

5. **Acesse a aplicação**: Abra o navegador e vá para `http://localhost:5000`.

## Link do Deploy

A aplicação está disponível online e pode ser acessada através do seguinte link:  
[GitHub Profiles](https://ianfelps.pythonanywhere.com)

## Conclusão

O projeto "GitHub Profiles" é uma aplicação web desenvolvida com Python e Flask, que demonstra de forma prática e eficiente como consumir APIs externas, especificamente a API do GitHub. Através de uma interface intuitiva, os usuários podem buscar informações detalhadas sobre perfis do GitHub, explorar repositórios públicos e visualizar estatísticas relevantes, como o número de estrelas, forks e linguagens utilizadas em cada repositório.