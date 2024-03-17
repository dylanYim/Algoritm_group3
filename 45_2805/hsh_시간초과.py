import sys
N,M = map(int,sys.stdin.readline().split())

list1_str = input()
list1 = list1_str.split()
for i in range(len(list1)):
    list1[i] = int(list1[i])

list1.sort(reverse=True)
trial = 0


for i in range(len(list1)):
    if i == len(list1)-1:
        while M > 0:
            M -= len(list1)
            trial += 1
        break

    for j in range(list1[i]-list1[i+1]):
        M -=(i+1)
        trial += 1
        if M <= 0:
            break

    if M <= 0:
        break

print(list1[0]-(trial))
