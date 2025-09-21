b = int(input())
c = 0
while True :
    if b == 1 :
        break
    if b % 2 != 0 :
        b -= 1
        c += 1
    b /= 2
    if b != int(b) :
        b *= 2
print(int(b+c))