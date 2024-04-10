import copy

n, m, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
move = [list(map(int, input().split())) for _ in range(q)]


def rotate(x, d, k):
    if not d:
        k = m - k
    cnt = x
    while (x <= n):
        tmp = board[x - 1][k:] + board[x - 1][:k]
        board[x - 1] = tmp
        x += cnt


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for x, d, k in move:
    rotate(x, d, k)

    cnt = 0
    new_board = copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if nj < 0:
                    nj += m
                elif nj >= m:
                    nj -= m
                if 0 <= ni < n and board[i][j] == board[ni][nj] and new_board[ni][nj]:
                    new_board[ni][nj] = 0
                    if new_board[i][j]:
                        new_board[i][j] = 0
                    cnt += 1

    if not cnt:
        avg = 0
        total = 0
        for i in range(n):
            for j in range(m):
                if new_board[i][j]:
                    total += 1
                    avg += new_board[i][j]
        avg = avg // total
        for i in range(n):
            for j in range(m):
                if new_board[i][j]:
                    if new_board[i][j] > avg:
                        new_board[i][j] -= 1
                    elif new_board[i][j] < avg:
                        new_board[i][j] += 1
    board = new_board

answer = 0
for i in board:
    answer += sum(i)

print(answer)