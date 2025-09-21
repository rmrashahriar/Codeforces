n = int(input())
for x in range(n):
    print(["I hate", "I love"][x%2],end = "")
    if x < n-1 :
        print(" that ", end = "")
    if x == n-1 :
        print(" it")