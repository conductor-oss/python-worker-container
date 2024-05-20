# Base container for python workers
This repository contains a sample set of workers and Dockerfile for running python workers in a container environment.

# Build Container
```shell
docker build . -t <TAG>
```
```shell
docker run -e CONDUCTOR_AUTH_KEY=<KEY> -e CONDUCTOR_AUTH_SECRET=<SECRET> -e CONDUCTOR_SERVER_URL=<API_ENDPOINT> -t <TAG>
```
 

