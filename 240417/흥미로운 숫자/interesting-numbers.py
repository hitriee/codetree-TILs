X, Y = map(int, input().split())
cnt = 0
for i in range(X, Y+1):
    str_num = str(i)
    num_dict = {}
    length = 0
    for element in str_num:
        if num_dict.get(element):
            num_dict[element] += 1
        elif length < 2:
            num_dict[element] = 1
            length += 1
        else:
            break
    else:
        one = num_dict[str_num[0]]
        if one == 1 or one == len(str_num) - 1:
            cnt += 1

print(cnt)