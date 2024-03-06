n = int(input())
set1 = set(input().split())
m = int(input())
arr = input().split()

for i in range(m):
    arr[i] = '1' if arr[i] in set1 else '0'

print(' '.join(arr))