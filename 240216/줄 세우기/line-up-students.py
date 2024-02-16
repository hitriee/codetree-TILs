class Student:
    def __init__(self, height, weight, num):
        self.h = int(height)
        self.w = int(weight)
        self.n = num

N = int(input())
students = [Student(*input().split(), i) for i in range(1, N+1)]
students.sort(key=lambda student: (-student.h, -student.w, student.n))

for student in students:
    print(f'{student.h} {student.w} {student.n}')