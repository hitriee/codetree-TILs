n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
max_score = 0
arr = [1] * k

def backtracking(level):
    global max_score

    if level == n:
        score = 0
        for i in range(k):
            if arr[i] >= m:
                score += 1
        
        if max_score < score:
            max_score = score
        return

    new_level = level + 1
    for i in range(k):
        arr[i] += nums[level]
        
        backtracking(new_level)
        
        arr[i] -= nums[level]

backtracking(0)
print(max_score)