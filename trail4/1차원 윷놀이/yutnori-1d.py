n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
max_score = 0
arr = [1] * k

def backtracking(level, score):
    global max_score
    
    if score == k:
        max_score = k
        return

    if level == n:
        if max_score < score:
            max_score = score
        return

    new_level = level + 1
    for i in range(k):
        val = arr[i]
        if val >= m:
            continue
        
        new_val = val + nums[level]
        
        new_score = score + 1 if new_val >= m else score
        
        arr[i] = new_val
        
        backtracking(new_level, new_score)
        
        arr[i] = val

backtracking(0, 0)
print(max_score)