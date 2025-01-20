# Passo a passo de como utilizar

# Inicializar o ambiente virtual
1. make enable_venv

# Habilita o ambiente virtual
1. source .venv/bin/activate

# Instala as dependencias
1. make install

# Inicializar MLFlow, Minio e Postgres
1. make up_docker

# Criar o bucket de nome mlflow e a chave de acesso no minio
## copiar a chave nas variaveis: MINIO_ACCESS_KEY, AWS_ACCESS_KEY_ID, MINIO_SECRET_ACCESS_KEY, AWS_SECRET_ACCESS_KEY


# Editar o arquivo .env as variaveis FLASK_MODEL_NAME, FLASK_MODEL_VER
## As variaveis contem o nome e versão do modelo registrado

# Editar arquivo potability.ipynb para criar os modelos

# Deletar recursos do Docker (Opcional)
1. make clean_docker
