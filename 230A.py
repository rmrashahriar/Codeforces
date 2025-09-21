s, n = [ int(x) for x in input().split() ]
FLAG = 0
strength = []
bonus = []
for _ in range(n):
    p, q = [ int(x) for x in input().split() ]
    strength.append(p)
    bonus.append(q)
for _ in range(len(strength)):
    least = min(strength)
    index = strength.index(least)
    if s > least :
        strength.remove(least)
        s += bonus[index]
        del bonus[index]
    else:
        FLAG = 1
print(["YES", "NO"][FLAG])