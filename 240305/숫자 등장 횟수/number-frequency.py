n, m = map(int, input().split())
arr = input().split()
query_tuple = input().split()
cnt_frequency = {}

for num in arr:
    cnt_frequency[num] = cnt_frequency.get(num, 0) + 1

for num in query_tuple:
    print(cnt_frequency.get(num, 0), end=' ')