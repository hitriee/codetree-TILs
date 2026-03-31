n = int(input())
arr = [0] + list(map(int, input().split()))

if n == 1:
    print(1)
elif n == 2:
    print(2 if arr[0] < arr[1] else 1)
else:
    max_arr = [0] * (n+1)
    max_arr[1] = 1

    for i in range(2, n+1):
        num1 = max_arr[i-2] + (1 if arr[i-2] < arr[i] else 0)
        num2 = max_arr[i-1] + (1 if arr[i-1] < arr[i] else 0)
        max_arr[i] = max(num1, num2)

    print(max(max_arr))