n, m = map(int, input().split())
dots = [tuple(map(int, input().split())) for _ in range(n)]
chosen = []
min_dist = 2e4

def calc_distance(y1, x1, y2, x2):
    return (y1 - y2)**2 + (x1 - x2)**2

def choose_dots(level, start):
    global min_dist

    if level == m:
        dist = 0
        for i in range(m):
            for j in range(i+1, m):
                new_dist = calc_distance(*chosen[i], *chosen[j])
                if dist < new_dist:
                    dist = new_dist

        if min_dist > dist:
            min_dist = dist

        return
    
    for i in range(start, n):
        chosen.append(dots[i])
        choose_dots(level+1, i+1)
        chosen.pop()


choose_dots(0, 0)

print(min_dist)