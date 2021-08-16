git init
git add .
git commit -m "project setup commit"
git checkout -b "dev"


{% if cookiecutter.conda_env_install == "yes" %}

conda env create -f ../{{cookiecutter.project_slug}}/envs/environment.yml -n {{cookiecutter.conda_env_name}}

{% endif %}
