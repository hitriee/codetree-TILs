n = int(input())
latest_info = ['2111-12-31', '', '']

for _ in range(n):
    weather = input().split()
    if weather[-1] == 'Rain' and latest_info[0] > weather[0]:
        latest_info = weather

print(*latest_info)