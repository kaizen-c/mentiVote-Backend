# Menti Votes Reader

This backend server will run inside Heroku and pull data from following two url's and expose an end point for Frontend data manipulation work. 

- https://api.mentimeter.com/questions/48d75c359ce4
- https://api.mentimeter.com/questions/48d75c359ce4/result


## Prerequisites

- [Heroku](https://www.heroku.com/) account created to push your application 
- Should have [Docker](https://docs.docker.com/engine/install/ubuntu/#installation-methods) installed locally so that you can test before pushing to Heroku

## Installation

Build the Docker image locally and make sure it's working without any errors

```bash
docker build -t flask-heroku:latest .
# Check newly created images
docker images
# Run Docker locally
docker run -d -p 5000:5000 flask-heroku
# Check running containers
docker ps
```
Open Localhost port 5000 and you should observe something similar to http://localhost:5000 

>{"question": "Which is the best interactive presentation platform?", "results": [{"id": 1, "label": "Kahoot", "score": [2]}, >{"id": 2, "label": "Mentimeter", "score": [3]}, {"id": 3, "label": "Slido", "score": [1]}]}

## Deploying application to Heroku

Once you confirmed that your application is running locally without any errors. next step is to push the code to Heroku.

Login to Heroku 
```bash
heroku login --interactive
```
Login to Heroku Container
```bash
heroku container:login
```

Create a new app inside heroku
```bash
heroku create <appName>
```
Make sure you are inside the main folder and execute following command to push the container onto Heroku
```bash
heroku container:push web --app <appName>
```
release the container
```bash
heroku container:release web --app <appName>
```
Once the application is released you will get a url to traverse to your application as follow 
https://<appName>.herokuapp.com/voting?questionid=48d75c359ce4

* As of now the only working exposed endpoint ID is 48d75c359ce4
