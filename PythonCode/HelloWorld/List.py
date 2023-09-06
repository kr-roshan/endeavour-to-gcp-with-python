fullList = [1,2,3,4,5,6,7,8,9,10]

myList = [1,2,3,4,5,6,7,8,10]

for i in fullList:
    if i not in myList:
        print(i)
        break

# sum values in full list
fullListSum = 0
for i in fullList:
    fullListSum += i
print(fullListSum)

# sum values in myList
myListSum = 0
for i in myList:
    myListSum += i
print(myListSum)

