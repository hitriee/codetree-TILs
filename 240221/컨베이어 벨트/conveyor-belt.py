n, t = map(int, input().split())
top_numbers = input().split()
bottom_numbers = input().split()

for _ in range(t):
    last_top, last_bottom = top_numbers[-1], bottom_numbers[-1]
    for i in range(n-1, 0, -1):
        top_numbers[i] = top_numbers[i-1]
        bottom_numbers[i] = bottom_numbers[i-1]
    top_numbers[0] = last_bottom
    bottom_numbers[0] = last_top

print(' '.join(top_numbers))
print(' '.join(bottom_numbers))