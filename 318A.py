import math

n, k = [ int(x) for x in input().split() ]

def even(x):
    print(x*2)
    
def odd(x):
    print(x+(x-1))
    
half_value = int(math.ceil(n/2))

if k > half_value:
    even(k-half_value)
else:
    odd(k)