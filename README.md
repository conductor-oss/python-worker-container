# Base container for python workers
This repository contains a sample set of workers and Dockerfile for running python workers in a container environment.

# Python SDK for Conductor
https://github.com/conductor-sdk/conductor-python

#### ⭐ Conductor OSS 
[![GitHub stars](https://img.shields.io/github/stars/conductor-oss/conductor.svg?style=social&label=Star&maxAge=)](https://GitHub.com/conductor-oss/conductor/)

Show support for the Conductor OSS.  Please help spread the awareness by starring Conductor repo.



# Build Container
```shell
docker build . -t <TAG>
```
```shell
docker run \
  -e CONDUCTOR_AUTH_KEY=<KEY> \
  -e CONDUCTOR_AUTH_SECRET=<SECRET> \
  -e CONDUCTOR_SERVER_URL=<API_ENDPOINT> \
  -t <TAG>
```
 

