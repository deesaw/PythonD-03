#bitwise operators

a=10    #binary representation of 10 is 00001010
b=30    #binary representation of 30 is 00001110
print(bin(10))
print(int(0b1010))
#(if both bits are same the result is true , else it is false) 
print(a&b) #a&b is  00001010 (10)  
#(if any one of the bits is true the result is true) 
print(a|b) #a|b is 00001110 (14)

#XOR (^ is used)
'''
In XOR when both bits are same the result is 0 else 1
0 0 --> 0
0 1 --> 1
1 0 --> 1
1 1 --> 0
'''
# 12 --         1100
# 13 --         1101
#Result --- >   0001
print(12^13)

#left shift ...adds two bits at the end
#1010 
#1010 <<2  -->101000 --->40
print(10<<2)
#1010 << 3  --> 1010000 --->80
print(10<<3)

#right shift ---removes two bits from the end
#1010 --->10 ---> 2
print(10>>2)

#Complement or tilde operator
#Formulae -x-1
#~30= -30-1=-31
print(~a)  00001100


