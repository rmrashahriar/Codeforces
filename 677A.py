n, h = [ int(x) for x in input().split() ]
e = [ int(x) for x in input().split() if int(x) > h ]
print(n + len(e) )