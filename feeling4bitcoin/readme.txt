# CRIAÇÃO DO BANCO

docker pull tutum/mongodb

docker run -d -p 27017:27017 -p 28017:28017 -e AUTH=no tutum/mongodb

docker ps -a

docker start <id>

use feeling4bitcoin

- criar coleções
db.createCollection("tweet")

- apresentar coleções
show collections

