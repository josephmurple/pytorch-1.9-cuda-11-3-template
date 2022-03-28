#!/usr/bin/env bash

PORT=${PORT:-8888}

{%- if cookiecutter.use_nvidia_gpu == 'no' %}
docker run -it --ipc=host -p $PORT:$PORT -p 5000:5000 -v $PWD:/workspace/{{cookiecutter.project_slug}}/ {{cookiecutter.project_slug}}:latest bash
{%- else -%}
docker run --gpus=all -it -e CUDA_VISIBLE_DEVICES --ipc=host -p $PORT:$PORT -p 5000:5000 -v $PWD:/workspace/{{cookiecutter.project_slug}}/ {{cookiecutter.project_slug}}:latest bash
{%- endif %}
