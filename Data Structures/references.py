a=[4,5,6]
b=a[:] 		# make a copy of a
c=a 		#add a reference

print id(a)
print id(b)
print id(b)

d={4:5}
e=d 		#add a reference
f=d.copy()	# make a copy of d
print id(d)
print id(e)
print id(f)