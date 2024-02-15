alp_string = input()

alp_cnt = {}

for alp in alp_string:
    if alp_cnt.get(alp):
        alp_cnt[alp] += 1
    else:
        alp_cnt[alp] = 1

new_string = ''

for alp in sorted(alp_cnt):
    new_string += alp*alp_cnt[alp]

print(new_string, sep='')