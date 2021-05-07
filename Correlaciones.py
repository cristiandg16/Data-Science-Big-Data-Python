#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/PC/Downloads/archivos_base_python_data_science_big_data_esencial/base_datos_2008.csv")


# In[9]:


np.corrcoef(df["ArrDelay"],df["DepDelay"])


# In[13]:


np.corrcoef([df["ArrDelay"],df["DepDelay"],df["DepTime"]])


# In[14]:


df.drop(inplace = True, columns = ["Year","Cancelled","Diverted"])


# In[15]:


df.corr()


# In[16]:


df.drop(inplace = True, columns = ["Month"])
corr = round(df.corr(),3)
corr.style.background_gradient()


# In[8]:


df.dropna(inplace=True, subset = ["ArrDelay","DepDelay"])

