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


# Exemplo de chamada de API
POST: http://localhost:8081/predict
{
  "numeric__ph": "0.433417",
	"numeric__Hardness": "2.001473",
	"numeric__Solids": "0.530563",
	"numeric__Chloramines": "1.067017",
	"numeric__Sulfate": "1.772637",
	"numeric__Conductivity": "-0.556168",
	"numeric__Organic_carbon": "0.181255",
	"numeric__Trihalomethanes": "-0.456707",
	"numeric__Turbidity": "-0.271335"
}

# Link para o repositório
https://github.com/aexpedito/mlflow
