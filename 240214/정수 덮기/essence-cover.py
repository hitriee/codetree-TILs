n, l = map(int, input().split())
position_list = list(map(int, input().split()))
position_list.sort()

end = position_list[0] + l - 0.5
cnt = 1
for i in range(1, n):
    if position_list[i] > end:
        cnt += 1
        end = position_list[i] + l - 0.5

print(cnt)