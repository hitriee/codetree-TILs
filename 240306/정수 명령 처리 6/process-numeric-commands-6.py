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
    command = input()
    if command[:4] == 'push':
        num = int(command.split()[1])
        maxheap.push(num)
    elif command == 'pop':
        maxheap.pop()
    elif command == 'size':
        maxheap.size()
    elif command == 'empty':
        maxheap.empty()
    else:
        maxheap.top()