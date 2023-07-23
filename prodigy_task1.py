#!/usr/bin/env python
# coding: utf-8

# # importing the required libraries 
# 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# # importing the dataset
# 

# In[2]:


df = pd.read_excel('task_1_data.xlsx')


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df.describe()


# # filling the null values 

# In[7]:


df.isnull().sum().any()


# In[8]:


df = df.fillna(method = "bfill")
df.head()


# In[9]:


df.columns


# # Data visualization:
# 

# 
# FOR YEAR -1990

# In[10]:


plt.figure(figsize=(16, 9))
sns.histplot(df[1990], bins=15,color='red')
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram of 1990")
plt.show()


# FOR YEAR -2003

# In[11]:


plt.figure(figsize=(16, 9))
sns.histplot(df[2003], bins=15,color='purple')
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram of 2003")
plt.show()


# FOR YEAR - 2015

# In[12]:


plt.figure(figsize=(16, 9))
sns.histplot(df[2015], bins=15,color='yellow')
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram of 2015")
plt.show()


# FOR YEAR - 2022

# In[13]:


plt.figure(figsize=(16, 9))
sns.histplot(df[2022], bins=15,color='orange')
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram of 2022")
plt.show()


# END 
# 
