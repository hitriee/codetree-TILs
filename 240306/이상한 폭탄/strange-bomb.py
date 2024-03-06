N, K = map(int, input().split())
dynamite = {}
for i in range(N):
    num = int(input())
    if dynamite.get(num):
        dynamite[num].append(i)
    else:
        dynamite[num] = [i]

def find_max_num():
    sorted_num = sorted(dynamite, reverse=True)
    
    for num in sorted_num:
        length = len(dynamite[num])
        for i in range(length-1):
            if dynamite[num][i+1] - dynamite[num][i] <= K:
                return num
    
    return -1

print(find_max_num())