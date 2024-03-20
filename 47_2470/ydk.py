import sys

N = int(input())
lst = list(map(int,input().split()))

lst.sort()
start = 0
end = len(lst) - 1
minimal = sys.maxsize
ans = [0,0]
while start < end:

    val = lst[start] + lst[end]
    if abs(val) < minimal:
        minimal = abs(val)
        ans[0] = lst[start]
        ans[1] = lst[end]
    if val == 0:
        break
    if val < 0:
        start += 1
    if val > 0:
        end -= 1

print(*ans)