def int_input():
    return map(int, input().split())

def can_pass(option):
    cnt = 0
    # 평지 - 0, 낮아지는 경사로 - 1, 높아지는 경사로 - 2
    for i in range(N):
        before = heights[i][0] if option == 'row' else heights[0][i]
        to_top = to_bottom = False
        length = 1
        for j in range(1, N):
            now = heights[i][j] if option == 'row' else heights[j][i]
            if now == before:
                length += 1
            # 낮아짐
            elif now == before - 1:
                # 0 - 1 : 상관 없음
                # 1 - 1 : 이전 길이가 경사로 길이 이상이어야 함
                if to_bottom and length < L:
                    break
                # 2 - 1 : 상관 없음
                
                to_top = False
                to_bottom = True
                length = 1
            # 높아짐
            elif now == before + 1:
                # 0 - 2 : 이전 길이가 경사로 길이 이상이어야 함
                # 1 - 2 : 이전 길이가 2 * 경사로 길이 이상이어야 함
                if to_bottom:
                    if length < 2*L:
                        break
                elif length < L:
                    break
                to_bottom = False
                length = 1
                # 2 - 2 : 상관 없음
                to_top = True
            # 높이 차이가 1보다 큰 경우
            else:
                break
            before = now
        else:
            if not to_bottom or length >= L:
                cnt += 1
    return cnt


N, L = int_input()
heights = [list(int_input()) for _ in range(N)]
total_cnt = 0

total_cnt += can_pass('row')
total_cnt += can_pass('col')

print(total_cnt)