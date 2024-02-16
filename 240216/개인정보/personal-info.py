class Person:
    def __init__(self, name, height, weight):
        self.n = name
        self.h = int(height)
        self.w = weight

people = [Person(*input().split()) for _ in range(5)]
sorted_by_name = sorted(people, key=lambda person: person.n)
sorted_by_height = sorted(people, key=lambda person: -person.h)

print('name')
for person in sorted_by_name:
    print(f'{person.n} {person.h} {person.w}')

print('\nheight')
for person in sorted_by_height:
    print(f'{person.n} {person.h} {person.w}')