from itertools import permutations

result_lst =[]
result = 0
max_result = 0

n, m = map(int, input().split())
lst = list(map(int, input().split()))

arr = list(permutations(lst, 3))

for i in range(len(arr)):
    result = 0
    for j in range(len(arr[i])):
        result += arr[i][j]
        result_lst.append(result)
    if result <= m:
        if max_result < result:
            max_result = result

print(max_result)