n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
check = [0] * 101
for i in range(n):
    check[A[i]] += 1
    check[B[i]] -= 1

for i in range(1, 101):
    if check[i]:
        print('No')
        break
else:
    print('Yes')