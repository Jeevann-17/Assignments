#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ReverseArray(Array, first, last):
    while first < last:
        Array[first],Array[last] = Array[last],Array[first]
        
        first += 1
        last -= 1
        
        
Array = [10,20,130,40,150,80,100]
print(Array)
ReverseArray(Array, 0, 6)
print("REVERSED ARRAY")
print(Array)

