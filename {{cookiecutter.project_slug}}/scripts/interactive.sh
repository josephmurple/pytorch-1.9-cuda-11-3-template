#!/usr/bin/env bash

PORT=${PORT:-8888}

# if gpu not available
docker run -it --rm --ipc=host -p $PORT:$PORT -v $PWD:/workspace/{{cookiecutter.project_slug}}/ {{cookiecutter.project_slug}}:latest bash

# if gpu available
#docker run --gpus=all -it --rm -e CUDA_VISIBLE_DEVICES --ipc=host -p $PORT:$PORT -v $PWD:/workspace/{{cookiecutter.project_slug}}/ {{cookiecutter.project_slug}}:latest bash
