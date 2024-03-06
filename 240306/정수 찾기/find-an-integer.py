_ = int(input())
a = set(input().split())
m = int(input())
b = input().split()

for i in range(m):
    b[i] = '1' if b[i] in a else '0'

print('\n'.join(b))