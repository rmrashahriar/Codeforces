n, k = [int(x) for x in input().split()]

for _ in range (k):
    if not n%10==0:
        n -= 1
    else:
        n = int(n/10)
         
print(n)