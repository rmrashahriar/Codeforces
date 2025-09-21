import math

lengthOfList = int(input())

myList = []

for x in range (lengthOfList):
    myList.append([])
    val1, val2 = [ int (x) for x in input().split() ]
    myList[-1].append(val1)
    myList[-1].append(val2)
    
for x in range (lengthOfList) :
    nAlter = n = myList[x][0] 
    k = myList[x][1]
    tempArray = []
    resultArray = []
    FLAG = 0
    for x in range (n) :
            tempArray.append(1)
    
    while nAlter >= math.floor(n/2) :
        count = 0
        for i in range (n) :     
            for j in range (n) :
                if j > i :
                    if tempArray[i] * tempArray[j] == 1 :
                        count += 1
        if count == k :
            FLAG = 1
            print ( 'Yes' )
            print(' '.join(map(str, tempArray))) 
            break
        nAlter -= 1
        tempArray[nAlter] *= -1
        
    if FLAG == 0 :
        print ('No')
        
        
        
    