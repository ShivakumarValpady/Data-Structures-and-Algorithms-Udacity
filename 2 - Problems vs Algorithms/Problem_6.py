#!/usr/bin/env python
# coding: utf-8

# In[2]:


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) <= 1:
        return None
    small = ints[0]
    big = ints[0]
    
    for num in ints:
        if num < small:
            small = num
        if num > big:
            big = num
    return (small,big)


# In[ ]:





# In[ ]:





# In[3]:


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


# In[ ]:




