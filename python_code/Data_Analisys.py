#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import glob
import os


# In[286]:


def data_table(path = '..\data\cleaned'):
    
    
    '''
    This function receives a path for the data.
    It asks the initial and final dates wich are used to filter the original dataframe.
    Then it aks the hour for the funding fees, the percentages for the target price and the liquidation price and
    the minutes to analyse.
    With this data whe start a counter that is summed every time the liquidation price is not reached and
    the target price is reached.
    Prints the results
    
    Input:
    path - str; the path to the original data 
    
    
    Output:
    
    
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
    df.drop("Unnamed: 0",axis=1, inplace=True)
    df.index = pd.to_datetime(df.index)
    
    
    print()
    print("Select a date  between {} and {}".format(df.index.min(), df.index.max()))
    print()
    
    
    #get the inputs
    init_date = input("Begin date (format : year-month-day hour:min:sec). Ex: '2020-02-19 17:30:00':   ")
    final_date = input("Final date (format : year-month-day hour:min:sec). Ex: '2020-02-19 17:30:00':   ")
    print()
    hour = input("Select the funding hour (integer with two digits, ex : 16):   ")
    
    print()
    funding = float(input("Select the funding fee (as a decimal format, ex: 0.01):   "))
    print()
    target_price = float(input("Select the target price increase (as a decimal format, ex: 0.01):   "))
    print()
    liquidation_price = float(input("Select the liquidation price decrease (as a decimal format, ex: 0.01):   "))
    print()
    minutes = input("Select the minutes interval (integer with two digits, ex : 16):   ")
    print()
    filename = input("Name for the dataframe to save:  ")
    
    
    df_exact_hour = df_time_period.at_time(hour+":00")
    
    
    
    #Initialize the counter and the percentage
    counter = 0
    percentage = 0
    
    
    #Check if the max value from the fundingRate input is higher than the one from the dataframe 
    if funding > df_exact_hour['fundingRate'].values.max():
        
        #slice the dataframe with the hour and minutes provided
        df_sliced = df_time_period.between_time(start_time='{}:00'.format(hour), end_time='{}:{}'.format(hour,minutes))
        
        #gets the base price
        default_price = df_sliced['close'][0]
        
        # update the target and liquidation prices with the default price
        
        target_price= default_price * (1 +target_price)
        liquidation_price= default_price * (1 -liquidation_price)
        
        #iterates through the sliced dataframe and counts only if the liquidation price is higher
        # than the minimum of the day and the target price is below the high
        for i in df_sliced[['low', 'high']].iterrows():
            if liquidation_price >= i[1][0]:
                counter +=0
            elif target_price <= i[1][1]:
                counter +=1
        percentage = counter/len(df_sliced)
        
        #save the dataframe
        df_sliced.to_csv("..\saved_dataframes\{}.csv".format(filename))

    # If the funding is not higher stops
    else:
        
        print("The percentage selected for the funding fee is :{} , and for the select time period the"              "maximum fee is: {}. So funding fee is below the select percentage".format(fundingnding, df_exact_hour['fundingRate'].values.max()))
    

    
    print()


    print(("For the dates between {} and {}, considering the funding hour {} within {} minutes"     "period, the target price of: {} , the liquidation price of :{} the target price was hit on {}"     "of the total periods").format(init_date,final_date,hour,minutes,target_price,liquidation_price, percentage))
    
    
    


# In[343]:


data_table()


# In[ ]:




