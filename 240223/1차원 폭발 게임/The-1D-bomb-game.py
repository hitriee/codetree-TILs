N, M = map(int, input().split())
arr = [input() for _ in range(N)]
while N:
    bomb = False
    cnt = 1
    new_arr = []
    for i in range(1, N):
        if arr[i] == arr[i-1]:
            cnt += 1
        else:
            if cnt >= M:
                bomb = True
                N -= cnt
            else:
                new_arr.extend(arr[i-1] * cnt)
            
            cnt = 1

    if cnt >= M:
        bomb = True
        N -= cnt
    else:
        new_arr.extend(arr[-1] * cnt)

    if not bomb:
        break

    arr = new_arr[:]

print(N, *arr, sep='\n')