from collections import deque

def int_input():
    return map(int, input().split())

def fill_minus_set():
    minus_set = set()
    for j in range(M):
        number = arr[0][j]
        if number:
            nj = (j-1) % M
            if arr[0][nj] == number:
                minus_set.add((0, nj))
                minus_set.add((0, j))
            
                
    for i in range(1, N):
        for j in range(M):
            number = arr[i][j]
            if number:
                has_same_num = False
                for idx in range(2):
                    ni, nj = (i+di[idx]) % N, (j+dj[idx]) % M
                    if arr[ni][nj] == number:
                        minus_set.add((ni, nj))
                        has_same_num = True
                if has_same_num:
                    minus_set.add((i, j))

    return minus_set

def normalize():
    avg = total // cnt
    removed_total = 0

    for i in range(N):
        for j in range(M):
            number = arr[i][j]
            if number:
                if number > avg:
                    arr[i][j] -= 1
                    removed_total += 1
                elif number < avg:
                    arr[i][j] += 1
                    removed_total -= 1
    return removed_total


def remove():

    removed_total = 0
    minus_set = fill_minus_set()
                
    if minus_set:
        for i, j in minus_set:
            removed_total += arr[i][j]
            arr[i][j] = 0
    else:
        removed_total = normalize()
        
    return (len(minus_set), removed_total)


def rotate(x, d, k):
    if total == 0:
        return (0, 0)
    
    for i in range(x-1, N, x):
        temp = arr[i]
        if d == 0:
            for _ in range(k):
                temp.appendleft(temp.pop())
        else:
            for _ in range(k):
                temp.append(temp.popleft())
    
    return remove()
    


N, M, Q = int_input()
arr = [deque(int_input()) for _ in range(N)]
di, dj = (0, -1,), (-1, 0)
cnt = N*M
total = sum([sum(arr[i]) for i in range(N)])

for _ in range(Q):
    cnt_minus, minus = rotate(*int_input())
    cnt -= cnt_minus
    total -= minus

print(total)
