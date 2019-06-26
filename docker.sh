#!/bin/bash
# This script will pull image from docker hub and copy a python source code file present in current directory inside the docker hub
docker pull vivekk1/omdb_repo:Python-Container
docker run --name Python-Container -td docker.io/vivekk1/omdb_repo:Python-Container
docker cp OMDB_API.py Python-Container:/var/tmp/OMDB_API.py
docker exec -it Python-Container bash 
