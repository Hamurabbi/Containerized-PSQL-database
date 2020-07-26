import pandas as pd
import argparse
import os
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database


def populateDB(dataframe, engine_url):
	"""Populate a postgres database with data using
	pandas and sqlalchemy
	:param dataframe: pandas dataframe
	:param engine_url: url to database
	"""
	engine = create_engine(engine_url)
	data_type = str(engine.url).rsplit('/', 1)[1]
	print('Populating database with', data_type)
	dataframe.to_sql(data_type, engine, if_exists="replace", index=False)
	print('Done')

def main():

	df = pd.read_csv('data/test_data.csv')
	populateDB(df,'postgresql://postgres:postgres@localhost:6234/my_data')

if __name__ == '__main__':
    main()
