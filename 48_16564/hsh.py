import sys
N, K = map(int,sys.stdin.readline().split())
M = N
list1 = []
while M > 0:
    list1.append(int(sys.stdin.readline()))
    M -= 1

start = min(list1)
end = 1000000001

while start <= end:
    cut_level = (start + end) //2
    sum_level = 0
    for i in range(len(list1)):
        if list1[i] < cut_level:
            sum_level += cut_level - list1[i]
    if sum_level <= K:
        result = cut_level
        start = cut_level + 1
    else:
        end = cut_level - 1
        

print(result)
