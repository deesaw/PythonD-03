#Strings
a="Welcome to Python World"
b='hello world'
c='''Good morning
how are you doing 
today'''

#input() function is used to read a string from standard input such as keyboard.
name = input("Enter your name: ")
print(name)
print (len(name))
print (type(name))

#Python index starts from 0

test = "Its healthy to have vegetables"
print( test)

print( test[4])                                
print( test[0])                      # Slicing
print( test[4:10])                   # Range slicing 
print( test[:10])
print( test[2:])
print( test[0:10:2])
print( test[0::2])                    #prints every second character
print( test[::1])
print(test[-1])                       #prints the last character
print( test[::-1])                    #reverse the string
print( test[:])
print( test[-2:])                     #prints last two characters    
