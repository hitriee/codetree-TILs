n = int(input())
hashmap = {}

for _ in range(n):
    command, *nums = input().split()
    if command == 'add':
        hashmap[nums[0]] = nums[1]
    elif command == 'remove':
        del hashmap[nums[0]]
    else:
        print(hashmap.get(nums[0]))