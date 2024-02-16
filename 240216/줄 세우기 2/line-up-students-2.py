class Student:
    def __init__(self, height, weight, idx):
        self.h = int(height)
        self.w = int(weight)
        self.i = idx

N = int(input())
students = [Student(*input().split(), i) for i in range(1, N+1)]
students.sort(key=lambda student: (student.h, -student.w))

for student in students:
    print(f'{student.h} {student.w} {student.i}')