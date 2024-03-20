import sys

ch = []
n, k = list(map(int, sys.stdin.readline().split()))

for _ in range(n):
    lv = int(sys.stdin.readline())
    ch.append(lv)

ch.sort()

s = ch[0]
e = ch[len(ch)-1] + k
result = 0

while s <= e:
    h = (s + e) // 2
    sum = 0
    for i in range(len(ch)):
        if ch[i] < h:
            sum += (h - ch[i])
    if k >= sum:
        if (result < h):
            result = h
        s = h + 1
    else:
        e = h - 1

print(result)
