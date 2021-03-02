#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#for
for x in range(5):
    print(x)
print('************')
for x in range(3,10):
    print(x)
print('************')
for x in range(0,20,5):
    print(x)
print('************')


# In[ ]:


for places in "Hyderabad","Chennai","Mumbai":
    print(places)


# In[ ]:


a = [10,20,30,40,50,100]
for x in a:
    print(x)


# In[ ]:


report={'CS':90,'NS':80,'PS':60}

for subject,marks in report.items():
    print(subject,marks)


# In[ ]:


#Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
for index,count in enumerate(range(20,30)):   
    print(index,count)


# In[ ]:


count = 0
while count <=10:
    print(count)
    count=count+1            #count+=1


# In[ ]:




