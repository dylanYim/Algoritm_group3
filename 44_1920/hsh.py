import sys
N = int(sys.stdin.readline())

list1 = list(map(int, sys.stdin.readline().split()))
list1.sort()

M = int(sys.stdin.readline())

list2 = list(map(int, sys.stdin.readline().split()))

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