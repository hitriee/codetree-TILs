from collections import deque

_, G = map(int, input().split())
invited = set()
groups = deque()
for _ in range(G):
    headcount, *group = map(int, input().split())
    if headcount <= 2:
        invited.update(group)
        G -= 1
    else:
        invited.add(group[0])
        groups.append((headcount, set(group)))

while True:
    changed = False
    for _ in range(G):
        headcount, group = groups.popleft()
        not_invited = group - invited
        if len(group - invited) <= 1:
            invited.update(not_invited)
            changed = True
            G -= 1
        else:
            groups.append((headcount, group))
    
    if not changed:
        break

print(len(invited))