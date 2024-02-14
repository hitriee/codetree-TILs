class Weather:
    def __init__(self, date, day, result):
        self.date = date
        self.day = day
        self.result = result
    
n = int(input())
latest_info = Weather('2111-12-31', 'Wed', 'Rain')

for _ in range(n):
    weather = Weather(*input().split())
    if weather.result == 'Rain' and latest_info.date > weather.date:
        latest_info = weather

print(f'{latest_info.date} {latest_info.day} {latest_info.result}')