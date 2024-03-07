n = int(input())
energy_info = list(map(int, input().split()))
cost_info = list(map(int, input().split()))
min_total = energy = 0
min_cost = cost_info[0]

for i in range(1, n):
    energy += energy_info[i-1]
    if cost_info[i] < min_cost:
        min_total += energy * min_cost
        min_cost = cost_info[i]
        energy = 0

min_total += energy * min_cost

print(min_total)