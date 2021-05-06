#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df = pd.read_csv("C:/Users/PC/Downloads/archivos_base_python_data_science_big_data_esencial/base_datos_2008.csv")


# In[3]:


df["ArrDelay"].head #Ver los primeros elementos de la columna ARRDELAY


# In[5]:


df[df["ArrDelay"]<60].head() #ver los 5 primeros vuelos que se retrasaron menos de 60 minutos


# In[6]:


df[df["Origin"] == "ATL"].head() # Primeros cinco vuelos que salieron de atlanta


# In[7]:


df[(df["Origin"]== "ATL") & (df["ArrDelay"] > 60)].head() #Vuelos que salieron de Atlanta y demoraron mas de 60 minutos (Primeros 5)


# In[9]:


df[df.Origin.isin(["HOU","ATL"])].head() #Vuelos que salieron de Houston y Atlanta


# In[10]:


df[pd.isna(df["ArrDelay"])].head()  #Elementos que no tienen el valor ArrDelay en las tablas


# In[11]:


len(df[pd.isna(df["ArrDelay"])]) #Cuantos elementos no tiene el valor ArrDelay en nuestra tablas


# In[4]:


df[100:110] #Ver ciertas filas

