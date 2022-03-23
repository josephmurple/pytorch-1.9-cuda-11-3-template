#!/usr/bin/env bash

PORT=${PORT:-8888}

# if gpu not available
docker run -it --rm --ipc=host -p $PORT:$PORT -v $PWD:/workspace/{{cookiecutter.project_slug}}/ {{cookiecutter.project_slug}}:latest bash

# if gpu available
#docker run --gpus device=0 -it --rm --ipc=host -p $PORT:$PORT -v $PWD:/workspace/{{cookiecutter.project_slug}}/ {{cookiecutter.project_slug}}:latest bash
