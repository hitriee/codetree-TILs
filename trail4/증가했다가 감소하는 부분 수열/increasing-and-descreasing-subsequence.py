n = int(input())
sequence = list(map(int, input().split()))

def plus(num1, num2):
    return num1 + num2

# Please write your code here.
cnt1, cnt2 = [0] * n, [0] * n
cnt1[0] = cnt2[-1] = 1
for i in range(1, n):
    num = sequence[i]
    max_val = 1
    for j in range(i):
        if sequence[j] < num:
            max_val = max(max_val, cnt1[j] + 1)
    cnt1[i] = max_val

for i in range(n-2, -1, -1):
    num = sequence[i]
    max_val = 1
    for j in range(i+1, n):
        if sequence[j] < num:
            max_val = max(max_val, cnt2[j] + 1)
    cnt2[i] = max_val


print(max(map(plus, cnt1, cnt2)) - 1)




