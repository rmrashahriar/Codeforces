firstInput=[int(x) for x in input().split()]
secondInput=[int(x) for x in input().split()]
count=0
for x in range (len(secondInput)):
    count += (secondInput[x]>=secondInput[firstInput[1]-1] and (secondInput[x]!=0))
  
print(count)