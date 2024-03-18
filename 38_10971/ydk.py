import sys

N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))
ans = sys.maxsize

def dfs(start, now, visited, value):
    global ans
    if len(visited) == N:
        if cost[now][start] != 0:
            ans = min(cost[now][start] + value, ans)
        else:
            return

    for i in range(N):
        if cost[now][i] == 0:
            continue

        next_value = value+cost[now][i]
        if i in visited:
            continue
        if next_value >= ans:
            continue

        visited.append(i)
        dfs(start, i, visited, next_value)
        visited.pop()


for i in range(N):
    dfs(i,i,[i],0)

print(ans)