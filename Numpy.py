#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


valoraciones = np.array([[8,7,8,5],[2,6,8,1],[8,8,9,5]])
valoraciones


# In[3]:


valoraciones[0][1]


# In[4]:


valoraciones[0,1]


# In[5]:


valoraciones2 = np.array([[[8,7,8,5],[2,5,5,2]],[[2,6,8,4],[8,9,7,4]],[[8,8,9,3],[10,9,10,8]]])
valoraciones2


# In[6]:


valoraciones2[0,1,2]


# In[7]:


np.zeros((3,2,4)) #ARRAY vacio


# In[8]:


valoraciones2 + np.ones((3,2,4))


# In[9]:


np.mean(valoraciones2)


# In[10]:


np.mean(valoraciones2,axis = 0)


# In[11]:


np.mean(valoraciones2,axis = 1)


# In[12]:


np.reshape([1,2,3,4,5,6,7,8,9,10,11,12],(3,2,2))


# In[ ]:


np.median(df["Columna1"])


# In[13]:


np.random.rand(2,2)

