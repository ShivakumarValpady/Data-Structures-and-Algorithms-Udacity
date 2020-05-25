#!/usr/bin/env python
# coding: utf-8

# In[118]:


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 1 or number== 0:
        return number
        
    low = 0
    high = number//2
    
    '''while low<=high:
        mid = low + (high - low)//2
        print(mid)
        if (mid**2 > number):
            high = mid-1
        elif (mid**2 < number):
            low = mid+1
        else:
            return mid
        print(low, high)'''
    
    while low<=high:
        mid = low + (high - low)//2
        print(mid)
        if mid == low or mid == high:
            return mid
        if (mid**2 > number):
            high = mid
        elif (mid**2 < number):
            low = mid
        else:
            return mid
        print(low, high)
        
        
    return mid
            


# In[119]:


sqrt(25)


# In[ ]:





# In[ ]:





# In[115]:


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")


# In[ ]:




