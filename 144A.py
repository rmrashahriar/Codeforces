n = int(input())

queue = [int(x) for x in input().split()]
mx = max(queue)
h = queue.index(max(queue))
queue.remove(mx)
queue.insert(0,mx)
queue.reverse()
l = queue.index(min(queue))

print((h),(l))
