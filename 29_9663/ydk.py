n = int(input())

cnt = 0
def bt(N, row, col, col_set, diagonal1_set, diagonal2_set, board):
    global cnt

    if row == N or col == N:
        return 0
    if col in col_set:
        return
    diagonal1 = row - col
    diagonal2 = row + col
    if diagonal1 in diagonal1_set:
        return
    if diagonal2 in diagonal2_set:
        return

    board.append(col)

    if len(board) == N:
        cnt += 1
        board.pop()
        return

    col_set.add(col)
    diagonal1_set.add(diagonal1)
    diagonal2_set.add(diagonal2)

    for x in range(N):
        bt(N, row+1, x, col_set, diagonal1_set, diagonal2_set, board)

    col_set.remove(col)
    diagonal1_set.remove(diagonal1)
    diagonal2_set.remove(diagonal2)
    board.pop()

def process(N):
    col_set = set()
    diagonal1_set = set()
    diagonal2_set = set()

    for i in range(N):
        bt(N, 0, i, col_set, diagonal1_set, diagonal2_set, [])

    return cnt

print(process(n))