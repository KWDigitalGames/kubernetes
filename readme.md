# Kubernetes sample project

This project consists of FLASK API application writing to PostgreSQL database. Both applications are containerized, images are pulled from Docker Hub during the installation process. The application is supposed to be a basis of RPG web browser game and provides following endpoints:

POST /character/create - create a new character, requires three arguments: name, level, ID
GET /characters - get list of all characters
GET /character/<name> - get information about particular character
GET /metrics

# Installation

Create namespace:
```
kubectl create namespace rpgapp-namespace 
```
Apply db service:
```
kubectl apply -f ./rpg-db/rpg-db-service.yaml
```
Apply db stateful set:
```
kubectl apply -f ./rpg-db/rpg-db-statefulyaml
```
Install helm chart:
```
helm install rpg-app-api ./rpg-api/rpg-app-api-1.0.0.tgz
```

# Usage

Create new characters:
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"Tordek","level":1, "id":1}' \
  http://127.0.0.1:32000/character/create 
```
Get list of characters:
```
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://127.0.0.1:32000/characters
```

