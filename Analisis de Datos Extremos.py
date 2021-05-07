#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/PC/Downloads/archivos_base_python_data_science_big_data_esencial/base_datos_2008.csv")


# In[3]:


x = df["ArrDelay"].dropna()


# In[4]:


Q1 = np.percentile(x,25)
Q3 = np.percentile(x,75)
rangoInter = Q3 - Q1


# In[6]:


umbralsup = Q3 +1.5*rangoInter
umbralinf = Q1 - 1.5*rangoInter


# In[7]:


umbralsup


# In[8]:


umbralinf


# In[9]:


np.mean(x > umbralsup)  #Casos por encima


# In[10]:


np.mean(x < umbralinf) #Casos por debajo


# In[12]:


from sklearn.covariance import EllipticEnvelope


# In[13]:


outliers = EllipticEnvelope(contamination = .01)


# In[14]:


var_list = ["DeepDelay","TaxiIn","TaxiOut","CarrierDelay","WeatherDelay","NASDelay","SecurityDelay"]


# In[15]:


x = np.array(df.loc[:,var_list].dropna())


# In[ ]:


outliers.fit(x)


# In[ ]:


pred=outliers.predict(x)


# In[ ]:


pred


# In[ ]:


elips_outliers = np.where(pred == -1)[0]


# In[ ]:


elips_outliers

