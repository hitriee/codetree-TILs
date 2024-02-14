from collections import deque
n, x = map(int, input().split())
q = deque(enumerate(map(int, input().split())))
cnt = 0

while True:
    idx, value = q.popleft()
    n -= 1
    for i in range(n):
        if value < q[i][1]:
            n += 1
            q.append((idx, value))
            break
    else:
        cnt += 1
        if idx == x:
            break

print(cnt)