#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from joblib import Parallel, delayed

df = pd.read_csv("C:/Users/PC/Downloads/archivos_base_python_data_science_big_data_esencial/base_datos_2008.csv",nrows=100000)


# In[3]:


df_sub = df[["CarrierDelay","WeatherDelay","NASDelay","SecurityDelay","LateAircraftDelay"]]
df_sub.head(10)


# In[4]:


def retraso_maximo(fila):
    if not np.isnan(fila).any():
        names = ["CarrierDelay","WeatherDelay","NASDelay","SecurityDelay","LateAircraftDelay"]
        return names[fila.index(max(fila))]
    else:
        return "None"


# In[5]:


resultados = []
for fila in df_sub.values.tolist():
    resultados.append(retraso_maximo(fila))


# In[6]:


resultados


# In[ ]:


result = Parallel(n_jobs = 2, backend = "multiprocessing")(
map(delayed(retraso_maximo), df_sub.values.tolist()))

