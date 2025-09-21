n = int(input())

soln = []
inp = []

for x in range(n):
    inp = [int(x) for x in input().split() ]
    test = inp[0]/inp[1]
    if int(test) == test:
        soln.append(0)
    else:
        res = (int(test)+1)*inp[1] - inp[0]
        soln.append(int(res))
    inp.clear()
    
for x in range(n):
    print(soln[x])