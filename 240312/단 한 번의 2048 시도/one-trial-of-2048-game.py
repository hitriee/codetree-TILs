arr = [list(map(int, input().split())) for _ in range(4)]
direction = input()
for j in range(4):
    temp1, temp2 = [], []
    for i in range(4):
        if arr[i][j]:
            temp1.append(arr[i][j])
    
    if direction == 'U':
        for i in range(len(temp1)-1):
            if temp1[i]:
                if temp1[i] == temp1[i+1]:
                    temp2.append(temp1[i] * 2)
                    temp1[i+1] = 0
                else:
                    temp2.append(temp1[i])
        
        if temp1 and temp1[-1]:
            temp2.append(temp1[-1])

        for i in range(len(temp2)):
            arr[i][j] = temp2[i]
        for i in range(len(temp2), 4):
            arr[i][j] = 0

    elif direction == 'D':
        for i in range(len(temp1)-1, 0, -1):
            if temp1[i]:
                if temp1[i] == temp1[i-1]:
                    temp2.append(temp1[i] * 2)
                    temp1[i-1] = 0
                else:
                    temp2.append(temp1[i])
        
        if temp1 and temp1[0]:
            temp2.append(temp1[0])

        for i in range(3, 3-len(temp2), -1):
            arr[i][j] = temp2[3-i]
        
        for i in range(3-len(temp2)+1):
            arr[i][j] = 0
        
    elif direction == 'R':
        
        for j in range(len(temp1)-1, 0, -1):
            if temp1[j]:
                if temp1[j] == temp1[j-1]:
                    temp2.append(temp1[j] * 2)
                    temp1[j-1] = 0
                else:
                    temp2.append(temp1[j])
        
        if temp1 and temp1[0]:
            temp2.append(temp1[0])
        
        arr[i] = [0] * (4 - len(temp2)) + temp2[::-1]

    else:
        for j in range(len(temp1)-1):
            if temp1[j]:
                if temp1[j] == temp1[j+1]:
                    temp2.append(temp1[j] * 2)
                    temp1[j+1] = 0
                else:
                    temp2.append(temp1[j])
        
        if temp1 and temp1[-1]:
            temp2.append(temp1[-1])
        
        arr[i] = temp2 + [0] * (4 - len(temp2))

for i in range(4):
    print(*arr[i])