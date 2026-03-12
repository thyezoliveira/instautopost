# instAutopost 📸

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
- **Postagem Automática (Feed e Carrossel):**
  - Realiza uploads baseados em pastas organizadas por data (`content/YYYY-MM-DD`).
  - Suporte a post único (1 imagem) ou carrossel (múltiplas imagens).
  - Leitura automática de legenda do arquivo `caption.txt`.
- **Medidas Anti-Bot:** Implementação de delays aleatórios e simulação de dispositivo em todas as interações.

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

3. Preencha as suas credenciais no `.env`.

## 🏃 Como Rodar
## 🏃 Como Rodar

### Modo Manual (Execução Única)
Para postar o conteúdo da pasta do dia atual uma única vez:
```bash
uv run python main.py
```

Para listar seus posts recentes:
```bash
uv run python main.py --list
```

### Modo Automação (Loop Contínuo)
O script verificará a cada **1 hora** se existe conteúdo para o dia atual. Se encontrar e ainda não tiver postado (verificado via `posted_dates.json`), ele realizará o upload automaticamente:
```bash
uv run python main.py --loop
```

## ⚙️ Configuração do Servidor (Systemd)

Para manter o bot rodando 24/7 em um servidor Linux, utilize o arquivo de serviço incluso:

1. **Copie o arquivo de serviço:**
   ```bash
   sudo cp systemd/instapi.service /etc/systemd/system/
   ```

2. **Ative e inicie o serviço:**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable instapi.service
   sudo systemctl start instapi.service
   ```

3. **Monitore a execução:**
   - **Logs do Arquivo:** `tail -f instapi.log`
   - **Status do Systemd:** `systemctl status instapi.service`
   - **Logs do Systemd:** `journalctl -u instapi -f`

## 📂 Estrutura do Projeto


- `main.py`: Ponto de entrada que orquestra o fluxo de login e execução de comandos.
- `auth.py`: Módulo responsável pela lógica de autenticação e simulação de dispositivo.
- `controller.py`: Módulo que contém as funcionalidades de negócio (listagem e postagem).
- `docs/plano.md`: Documentação conceitual e planejamento de features.

## ⚠️ Aviso Legal

Este projeto é apenas para fins educacionais. O uso de automação no Instagram pode violar os Termos de Serviço da plataforma. Use com moderação e por sua conta e risco.
