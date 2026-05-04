from math import ceil

n = int(input())
customers = list(map(int, input().split()))
leader, follower = list(map(int, input().split()))
cnt = 0

for customer in customers:
    cnt += 1
    if customer > leader:
        cnt += ceil((customer - leader) / follower)

print(cnt)