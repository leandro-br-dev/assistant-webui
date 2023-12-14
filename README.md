# assistant-webui


#---------------- LINHAS DE COMANDO IMPORTANTES -----------------#


<!-- Ativa o ambiênte virtual -->
# & C:\IA\assistant-webui\dev\venv\Scripts\Activate.ps1

<!-- Inicia o servidor Web -->
# python .\run.py

<!-- Inicia o servidor Postgres -->
# C:\IA\assistant-webui\dev\scripts\start_postgres.bat

<!-- Procedimentos para migração de estrutura de dados -->
# flask db init
# $env:FLASK_CLI_COMMAND="migrate" ; flask db migrate -m "Criação da tabela de usuários"
# $env:FLASK_CLI_COMMAND="migrate" ; flask db upgrade




<!-- Executa os testes unitários com configurações customizadas -->
# python .\run_tests.py

<!-- Executa o commit da última versão do banco de dados de PRODUÇÃO -->
# alembic -c alembic.ini revision --autogenerate -m "Descricao"

<!-- Executa o build do banco de dados de PRODUÇÃO -->
# alembic -c alembic.ini upgrade head

<!-- Executa o commit da última versão do banco de dados de TESTE -->
# alembic -c alembic_test.ini revision --autogenerate -m "Descricao"

<!-- Executa o build do banco de dados de TESTE -->
# alembic -c alembic_test.ini upgrade head

<!-- Executa a compilação dos códigos transcrevendo em um arquivo compile_code.txt -->
# python compile_code.py

<!-- Executa a construção da documentação em formato WEB -->
# .\make html

#---------------- CONFIGURAÇÕES NECESSÁRIAS -----------------#

<!-- DECLARAÇÃO DE VARIÁVEIS GLOBAIS .env -->

# Ambiente do servidor de dados
DB_SERVER=

# Configurações usuário administrador do Banco
DB_ADM_USER=
DB_ADM_PASSWORD=

# Configurações para Migração
DB_MIGRATION_USER=
DB_MIGRATION_PASSWORD=

# Configurações para Consumo da API
DB_API_USER=
DB_API_PASSWORD=

# Configurações para Desenvolvimento
SQLALCHEMY_DATABASE_URI_DEV=db_assistant_dev

# Configurações para Produção
SQLALCHEMY_DATABASE_PROD=db_assistant_prod

# Configurações FLASK
FLASK_APP=run.py
FLASK_ENV=development

# Credenciais do GOOGLE
GOOGLE_API_KEY=

# Chave de autenticação GOOGLE
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_REDIRECT_URI=

<!---------------------------------------------------------->