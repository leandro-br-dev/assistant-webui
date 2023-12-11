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