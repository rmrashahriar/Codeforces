n=int(input())
s=[ x for x in input() ]
a=0
d=0
for x in s:
    if x == "A":
        a += 1
    else:
        d += 1
        
if a > d :
    print("Anton")
elif d > a :
    print("Danik")
else:
    print("Friendship")
    
    