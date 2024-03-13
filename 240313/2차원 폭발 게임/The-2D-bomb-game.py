N, M, K = map(int, input().split())
arr = [input().split() for _ in range(N)]
# start_i = [0] * N
cnt = N*N

def bomb(cnt):
    for j in range(N):
        num, cnt_acc = '0', 0
        for i in range(N):
            if arr[i][j] == num:
                cnt_acc += 1
            else:
                if cnt_acc >= M and num != '0':
                    cnt -= cnt_acc
                    for k in range(i-1, i-1-cnt_acc, -1):
                        arr[k][j] = '0'
                cnt_acc, num = 1, arr[i][j]

        if cnt_acc >= M and num != '0':
            cnt -= cnt_acc
            for k in range(N-1, N-1-cnt_acc, -1):
                arr[k][j] = '0'
                
    return cnt

def gravity():
    for j in range(N):
        temp = []
        for i in range(N-1, -1, -1):
            if arr[i][j] != '0':
                temp.append(arr[i][j])
        for i in range(N-1, N-1-len(temp), -1):
            arr[i][j] = temp[N-1-i]
        # start_i[j] = i
        for i in range(N-1-len(temp), -1, -1):
            arr[i][j] = '0'

def rotate():
    new_arr = [[''] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[N-1-j][i]
    return new_arr


for _ in range(K):
    while True:
        new_cnt = bomb(cnt)
        gravity()
        # print(_, arr)
        # print(_, new_cnt, cnt)
        if new_cnt == cnt:
            break
        cnt = new_cnt
    arr = rotate()
    gravity()

while True:
    new_cnt = bomb(cnt)
    gravity()
    if new_cnt == cnt:
        break
    cnt = new_cnt


print(cnt)