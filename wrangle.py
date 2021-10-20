import pandas as pd
import numpy as np

import acquire
import prepare

def wrangle_cohort_data():
    '''
    This function takes in two dataframes and only leaves with one clean beautiful dataframe with all the
    information im going to need for the rest of this project.
    '''
    # Getting the data from the codeup sql database
    df = acquire.get_cohort_data()
    # Getting the data that holds cohort information
    info_df = acquire.get_cohort_information_data()
    # Joining the dataframes
    df = df.join(info_df,on = 'cohort_id',how = 'outer',lsuffix = 'str')
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
    df.rename(columns = {'name':'cohort_name'})
    # Dropping the 6 null values for path
    df.dropna(inplace = True)
    # Changing the cohort id into an int for astetics
    df = df.astype({"cohort_id": int})
    # Moving the datetime column to my index
    df['datetime'] = df.date + ' ' + df.time
    df['datetime'] = pd.to_datetime(df['datetime'])
    df = df.set_index('datetime')
    # Making new columns to help me.
    df['count_helper'] = 1
    df['program_name'] = df.program_id.replace({1:'PHP Full Stack Web Development',2:'Java Full Stack Web Development',3:'Data Science',4:'Front End Web Development'})
    df['program_subdomain'] = df.program_id.replace({1:'php',2:'java',3:'ds',4:'fe'})
    return df
