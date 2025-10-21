dict = {1:1,2:2}

for i in dict:
    print(dict.get(i))
for i in dict.items():
    print(i[0])
    print(i[1])

list = [2,3,4,5,6,7,2,2,7,7,7,5]
for i in list:
    if i in dict:
        a=dict.get(i) 
        dict[i]=a+1
    else:
        dict[i]=1

print(dict)
