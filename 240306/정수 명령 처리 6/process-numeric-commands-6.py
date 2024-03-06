from heapq import heappush, heappop

class MaxHeap:
    def __init__(self):
        self.nums = []
    
    def push(self, num):
        heappush(self.nums, -num)
    
    def pop(self):
        print(-heappop(self.nums))
    
    def size(self):
        print(len(self.nums))
    
    def empty(self):
        print('0' if self.nums else '1')
    
    def top(self):
        print(-self.nums[0])

n = int(input())
maxheap = MaxHeap()
for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        maxheap.push(int(command[1]))
    elif command[0] == 'pop':
        maxheap.pop()
    elif command[0] == 'size':
        maxheap.size()
    elif command[0] == 'empty':
        maxheap.empty()
    else:
        maxheap.top()