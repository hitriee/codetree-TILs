_ = int(input())
a = set(input().split())
m = int(input())
b = input().split()
c = ['0'] * m

for i in range(m):
    if b[i] in a:
        c[i] = '1'

print('\n'.join(c))