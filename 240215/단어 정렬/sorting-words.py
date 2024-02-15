n = int(input())
word_list = [input() for _ in range(n)]
word_list.sort()

print(*word_list, sep='\n')