_, m = map(int, input().split())
arr = input().split()
query_list = input().split()
cnt_frequency = {}

for num in arr:
    cnt_frequency[num] = cnt_frequency.get(num, 0) + 1

for i in range(m):
    query_list[i] = str(cnt_frequency.get(query_list[i], 0))

print(' '.join(query_list))