A = list(input())
length = len(A)

if A[0] != A[-1]:
    t = 0
else:
    before_alp, cnt = A[-1], 1
    for i in range(length-2, 0, -1):
        if before_alp != A[i]:
            t = length - i
            break
    else:
        t = 0

for _ in range(t):
    last_alp = A[-1]
    for i in range(length-1, 0, -1):
        A[i] = A[i-1]
    A[0] = last_alp
    
before_alp, cnt, new_A = A[0], 1, ''
for i in range(1, length):
    if before_alp == A[i]:
        cnt += 1
    else:
        new_A += before_alp + str(cnt)
        before_alp, cnt = A[i], 1

new_A += before_alp + str(cnt)

print(len(new_A))