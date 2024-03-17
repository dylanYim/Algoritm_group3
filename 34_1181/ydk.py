n = int(input())
ans = set()
for _ in range(n):
    ans.add(input())

ans = list(ans)

ans.sort()
ans.sort(key=len)

for i in ans:
    print(i)