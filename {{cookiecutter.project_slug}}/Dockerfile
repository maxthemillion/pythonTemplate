FROM continuumio/miniconda3
LABEL version="0.1"
LABEL description="This image provides a development environment for the current project"
EXPOSE 9999

RUN apt-get update && apt-get install -y git

RUN mkdir /temp
COPY environment.yml /temp
    
RUN conda env update --name base --file /temp/environment.yml

{% if cookiecutter.use_R == 'yes' %}

RUN apt install -y r-base
RUN R -e "install.packages('IRkernel')"
RUN R -e "IRkernel::installspec()"

{% endif %}

WORKDIR /src/notebooks
CMD jupyter lab --ip 0.0.0.0 --port 9999 --allow-root --no-browser --NotebookApp.token='' --NotebookApp.password=''
