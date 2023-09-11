# Write a program to find the second most frequent element in a list
myList = [1,2,3,4,5,6,2,8,9,10,1,2,4,2,2,5]

myOrderedDistinctList = {}

for i in myList:
    if i not in myOrderedDistinctList:
        myOrderedDistinctList[i] = 1
    else:
        myOrderedDistinctList[i] += 1    

print(dict(sorted(myOrderedDistinctList.items(), key = lambda x:x[1], reverse=True)))

