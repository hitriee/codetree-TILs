from sys import stdin

new_input = stdin.readline
N = int(new_input())
small_ref = ord('a')
alp_to_num = {chr(small_ref+i): i for i in range(26)}
order = [[] for _ in range(N)]
word_asc, word_des = [], []

for i in range(N):
    alp_list = list(new_input().rstrip())
    alp_list.sort()
    word_asc.append((''.join(alp_list), i))
    word_des.append((''.join(alp_list[::-1]), i))

word_asc.sort()
word_des.sort()

for i in range(N):
    _, idx1 = word_asc[i]
    _, idx2 = word_des[i]
    order[idx1].append(i+1)
    order[idx2].append(i+1)

for i in range(N):
    print(*sorted(order[i]))