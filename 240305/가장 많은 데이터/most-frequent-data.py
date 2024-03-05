n = int(input())
frequency = {}
max_freq = 1
for _ in range(n):
    word = input()
    if frequency.get(word):
        frequency[word] += 1
        if max_freq < frequency[word]:
            max_freq = frequency[word]
    else:
        frequency[word] = 1


print(max_freq)