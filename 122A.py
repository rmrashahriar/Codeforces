n = int(input())
FLAG = 0
for x in range (n+1):
    y = str(x)
    if y.count("4")+y.count("7") == len(y):
        if n % x == 0 :
            FLAG += 1
            break
print(["NO", "YES"][FLAG])
    