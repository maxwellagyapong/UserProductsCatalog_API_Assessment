# User Product Catalog Management Project
Simple django application with products CRUD and user authentication as main features

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Commands](#commands)
* [App endpoints](#app-endpoints)
* [API Documentation](#api-documentation)


## General info
Simple django application with products CRUD and user authentication as main features


## Technologies
* Python
* Django
* Django Rest Framework
* Docker
* PostgreSQL
* Redis
* Celery

### Setup
## Installation on Linux and Mac OS
* [Follow the guide here](https://help.github.com/articles/fork-a-repo) on how to clone or fork a repo
* [Follow the guide here](https://docs.docker.com/engine/install/) on how to install and run docker
* To run application with docker
```
docker-compose up --build
```
  
* Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at http://0.0.0.0:8000).
* Open the address in the browser

## Commands
Open docker bash with 
```
docker ps
docker exec -it <CONTAINER_NAME> bash
```
In our case, default container name is "catalog"
* To run migrations
```
python manage.py makemigrations
python manage.py migrate

```

## App Endpoints
* /api/products - return the list of all saved user products
* /api/products/<int:pk> - returns a single user product (put, patch and delete allowed)
* /api/products/create - add a new product to a user's catalog
* /api/account/register - register a new user account
* /api/account/login - login to an existing user account

## API Documentation
```
http://127.0.0.1:8000/api/doc
```
