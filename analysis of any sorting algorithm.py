#!/usr/bin/env python
# coding: utf-8

# # This libraries have to be included for running this program:-

# In[33]:


import random
import time
import matplotlib.pyplot as plt


# # Storing n Random numbers int the list()

# In[34]:


l = []
def storran(n):
    for i in range(n):
        l.append(random.randint(1,100))


# # Bubble Sorting Algorithm

# In[35]:


def bubble():
    for i in range(0,len(l)-1):
        for j in range(0,len(l)-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]


# # Selection Sorting Algorithm

# In[36]:


def selecte():
    for i in range(0, len(l) - 1):
        smallest = i
        for j in range(i + 1, len(l)):
            if l[j] < l[smallest]:
                smallest = j
        l[i],l[smallest] = l[smallest], l[i]


# # List of numbers for X_Label

# In[37]:


x_lim = [*range(1000)] # Argument of range should be == number of time sorting functions is being called


# # Calculating the time to sort each list of Random Numbers

# In[38]:


y_lim = [] #List of the numbers for the Y_Label
for i in range(1,1001):
    l.clear()
    storran(i)
    s_time = time.time()# Start Time
    bubble()
    #selecte()
    e_time = time.time()#End Time
    y_lim.append(e_time-s_time)
    #print(i,"Elements sorted in:- ",e_time-s_time)# Incase if we want to see the sorting time of each list
    #print(l)# To print the lists of all the random numbers


# # Plotting the graph to find the time complexity

# In[49]:


plt.xlabel('Iteration')
plt.ylabel("Time[t]")
plt.plot(x_lim,y_lim)
plt.fill_between(x_lim,y_lim,facecolor='y', alpha=0.9)
plt.title("Sorting Analysis")
#plt.stem(x_lim, y_lim, use_line_collection=True)
https://drive.google.com/open?id=1OTSOioqEbt7YVwmsrHV2g5j50TfivpFW

