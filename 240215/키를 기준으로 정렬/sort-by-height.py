n = int(input())
people = [input().split() for _ in range(n)]

people.sort(key=lambda person: int(person[1]))

for person in people:
    print(*person)