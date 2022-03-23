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

    $ pip install "cookiecutter>=1.7.0"

Now run it against this repo:

    $ cookiecutter https://github.com/josephmurple/pytorch-1.9-cuda-11-3-template

You'll be prompted for some values. Provide them, then a Pytorch project will be created for you.

    project_name [Template Project]: mypytorch
    project_slug [mypytorch]:
    Select open_source_license:
    1 - MIT license
    2 - ISC license
    3 - Apache Software License 2.0
    4 - GNU General Public License v3
    5 - Not open source
    Choose from 1, 2, 3, 4, 5 [1]: 5
    author_name [contact]: joseph.suh
    email [joseph.suh@murple.ai]:
    Select package_management:
    1 - pip
    2 - poetry
    Choose from 1, 2 [1]: 1
    [getcwd]: /home/xuhu357/mypytorch
    [file to delete]: /home/xuhu357/mypytorch/pyproject.toml
    Done!! Now, you can develop your own Pytorch project!!

Enter the project and take a look around:

    $ cd mypytorch/
    $ ls

You can use shell scripts under ./script folder. Make sure docker is pre-installed on your machine!

    # For build the docker images
    $ bash scripts/build.sh

    # For interact with docker, using cpu is default option, if gpus are available, you can modify the file: ./scripts/interactive.sh
    $ bash scripts/interactive.sh

Then you will see that the Dev Environment is ready for you!

    $ root@e4882be8e567:/workspace/mypytorch# 

Thank you!


