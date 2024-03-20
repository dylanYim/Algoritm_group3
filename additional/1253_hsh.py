import sys
trial = int(sys.stdin.readline())
# 1 10 4 9  -> [1, 10, 4, 9]
num = list(map(int, sys.stdin.readline().split()))
num.sort()

cnt = 0
for i in range(0, len(num)):
    start = 0
    end = len(num)-1
    while start < end:
        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue
        
        if num[start] + num[end] == num[i]:
            cnt += 1
            break
        elif num[start] + num[end] < num[i]:
            start += 1
        else:
            end -= 1

print(cnt)
