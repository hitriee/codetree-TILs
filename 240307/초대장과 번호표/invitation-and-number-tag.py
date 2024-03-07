from collections import deque

N, G = map(int, input().split())
invited = {1}
groups = []
people = [[] for _ in range(N+1)]
for i in range(G):
    headcount, *group = tuple(map(int, input().split()))
    groups.append(set(group))
    for j in group:
        people[j].append(i)

removed = [False] * G
q = deque(invited)

while q:
    num = q.popleft()
    for i in people[num]:
        if not removed[i]:
            not_invited = groups[i] - invited
            if len(not_invited) == 0:
                removed[i] = True
            elif len(not_invited) == 1:
                invited.update(not_invited)
                q.extend(not_invited)
                removed[i] = True


print(len(invited))