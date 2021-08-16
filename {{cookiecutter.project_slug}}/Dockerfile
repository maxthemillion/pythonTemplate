FROM continuumio/miniconda3

RUN apt-get update && apt-get install -y git

RUN mkdir /temp
COPY ./envs /temp
    
RUN conda env update --name base --file /temp/envs/environment.yml


