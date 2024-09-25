# stop the container and remove the network

docker network disconnect microservice-net notifications-microservice
docker network disconnect microservice-net postgresql-server
docker network rm microservice-net
docker stop postgresql-server
docker rm postgresql-server
docker stop notifications-microservice
docker rm notifications-microservice