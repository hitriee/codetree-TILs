N, k = map(int, input().split())
numbers = list(map(int, input().split()))
check = [0] * 1001

for number in numbers:
    check[number] += 1

cnt = 0
for i in range(1, 1001):
    if check[i]:
        cnt += check[i]
        if cnt >= k:
            print(i)
            break