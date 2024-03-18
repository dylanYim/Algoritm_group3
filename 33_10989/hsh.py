import sys
trial = int(sys.stdin.readline())
list1=[0] * 10001

for i in range(trial):
    x = int(sys.stdin.readline())
    list1[x] += 1


for i in range(len(list1)):
    if list1[i] >= 1:
        for j in range(list1[i]):
            print(i)
