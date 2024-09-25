#!/bin/bash

# check if docker network microservice-net already exists
if [ ! "$(docker network ls | grep ' microservice-net')" ]; then
  docker network create --driver bridge microservice-net
fi

# check if container postgresql-server already exists, is running and is connected to the network
if [ ! "$(docker ps -q -f name=postgresql-server)" ]; then
  if [ "$(docker ps -aq -f status=exited -f name=postgresql-server)" ]; then
    docker rm postgresql-server
  fi
  docker run -d --name postgresql-server --network microservice-net \
    -e POSTGRESQL_PASSWORD=mysupersecretpassword \
    -v $(pwd)/init.sql:/docker-entrypoint-initdb.d/init.sql \
    bitnami/postgresql
fi

# Wait for PostgreSQL server to be ready
echo "Waiting for PostgreSQL to start..."
until docker exec postgresql-server pg_isready -U postgres; do
  >&2 echo "PostgreSQL is unavailable - sleeping"
  sleep 2
done

echo "PostgreSQL is up - starting notifications-microservice"

# Build the notifications-microservice image
docker build -t notifications-microservice .

# Run the notifications-microservice container
docker run -d --name notifications-microservice --network microservice-net -p 8001:8001 notifications-microservice
