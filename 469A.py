inp = int(input())

X_pass = [ int(x) for x in input().split() ]

del X_pass[0]

Y_pass = [ int(x) for x in input().split() ]

del Y_pass[0]

T_pass = X_pass + Y_pass

T_pass_set = set(T_pass)

#T_pass_set.discard(0)

print(["I become the guy.", "Oh, my keyboard!"][len(T_pass_set)!=inp])