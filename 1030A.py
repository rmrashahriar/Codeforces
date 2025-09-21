n = int(input())
l = [x for x in input().split() if x == "1" ]
if len(l) >= 1:
    print("HARD")
else:
    print("EASY")