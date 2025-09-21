line = [x for x in input().split('WUB')]

finalLine = ''

for l in line:
    if l != '':
        finalLine = finalLine + l + ' '
        
print(finalLine)