#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv('points-of-sale-transactions-mar-22.csv')


# In[3]:


data


# In[4]:


missing_data = data.isnull()
missing_data.head(5)


# In[5]:


for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("") 


# In[7]:


avg_Weekly_Sales = data["Unnamed: 2"].astype("float").mean(axis=0)
print("Average of Unnamed: 2", avg_Weekly_Sales)


# In[8]:


avg_Weekly_Sales=data['Unnamed: 2'].astype('float').mean(axis=0)
print("Average of Unemployment:", avg_Weekly_Sales)
# replace NaN by mean value in "Weekly_Sales" column
data["Unnamed: 2"].replace(np.nan, avg_Weekly_Sales, inplace = True)


# In[17]:


data['Unnamed: 5'].value_counts()


# In[13]:


# simply drop whole row with NaN in "CPI" column
data.dropna(subset=["Unnamed: 4"], axis=0, inplace=True)

# reset index, because we droped two rows
data.reset_index(drop=True, inplace=True)
data.head()


# In[14]:


data.dtypes


# In[36]:


data.head()


# In[37]:


for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("") 


# In[ ]:





# In[ ]:




