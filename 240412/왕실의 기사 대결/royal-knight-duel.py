import copy
from collections import deque

l, n, q = map(int, input().split())
chess = [list(map(int, input().split())) for _ in range(l)]
knight = [list(map(int, input().split())) for _ in range(n)]
order = [list(map(int, input().split())) for _ in range(q)]

knight = {i + 1: k + [0] for i, k in enumerate(knight)}

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def make_square(knight):
    result = {}
    result_idx = {}
    for key, val in knight.items():
        r, c, h, w, k, d = val
        result[key] = [k, d]
        result_idx[key] = []
        for i in range(r - 1, r + h - 1):
            for j in range(c - 1, c + w - 1):
                result_idx[key].append([i, j])
    return result, result_idx


knight, knight_idx = make_square(knight)

# print(knight, knight_idx)


def attack(i):
    idx = knight_idx[i]
    cnt = 0
    for x, y in idx:
        if chess[x][y] == 1:
            cnt += 1
    if knight[i][0] <= cnt:
        knight.pop(i)
        knight_idx.pop(i)
    else:
        knight[i][0] -= cnt
        knight[i][1] += cnt

def move_knight(i, d):
    if not knight_idx.get(i):  # 사라진 기사의 번호가 주어졌을때
        return 0
    q = deque(knight_idx[i])
    visited = [[0] * l for _ in range(l)]
    for x, y in knight_idx[i]:
        visited[x][y] = 1
    can_go = True
    tmp_idx = set([i])
    while q:
        x, y = q.popleft()
        nx = x + dx[d]
        ny = y + dy[d]
        if ny < 0 or ny >= l or nx < 0 or nx >= l or chess[nx][ny] == 2:
            can_go = False
            break
        if visited[nx][ny]:
            continue
        for key, val in knight_idx.items():
            if key != i:
                if [nx, ny] in val:
                    q += knight_idx[key]
                    tmp_idx.add(key)
                    visited[nx][ny] = 1
                    break

    if not can_go:
        return 0

    for key in tmp_idx:
        tmp = []
        for x, y in knight_idx[key]:
            nx = x + dx[d]
            ny = y + dy[d]
            tmp.append([nx, ny])
        knight_idx[key] = tmp

    # print(knight_idx)

    for j in tmp_idx:
        if j == i:
            continue
        attack(j)
    # print(knight)

for i, d in order:
    move_knight(i, d)

answer = 0
for k in knight.values():
    answer += k[1]
print(answer)