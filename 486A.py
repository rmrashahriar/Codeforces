import math
n  = int(input())
if n/2 == math.ceil(n/2):
    print(int(n/2))
else:
    print(math.ceil(n/2)*(-1))