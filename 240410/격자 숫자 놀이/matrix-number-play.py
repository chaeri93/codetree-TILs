from collections import Counter


def sort_row(A):
    result = []
    for i in A:
        i = [j for j in i if j != 0]
        count = sorted(Counter(i).items(), key=lambda x: (x[1], x[0]))
        result.append([elem for sublist in count for elem in sublist])
    max_len = max(len(elem) for elem in result)
    for r in result:
        r += [0] * (max_len - len(r))
        if len(r) > 100:
            r = r[:100]
    return result


def sort_column(A):
    result = []
    for i in A:
        i = [j for j in i if j != 0]
        count = sorted(Counter(i).items(), key=lambda x: (x[1], x[0]))
        result.append([elem for sublist in count for elem in sublist])
    max_len = max(len(elem) for elem in result)
    for r in result:
        r += [0] * (max_len - len(r))
        if len(r) > 100:
            r = r[:100]
    return list(zip(*result))


if __name__ == '__main__':

    r, c, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(3)]

    cnt = 0
    while True:
        if len(A) >= r and len(A[0]) >= c and A[r - 1][c - 1] == k:
            print(cnt)
            break
        if cnt > 100:
            print(-1)
            break
        if len(A) >= len(A[0]):
            A = sort_row(A)
        else:
            A = sort_column(list(zip(*A)))
        cnt += 1