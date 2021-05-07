#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/PC/Downloads/archivos_base_python_data_science_big_data_esencial/base_datos_2008.csv",nrows=100000)

data = np.unique(df.DayOfWeek,return_counts=True)
labs = ["Lun","Mar","Mie","Jue","Vie","Sab","Dom"]
data


# In[5]:


plt.pie(x = data[1],
       labels = labs,
       radius = 0.7,
       colors = sns.color_palette("hls",7),  #Comando para indicar que son 7 colores y que use una paleta definida en sns
       explode = (0,0,0,0,0,0,0.1),          #Resalta o aleja los valores en el grafico
       startangle = 90,
       autopct = "%1.1f%%")                  #Muestra los valores en formato float

plt.legend(loc="upperleft",labels= labs)     #Ubica la legenda en la parte que desees
plt.show()


# In[7]:


plt = sns.barplot(x=labs,y=data[1])
plt.set(xlabel = "Dia de la semana",ylabel = "Numero de vuelos")

