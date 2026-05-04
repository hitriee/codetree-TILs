from math import ceil

n = int(input())
customers = list(map(int, input().split()))
leader, follower = map(int, input().split())
cnt = n

for customer in customers:
    if customer > leader:
        cnt += ceil((customer - leader) / follower)

print(cnt)