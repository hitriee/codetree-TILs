word = input()
check = {}

for alp in word:
    if check.get(alp):
        check[alp] += 1
    else:
        check[alp] = 1

for alp in check:
    if check[alp] == 1:
        print(alp)
        break
else:
    print('None')