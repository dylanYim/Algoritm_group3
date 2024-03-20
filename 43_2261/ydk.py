import sys

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
points.sort()

def distance(a, b):
    return (b[0]-a[0]) ** 2 + (b[1]-a[1]) ** 2

def brute(start, end):

    min_dis = sys.maxsize

    for i in range(start, end):
        for j in range(i + 1, end+1):
            min_dis = min(min_dis, distance(points[i], points[j]))

    return min_dis

def mid_band(start, mid, end, min_dist):

    lst = []
    mid_x = points[mid][0]
    for i in range(start, end+1):
        x_dist = points[i][0] - mid_x
        if x_dist * x_dist < min_dist:
            lst.append(points[i])

    lst.sort(key=lambda p:p[1])

    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            y_dist = lst[i][1] - lst[j][1]
            if y_dist * y_dist < min_dist:
                min_dist = min(min_dist, distance(lst[i],lst[j]))

            else:
                break

    return min_dist

def divide(start, end):

    if end - start + 1 < 4:
        return brute(start, end)

    mid = (start + end) // 2

    left = divide(start, mid)
    right = divide(mid + 1, end)

    min_dist = min(left, right)
    band = mid_band(start, mid, end, min_dist)

    return min(min_dist, band)


print(divide(0,n-1))