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
        new_distance = calc_dist(*position, *people[j])
        if distance_arr[i][j] > new_distance:
            distance_arr[i][j] = new_distance

distance_info = [min_distance] * l2


def backtracking(level, distance, start):
    global min_distance
    
    if level == m:
        if distance < min_distance:
            min_distance = distance
        # print(path, min_distance, distance_info)
        return
    
    
    
    temp = list(distance_info)
    for i in range(start, l1):
        for j in range(l2):
            new_distance = distance_arr[i][j]
            if distance_info[j] > new_distance:
                distance_info[j] = new_distance
        
        backtracking(level+1, sum(distance_info), i+1)
        for j in range(l2):
            distance_info[j] = temp[j]


backtracking(0, 0, 0)

print(min_distance)