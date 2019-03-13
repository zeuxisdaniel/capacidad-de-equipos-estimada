#!/bin/bash
imageName=flask-vuejs-docker
containerName=flask-vuejs-docker

docker stop $containerName

docker rm -f $containerName

docker build -t $imageName .

docker run -i -d -p 80:8080 --name $containerName $imageName