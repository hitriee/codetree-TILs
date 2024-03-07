_, G = map(int, input().split())
invited = {1}
groups = []
for _ in range(G):
    headcount, *group = map(int, input().split())
    groups.append((headcount, set(group)))

removed = [False] * G


while True:
    changed = False
    for i in range(G):
        if not removed[i]:
            headcount, group = groups[i]
            not_invited = set(group) - invited
            if len(not_invited) <= 1:
                invited.update(not_invited)
                removed[i] = True
                changed = True
        
    if not changed:
        break

print(len(invited))