n = int(input())
poles = list(map(int, input().split()))
poles.sort()

longest_pole = sum(poles)
min_cost = 0

for i in range(n-1):
    pole = poles[i]
    longest_pole -= pole
    min_cost += longest_pole * pole

print(min_cost)