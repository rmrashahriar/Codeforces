n, t = [ int(x) for x in input().split() ]
myList = [ int(x) for x in input().split() ]
myList.insert(0, 0)
x = 1
FLAG = 0
while True:
    x += myList[x]
    if x == t :
        FLAG = 1
        break
    if x == n :
        break
print(["NO", "YES"][FLAG])