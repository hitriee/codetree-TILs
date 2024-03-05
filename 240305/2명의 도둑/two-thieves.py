N, M, C = map(int, input().split())
weight_info = [list(map(int, input().split())) for _ in range(N)]
square = N*N
thief1, thief2 = [], []
max_total = 0

def calc_total(arr):
    total = 0
    for num in arr:
        total += num*num
    
    return total

def remove_nums(level, limit, arr, sum_arr, jump, new_start, before):
    if level == limit:
        if sum_arr <= C:
            steal_stuff(jump, new_start, before+arr)
        return
    for i in range(M-level):
        new_arr = [arr[j] for j in range(M-level) if i != j]
        remove_nums(level+1, limit, new_arr, sum_arr - arr[i], jump, new_start, before)


def steal_stuff(level, start, thief):
    global max_total

    if level == 2:
        total = calc_total(thief)
        if max_total < total:
            max_total = total
        return
    
    ref_quot, ref_remain = divmod(start, N)
    
    for i in range(start, square):
        quot, remain = divmod(i, N)
        if remain + M > N:
            continue
        if level == 1 and ref_quot == quot and abs(remain - ref_remain) < M:
            continue
        arr = weight_info[quot][remain:remain+M][:]
        sum_arr = sum(arr)
        if sum_arr <= C:
            steal_stuff(level+1, i+1, thief+arr)
        else:
            for j in range(1, M):
                remove_nums(0, j, arr, sum_arr, level+1, i+1, thief)

steal_stuff(0, 0, [])

print(max_total)