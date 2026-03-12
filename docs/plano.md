# Plano de Operação

O script principal (`main.py`) utiliza a biblioteca `instagrapi` para automatizar o acesso a uma conta do Instagram de forma segura.

- **Configurações:** Utiliza um arquivo `.env` para armazenar de forma segura o usuário, a senha e outras chaves de acesso.
- **Acesso Automatizado:** Realiza o login utilizando os dados configurados.
- **Segurança (2FA):** Gera automaticamente o código de verificação de duas etapas para concluir a entrada.
- **Persistência:** Salva a sessão atual em um arquivo local para que os próximos acessos sejam mais rápidos e não exijam login manual novamente.

## Funcionalidades Planejadas

### 1. Listagem de Posts do Usuário
Recupera e exibe no terminal as publicações da conta conectada.
- **Dados extraídos:** Identificação única (ID), legenda (label) e data de criação.
- **Segurança e Simulação Humana:**
    - **Identidade de Dispositivo:** Configuração de "User Agent" e detalhes de hardware para simular um celular real.
    - **Pausas Estratégicas (Delays):** Intervalos aleatórios entre requisições para evitar padrões robóticos.
    - **Tratamento de Erros:** Monitoramento de bloqueios temporários e desafios (checkpoints) do Instagram, com interrupção segura ou reativação inteligente para evitar banimentos.

### 2. Postagem Automática (Feed e Carrossel)
Automatiza o upload de conteúdos a partir de uma estrutura de arquivos organizada.
- **Estrutura de Arquivos:**
    - Pasta raiz `content/` contendo subpastas nomeadas com a data da postagem (ex: `2026-03-12/`).
    - **Post Único:** Uma imagem dentro da pasta da data.
    - **Carrossel:** Múltiplas imagens dentro da mesma pasta de data.
    - **Legenda:** Arquivo `caption.txt` na pasta com o texto e hashtags.
- **Configurações de Mídia:**
    - Suporte a diferentes proporções (Quadrado 1:1 ou Retangular/Portrait 4:5).
    - Redimensionamento automático se necessário para cumprir requisitos do Instagram.
- **Fluxo de Operação:**
    - O script identifica a pasta do dia atual, valida os arquivos e realiza o upload seguindo a ordem alfabética das imagens para carrosséis.
    - Mantém os mesmos padrões de **Segurança e Simulação Humana** (delays e User-Agent) aplicados na listagem.

### 3. Automação e Servidor (Systemd)
Configuração para execução contínua em um servidor Linux, garantindo que o script verifique e realize postagens de forma autônoma.
- **Loop de Verificação:** O script operará em um loop com intervalo de **1 hora**.
- **Lógica de Postagem Diária:**
    - A cada hora, o script verifica se existe uma pasta correspondente à data atual (`content/YYYY-MM-DD/`).
    - Implementação de um controle de estado (ex: `posted_dates.json`) para garantir que a postagem seja feita apenas uma vez por dia.
    - Caso exista conteúdo para o dia e a postagem ainda não tenha sido realizada, o fluxo de upload é disparado.
- **Serviço do Sistema (Daemon):** Utilização de uma unidade do **systemd** (`instapi.service`) para:
    - **Persistência:** Inicialização automática junto com o servidor.
    - **Resiliência:** Reinicialização automática em caso de falhas críticas.
    - **Logs:** Monitoramento centralizado de saídas e erros via `journalctl -u instapi`.
- **Ambiente Isolado:** Execução garantida dentro do ambiente virtual (`.venv`) gerenciado pelo `uv`.



