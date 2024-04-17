X, Y = map(int, input().split())
cnt = 0
for i in range(X, Y+1):
    str_num = str(i)
    num_dict = {}
    for element in str_num:
        num_dict[element] = num_dict.get(element, 0) + 1
    
    if len(num_dict) == 2:
        one = num_dict[str_num[0]]
        if one == 1 or one == len(str_num) - 1:
            cnt += 1

print(cnt)