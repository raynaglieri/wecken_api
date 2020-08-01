#!/bin/sh

ssh -o StrictHostKeyChecking=no root@$DIGITAL_OCEAN_TEST_ENVIRONMENT_IP << 'ENDSSH'
  cd /wecken
  export $(cat .env | xargs)
  echo "$DOCKER_HUB_ACCESS_TOKEN" | docker login --username $DOCKER_HUB_USERNAME --password-stdin
  docker pull  $DOCKER_ORGANIZATION/$DOCKER_APP:$CIRCLE_SHA1
  docker-compose up -d
ENDSSH