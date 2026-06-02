def main():
    # 먼지가 인접한 4방향으로 확산 - 원래 먼지 // 5
    # 모든 먼지 확산 끝낸 다음 해당 칸 더해짐
    def spread():
        temp = [area[i][:] for i in range(n)]
        for i in range(n):
            for j in range(m):
                val = area[i][j]
                if val != -1:
                    fifth = val // 5
                    for k in range(4):
                        ni, nj = i+dy[k], j+dx[k]
                        if 0 <= ni < n and 0 <= nj < m and area[ni][nj] != -1:
                            temp[ni][nj] += fifth
                            temp[i][j] -= fifth
                    
        return [temp[i][:] for i in range(n)]

    # 시공의 돌풍 청소
    def clean(length, arr):
        # 위칸에서는 반시계 방향, 아래칸에서는 시계 방향
        # 바람이 불면 먼지가 바람의 방향대로 한 칸씩 이동
        # 시공의 돌풍으로 들어간 먼지는 사라짐
        val = 0
        
        for i in range(length):
            ny, nx = arr[i]
            val, area[ny][nx] = area[ny][nx], val
    
    # 시공의 돌풍 위치와 이동 순서 찾기
    def find_order():
        for k in range(2, n-1):
            if area[k][0] == -1:
                y1, y2 = k, k+1
                ccw, cw = [], []
                for j in range(1, m):
                    ccw.append((y1, j))
                    cw.append((y2, j))

                for i in range(y1-1, -1, -1):
                    ccw.append((i, m-1))
                
                for i in range(y2+1, n):
                    cw.append((i, m-1))
                
                for j in range(m-2, -1, -1):
                    ccw.append((0, j))
                    cw.append((n-1, j))
                
                for i in range(1, y1):
                    ccw.append((i, 0))
                
                for i in range(n-2, y2, -1):
                    cw.append((i, 0))

                return ccw, cw
    


    n, m, t = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]
    dy, dx = (-1, 0, 1, 0), (0, -1, 0, 1)
    ccw, cw = find_order()
    len_ccw, len_cw = len(ccw), len(cw)
    
    for _ in range(t):
        area = spread()
        clean(len_ccw, ccw)
        clean(len_cw, cw)
    
    total = 0
    for i in range(n):
        for j in range(m):
            total += area[i][j]

    return total + 2

print(main())