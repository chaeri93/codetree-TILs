k = int(input())

block = [map(int, input().split()) for _ in range(k)]

yellow = [[0] * 4 for _ in range(6)]
red = [[0] * 6 for _ in range(4)]

dx = [0, 0, 1]
dy = [0, 1, 0]
answer = 0


def clear(board, i):
    for k in range(5 - i - 3):
        board.pop()
        board.insert(0, [0, 0, 0, 0])
    return board


def check(board):
    global answer
    idx = []
    for i, b in enumerate(reversed(board)):
        if b == [1, 1, 1, 1]:
            answer += 1
            idx.append(i)
    for i in idx:
        board.pop(5 - i)
        board.insert(0, [0, 0, 0, 0])
    return board


for t, x, y in block:
    i = 0
    while i < 6:
        nx = x + dx[t - 1]
        ny = i + dy[t - 1]
        if 0 > nx or nx >= 4 or 0 > ny or ny >= 6 or red[x][i] or red[nx][ny]:
            i -= 1
            break
        if i == 5 or ny == 5:
            break
        i += 1
    nx = x + dx[t - 1]
    ny = i + dy[t - 1]
    red[x][i] = 1
    red[nx][ny] = 1
    red = list(map(list, zip(*check(list(map(list, zip(*red)))))))
    if i < 2:
        red = list(map(list, zip(*clear(list(map(list, zip(*red))), i))))

    j = 0
    while j < 6:
        nx = j + dx[t - 1]
        ny = y + dy[t - 1]
        if 0 > nx or nx >= 6 or 0 > ny or ny >= 4 or yellow[j][y] or yellow[nx][ny]:
            j -= 1
            break
        if j == 5 or nx == 5:
            break
        j += 1
    nx = j + dx[t - 1]
    ny = y + dy[t - 1]
    yellow[j][y] = 1
    yellow[nx][ny] = 1
    yellow = check(yellow)
    if j < 2:
        yellow = clear(yellow, j)

print(answer)
sum_all = 0
for i in red:
    sum_all += sum(i)
for j in yellow:
    sum_all += sum(j)
print(sum_all)