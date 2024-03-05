n, k = map(int, input().split())
numbers = list(map(int, input().split()))
check = {}

for number in numbers:
    if check.get(number):
        check[number] += 1
    else:
        check[number] = 1

sorted_keys = sorted(check)
m = len(sorted_keys)

def comb(m, r):
    num1, num2 = m, 1
    for i in range(1, r):
        num1 *= (m-i)
        num2 *= (i+1)
    
    return num1//num2


def cnt_comb():
    cnt = 0

    for i in range(m):
        num1 = sorted_keys[i]
        val1 = check[num1]
        num2 = k-num1*2
        if num1 == num2:
            cnt += comb(val1, 3)
        elif num1 < num2 and check.get(num2):
            cnt += comb(val1, 2) * check[num2]

        for j in range(i+1, m):
            num2 = sorted_keys[j]
            val2 = check[num2]
            num3 = k - (num1 + num2)
            if num3 == num2:
                cnt += val1 * comb(val2, 2)
            elif num2 < num3 and check.get(num3):
                cnt += val1 * val2 * check[num3]
            
    return cnt

print(cnt_comb())