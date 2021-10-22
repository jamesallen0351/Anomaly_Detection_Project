import pandas as pd
import numpy as np

'''
def clean_cohort_data(df):
    df['datetime'] = df.date + ' ' + df.time
    df['datetime'] = pd.to_datetime(df['datetime'])
    df = df.set_index('datetime')
    df['program_name'] = df.program_id.replace({1:'PHP Full Stack Web Development',2:'Java Full Stack Web Development',3:'Data Science',4:'Front End Web Development'})
    df['program_subdomain'] = df.program_id.replace({1:'php',2:'java',3:'ds',4:'fe'})
    df.drop(columns = ['date','time','deleted_at','program_id','id'],inplace = True)
    df.rename(columns = {'name':'cohort_name'},inplace = True)
    dictionary = {'Bash':61,'Hyperion':58,'Darden':59,'Florence':137,'Jupiter':62}
    df['cohort_id'].fillna(df['cohort_name'].map(dictionary), inplace=True)
    df = df.astype({"cohort_id": int})
    df['count_helper'] = 1
    df['split_path'] = df['path'].str.split('/')
    return df
'''

def remove_empty_paths(df):
    df = df[df.path != '/']
    return df

def clean_cohort_data(df):
    '''
    This function takes in the joined dataframes of the cohort information csv, and the curriculum logs
    and cleans the data
    '''
    # Deleting the columns that had over 700000+ nulls
    df.drop(columns = ['id',
    'namestr',
    'slack',
    'start_datestr',
    'end_datestr',
    'created_at',
    'updated_at',
    'deleted_at',
    'program_idstr'],inplace = True)
    # Renaming the column for readability
    df.rename(columns = {'name':'cohort_name'},inplace = True)
    # Dropping the 6 null values for path
    df.dropna(inplace = True)
    # Changing the cohort id and user id into an int for astetics
    df = df.astype({"cohort_id": int,"user_id":int})
    # Moving the datetime column to my index
    df['datetime'] = df.date + ' ' + df.time
    df['datetime'] = pd.to_datetime(df['datetime'])
    df = df.set_index('datetime')
    # Making new columns to help me.
    df['count_helper'] = 1
    df['program_name'] = df.program_id.replace({1:'PHP Full Stack Web Development',2:'Java Full Stack Web Development',3:'Data Science',4:'Front End Web Development'})
    df['program_subdomain'] = df.program_id.replace({1:'php',2:'java',3:'ds',4:'fe'})
    df['slack'] = '#' + df.cohort_name.str.lower()
    # Droping date and time columns because we already have a datetime index
    df.drop(columns = ['date','time'],inplace = True)
    # Removing any paths that just contain a '/'
    df = df[df.path != '/']
    return df

def split_by_program(df):
    '''
    makes a seperate dataframe for each of the different programs at codeup.
    '''
    php_df = df[df.program_id == 1]
    java_df = df[df.program_id == 2]
    ds_df = df[df.program_id == 3]
    fe_df = df[df.program_id == 4]
    return php_df,java_df,ds_df,fe_df