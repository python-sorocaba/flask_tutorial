#!/bin/bash
PORT=5432
NAME=postgresql_flask_tutorial
VOLUME=$(pwd)/data_postgres
POSTGRES_PASSWORD=123

mkdir -p $VOLUME
docker run -t -i -p $PORT:$PORT --name $NAME -v $VOLUME:/var/lib/postgresql/data -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD postgres
