n = int(input())
set1 = set(input().split())
m = int(input())
arr = input().split()
result = ''

for i in range(m):
    result += '1 ' if arr[i] in set1 else '0 '

print(result)