n, t = map(int, input().split())
top_numbers = input().split()
bottom_numbers = input().split()

for _ in range(t):
    last = top_numbers[-1:]
    top_numbers = bottom_numbers[-1:] + top_numbers[:-1]
    bottom_numbers = last + bottom_numbers[:-1]

print(' '.join(top_numbers))
print(' '.join(bottom_numbers))