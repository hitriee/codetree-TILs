n = int(input())
word_cnt = {}

for _ in range(n):
    word = ''.join(sorted(input()))
    word_cnt[word] = word_cnt.get(word, 0) + 1

print(max(word_cnt.values()))