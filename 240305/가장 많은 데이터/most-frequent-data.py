n = int(input())
frequency = {}
for _ in range(n):
    word = input()
    if frequency.get(word):
        frequency[word] += 1
    else:
        frequency[word] = 1

print(max(frequency.values()))