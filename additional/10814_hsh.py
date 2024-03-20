import sys
trial = int(sys.stdin.readline())
lst = []
while trial > 0:
    num = list(map(str, sys.stdin.readline().split()))
    num[0] = int(num[0])
    lst.append(num)
    trial -= 1
lst.sort(key = lambda x: x[0])
for i in range(len(lst)):
    print((lst[i][0]), lst[i][1])