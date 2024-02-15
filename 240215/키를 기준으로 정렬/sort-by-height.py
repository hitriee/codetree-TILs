class Person:
    def __init__(self, name, height, year):
        self.name = name
        self.height = int(height)
        self.year = year

n = int(input())
people = [Person(*input().split()) for _ in range(n)]

people.sort(key=lambda person: person.height)

for person in people:
    print(f'{person.name} {person.height} {person.year}')