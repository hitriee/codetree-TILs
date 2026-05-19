n = int(input())

# Please write your code here.
div_num = 10007
before1 =  before2 = 1
for i in range(n-1):
    before1, before2 = before2, (2*before1 + before2) % div_num
print(before2)

