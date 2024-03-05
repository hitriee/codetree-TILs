n = int(input())
hashmap = {}

for _ in range(n):
    command = input().split()
    if command[0] == 'add':
        hashmap[command[1]] = command[2]
    elif command[0] == 'remove':
        del hashmap[command[1]]
    else:
        print(hashmap.get(command[1]))