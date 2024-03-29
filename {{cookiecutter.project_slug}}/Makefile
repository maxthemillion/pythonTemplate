.PHONY: install clean flake black docker_build docker_run test

help:
	@echo "install		installs conda environment as specified in environment.yml"
	@echo "install_dev	installs the module {{cookiecutter.module_slug}} into the current environment"
	@echo "clean		removes python artifacts such as __pycache__ files"
	@echo "flake		runs flake8 on the working directory to check for code style violations"
	@echo "black		runs code formatter black on the working directory"
	@echo "d_build		builds docker image as specified in Dockerfile"
	@echo "d_run		runs docker container, mounts cwd and forwards configured ports to jupyter lab"
	@echo "test		runs pytest"
	@echo "datasette	converts all csv files in ./data to a sqlite.db and hosts it with datasette"

install:
	conda env create -f environment.yml

dev_install:
	conda develop .

clean:
	rm -rf __pycache__ .pytest_cache

flake:
	flake8 .

black: 
	black .

d_build:
	docker build -t {{cookiecutter.project_slug}} .

d_run:
	docker run --rm --mount type=bind,source=$(PWD),target=/src -p {{cookiecutter.jupyter_port}}:{{cookiecutter.jupyter_port}} {{cookiecutter.project_slug}}

test:
	pytest -q

datasette:
	csvs-to-sqlite ./data ./data/sqlite.db
	datasette ./data/sqlite.db