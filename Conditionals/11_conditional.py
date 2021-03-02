#if .. 
response = input("Are you hungry?: ")
if response.lower() == 'yes':
    print("That is good for your health")

#if ....else
response = input("Are you hungry?: ")
if response.lower() == 'yes':
    print("That is good for your health")
else:
    print("Please have nuts")

#if .... elif ..else
response = input("Are you hungry?: ")
if response.lower() == 'yes':
    print("That is good for your health")
elif response.lower() == 'no':
    print("Please have nuts")
else:
    print("Please have heavy breakfast")
