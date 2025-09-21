l1 = [ x for x in input() ]
l2 = [ x for x in input() ]
for x in range (len(l1)):
    print( [ "1", "0" ] [ l1[x] == l2[x] ], end = "" )