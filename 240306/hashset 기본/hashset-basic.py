n = int(input())
hashset = set()
for _ in range(n):
    command, num = input().split()
    if command == 'add':
        hashset.add(num)
    elif command == 'remove':
        hashset.remove(num)
    else:
        print('true' if num in hashset else 'false')