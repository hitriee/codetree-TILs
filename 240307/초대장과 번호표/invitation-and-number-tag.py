from collections import deque

_, G = map(int, input().split())
invited = {1}
groups = deque()
for _ in range(G):
    _, *group = map(int, input().split())
    groups.append(tuple(group))

while True:
    changed = False
    for _ in range(G):
        group = groups.popleft()
        not_invited = set(group) - invited
        if len(not_invited) <= 1:
            invited.update(not_invited)
            changed = True
            G -= 1
        else:
            groups.append(group)
    
    if not changed:
        break

print(len(invited))