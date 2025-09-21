n = int(input())
xsum = 0
ysum = 0
zsum = 0
for x in range(n):
    val = [ int(x) for x in input().split() ]
    xsum += val[0]
    ysum += val[1]
    zsum += val[2]
    
print(["NO", "YES"][xsum == 0 and ysum == 0 and zsum == 0] )
