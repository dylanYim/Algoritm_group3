import sys
N_cables, N = map(int,sys.stdin.readline().split())
cables_lst = []
for i in range(N_cables):
    cables_lst.append(int(sys.stdin.readline()))

start = 1
end = max(cables_lst)
mid = (start + end) // 2

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in cables_lst:
        total += i//mid
    
    if total >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1 

print(result)