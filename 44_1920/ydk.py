N = int(input())
A = list(map(int,input().split()))
M = int(input())
lst = list(map(int,input().split()))
ans = []

def binary_search(lst, target):
    flag = False
    start = 0
    end = len(lst)-1
    while True:
        mid = (end + start) // 2
        if lst[mid] == target:
            flag = True
            break
        if lst[mid] > target:
            end = mid -1
            mid = (start + end) // 2 + 1
        if lst[mid] < target:
            start = mid + 1
            mid = (start + end)
        if start > end:
            break
    return flag

A.sort()
for a in lst:
    if binary_search(A,a):
        print(1)
    else:
        print(0)