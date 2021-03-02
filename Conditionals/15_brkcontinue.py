#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Break
numbers = [100, 25, 125, 50, 150, 75, 175]
for x in numbers:
    print( x )
    # As soon as we find 50 - stop the search!
    if x == 50:
        print( "Found It!" )
        break


# In[ ]:


#Program to skip all the three digit numbers
numbers = [100, 25, 125, 50, 150, 75, 175]
for x in numbers:
    if x >= 100:
        continue
    print( x )


# In[ ]:




