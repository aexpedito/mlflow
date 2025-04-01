help:
	@echo "Help to use"

clean_docker:
	@docker-compose down
	@docker container prune
	@docker image prune -a

build: #build first time api image in local docker
	@docker-compose -f docker-compose.yaml --env-file myenv.env up --build

up:
	@docker-compose -f docker-compose.yaml --env-file myenv.env up

down:
	@docker-compose down

enable_venv:  #make sure python 3.12, python-pip and python3-venv are installed in current machine
	@rm -rf .venv/
	@python3 -m venv .venv/

install: #enable virtualenv before make install: source .venv/bin/activate
	@python -m pip install -q poetry==1.8.5
	@poetry install

quality:
	@poetry run pre-commit run --all-files
