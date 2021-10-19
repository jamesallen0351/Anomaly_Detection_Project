# acquire.py

# imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os
from sklearn import metrics
from env import user, host, password

# creating functions to use in my notebook
def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my env file to create a connection url to access
    the Codeup database. '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
def curriculum_data():
    '''
    This function get the curriculum data from the codeup database
    '''

    sql_query = '''select *
    FROM logs
    LEFT JOIN cohorts on cohorts.id = logs.user_id
    '''
    
    return pd.read_sql(sql_query, get_connection('curriculum_logs'))

def get_curriculum_data():
    '''
    Reading curriculum data from codeup database and creates a csv file into a dataframe
    '''
    if os.path.isfile('curriculum_logs.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('curriculum_logs.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        df = curriculum_data()
     
        # Cache data
        df.to_csv('curriculum_logs.csv')
        
    return df