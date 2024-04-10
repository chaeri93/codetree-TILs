from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

answer = 1e9
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

virus = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus.append([i, j])


def bfs(v):
    q = deque(v)
    visited = [[-1 for _ in range(n)]  for _ in range(n)]
    for x, y in v:
        visited[x][y] = 0
    m = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and board[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
                if board[nx][ny] != 2:
                    m = max(visited[x][y] + 1, m)

    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and board[i][j] == 0:
                return 1e9
    return m


def combination(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(0, len(arr)):  # 1번 루프라 하고
        elem = arr[i]
        rest_arr = arr[i + 1:]
        for c in combination(rest_arr, n - 1):  # 2번 루프라 하면
            result.append([elem] + c)

    return result


for v in combination(virus, m):
    answer = min(bfs(v), answer)

if answer == 1e9:
    print(-1)
else:
    print(answer)