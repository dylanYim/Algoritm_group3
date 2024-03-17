import sys
N = int(sys.stdin.readline())

list1_str = input()
list1 = list1_str.split()
for i in range(len(list1)):
    list1[i] = int(list1[i])

M = int(sys.stdin.readline())

list2_str = input()
list2 = list2_str.split()
for i in range(len(list2)):
    list2[i] = int(list2[i])

list1.sort()

def find(list1, i, left, right):
    mid = (left + right)//2
    pivot = list1[mid]
    if left >= right:
        if list1[left] == i:
            print(1)
            return
        else:
            print(0)
            return
    if i == pivot:
        print(1)
    elif i < pivot:
        find(list1, i, left, mid-1)
    elif i > pivot:
        find(list1, i, mid+1, right)

for i in list2:
    find(list1, i, 0, len(list1)-1)