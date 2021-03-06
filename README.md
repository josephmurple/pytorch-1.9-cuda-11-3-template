# Cookiecutter Pytorch-1.9-CUDA-11.3-Template

## Features
- For Pytorch 1.9
- Works with Python 3.8
- CUDA_VERSION=11.3.0.016
- CUDNN_VERSION=8.2.0.51
- Jupyter Notebook
- Etc


## Usage
Let's pretend you want to create a Pytorch project called "mypytorch". Rather than using `Template Project`
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get [cookiecutter](https://github.com/cookiecutter/cookiecutter) to do all the work.

First, get Cookiecutter. Trust me, it's awesome:

    $ pip install -r requirements_template.txt

Now run it against this repo:

    $ cookiecutter https://github.com/josephmurple/pytorch-1.9-cuda-11-3-template

You'll be prompted for some values. Provide them, then a Pytorch project will be created for you.

    project_name [Template Project]: mypytorch
    project_slug [mypytorch]:
    author_name [joseph.suh]:
    email [joseph.suh@murple.ai]:
    Select package_management:
    1 - pip
    2 - poetry
    Choose from 1, 2 [1]: 1
    Select use_nvidia_gpu:
    1 - no
    2 - yes
    Choose from 1, 2 [1]: 1
    [getcwd]: /home/xuhu357/mypytorch
    [file to delete]: /home/xuhu357/mypytorch/pyproject.toml
    Done!! Now, you can develop your own Pytorch project!!

Enter the project and take a look around:

    $ cd mypytorch/
    $ ls

You can use shell scripts under ./script folder. Make sure [pre-requisites](<https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#pre-requisites>) is pre-installed on your machine!

    # To build the docker images
    $ bash scripts/build.sh

    # To interact with docker
    $ bash scripts/interactive.sh

Then you will see that the Dev Environment is ready for you!

    $ root@e4882be8e567:/workspace/mypytorch# 

Thank you!


