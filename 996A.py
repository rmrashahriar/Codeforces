noteList = [100, 20, 10, 5, 1]

amount = int(input())

count = 0

for i in range (0, 6):
    left = amount / noteList[i]
    left = int(left)
    count = count + left
    amount = amount - (left * noteList[i])
    if amount == 0:
        break
    
print(count)