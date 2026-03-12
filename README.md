# InstAPI 📸

Automação inteligente para Instagram utilizando a biblioteca `instagrapi`. O foco deste projeto é fornecer uma interface modular e segura para gerenciar perfis do Instagram, simulando o comportamento humano e dispositivos reais para evitar detecção de bots.

## 🚀 Funcionalidades Atuais

- **Autenticação Segura:**
  - Suporte a login com usuário e senha.
  - Integração com **2FA (Autenticação de Dois Fatores)** via TOTP.
  - Persistência de sessão em arquivo JSON para evitar logins repetitivos.
- **Simulação de Dispositivo:** Configuração de User-Agent e hardware para emular um dispositivo Android real (Samsung S8).
- **Listagem de Posts:** 
  - Recupera os últimos 20 posts do perfil conectado.
  - Exibe ID, data de criação e legenda formatada no terminal.
  - **Medidas Anti-Bot:** Implementação de delays aleatórios entre as requisições.

## 🛠️ Tecnologias Utilizadas

- **Python 3.13+**
- **[instagrapi](https://github.com/adw0rd/instagrapi):** Biblioteca base para interação com a API privada do Instagram.
- **[uv](https://github.com/astral-sh/uv):** Gerenciador de pacotes e ambientes Python ultrarrápido.
- **python-dotenv:** Gerenciamento de variáveis de ambiente.
- **pyotp:** Geração de códigos 2FA.

## 📋 Pré-requisitos

Certifique-se de ter o `uv` instalado em sua máquina. Se não tiver, instale com:
```bash
curl -LsSf https://astral-sh/uv/install.sh | sh
```

## ⚙️ Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/thyezoliveira/instautopost.git
   cd instautopost
   ```

2. Crie o arquivo `.env` baseado no exemplo:
   ```bash
   cp .env.example .env
   ```

3. Preencha as suas credenciais no `.env`:
   - `IG_USERNAME`: Seu usuário do Instagram.
   - `IG_PASSWORD`: Sua senha.
   - `TOTP_KEY`: A chave secreta do seu autenticador 2FA.

## 🏃 Como Rodar

Para executar o script de listagem de posts:
```bash
uv run main.py
```

## 📂 Estrutura do Projeto

- `main.py`: Ponto de entrada que orquestra o fluxo de login e execução de comandos.
- `auth.py`: Módulo responsável pela lógica de autenticação e simulação de dispositivo.
- `controller.py`: Módulo que contém as funcionalidades de negócio (ex: listagem de posts).
- `docs/plano.md`: Documentação conceitual e planejamento de features.

## ⚠️ Aviso Legal

Este projeto é apenas para fins educacionais. O uso de automação no Instagram pode violar os Termos de Serviço da plataforma. Use com moderação e por sua conta e risco.
