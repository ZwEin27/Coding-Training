import heapq

h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (30, 'create tests'))
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (20, 'create tests'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (40, 'create tests'))
heapq.heappush(h, (3, 'create tests'))
heapq.heappush(h, (10, 'create tests'))




print heapq.nsmallest(4, h)
