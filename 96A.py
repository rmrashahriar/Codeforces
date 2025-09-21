foot = [ x for x in input() ]
curr_digit = foot[0]
FLAG = 0
count = 1
for y in range(1, len(foot)):
    if curr_digit == foot[y]:
        count += 1
        if count == 7:
            FLAG = 1
    else:
        count = 1
        curr_digit = foot[y]
    
print(["NO","YES"][FLAG])

