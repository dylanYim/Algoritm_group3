import sys

def cut_tree(a, lst):
    first, last = 0, max(lst)
    while first <= last:
        mid = (first + last) // 2
        sum = 0
        for i in range(len(lst)):
            if lst[i] > mid:
                sum += lst[i]
        if sum > a:
            first = mid
        elif sum < a:
            last = mid
        else:
            break
    return mid
            

n, m = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().split()))
t.sort()

print(cut_tree(m, t))