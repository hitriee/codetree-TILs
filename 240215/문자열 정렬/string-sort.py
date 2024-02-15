alp_string = input()

alp_cnt = {chr(ord('a')+i):0 for i in range(26)}

for alp in alp_string:
    alp_cnt[alp] += 1

new_string = ''

for alp in alp_cnt:
    new_string += alp*alp_cnt[alp]

print(new_string, sep='')