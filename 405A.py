n = input()
val = [ int(x) for x in input().split() ]
val.sort()
print(" ".join(str(x) for x in val))
