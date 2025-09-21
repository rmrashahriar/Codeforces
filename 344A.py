n  = int(input())
c = 1
val = input()
for _ in range(n-1):
        temp = input()
        if not val == temp:
            val = temp
            c += 1               
print(c)