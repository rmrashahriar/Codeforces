n = int(input())
count = 0
for x in range (n) :   
    p, c = [ int(x) for x in input().split() ]
    if c - p >= 2:
        count += 1
        
print(count)