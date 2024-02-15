N = int(input())
numbers = list(map(int, input().split()))
check = [0] * 1001

for num in numbers:
    check[num] += 1

left, right = 1, 1000
max_total = 0
while True:
    for i in range(left, right+1):
        if check[i]:
            left = i
            break
    else:
        break
    
    check[left] -= 1

    for i in range(right, left-1, -1):
        if check[i]:
            right = i
            break
    else:
        break
    
    check[right] -= 1
    
    total = left + right
    if max_total < total:
        max_total = total

print(max_total)