n = int(input())
sum_dict_list = [{} for _ in range(2)]
cnt = 0

for i in range(2):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for num1 in A:
        for num2 in B:
            sum_val = num1 + num2
            if sum_dict_list[i].get(sum_val):
                sum_dict_list[i][sum_val] += 1
            else:
                sum_dict_list[i][sum_val] = 1

for key in sum_dict_list[0]:
    if sum_dict_list[1].get(-key):
        cnt += sum_dict_list[0][key] * sum_dict_list[1][-key]

print(cnt)