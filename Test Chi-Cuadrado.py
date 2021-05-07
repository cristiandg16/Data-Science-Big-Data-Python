#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/PC/Downloads/archivos_base_python_data_science_big_data_esencial/base_datos_2008.csv")


# In[ ]:





# In[3]:


np.random.seed(0)
df = df[df["Origin"].isin(["HOU","ATL","IND"])]
df = df.sample(frac = 1)
df = df[0:10000] #Toma 10000 valores ya que no es necesario tomar demasiados porque se van encontrando relaciones


# In[4]:


df["BigDelay"] = df["ArrDelay"] > 30
observados = pd.crosstab(index = df["BigDelay"],columns = df["Origin"],margins = True)


# In[5]:


observados


# In[6]:


from scipy.stats import chi2_contingency


# In[7]:


test = chi2_contingency(observados)


# In[8]:


test


# In[9]:


esperados = pd.DataFrame(test[3])


# In[10]:


esperados


# In[11]:


esperados_rel = round(esperados.apply(lambda r : r/len(df)*100,axis=1),2)


# In[12]:


observados_rel = round(observados.apply(lambda r : r/len(df)*100,axis=1),2)


# In[13]:


observados_rel


# In[14]:


esperados_rel


# In[15]:


test[1]


# Si el p-valor < 0.05, hay diferencias significativas: Hay relacion entre variables
# Si el p-valor > 0.05, no hay diferencias significativas: No hay relacion entre variables

