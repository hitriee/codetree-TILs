n, k = map(int, input().split())
numbers = list(map(int, input().split()))
check = {}
cnt = 0

for number in numbers:
    if check.get(number):
        check[number] += 1
    else:
        check[number] = 1

sorted_keys = sorted(check)
m = len(sorted_keys)

for i in range(m):
    num1 = sorted_keys[i]
    val1 = check[num1]
    if num1*3 == k:
        cnt += ((val1-2)*(val1-1)*val1)//6
    elif check.get(k-num1*2):
        cnt += check[k-num1*2]

    for j in range(i+1, m):
        num2 = sorted_keys[j]
        val2 = check[num2]
        num3 = k - (num1 + num2)
        if num3 == num2:
            cnt += val1 * (((val2-1)*val2)//2)
        elif num3 > num2 and check.get(num3):
            cnt += val1 * val2 * check[num3]
        
print(cnt)