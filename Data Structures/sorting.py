#sorting lists

a=[1,3,5,7,3,4,12,11,34,32,67,45]

b=sorted(a)
print(b)#sort as numbers ascending
print(sorted(a,reverse=True))#sort as numbers descending
print(sorted(a,key=lambda x:str(x))) #sort as string


b=["simla","Ooty","Leh","Srinagar","Mahabaleshwar","Araku"]

print(sorted(b))
print(sorted(b,key=lambda x:x.lower())) # sort by lower case of element
print(sorted(b,key=lambda x:len(x))) # sort by length of element












#sorting list of tuples/lists

c=[("H",1),("Ca",20),("Ar",18),("O",8)]

print(sorted(c,key=lambda x:x[0])) #sort by element name
print(sorted(c,key=lambda x:x[1])) #sort by atomic number







import operator

c.sort(key=operator.itemgetter(1)) #sort by atomic number inplace
print(c)

#sorting dictionaries

#sort by keys

d={"a":1,"c":2,"b":3,"d":0}
print(sorted(d))

for x in sorted(d):
	print(x,d[x])

	
#sort values
print(sorted(d.values()))


#sort by values

d1=sorted(d, key=d.__getitem__)

for x in d1:
	print(x,d[x])

	
	
	
	
	
	