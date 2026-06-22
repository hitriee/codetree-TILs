n = int(input())
info = {}

def minus_one(num):
    return int(num) - 1

for _ in range(n):
    s, e = map(minus_one, input().split())
    info[s] = info.get(s, 0) + 1
    info[e] = info.get(e, 0) - 1


keys = sorted(info)
m = len(keys)
for i in range(1, m):
    info[keys[i]] += info[keys[i-1]]

print(max(info.values()))

