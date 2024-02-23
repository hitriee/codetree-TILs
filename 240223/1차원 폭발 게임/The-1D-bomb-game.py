N, M = map(int, input().split())
arr = [input() for _ in range(N)]
while True:
    bomb = False
    cnt = 1
    new_arr = arr[:1]
    for i in range(1, N):
        if arr[i] == arr[i-1]:
            cnt += 1
        else:
            if cnt >= M:
                bomb = True
                N -= cnt
                for _ in range(cnt):
                    new_arr.pop()
            
            cnt = 1
        
        new_arr.append(arr[i])

    if cnt >= M:
        bomb = True
        N -= cnt
        for _ in range(cnt):
            new_arr.pop()

    if not bomb:
        break

    arr = new_arr[:]

print(N, *arr, sep='\n')