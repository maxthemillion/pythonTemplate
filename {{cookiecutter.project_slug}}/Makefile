install:
    conda env create -f environment.yml

clean:
    rm -rf __pycache__ .pytest_cache

flake:
    flake8 .

black: 
    black .

docker_build:
    docker build -t {{cookiecutter.project_slug}} .

docker_run:
    docker run --rm --mount type=bind,source=$(PWD),target=/src -p {{cookiecutter.jupyter_port}}:{{cookiecutter.jupyter_port}} {{cookiecutter.project_slug}}

test:
    pytest -q