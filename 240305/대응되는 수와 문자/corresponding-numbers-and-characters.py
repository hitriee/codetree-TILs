n, m = map(int, input().split())
converted_values = {}
for i in range(1, n+1):
    alp = input()
    str_num = str(i)
    converted_values[alp] = str_num
    converted_values[str_num] = alp

for _ in range(m):
    print(converted_values[input()])