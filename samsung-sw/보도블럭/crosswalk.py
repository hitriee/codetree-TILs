def int_input():
    return map(int, input().split())

def can_pass(option):
    cnt = 0
    for i in range(N):
        before = heights[i][0] if option == 'row' else heights[0][i]
        to_top = to_bottom = False
        length = 1
        for j in range(1, N):
            now = heights[i][j] if option == 'row' else heights[j][i]
            if now == before:
                length += 1
            elif now == before - 1:
                if to_bottom and length < L:
                    break
                to_top = False
                to_bottom = True
                length = 1
            # 높아짐
            elif now == before + 1:
                if to_bottom:
                    if length < 2*L:
                        break
                elif length < L:
                    break
                to_bottom = False
                length = 1
                to_top = True
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