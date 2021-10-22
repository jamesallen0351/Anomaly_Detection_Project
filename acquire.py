# acquire.py

import pandas as pd
import numpy as np
import os
import env

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def create_cohort_data():
    '''
    puts cohort data into a pandas dataframe
    '''
    query = '''
SELECT *
FROM logs
LEFT JOIN cohorts on cohorts.id = logs.user_id
WHERE cohort_id IS NOT NULL;
    '''
    df = pd.read_sql(query, get_connection("curriculum_logs"))
    return df


def get_cohort_data():
    '''
    gets our cohort csv and reads it into a pandas dataframe
    '''
    if os.path.isfile("cohort.csv"):
        df = pd.read_csv("cohort.csv",index_col = 0)
    else:
        df = create_cohort_data()
        df.to_csv("cohort.csv")
    return df

