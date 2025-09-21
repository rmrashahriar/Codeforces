FLAG = 0
string = ["h", "e", "l", "l", "o"]
s = [ x for x in input() ]
for x in s:
    if x == string[FLAG]:
        FLAG += 1
        if FLAG == 5:
            break
print(["NO", "YES"][FLAG == 5])