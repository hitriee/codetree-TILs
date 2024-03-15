n = int(input())
limit = sorted(map(int, input().split()))
k = int(input())
stuff_weights = sorted(map(int, input().split()))

def calc_time():
    i = start = time = 0
    while True:
        time += 1

        for j in range(start, n):
            if limit[j] >= stuff_weights[i]:
                i += 1
                if i >= k:
                    return time
            else:
                start = j+1
        
        if start >= n and i < k:
            return -1

    return time

print(calc_time())