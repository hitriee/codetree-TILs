class Student:
    def __init__(self, height, weight, idx):
        self.h = height
        self.w = weight
        self.i = idx

N = int(input())
students = [Student(*map(int, input().split()), i) for i in range(1, N+1)]
students.sort(key=lambda student: (student.h, -student.w))

for student in students:
    print(f'{student.h} {student.w} {student.i}')