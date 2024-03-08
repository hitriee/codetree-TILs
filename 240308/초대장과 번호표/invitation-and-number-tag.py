from collections import deque

_, G = map(int, input().split())
invited = {1}
groups = deque()
for _ in range(G):
    _, *group = map(int, input().split())
    groups.append(set(group))

while True:
    changed = False
    for _ in range(G):
        group = groups.popleft()
        not_invited = set(group) - invited
        if len(not_invited) <= 1:
            G -= 1
            invited.update(not_invited)
            changed = True
        else:
            groups.append(not_invited)
        
    if not changed:
        break

print(len(invited))