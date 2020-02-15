#!/usr/bin/env python
# coding: utf-8

# In[182]:


import random
import time
import matplotlib.pyplot as plt


# In[183]:


l = []
def storran(n):
    for i in range(n):
        l.append(random.randint(1,100))


# In[184]:


def bubble():
    for i in range(0,len(l)-1):
        for j in range(0,len(l)-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]


# In[185]:


def selecte():
    for i in range(0, len(l) - 1):
        smallest = i
        for j in range(i + 1, len(l)):
            if l[j] < l[smallest]:
                smallest = j
        l[i],l[smallest] = l[smallest], l[i]


# In[186]:


x_lim = [*range(1000)]


# In[187]:


y_lim = []
for i in range(1,1001):
    l.clear()
    storran(i)
    s_time = time.time()
    bubble()
    #selecte()
    e_time = time.time()
    y_lim.append(e_time-s_time)
    #print(i,"Elements sorted in:- ",e_time-s_time)
    #print(l)


# In[188]:


plt.xlabel('Iteration')
plt.ylabel("Time[t]")
plt.plot(x_lim,y_lim)
#plt.stem(x_lim, y_lim, use_line_collection=True)

