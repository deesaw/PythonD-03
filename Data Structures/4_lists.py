#List
li = [2,3,4,5,100,4,20,40,50,4]
print(type(li))
print(len(li))
print(sum(li))          #sum of all the elements in the list
print(min(li))          
print(max(li))
#count of number of times '4' has been repeated in the list
print(count(4))

#accessing values from the list
print(li[5])
print(li[3:7])
print(li[6:])

#Updating values in the list
li[2:5]=[50,60,90]
print(li)

#deleting values from the list
del li[5]
print(li)
li[3:6]=[]
print(li)

#appending values to the list
a=[50,30,80,90,100,30,140,30]
a.append(70)
print(a)

#inserting values at particular position
a.insert(1,200)
print(a)

#removing elements from the list
a=[50,30,80,90,100,30,140,30]
a.remove(80)
print(a)

#removing elements using pop
#removes the element from the end, and returns the element that is removed
c=a.pop()  
print(c)
print(a)
a.pop(2)            #removes the element which is at index position 2

#Sorting
a=[50,30,80,90,100,30,140,30]
a.sort()                      #by default sorts in ascending order
print(a)
a.reverse()                   #reverses the list
#Sorting in descending by default
b=[5,1,2,310,80,60]
b.sort(reverse=True)

#Finding the position of an element
fruits=['apple','pear','grapes','orange']
print(fruits.index('grapes'))


print(b)

print(a)

