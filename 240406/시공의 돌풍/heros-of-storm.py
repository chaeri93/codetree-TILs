import sys

input = sys.stdin.readline


def diffusion(array, n, m):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    tmp_arr = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if array[i][j] != 0 and array[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and array[nx][ny] != -1:
                        tmp_arr[nx][ny] += array[i][j] // 5
                        tmp += array[i][j] // 5
                array[i][j] -= tmp

    for i in range(n):
        for j in range(m):
            array[i][j] += tmp_arr[i][j]


def clean_up(array, up, n, m):
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    before = 0
    idx = 0
    x, y = up, 1
    while True:
        nx = x + dx[idx]
        ny = y + dy[idx]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            idx += 1
            continue
        array[x][y], before = before, array[x][y]
        x = nx
        y = ny


def clean_down(array, down, n, m):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    before = 0
    idx = 0
    x, y = down, 1
    while True:
        nx = x + dx[idx]
        ny = y + dy[idx]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            idx += 1
            continue
        array[x][y], before = before, array[x][y]
        x = nx
        y = ny


if __name__ == '__main__':
    n, m, t = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    up = -1
    down = -1
    for i in range(n):
        if array[i][0] == -1:
            up = i
            down = i + 1
            break

    for _ in range(t):
        diffusion(array, n, m)
        clean_up(array, up, n, m)
        clean_down(array, down, n, m)

    answer = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] > 0:
                answer += array[i][j]

    print(answer)