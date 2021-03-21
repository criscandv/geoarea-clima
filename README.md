# Geoarea Climate

#### Run with docker and docker-compose

> Download the repository and run the command ```docker-compose build```to build the dependences and all the docker ecosystem

> After that, run the command ```docker-compose up``` to start the docker containters.

> To connect to container, in this case, the flask container run the command ```docker exec -it geoarea_clima_api_1 sh```

> In the container, you can run the migrations with the manager ```python manage.py db upgrade``` and run the python unittest with pytest ```pytest```

