people = [input() for _ in range(4)]
idx_arr = [0] * 4

def rotate(func, i, nd, step):
    while func(i):
        j1, j2 = (idx_arr[i] + step * 2) % 8, (idx_arr[i+step] - step * 2) % 8
        if people[i][j1] != people[i+step][j2]:
            i += step
            new_idx_arr[i] = (new_idx_arr[i] - nd) % 8
            nd = -nd
        else:
            return

k = int(input())
for _ in range(k):
    # 번호, 방향
    n, d = map(int, input().split())
    n -= 1
    new_idx_arr = list(idx_arr)
    new_idx_arr[n] = (new_idx_arr[n] - d) % 8

    # 왼쪽으로 이동
    rotate(lambda x: x > 0, n, -d, -1)
    
    # 오른쪽으로 이동
    rotate(lambda x: x < 3, n, -d, 1)

    idx_arr = list(new_idx_arr)

total, num = 0, 1
for i in range(4):
    if people[i][idx_arr[i]] == '1':
        total += num
    num *= 2

print(total)
