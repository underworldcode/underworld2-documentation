#! /usr/bin/env  bash

export IMAGE_NAME=uw-docker-landing-page:2.6.0b

set -e
cd $(dirname "$0")/..

# One shot build in cwd

docker build -t $IMAGE_NAME -f Docker/Dockerfile .
