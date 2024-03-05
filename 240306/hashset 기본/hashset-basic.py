n = int(input())
hashset = set()
for _ in range(n):
    command, num = input().split()
    if num not in hashset:
        if command == 'add':
            hashset.add(num)
        else:
            print('false')
    elif command == 'remove':
        hashset.remove(num)
    elif command == 'find':
        print('true')