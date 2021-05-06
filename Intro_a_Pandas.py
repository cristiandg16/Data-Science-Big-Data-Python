#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("C:/Users/PC/Downloads/archivos_base_python_data_science_big_data_esencial/base_datos_2008.csv",nrows = 100000)


# In[4]:


df.head(10)


# In[5]:


df.tail() #Ultimos 5 elementos de la tabla


# In[6]:


df.sample(frac=1)


# In[7]:


df = df.sample(frac = 1)


# In[8]:


df.columns


# In[10]:


df.dtypes


# In[11]:


df.values


# In[12]:


df2 = df.head(10)


# In[13]:


df2.head(20)

