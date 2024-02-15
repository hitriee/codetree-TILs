class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = int(kor)
        self.eng = int(eng)
        self.math = int(math)

n = int(input())
students = [Student(*input().split()) for _ in range(n)]
students.sort(key=lambda student: (-student.kor, -student.eng, -student.math))

for student in students:
    print(f'{student.name} {student.kor} {student.eng} {student.math}')