#dictionary
marks={'Maths':97,'Science':98,'History':78}
print(marks)
print(type(marks))
print(len(marks))
print(sum(marks.values()))
print(max(marks.values()))
print(min(marks.values()))

print(marks.keys())     #prints keys from the dictionary                                                          
print(marks.values())   #prints values from the dictionary
print(marks.items())    #prints keys and values from the dictionary,returns list of tuples

#printing value of the element from the dictionary
print(marks['History'])
#adding new item to the dictionary
marks['Computers'] = 90
print(marks)
#Changing the value of the existing key
marks['History']=80
print(marks)
#removing an element from the dictionary
del marks['History']
print(marks)
