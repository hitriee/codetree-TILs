n, k, T = input().split()
n, k = map(int, [n, k])
limit = len(T)
word_list = []

for _ in range(n):
    word = input()
    if word[:limit] == T:
        word_list.append(word[limit:])

word_list.sort()
print(T+word_list[k-1])