import sys

i = 1
list1 = []
while i < 10:
    trial = int(sys.stdin.readline())
    list1.append(trial)
    i+=1

max_idx = 0
max = 0
for i in range(len(list1)):
    if list1[i] > max:
        max = list1[i]
        max_idx = i + 1

print(max)
print(max_idx)

