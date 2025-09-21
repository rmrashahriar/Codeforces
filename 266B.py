n, t = [ int(x) for x in input().split() ]
s = [ x for x in input() ]
for x in range (t):
    y = 0
    while y < len(s)-1 :
        if s[y] == "B" and s[y+1] == "G":
            temp = s[y]
            s[y] = s[y+1]
            s[y+1] = temp
            y += 2
        else:
            y += 1
    
print("".join(s))