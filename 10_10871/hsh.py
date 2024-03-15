import sys
N,max = map(int,sys.stdin.readline().split())

list1_str=input()
list1 = list1_str.split()
list2 = []
for i in list1:
    i = int(i)
    if i < max:
        list2.append(i)

for i in range(len(list2)):
    if i == len(list2) - 1:
        print(list2[i])
    else:
        print(f"{list2[i]} ", end="")