n = int(input())
l = [ int(x) for x in input().split() ]

for x in range (1, n+1):
    for y in range ( n ):
        if x == l[y]:
            print(y+1, end=' ')
            
        

