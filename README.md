# Spark-Practice
Counting number of tweet in difference countries in twitter stream using Spark, then store the result into mongoDB

## Required platform
- Docker with Docker-compose

## Installation
1. Edit the volumes share path of docker container in mongo-compose.yml
```notepad
  jupyterspark:
    volumes:
    - <PATH TO STORE CONTAINER DOCUMENT>:/home/jovyan/work
```
1. Start the service with mongo-compose.yml
```sh
$ docker-compose -f mongo-compose.yml start -d
```
1. Put socketlis.py and twitterstreamonsocketserver.py into file that shared to docker container
1. Run twitterstreamonsocketserver.py first, then socketlis.py
