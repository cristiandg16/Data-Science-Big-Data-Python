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
df.dropna(inplace=True,subset=["ArrDelay","DepDelay","Distance","AirTime"])

sns.set(rc={"figure.figsize":(15,10)})


# In[3]:


df2 = df[df["Origin"].isin(["ATL","HOU","IND"])].sample(frac=1).head(1000)

sns.jointplot(df2["DepDelay"],df2["ArrDelay"])


# In[4]:


df3 = df2[np.abs(df2["DepDelay"])<40]
df3 = df3[np.abs(df3["ArrDelay"])<40]


# In[5]:


sns.jointplot(df3["DepDelay"],df3["ArrDelay"],kind="hex")


# In[6]:


sns.jointplot(df3["DepDelay"],df3["ArrDelay"],kind="kde")


# In[7]:


gb_df = pd.DataFrame(df2.groupby(["Origin","Month"],as_index=False)["DepDelay"].mean())
gb_df.head()


# In[8]:


data =  gb_df.pivot("Month","Origin","DepDelay")
data


# In[9]:


sns.set(rc = {"figure.figsize":(15,8)})
sns.heatmap(data = data,annot = True,linewidths=0.5)

