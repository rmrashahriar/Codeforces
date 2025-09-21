shoes_list = [ int(x) for x in input().split() ]

shoes_set = set(shoes_list)

print(len(shoes_list)-len(shoes_set))