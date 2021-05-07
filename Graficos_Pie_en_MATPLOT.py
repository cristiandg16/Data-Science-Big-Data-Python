#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/PC/Downloads/archivos_base_python_data_science_big_data_esencial/base_datos_2008.csv",nrows=100000)


# In[ ]:





# In[2]:


data = np.unique(df.Cancelled, return_counts = True)
data


# In[3]:


plt.pie(x = data[1],
       labels = data[0],         # Parametros
       colors = ["Red","Blue"],  # Colores del grafico
       shadow = True,            # Sombreado (True = si, False = No)
       startangle = 90,          # Angulo donde comienzan los datos
       radius = 1)               # Radio del grafico

plt.show()                       # Comando para mostrar el grafico

