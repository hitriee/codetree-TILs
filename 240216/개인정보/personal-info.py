class Person:
    def __init__(self, name, height, weight):
        self.n = name
        self.h = int(height)
        self.w = weight

people = [Person(*input().split()) for _ in range(5)]

return_n = lambda person : person.n
return_h = lambda person : -person.h

for func, word in (return_n, 'name'), (return_h, '\nheight'):
    people.sort(key=func)
    print(word)

    for person in people:
        print(f'{person.n} {person.h} {person.w}')