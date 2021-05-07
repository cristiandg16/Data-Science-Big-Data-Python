#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(0)

df = pd.read_csv("C:/Users/PC/Downloads/archivos_base_python_data_science_big_data_esencial/base_datos_2008.csv",nrows=100000)
df = df.sample(frac=1).head(100)


# In[2]:


plt.scatter(x=df.DayofMonth,y=df.ArrDelay,s= df.Distance)


# In[12]:


plt.scatter(x=df.DayofMonth,y=df.ArrDelay,s= df.Distance,
           alpha = 0.3,                    #Hace que las burbujas sean translucidas u opacas
           c = df.DayOfWeek.isin([6,7]))   #Destaca los sabados y domingos con otro color
           
plt.title("Retrasos en EEUU")
plt.xlabel("Dia del Mes")
plt.ylabel("Retraso al Llegar")  
plt.ylim([0,150])
plt.xticks([0,15,30])
plt.text(x=28,y=120,s = "Mi vuelo")
plt.show

