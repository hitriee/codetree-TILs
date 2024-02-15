n = int(input())
arr = list(map(int, input().split()))
arr.sort()

print(*arr)
print(*reversed(arr))