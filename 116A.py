n=int(input())
es=[]
ps=0
for _ in range (n):
    ex, en = [ int(x) for x in input().split() ]
    ps=(ps+en)-ex
    es.append(ps)
    
print(max(es))