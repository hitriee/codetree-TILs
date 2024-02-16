class Person:
    def __init__(self, name, height, weight):
        self.n = name
        self.h = int(height)
        self.w = weight

people = [Person(*input().split()) for _ in range(5)]

def return_n(person):
    return person.n

def return_h(person):
    return -person.h

func_tuple = (return_n, return_h)
print_tuple = ('name', '\nheight')


for i in range(2):
    people.sort(key=func_tuple[i])
    print(print_tuple[i])

    for person in people:
        print(f'{person.n} {person.h} {person.w}')