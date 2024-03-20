N, M = map(int, input().split())
trees = list(map(int, input().split()))

def find_height(f, c):
    start = f
    end = c
    while start <= end:
        h = (start + end) // 2
        cuttings = sum([(t-h) for t in trees if t-h > 0])

        if cuttings >= M:
            start = h + 1
        elif cuttings < M:
            end = h - 1

    return end

print(find_height(0, max(trees)))