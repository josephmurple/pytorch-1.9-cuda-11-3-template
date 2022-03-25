# Cookiecutter Pytorch-1.9-CUDA-11.3-Template

## Features
- For Pytorch 1.9
- Works with Python 3.8
- CUDA_VERSION=11.3.0.016
- CUDNN_VERSION=8.2.0.51
- Jupyter Notebook
- Etc


## Usage

First, install requirements:

    $ pip install -r requirements/requirements.txt

Enter the project and take a look around:

    $ cd mypytorch/
    $ ls

Then, execute shell script under ./script folder. Make sure [pre-requisites](<https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#pre-requisites>) is pre-installed on your machine!

    # To build the docker images
    $ bash scripts/build.sh

    # To interact with docker
    $ bash scripts/interactive.sh

Then you will see that the Dev Environment is ready for you!

    $ root@e4882be8e567:/workspace/mypytorch# 

Thank you!


