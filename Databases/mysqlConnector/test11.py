dic={}
dic["fruit"]="Orange"
dic["Vegetable"]="Brinjal"

print(dic)
'''for key,value in dic:
          print("key : {}, value: {}").format(key,value)
'''
for x in dic:
          print(x,dic[x])
for key,value in dic.items():
          print(key,value)
