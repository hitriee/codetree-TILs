n = int(input())
LIMIT = int(2e5)
arr = [0] * LIMIT

def minus_one(num):
    return int(num) - 1

for _ in range(n):
    s, e = map(minus_one, input().split())
    arr[s] += 1
    arr[e] -= 1

for i in range(1, LIMIT):
    arr[i] += arr[i-1]

print(max(arr))

