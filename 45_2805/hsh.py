import sys
N,M = map(int,sys.stdin.readline().split())

list1_str = input()
list1 = list1_str.split()
for i in range(len(list1)):
    list1[i] = int(list1[i])
start = 0
end = max(list1)
cut_height = max(list1) // 2

while True:
    sum = 0
    if start == end:
        break
    for i in list1:
        if i > cut_height:
            sum += i-cut_height
    if sum == M:
        break
    elif sum > M:
        sum = 0
        for i in list1:
            if i > cut_height +1:
                sum += i-(cut_height+1)
        if sum < M:
            break
        start = cut_height
        cut_height = (start + end)//2
    elif sum < M:
        sum = 0
        for i in list1:
            if i > cut_height -1:
                sum += i-(cut_height-1)
        if sum > M:
            cut_height = cut_height - 1
            break
        end = cut_height
        cut_height = (start + end)//2
    
print(cut_height)