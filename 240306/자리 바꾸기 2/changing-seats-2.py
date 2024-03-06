N, K = map(int, input().split())
people = list(range(N))
possible_seat = [{i} for i in range(N)]
commands = [tuple(map(lambda x:int(x)-1, input().split())) for _ in range(K)]

for _ in range(3):
    for i, j in commands:
        people[i], people[j] = people[j], people[i]
        possible_seat[people[i]].add(i)
        possible_seat[people[j]].add(j)

for i in range(N):
    print(len(possible_seat[i]))