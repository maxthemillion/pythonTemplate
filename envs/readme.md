# Environment Templates
These environments are boilerplates to be extended by what I may use in a specific case.

**Standard environment** Installs the most basic environment for data analytics.
**Jupyter environment:** Installs jupyter lab and the nb_conda_kernels extension so that we can load any installed conda environment as a kernel. Jupyter lab is only included in the jupyter environment but you should be able to load every installed environemnt as a kernel when starting jupyter from the Jupyter environment.
**Data Analytics environment:** Installs the packages that I personally use most often for data analytics.

# Installing 

> conda env create --name envname --file=environments.yml

# Exporting
 
> conda env export > environment.yml