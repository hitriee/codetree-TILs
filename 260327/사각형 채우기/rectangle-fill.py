n = int(input())
if n <= 2:
    print(n)
else:
    pre_pre, pre = 1, 2

    for _ in range(3, n+1):
        pre_pre, pre = pre, (pre_pre + pre) % 10007

    print(pre)
