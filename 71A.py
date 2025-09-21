n=int(input())
while not (n<=100 and n>=1):
    n=int(input())
w_list=[]
for x in range (0,n):
    w=input()
    while not (len(w)<=100 and len(w)>=1):
        w=input()
        
    w_list.append(w)
    

for x in w_list:
    l=len(x)
    if len(x)>10:
        print("{0:s}{1:d}{2:s}".format(x[0],l-2,x[l-1]))
    else:
         print(x)
