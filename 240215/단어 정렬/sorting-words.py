n = int(input())
word_list = [input() for _ in range(n)]
word_list.sort()

for word in word_list:
    print(word)