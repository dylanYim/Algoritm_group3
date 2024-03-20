N, C = map(int, input().split())
X = [int(input()) for _ in range(N)]
X.sort()
min_d = 1
max_d = X[N-1] - X[0]


def binary_search(c):
    start = min_d
    end = max_d
    while start <= end:
        dis = (start + end) // 2
        cnt = count_possible(dis)

        if cnt >= c:
            start = dis + 1

        elif cnt < c:
            end = dis - 1

    return end


def count_possible(d):
    count = 1
    last_house = X[0]
    for i in range(1, N):
        if (X[i] - last_house) >= d:
            count += 1
            last_house = X[i]

    return count


print(binary_search(C))