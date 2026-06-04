def main():
    def calc_row():
        max_m = m
        for i in range(n):
            cnt = {}
            for j in range(m):
                num = arr[i][j]
                if num != 0:
                    cnt[num] = cnt.get(num, 0) + 1
            result = sorted(cnt.items(), key=lambda x: (x[1], x[0]))
            next_m = len(result)
            twice_m = min(2*next_m, 100)
            arr[i] = []
            for j in range(twice_m//2):
                arr[i].extend(result[j])

            if max_m < twice_m:
                max_m = twice_m

        for i in range(n):
            arr[i].extend([0] * (max_m - len(arr[i])))

        return max_m

    def calc_col():
        max_n = n
        for j in range(m):
            cnt = {}
            for i in range(n):
                num = arr[i][j]
                if num != 0:
                    cnt[num] = cnt.get(num, 0) + 1

            result = sorted(cnt.items(), key=lambda x: (x[1], x[0]))
            next_n = len(result)
            twice_n = min(2 * next_n, 100)

            for _ in range(twice_n - max_n):
                arr.append([0] * m)

            for i in range(twice_n//2):
                arr[2 * i][j] = result[i][0]
                arr[2 * i + 1][j] = result[i][1]

            for i in range(twice_n, max_n):
                arr[i][j] = 0

            if max_n < twice_n:
                max_n = twice_n


        while arr[-1].count(0) == m:
            arr.pop()
            max_n -= 1

        return max_n

    def int_input(func=int):
        return map(func, input().split())

    r, c, k = int_input(lambda x: int(x) - 1)
    arr = [list(int_input()) for _ in range(3)]
    k += 1
    n = m = 3
    for duration in range(101):
        if n > r and m > c and arr[r][c] == k:
            return duration
        if n >= m:
            m = calc_row()
        else:
            n = calc_col()

    return -1


print(main())