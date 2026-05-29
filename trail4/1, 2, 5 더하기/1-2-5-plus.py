n = int(input())

# Please write your code here.
cnt = [0] * (n+1)
cnt[0] = 1
div_num = 10007

for i in range(1, n+1):
    for di in (1, 2, 5):
        if i >= di:
            cnt[i] = (cnt[i] + cnt[i-di]) % div_num

print(cnt[-1])