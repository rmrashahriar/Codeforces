n=int(input())
while not (n>=1 and n<=1000):
    n=int(input())

mat=[]
count=0
ps=0
for x in range(n):
    row=[]
    element=input()
    element=element.split()
    for y in range(3): 
        element[y]=int(element[y])
        row.append(element[y])
    mat.append(row)
    
for x in range(n):
    for y in range (3):
        ps=mat[x][y]+ps
        if ps==2:
            count=count+1
            break
    ps=0
        
print(count)
    


