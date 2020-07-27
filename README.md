# Humanised Jobnames

A small python library and command line wrapper to create humanised jobnames

## Example - command line

    ./bin/humanised-jobname.py 
    flaky-mogadishu

    ./bin/humanised-jobname.py 
    voiceless-damascus

## Example - flask

    FLASK_APP=bin/humanised-flask.py flask run

    curl http://127.0.0.1:5000/
    lively-taipei

## Docker container

This container can be built locally with this repository or pulled
from [Dockerhub](https://hub.docker.com/repository/docker/deanwilson/humanised-jobnames)

    docker build -t deanwilson/humanised-jobnames .

    docker run -p 5555:5000 deanwilson/humanised-jobnames

The Alpine image, built from the main [Dockerfile](/Dockerfile), is
107MB while the full Python image is 971MB.

