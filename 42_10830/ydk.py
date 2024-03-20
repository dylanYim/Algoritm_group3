N, B = map(int, input().split())
M = [list(map(int,input().split())) for _ in range(N)]

def dot(a, b):
    res = []
    for i in range(len(a)):
        res.append([])
        for j in range(len(a)):
            tmp = 0
            for k in range(len(a)):
                tmp += a[i][k] * b[k][j]
            res[i].append(tmp%1000)

    return res

def solve(m, b):
    if b == 1:
        for i in range(len(m)):
            for j in range(len(m)):
                m[i][j] %= 1000

        return m
    if b == 2:
        return dot(m, m)
    if b % 2 == 0:
        mm = solve(m,b//2)
        return dot(mm, mm)
    else:
        mm = solve(m,(b-1)//2)
        return dot(dot(mm, mm),m)

ans = solve(M,B)
for i in range(len(ans)):
    for j in range(len(ans)):
        print(ans[i][j], end=' ')
    print()