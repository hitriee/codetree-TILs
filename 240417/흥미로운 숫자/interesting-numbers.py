X, Y = map(int, input().split())
cnt = dict_len = 0
num_dict = {i: 0 for i in range(10)}
min_len, max_len = len(str(X)), len(str(Y))


def back_tracking(num, length, dict_len):
    global cnt

    if length > max_len:
        return
    if length >= min_len:
        int_num = int(num)
        if int_num < X:
            return
        if int_num > Y:
            return
        if dict_len == 2:
            cnt += 1

    for i in range(10):
        if num_dict[i]:
            num_dict[i] += 1
            back_tracking(num + str(i), length + 1, dict_len)
            num_dict[i] -= 1
        elif dict_len == 1:
            num_dict[i] = 1
            back_tracking(num + str(i), length + 1, dict_len + 1)
            num_dict[i] = 0


for i in range(1, 10):
    num_dict[i] += 1
    back_tracking(str(i), 1, 1)
    num_dict[i] -= 1

print(cnt)