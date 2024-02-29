N = int(input())
cnt = 0
num_candidates = tuple(map(str, range(1, 5)))

def cnt_beautiful_num(level, before_cnt, result):
    global cnt

    last = int(result[-1])
    if level == N:
        if last == before_cnt:
            cnt += 1
        return
    
    if last == before_cnt:
        for num in num_candidates:
            if num != last:
                cnt_beautiful_num(level+1, 1, result+num)
    else:
        cnt_beautiful_num(level+1, before_cnt+1, result+result[-1])


for num in num_candidates:
    cnt_beautiful_num(1, 1, num)

print(cnt)