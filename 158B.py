n = int(input())
seq = [int(x) for x in input().split()]

seq.sort(reverse=True)

t = 0
print(seq)
for i in range(n-1):
    while seq[i] + seq[i+1] < 4:
        i += 1
        if i == n-1:
            break
    t += 1
        
print(t)