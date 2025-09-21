w=101
while not (w<=100 and w>=1):
    w=int(input())
flag=False
for x in range (2,w+1,2):
    y=w-x
    if (y%2==0) and (y!=0):
        flag=True
        
if flag==True:
    print("Yes")
else:
    print("No")
