import sys

def a(lst):
    s = 0
    e = len(lst)-1

    temp = abs(lst[s] + lst[e])
    while abs(s-e) >= 1 :
        
        if abs(lst[s] + lst[e]) <= temp:
            temp = abs(lst[s] + lst[e])
            result = [lst[s], lst[e]]
        sum = lst[s] + lst[e]
        if sum > 0:
            e -= 1
        elif sum < 0:
            s += 1
        else:
            return result
    return result


n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

r = a(lst)
print(r[0], r[1])