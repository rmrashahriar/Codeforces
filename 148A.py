k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

drgSet = []

for x in k, l, m, n:
    for i in range(1, d+1):
        if i%x == 0:
            drgSet.append(i)
            
               
print(len(set(drgSet)))