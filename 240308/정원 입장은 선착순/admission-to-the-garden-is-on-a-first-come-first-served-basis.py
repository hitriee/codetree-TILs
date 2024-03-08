from sys import stdin
from heapq import heappush, heappop

new_input = stdin.readline
N = int(new_input())
people = []
for i in range(N):
    heappush(people, (*map(int, new_input().split()), i))

tags = []
max_delay = 0
while tags or people:
    if tags:
        i, start, duration = heappop(tags)
        delay = end - start
        if max_delay < delay:
            max_delay = delay
        end += duration
    else:
        start, duration, i = heappop(people)
        end = start + duration

    
    while people and people[0][0] < end:
        s, d, j = heappop(people)
        heappush(tags, (j, s, d))

print(max_delay)