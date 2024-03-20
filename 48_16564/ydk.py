import sys

N, K = map(int, input().split())
X = []
for _ in range(N):
    X.append(int(input()))

def check_min(t,k):
    sum = 0
    for x in X:
        if x <= t:
            sum += t - x
    return k-sum


def solve():
    start = 0
    end = max(X) + K
    while start <= end:
        mid = (start + end) // 2
        k = check_min(mid, K)
        if k == 0:
            return mid
        if k < 0:
            end = mid - 1
        else:
            start = mid + 1

    return end

print(solve())
