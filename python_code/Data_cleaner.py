#!/usr/bin/env python
# coding: utf-8

# In[47]:


# import modules
import pandas as pd
import glob
import datetime as dt
import os


# In[50]:


def cleaner(data_path = '..\data\original', save_path ='..\data\cleaned' ):
    
    '''
    This function receives a path for the data and for the saves. Remove the time column, transform the 
    date to the datetime format and fill the fundingrate Nans with zeros and them saves the files in the 
    corresponding folder.
    
    Input:
    data_path - str; the path to the original data 
    save_path - str; the path to save the modified data
    
    Output:
    Dataframes cleaned and saved
    
    '''
    
    #Use glob to get all the files names in the original folder

    path = data_path
    files = glob.glob(path + "/*.csv")

    # Iterate the files names and clean and save the data
    for file in files:    
        df = pd.read_csv(file, index_col= 0)


        # we have the date, so we don't need the time column

        df.drop('time', axis=1, inplace=True)


        # the date column is in the object format. Let's make it a datetime

        df['date'] = df['date'].apply(pd.to_datetime)

        # for the purpouse of this project i will consider the rows with no funding fee as zeros

        df['fundingRate'].fillna(0, inplace=True)

        #Saving the file. The os function gets only the name of the file to pass to the save path

        df.to_csv('{}\{}'.format(save_path,os.path.basename(os.path.normpath('{}'.format(file)))))


# In[ ]:


cleaner()

