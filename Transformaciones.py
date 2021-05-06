#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("C:/Users/PC/Downloads/archivos_base_python_data_science_big_data_esencial/base_datos_2008.csv")


# In[2]:


#Transformación, es una modificación en nuesttros valores de la base de datos, como borrar filas o añadir columnas.
df["HoursDelay"] = round(df["ArrDelay"] / 60)


# In[3]:


df["HoursDelay"].head()  #Muestra los primeros 5 elementos de la columna HoursDelay mostrado en horas.


# In[4]:


del(df["HoursDelay"]) #Elimina la columna HoursDelay de nuestra base de datos.


# In[5]:


df.drop(["Diverted","Cancelled","Year"],axis=1) #Muestra la base sin los elementos inscriptos (columnas) de la tabla.
df = df.drop(["Diverted","Cancelled","Year"],axis=1) # Elimina de la base los elementos inscriptos
df = df.drop(["Diverted","Cancelled","Year"],axis=1,inplace=True) # Igual que la query anterior


# In[8]:


dfATL = df[df.Origin == "ATL"]
dfHOU = df[df.Origin == "HOU"] #Cada una devuelve una nueva tabla con los valores correspondientes a atl o hou


# In[9]:


newdf = dfATL.append(dfHOU) #A la tabla de atlanta le agrega los valores de la tabla de houston


# In[10]:


newdf.Origin

