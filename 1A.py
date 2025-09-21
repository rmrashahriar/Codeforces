import math
n, m, a = [ int(x) for x in input().split() ]
if n*m <= a*a:
    print(1)
else:
    if n > a :
        n = int ( math.ceil( n /a ) ) * a
    if m > a :
        m = int ( math.ceil( m /a ) ) * a
    print(int((n*m)/(a*a)))