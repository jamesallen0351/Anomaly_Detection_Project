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
    info_df = pd.read_csv("info_cohorts.csv",index_col = 0)
    # Joining the dataframes
    df = df.join(info_df,on = 'cohort_id',how = 'outer',lsuffix = 'str')
    df = prepare.clean_cohort_data(df)
    # df_without_staff = df[df.cohort_id != 28]
    df['module/lesson'] = df.path.str.split('/').str[0] + '/' + df.path.str.split('/').str[1]

    return df