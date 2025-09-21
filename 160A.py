n = int(input())
coin_values = [ int(x) for x in input().split() ]
total = 0
count = 0
coin_values.sort(reverse = True)
for x in coin_values:
    count += 1
    total = total + x
    if ( sum(coin_values) - total ) < total :
        break       
print(count)
    
    