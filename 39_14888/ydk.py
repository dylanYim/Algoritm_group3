import sys

N = int(input())
lst = list(map(int,input().split()))
operator = list(map(int, input().split())) # +, -, * , /
min_val = sys.maxsize
max_val = sys.maxsize * -1
def dfs(i, val):
    global min_val, max_val, operator
    if sum(operator) == 0:
        min_val = min(min_val, val)
        max_val = max(max_val, val)
    else:
        if operator[0] > 0:
            operator[0] -= 1
            dfs(i + 1, val + lst[i])
            operator[0] += 1
        if operator[1] > 0:
            operator[1] -= 1
            dfs(i + 1, val-lst[i])
            operator[1] += 1
        if operator[2] > 0:
            operator[2] -= 1
            dfs(i + 1, val*lst[i])
            operator[2] += 1
        if operator[3] > 0:
            if val < 0:
                a = (abs(val) // lst[i]) * -1
            else:
                a = val // lst[i]
            operator[3] -= 1
            dfs(i + 1, a)
            operator[3] += 1

dfs(1, lst[0])
print(max_val)
print(min_val)
