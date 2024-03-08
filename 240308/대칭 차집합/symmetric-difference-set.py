N, M = map(int, input().split())
A = set(input().split())
B = set(input().split())

answer = N+M

for a in A:
    if a in B:
        answer -= 2

print(answer)