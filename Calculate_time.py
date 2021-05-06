#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time

start = time.time()

#nuestro codigo
time.sleep(1)

end = time.time()

print(end - start)


# In[2]:


from datetime import timedelta

start = time.monotonic()

#code

time.sleep(1)

end = time.monotonic()

print(timedelta(seconds = end - start))


# In[ ]:




