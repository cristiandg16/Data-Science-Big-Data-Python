#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import datetime

df = pd.read_csv("C:/Users/PC/Downloads/archivos_base_python_data_science_big_data_esencial/base_datos_2008.csv")


# In[2]:


df.dropna(inplace=True,subset = ["ArrDelay","DepDelay","Distance"])


# In[6]:


sns.displot(df["Distance"],kde = False,bins = 100) #kde elimina la aproximacion de la densidad


# In[8]:


sns.kdeplot(df["ArrDelay"])
sns.kdeplot(df["DepDelay"])
plt.xlim([-300,300])


# In[9]:


df2 = df[df["Origin"].isin(["ATL","HOU","IND"])].sample(frac=1).head(500)


# In[11]:


sns.boxplot(x="DepDelay",y = "Origin",data = df2)
plt.xlim([-20,150])

