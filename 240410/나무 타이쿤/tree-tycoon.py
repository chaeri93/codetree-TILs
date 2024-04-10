n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
move = [list(map(int, input().split())) for _ in range(m)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]


def move_nutrient(nutrients, m):
    d, p = m
    result = []
    for x, y in nutrients:
        nx = x + dx[d-1] * p
        ny = y + dy[d-1] * p
        if nx < 0:
            nx += n
        elif nx >= n:
            nx -= n
        if ny < 0:
            ny += n
        elif ny >= n:
            ny -= n
        result.append([nx, ny])
    return result


def cutdown(nutrients):
    new = []
    for i in range(n):
        for j in range(n):
            if [i, j] in nutrients:
                continue
            if board[i][j] >= 2:
                board[i][j] -= 2
                new.append([i, j])
    return new


nutrients = [[n - 1, 0], [n - 2, 0], [n - 1, 1], [n - 2, 1]]

di = [-1, -1, 1, 1]
dj = [1, -1, 1, -1]

for m in move:
    nutrients = move_nutrient(nutrients, m)
    for x, y in nutrients:
        board[x][y] += 1
    for i, j in nutrients:
        cnt = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and board[ni][nj]:
                cnt += 1
        board[i][j] += cnt
    nutrients = cutdown(nutrients)

answer = 0
for i in range(n):
    for j in range(n):
        answer += board[i][j]
print(answer)