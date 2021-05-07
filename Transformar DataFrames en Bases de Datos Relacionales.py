#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
df = pd.DataFrameame.from_records(data, columns = labels) # Creamos la tabla con los valores asginados


# In[ ]:


compradores = df.drop_duplicates(subset = "Comprador_id", keep = "first")
compradores #Eliminanos valores duplicados de Comprador_id

