n, m = map(int, input().split())
arr = input().split()
query_tuple = input().split()
cnt_frequency = {}

for num in arr:
    if cnt_frequency.get(num):
        cnt_frequency[num] += 1
    else:
        cnt_frequency[num] = 1

for num in query_tuple:
    print(cnt_frequency.get(num, 0), end=' ')