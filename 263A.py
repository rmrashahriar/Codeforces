mat=[]
for _ in range (5): 
     mat_ele=[int(x) for x in input().split()]
     mat.append(mat_ele)
     
for x in range (5):
    for y in range (5):
        if mat[x][y]==1:
            result=abs(2-x)+abs(2-y)
            print(result)

    