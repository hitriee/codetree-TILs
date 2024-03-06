N, K = map(int, input().split())
people = list(range(N+1))
possible_seat = [{i} for i in range(N+1)]
commands = [tuple(map(int, input().split())) for _ in range(K)]

for _ in range(3):
    for i, j in commands:
        people[i], people[j] = people[j], people[i]
        possible_seat[people[i]].add(i)
        possible_seat[people[j]].add(j)

for i in range(1, N+1):
    print(len(possible_seat[i]))