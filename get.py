import psycopg2
import pandas.io.sql as psql
import pandas as pd


def readDB():
	"""Read data from a postgres database table
	:param dataframe: pandas dataframe
	"""
	conn = psycopg2.connect(database = 'my_data',
        user = "postgres",
        password = "postgres",
        host = 'localhost',
        port = "6234")
	df = psql.read_sql("Select * from {}".format('my_data'), conn)
	print(df.head())

def main():
	readDB()

if __name__ == '__main__':
    main()
