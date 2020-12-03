# Grafana dashboards with Dummy postgres database
This code shows how to set up grafana dashboards and a dummy postgres database with docker. Simply run the following steps to get started:

1. Run `docker-compose up -d` to spin up a containerized postgres database and grafana 
2. Run `python put.py` to populate the database with test data.
3. navigate to `localhost:4000` and use grafana to connecto to your dummy postgres database for analytics. Use grafanas native datasource support and create your own dashboards from there. 

Notice that sevral things are predefined such as database name (my_data), port(5432), username(postgres) and password(postgres). They may be modified in the .env file and docker-compose.

# Cleaning up

Run `docker-compose down` To take down the containers again.

