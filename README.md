
# Basic structure for a new Python project

This repository holds my preferred structure for new python projects. Sample environments are contained in .envs

. The top-level directory can contain READMEs, Configs and the like. 
./scripts or ./bin is for command-line interface stuff 
./sample_module is for a python module 
./sample_module/tests for your module tests 
./envs for environment definitions
./doc for documentation  


All this should be placed in a top level folder my_new_project (or whatever the project should be called). Another project's PYTHONPATH, then, can include /path/to/my_new_project/sample_module to reuse the my_new_project.sample_module module.


