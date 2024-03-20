import sys
N, M = map(int,sys.stdin.readline().split())
list1 = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(list1)

while start <= end:
    sum = 0
    cut_height = (start + end) // 2
    for i in list1:
        if i > cut_height:
            sum += i - cut_height
    
    if sum >= M:
        result = cut_height
        start = cut_height + 1
    else:
        end = cut_height - 1
    
print(result)