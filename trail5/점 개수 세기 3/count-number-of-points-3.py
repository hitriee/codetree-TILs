n, q = map(int, input().split())
points = list(map(int, input().split()))

# Please write your code here.

def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        mid_num = points[mid]
        if mid_num == target:
            return mid
        elif mid_num < target:
            start = mid + 1
        else:
            end = mid - 1

points.sort()
for _ in range(q):
    a, b = map(int, input().split())
    left = binary_search(0, n-1, a)
    right = binary_search(left, n-1, b)

    print(right - left + 1)
