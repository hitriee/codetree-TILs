from sys import stdin

def to_int():
    return int(stdin.readline())

N = to_int()
numbers = [to_int() for _ in range(N)]
acc = [0]
for i in range(N):
    acc.append(acc[-1] + numbers[i])

def find_max_size():
    for size in range(N, 1, -1):
        for i in range(N-size+1):
            if (acc[i+size] - acc[i]) % 7 == 0:
                return size
    
    for i in range(N):
        if numbers[i] % 7 == 0:
            return 1
    
    return 0

print(find_max_size())