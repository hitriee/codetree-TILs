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
    val = nums[level]
    for i in range(k):
        if arr[i] < m:
            arr[i] += val
            new_score = score

            if arr[i] >= m:
                new_score += 1
            
            backtracking(new_level, new_score)
            
            arr[i] -= val

backtracking(0, 0)
print(max_score)