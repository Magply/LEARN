### Tasks related to docker-compose

For each task please create a folder like 'task1', 'task2', ..., 'taskN'.

1. Write docker-compose.yaml file where you launch a simple nginx container. After you launch it, nginx must be accessible at port '8080' from your local computer.

2. Write a simple python application (you can use AI to do this) which takes as input users information ('name', 'surname', 'email') in json format and saves it to file users.txt. Write docker-compose configuration to launch this code in docker.
Make sure you use docker volumes to save users.txt file if we restart docker container. Application requirements:
   
   - application must listen network traffic on port 3000
   - application takes input as json: {"name": "Mariya", "surname": "Novikava", "email", "123@gmail.com"}
   - when we send new request with new users details, application must append it to the users.txt file
