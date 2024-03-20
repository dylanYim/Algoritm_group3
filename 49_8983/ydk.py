M, N, L = map(int, input().split())

hunters = list(map(int, input().split()))

animals = [list(map(int, input().split())) for _ in range(N)]

hunters.sort()

cnt = 0

for a in animals:
    if a[1] > L:
        continue
    r = L - a[1]
    upper = a[0] + r
    lower = a[0] - r
    start = 0
    end = len(hunters) - 1
    while start <= end:
        mid = (start + end) // 2
        x = hunters[mid]
        if upper >= x >= lower:
            cnt += 1
            break
        if x < lower:
            start = mid + 1
        elif x > upper:
            end = mid - 1

print(cnt)
