a, b = [ int(x) for x in input().split() ]
count = 0
while not a>b:
    a *= 3
    b *= 2
    count += 1
    
print(count)