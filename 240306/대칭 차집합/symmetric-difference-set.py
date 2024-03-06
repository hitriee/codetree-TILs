N, M = map(int, input().split())
A = set(input().split())
B = set(input().split())

print(len(A|B) -len(B&A))