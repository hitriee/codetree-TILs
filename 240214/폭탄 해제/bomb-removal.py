class Bomb:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

bomb = Bomb(*input().split())

print(f'code : {bomb.code}\ncolor : {bomb.color}\nsecond : {bomb.sec}')