import sys
from itertools import permutations

ans = []
lst = []

for _ in range(9):
    h = int(sys.stdin.readline())
    ans.append(h)

arr = list(permutations(ans, 7))

for i in range(len(arr)):
    sum = 0
    for j in range(len(arr[i])):
        sum += arr[i][j]
    if sum == 100:
        lst.append(arr[i])
ans = list(lst[0])
ans.sort()
for i in ans:
    print(i)
