from sys import stdin

new_input = stdin.readline
n = int(new_input())
word_cnt = {}

for _ in range(n):
    word = ''.join(sorted(new_input().rstrip()))
    word_cnt[word] = word_cnt.get(word, 0) + 1

print(max(word_cnt.values()))