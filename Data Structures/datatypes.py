a=None
b=True
c=45
d=56.3
e="hello"
f=[]
g=3,4,5
h={"a":"apple","b":"Bat"}
i={5,4,3,9}

for x in a,b,c,d,e,f,g,h,i:
    print(type(x),x)

k=[5,6,7,3,4,5,6,2,3,4,5,6]

j=list(set(k))
print(j)
