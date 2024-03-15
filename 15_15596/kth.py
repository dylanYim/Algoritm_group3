def solve(a: list) -> int:
    sum = 0
    for i in range(len(a)):
        sum += int(a[i])
    return sum