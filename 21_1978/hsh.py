import sys, math
trial = int(sys.stdin.readline())
list1 = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in list1:
    if i == 1:
        cnt += 1
    for j in range(2, int(math.sqrt(i)+1)):
        if i % j == 0:
            cnt += 1
            break

print(trial-cnt)