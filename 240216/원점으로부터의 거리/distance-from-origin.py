class Spot:
    def __init__(self, x, y, num):
        self.d = abs(int(x)) + abs(int(y))
        self.n = num

N = int(input())
spots = [Spot(*input().split(), i) for i in range(1, N+1)]
spots.sort(key=lambda spot: (spot.d, spot.n))

for spot in spots:
    print(spot.n)