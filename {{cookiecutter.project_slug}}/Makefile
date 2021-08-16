install:
    conda env create -f envs/environment.yml

clean:
    rm -rf __pycache__ .pytest_cache

flake:
    flake8 .

black: 
    black .

docker_build:
    docker build -t {{cookiecutter.project_slug}} .

docker_run:
    docker run --rm --mount type=bind,source=$(PWD),target=/src -p 9999:9999 {{cookiecutter.project_slug}}