from math import ceil

n = int(input())
customers = list(map(int, input().split()))
limit = list(map(int, input().split()))
cnt = 0

for customer in customers:
    cnt += 1
    if customer > limit[0]:
        cnt += ceil((customer - limit[0]) / limit[1])

print(cnt)