import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')

    # Configurações para Consumo da API
    DB_SERVER = os.getenv('DB_SERVER')

    if os.getenv('FLASK_CLI_COMMAND') == 'migrate':
        DB_USER = os.getenv('DB_MIGRATION_USER')
        DB_PASSWORD = os.getenv('DB_MIGRATION_PASSWORD')
    else:
        DB_USER = os.getenv('DB_API_USER')
        DB_PASSWORD = os.getenv('DB_API_PASSWORD')

    if FLASK_ENV == 'development':
        DB_DATA_BASE = 'db_assistant_dev'
    else:
        DB_DATA_BASE = 'db_assistant_prod'   

    
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:5432/{DB_DATA_BASE}'  
    SQLALCHEMY_TRACK_MODIFICATIONS = False

