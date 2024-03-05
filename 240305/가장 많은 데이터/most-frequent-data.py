n = int(input())
frequency = {}
for _ in range(n):
    word = input()
    frequency[word] = frequency.get(word, 0) + 1

print(max(frequency.values()))