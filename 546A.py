k, n, w = [ int(x) for x in input().split() ]
p=0
for x in range (1,w+1):
    p=p+x*k

if p-n>=0:
     print(p-n)
else:
     print(0)