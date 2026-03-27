n = int(input())
if n == 1:
    print(2)
else:
    div_num = int(1e9)+7
    pre_pre, pre, multiple = 1, 2, 4

    for i in range(3, n+1):
        pre_pre, pre = pre, pre_pre + pre
        multiple *= 2


    print((pre*multiple - (pre - 1))% div_num)


