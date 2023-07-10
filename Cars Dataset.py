#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd


# In[58]:


df = pd.read_csv('Cars Data.csv')


# In[59]:


df.head(1)


# In[60]:


df.shape


# # Preprocessing

# In[61]:


# Null values

df.isnull()


# In[62]:


df.isnull().sum()


# 2. fill the null values with the mean

# In[63]:


df.head(1)


# In[64]:


df['Cylinders'].fillna(df['Cylinders'].mean(), inplace =True)
df['EngineSize'].fillna(df['EngineSize'].mean(), inplace =True)
df['Horsepower'].fillna(df['Horsepower'].mean(), inplace =True)
df['MPG_City'].fillna(df['MPG_City'].mean(), inplace =True)
df['MPG_Highway'].fillna(df['MPG_Highway'].mean(), inplace =True)
df['Weight'].fillna(df['Weight'].mean(), inplace =True)
df['Wheelbase'].fillna(df['Wheelbase'].mean(), inplace =True)
df['Length'].fillna(df['Length'].mean(), inplace =True)


# In[65]:


df.isnull().sum()


# In[66]:


# How about the others ?
df.dtypes


# In[67]:


df[df.Invoice.isnull()]


# In[68]:


# Remplace null values with specific values

df["Origin"].fillna("No Info", inplace = True)
df["Model"].fillna("No Info", inplace = True)
df["Make"].fillna("No Info", inplace = True)
df["Type"].fillna("No Info", inplace = True)
df["DriveTrain"].fillna("No Info", inplace = True)
df["MSRP"].fillna("No Info", inplace = True)
df["Invoice"].fillna("No Info", inplace = True)


# In[69]:


df.isnull().sum()


# #### What are the differents marks of cars and their count value

# In[70]:


df.Make.value_counts()


# #### Show all the records where origin is Asia or Europe

# In[71]:


# Filter

df['Origin'].isin(['Asia','Europe']) 


# In[72]:


# To show the records

df[df['Origin'].isin(['Asia','Europe']) ]


# ####  Remove all the records (rows) where Weight is above 4000

# In[73]:


# Filter

df['Weight'] > 4000


# In[74]:


# Shows the records

df[df['Weight'] > 4000]


# In[75]:


# Drop the records 

df[~(df['Weight'] > 4000)]

# We don't have the records anymore , you can do inplace = True to keep them.

# We have now 329 rows


# ### Add +1 to all the value of EngineSize

# In[76]:


df['EngineSize'] = df['EngineSize'].apply(lambda x:x+1)

df.head(2)


# In[ ]:




