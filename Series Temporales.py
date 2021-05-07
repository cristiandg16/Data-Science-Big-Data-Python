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
df2 = df[df["Origin"].isin(["ATL","HOU","IND"])]
df = df.head(500000)


# In[3]:


times = []
for i in np.arange(len(df)):
    times.append(datetime.datetime(year = 2008,month=df.loc[i,"Month"],day=df.loc[i,"DayofMonth"]))


# In[5]:


times[50000]


# In[6]:


df["Time"] = times


# In[7]:


data = df.groupby(by = ["Time"],as_index=False)["DepDelay","ArrDelay"].mean()
data.head()


# In[8]:


sns.lineplot(data["Time"],data["DepDelay"])


# In[10]:


data = df.groupby(by=["Time"])["DepDelay","ArrDelay"].mean()
data.head()


# In[12]:


sns.lineplot(data=data)


# In[14]:


times = []
for i in df2.index:
    times.append(datetime.datetime(year=2008,month=df2.loc[i,"Month"],day=df2.loc[i,"DayofMonth"]))

df2["Time"] = times


# In[15]:


sns.set(rc={"figure.figsize":(15,10)})
sns.lineplot(x="Time",y="ArrDelay",hue="Origin",data = df2)

