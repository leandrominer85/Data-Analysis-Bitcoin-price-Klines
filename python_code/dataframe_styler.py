#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import glob
import os


# In[36]:


def data_table(path = '..\data\cleaned'):
    
    
    '''
    This function receives a path for the data. First it asks the user wich file(complete path) he wants.
    Uses this to load the dataframe. Then ask the dates for slicing the data.
    Then it returns two dataframe with the column close_diff formated with a stylized function that shows
    the relative difference inside the column with a color gradient.
    The first dataframe is for the whole data. The second is filtered for the fundingRate column where it
    is different from zero.
    
    Input:
    path - str; the path to the original data 
    
    
    Output:
    full_df - Dataframe for the whole data (as sliced by the user)
    funding_df - - Dataframe with data only with funding rate (as sliced by the user)
    
    '''
    
    
    
    
    
    #Uses glob to get the list of files
    path = path
    files = glob.glob(path + "/*.csv")
    
    print("Select one of the data:")
    for i in files:
        print(i)
        
    #fet the file path
    file_path = input("File path")
    
    df = pd.read_csv(file_path, index_col="date")
    print()
    print("Select a date between {} and {}".format(df.index.min(), df.index.max()))
    print()
    
    
    #get the dates
    init_date = input("Begin date (format : year-month-day hour:min:sec). Ex: '2020-02-19 17:30:00'")
    final_date = input("Final date (format : year-month-day hour:min:sec). Ex: '2020-02-19 17:30:00'")
    
    global full_df
    global funding_df
    
    #drop the unused column and filter the data
    df.drop("Unnamed: 0",axis=1, inplace=True)
    df2 = df[init_date:final_date]
    df3 = df2[df2["fundingRate"] != 0]
    
    
    full_df = df2.style.bar(subset=['close_diff'], align='mid', color=['#d65f5f', '#5fba7d'])
    
    funding_df = df3.style.bar(subset=['close_diff'], align='mid', color=['#d65f5f', '#5fba7d'])
    

    return (full_df , funding_df)
    
    
    


# In[37]:


data_table()


# In[38]:


full_df


# In[39]:


funding_df


# In[ ]:




