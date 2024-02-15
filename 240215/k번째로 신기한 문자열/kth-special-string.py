n, k, T = input().split()
n, k = map(int, [n, k])
limit = len(T)
word_list = []

for _ in range(n):
    word = input()
    if word[:limit] == T:
        word_list.append(word)

word_list.sort()
print(word_list[k-1])