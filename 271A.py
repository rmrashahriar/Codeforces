n = 1 + int(input())

l = [ x for x in str(n) ]
s = set(l)

while not len(l) == len(s):
    l.clear()
    s.clear()
    n += 1
    l = [ x for x in str(n) ]
    s = set(l)
    
    
print(n)

