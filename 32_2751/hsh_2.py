import sys
trial = int(sys.stdin.readline())
list1=[None] * trial

for i in range(trial):
    list1[i] = int(sys.stdin.readline())

list1.sort()

for i in range(trial):
    print(list1[i])