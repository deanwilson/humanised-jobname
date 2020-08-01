# Humanised Jobnames

A python library and tools to create memorable, human friendly, job names.

## Introduction

Which pair of identifiers are easier to remember?

  * d9a911d0-d0a6-11ea-b16d-38baf832cdcd and e7930804-d0a6-11ea-9ed1-00000000000c

Or

  * wry-warsaw and puzzled-lobamba

This project provides a simple library to generate small, human-
friendly, not guaranteed to be unique, job names that will let you
replace the first example with the second one to make remembering which
task you were debugging a little easier. I currently have an internal
instance of this running inside a docker container and use the different
data sources to ensure my scheduled jobs have more friendly,
recognisable at a glance, names.

This project was inspired by Dockers random container naming.

## Example - command line

    ./bin/humanised-jobname.py 
    flaky-mogadishu

    ./bin/humanised-jobname.py 
    voiceless-damascus

## Example - flask

    FLASK_APP=humanisedflask.py flask run

    curl http://127.0.0.1:5000/
    lively-taipei

    # a full test overriding all the defaults
    curl 'http://127.0.0.1:5000/?separator=^^^&adjectives=data/capital-cities.yaml&right=data/adjectives.yaml'

    # view prometheus compatible metrics
    curl http://127.0.0.1:5000/metrics

    humanised_jobnames{version="0.0.3"} 1.0
    flask_exporter_info{version="0.15.4"} 1.0
    flask_http_request_total{method="GET",status="200"} 8.0
    flask_http_request_total{method="GET",status="500"} 4.0
    ... snip ...

    # view the available data sources
    curl 'http://127.0.0.1:5000/source_names?format=text'
    ... snip ...
    adjectives.yaml
    capital-cities.yaml
    fedora-names.yaml
    ... snip ...

    # view details about the available data sources
    curl 'http://127.0.0.1:5000/sources?format=text'
    ... snip ...
    adjectives.yaml: Adjectives for the left hand side - 523 words
    capital-cities.yaml: A list of capital cities. Unicode removed. - 239 words
    fedora-names.yaml: A list of Fedora release names - 21 words
    ... snip ...

## Docker container

This container can be built locally with this repository or pulled
from [Dockerhub](https://hub.docker.com/repository/docker/deanwilson/humanised-jobnames)

    docker build -t deanwilson/humanised-jobnames .

    # expose the web app on port 5555
    docker run -p 5555:5000 deanwilson/humanised-jobnames

The Alpine image, built from the main [Dockerfile](/Dockerfile), is
preferred as it's 107MB while the [full Python image](/Dockerfile-full-python)
is 971MB.


### Author

 * [Dean Wilson](https://www.unixdaemon.net)
