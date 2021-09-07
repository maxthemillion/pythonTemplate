
import os

if __name__ == "__main__":
    
    if "{{ cookiecutter.create_conda_env }}" == "yes":
        os.system(
            "conda env create "
            "--file environment.yml "
            "--name {{ cookiecutter.conda_env_name }}"
        )

        os.system("conda activate {{ cookiecutter.conda_env_name }} & deon -o ETHICS.md")

    if "{{ cookiecutter.init_git_repo }}" == "yes":
        os.system("git init & git commit -a -m 'initial commit'")