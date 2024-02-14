class Person:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region

n = int(input())
people = [Person(*input().split()) for _ in range(n)]

last_person = people[0]
for i in range(1, n):
    if last_person.name < people[i].name:
        last_person = people[i]

print(f'name {last_person.name}')
print(f'addr {last_person.address}')
print(f'city {last_person.region}')