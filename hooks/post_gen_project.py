
import sys, tempfile, os
from subprocess import call

if __name__ == "__main__":
    
    if "{{ cookiecutter.create_conda_env }}" == "yes":
        EDITOR = os.environ.get('EDITOR','vim')

        with open("./environment.yml", 'rb') as f: 
            initial_message = f.read()

        with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
            tf.write(initial_message)
            tf.flush()
            call([EDITOR, tf.name])

            # do the parsing with `tf` using regular File operations.
            # for instance:
            tf.seek(0)
            edited_message = tf.read()

        os.system(
            "conda env create "
            "--file environment.yml "
            "--name {{ cookiecutter.conda_env_name }}"
            "--prefix ./.env"
        )
        os.system("conda run -n {{ cookiecutter.conda_env_name }} pre-commit install ")

    if "{{ cookiecutter.init_git_repo }}" == "yes":
        os.system("git init")
        os.system("git add .")
        os.system("git commit -a -m 'initial commit'")
        os.system("git checkout -b dev")