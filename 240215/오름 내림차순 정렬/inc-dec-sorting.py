n = int(input())
arr = list(map(int, input().split()))

print(*sorted(arr))
print(*sorted(arr, reverse=True))