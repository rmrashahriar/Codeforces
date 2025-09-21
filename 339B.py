n, m = [ int(x) for x in input().split() ]
task = [ int(x) for x in input().split() ]
count = 0
for x in range (len(task)-1):
    if task[x] > task[x+1] :
        count += n
print(count + (task[-1] - 1))