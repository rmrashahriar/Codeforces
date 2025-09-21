n=int(input())
val=0
for x in range (n):
    
    op=input()
    
    if (op == "X++" or op == "++X") :
        val += 1
    else:
        val -= 1
        
print(val)

    