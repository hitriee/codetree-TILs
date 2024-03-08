n = int(input())
word_cnt = {}
max_cnt = 0

for _ in range(n):
    word = ''.join(sorted(input()))
    word_cnt[word] = word_cnt.get(word, 0) + 1

for cnt in word_cnt.values():
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)