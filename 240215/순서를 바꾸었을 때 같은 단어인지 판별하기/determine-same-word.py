word1 = input()
word2 = input()
check = {}

for alp in word1:
    if check.get(alp):
        check[alp] += 1
    else:
        check[alp] = 1

for alp in word2:
    if check.get(alp, 0) > 0:
        check[alp] -= 1
    else:
        print('No')
        break
else:
    print('Yes')