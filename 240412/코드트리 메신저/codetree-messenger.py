from collections import deque

n, q = map(int, input().split())
orders = [list(map(int, input().split())) for _ in range(q)]
messenger = [i for i in range(n + 1)]
alarm = [True for i in range(n+1)]
# OFF = 0, ON = 1
# print(f"alarm: {alarm}")

parent = {0: [], }
depth = {0: [0], }


def make_depth(parent):
    depth[1] = parent[0]
    cnt = 1
    while True:
        original = depth[cnt]
        if original is None:
            continue
        if n in original:
            break
        tmp = []
        for i in original:
            if parent.get(i):
                for j in parent[i]:
                    tmp.append(j)
        cnt += 1
        depth[cnt] = tmp
    # print(f"depth: {depth}")


def make_parent(parents):
    # print(parents)
    for i in set(parents):
        parent[i] = []
    for i, p in enumerate(parents):
        if i == 0:
            continue
        parent[p].append(i)
    # print(f"parent: {parent}")

for order in orders:
    if order[0] == 100:
        parents = [0] + order[1: n + 1]
        make_parent(parents)
        make_depth(parent)
        authority = [0] + order[n + 1:]
        # print(f"authority: {authority}")
    elif order[0] == 200:
        alarm[order[1]] = not alarm[order[1]]
    elif order[0] == 300:
        c, power = order[1:]
        authority[c] = power
    elif order[0] == 400:
        c1, c2 = order[1:]
        parents[c1], parents[c2] = parents[c2], parents[c1]
        make_parent(parents)
    elif order[0] == 500:
        c = order[1]
        cnt = 0
        for key, val in depth.items():
            if c in val:
                d = key
        if not parent.get(c):
            print(0)
            continue
        childs = deque(parent[c])
        while childs:
            # print(childs)
            child = childs.popleft()
            for key, val in depth.items():
                if child in val:
                    d_c = key
            lev = abs(d - d_c)
            if lev <= authority[child]:
                tmp = child
                alarm_flag = alarm[child]
                while True:
                    if tmp ==c:
                        break
                    p = parents[tmp]
                    # print(tmp, p, alarm_flag, alarm[p])
                    if not alarm[p]:
                        alarm_flag = False
                    tmp = p
                if alarm_flag:
                    # print(f"approved: {child}")
                    cnt += 1
            if parent.get(child):
                for i in parent[child]:
                    childs.append(i)
        print(cnt)