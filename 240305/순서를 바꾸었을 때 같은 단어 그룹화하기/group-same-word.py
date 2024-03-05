n = int(input())
words = [''.join(sorted(input())) for _ in range(n)]
words.sort()

i, max_cnt = 0, 1
while i < n-1:
    cnt = 1
    word = words[i]
    j = i+1
    while word == words[j]:
        j += 1
        cnt += 1
        if j == n:
            break
    i = j
            
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)