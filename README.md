# Dummy postgres database
This code shows how to set up a dummy postgres database with docker. This is done using sqlalchemy to connect to the database and pandas to write a dataframe to a table in the database. Simply run the following steps:

1. Run `docker-compose up -d` to spin up a containerized postgres database
2. Run `python put.py` to populate the database with test data.
3. Run `python get.py` to check that you can extract data again

Notice that sevral things are predefined such as database name (my_data), port(5432), username(postgres) and password(postgres). They may be modified in the .env file and docker-compose.

# Optional
Here are some optional steps.

- Run `docker-compose down` To take down the container again.
- Run `docker exec -it DATABASE_NAME bash` to enter the contaier and run psql commands
