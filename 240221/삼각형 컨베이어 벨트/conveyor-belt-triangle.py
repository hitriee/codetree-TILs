n, t = map(int, input().split())
left = input().split()
right = input().split()
bottom = input().split()

for _ in range(t):
    last_l, last_r, last_b = left[-1], right[-1], bottom[-1]
    for i in range(n-1, 0, -1):
        left[i] = left[i-1]
        right[i] = right[i-1]
        bottom[i] = bottom[i-1]

    left[0], right[0], bottom[0] = last_b, last_l, last_r

print(' '.join(left))
print(' '.join(right))
print(' '.join(bottom))