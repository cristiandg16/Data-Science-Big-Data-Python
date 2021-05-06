#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("C:/Users/PC/Downloads/archivos_base_python_data_science_big_data_esencial/base_datos_2008.csv")


# In[2]:


df.groupby(by = "DayOfWeek")["ArrDelay"].max() #Maximo ArrDelay segun cada dia de la semana


# In[3]:


df.groupby(by = "DayOfWeek")["ArrDelay"].mean() ##Mediana ArrDelay segun cada dia de la semana


# In[ ]:


df.groupby(by = "DayOfWeek")["ArrDelay"].min() ##Minimo ArrDelay segun cada dia de la semana


# In[4]:


df.groupby(by = "DayOfWeek")["ArrDelay"].count() #Numero de casos de ArrDelay segun cada dia de la semana


# In[5]:


df.groupby(by = "DayOfWeek")["ArrDelay"].describe() #Resumen estadistico agrupado de ArrDelay segun cada dia de la semana


# In[6]:


df.groupby(by = "DayOfWeek")["ArrDelay","DepDelay"].mean()


# In[7]:


df.groupby(by = "DayOfWeek")["ArrDelay"].max() - df.groupby(by = "DayOfWeek")["ArrDelay"].min()
#Distancia entre demoras por dia


# In[8]:


dfATLHOU = df[df.Origin.isin(["ATL","HOU"])] #Creamos una tabla con los vuelos cuyo origen es atlanta o houston


# In[9]:


dfATLHOU.groupby(by = ["DayOfWeek","Origin"])["ArrDelay"].mean()

#Media en los dias de la semana entre los vuelos de origen en ATl y Hou


# In[ ]:


mygrouby = dfATLHOU.groupby(by = ["DayOfWeek","Origin"])["ArrDelay"]

