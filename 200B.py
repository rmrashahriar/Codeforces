n = int(input())
p = [ int(x)/100 for x in input().split() ]
print(sum(p)/n*100)
