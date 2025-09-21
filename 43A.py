n = int(input())
myList = []
count = 0
for _ in range(n):
    myList.append(input())
mySet = set(myList)
mySet = list(mySet)
for x in range(len(mySet)):
    if myList.count(mySet[x]) > count :
        count = myList.count(mySet[x])
        res = mySet[x]
print(res)
        