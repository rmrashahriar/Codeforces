
n=[ int(x) for x in input() ]
m=[ int(x) for x in n if (x==4 or x==7) ]
if ( len(m) == 4 or len(m) == 7 ) :
    print("YES")
else:
    print("NO")
