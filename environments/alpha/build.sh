#!/bin/bash
set -e

echo "Building Docker image: ${DOCKER_IMAGE} with PORT ${PORT}"
docker build --build-arg PORT=${PORT} -t "${DOCKER_IMAGE}" -f ./environments/alpha/Dockerfile .

echo "Pushing Docker image: ${DOCKER_IMAGE}"
docker push "${DOCKER_IMAGE}"
