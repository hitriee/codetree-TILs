n, m = map(int, input().split())
hospital, people = [], []
for i in range(n):
    row = input().split()
    for j in range(n):
        if row[j] == '1':
            people.append((i, j))
        elif row[j] == '2':
            hospital.append((i, j))

min_distance = int(5e4)
l1, l2 = len(hospital), len(people)

def calc_dist(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)

distance_arr = [[min_distance] * l2 for _ in range(l1)]

for i in range(l1):
    position = hospital[i]
    for j in range(l2):
        distance_arr[i][j] = calc_dist(*position, *people[j])


def backtracking(level, distance_info, start):
    global min_distance
    
    if level == m:
        distance = sum(distance_info)
        if distance < min_distance:
            min_distance = distance
        return
    
    
    for i in range(start, l1):
        new_distance_info = [min(distance_arr[i][j], distance_info[j]) for j in range(l2)]
        
        backtracking(level+1, new_distance_info, i+1)


backtracking(0, [min_distance] * l2, 0)

print(min_distance)
