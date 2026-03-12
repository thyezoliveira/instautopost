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

