import sys

N,C = map(int,sys.stdin.readline().split())
M = N
lst1 = []

while M > 0:
    lst1.append(int(sys.stdin.readline()))
    M -= 1

lst1.sort()

start = 1
end = lst1[N-1]
distance = (start + end)//2
current = lst1[0]

while start <= end:
    cnt = 1
    distance = (start + end)//2
    current = lst1[0]
    for i in range(1, len(lst1)):
        if lst1[i] >= current + distance:
            cnt +=1
            current = lst1[i]
    if cnt >= C:
        result = distance
        start = distance + 1
    else:
        end = distance - 1
    

print(result)