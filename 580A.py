n = int(input())

dayList = [int(x) for x in input().split()]

maxSeq = 0
preSeq = 0

for i in range(n-1):
    if dayList[i+1] >= dayList[i]:
        preSeq += 1
    else:
        if preSeq > maxSeq:
            maxSeq = preSeq
        preSeq = 0
if preSeq > maxSeq:
    maxSeq = preSeq      
print(maxSeq+1)
    