n, k = map(int, input().split())
numbers = list(map(int, input().split()))
half, cnt = k//2, 0, 
check = {}

for number in numbers:
    if check.get(number):
        check[number] += 1
    else:
        check[number] = 1

for number in numbers:
    if number < half and check.get(k-number):
        cnt += check[k-number]

if check.get(half):
    if k % 2 == 0:
        cnt += ((check[half] - 1) * check[half]) // 2
    elif check.get(k-half):
        cnt += check[k-half]

print(cnt)