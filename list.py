list1 = []
list1.append(2)
list1.append(4)
list1.pop()
list1.clear()

for i in range(5):
    list1.append(i+1)

list1.insert(1,7)
print(list1)
print(list1.index(4))


for i in range(len(list1)):
    print(list1[i])
