n = int(input())
sum_dict = {}
cnt = 0

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))


for num1 in A:
    for num2 in B:
        sum_val = num1 + num2
        if sum_dict.get(sum_val):
            sum_dict[sum_val] += 1
        else:
            sum_dict[sum_val] = 1

for num1 in C:
    for num2 in D:
        minus_sum = -(num1 + num2)
        if sum_dict.get(minus_sum):
            cnt += sum_dict[minus_sum]

print(cnt)