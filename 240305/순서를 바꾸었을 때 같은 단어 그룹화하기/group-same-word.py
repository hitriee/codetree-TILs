n = int(input())
words = [input() for _ in range(n)]
finished = [False] * n
max_cnt = 0
for i in range(n-1):
    if not finished[i]:
        finished[i] = True
        cnt = 1
        check = {}
        for alp in words[i]:
            if check.get(alp):
                check[alp] += 1
            else:
                check[alp] = 1
        
        for j in range(i+1, n):
            if not finished[j]:
                temp = dict(check)
                for alp in words[j]:
                    if temp.get(alp):
                        temp[alp] -= 1
                        if temp[alp] == 0:
                            del temp[alp]
                    else:
                        break
                else:
                    if not temp:
                        cnt += 1
                        finished[j] = True

        if max_cnt < cnt:
            max_cnt = cnt

print(max_cnt)