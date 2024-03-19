import sys
from itertools import permutations

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
arr = list((permutations(lst, n)))
result = []

for i in range(len(arr)):
    sum = 0
    for j in range(len(arr[i])-1):
        sum += abs(arr[i][j]-arr[i][j+1])
    result.append(sum)

print(max(result))