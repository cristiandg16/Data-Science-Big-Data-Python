#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
df = pd.read_csv("C:/Users/PC/Downloads/archivos_base_python_data_science_big_data_esencial/base_datos_2008.csv",nrows=1e6)

#Un millon de elementos


# In[ ]:


dfduplicate = df.append(df)


# In[ ]:


dfduplicate = dfduplicate.sample(frac = 1)


# In[ ]:


dfclean = dfduplicate.drop_duplicates()


# In[ ]:


len(dfclean) == len(df)


# In[ ]:


dfclean.drop_duplicates(subset = "DayOfMonth")


# In[ ]:


df.dropna()


# In[ ]:


df.dropna(thresh = 25)


# In[ ]:


df.dropna(thresh = len(df.columns)-2)


# In[ ]:


df.dropna(subset = ["CancellationCode"])


# In[ ]:




