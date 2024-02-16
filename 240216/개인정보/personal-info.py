class Person:
    def __init__(self, name, height, weight):
        self.n = name
        self.h = int(height)
        self.w = weight

people = [Person(*input().split()) for _ in range(5)]

people.sort(key=lambda person: person.n)
print('name')
for person in people:
    print(f'{person.n} {person.h} {person.w}')

people.sort(key=lambda person: -person.h)
print('\nheight')
for person in people:
    print(f'{person.n} {person.h} {person.w}')