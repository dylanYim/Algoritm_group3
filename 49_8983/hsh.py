import sys
no_guns, N, shot_Range = map(int,sys.stdin.readline().split())
guns = list(map(int, sys.stdin.readline().split()))
guns.sort()

animals = []
for _ in range(N):
    animals.append([0]*2)  

for i in range(N):
    x, y = map(int,sys.stdin.readline().split())
    animals[i][0] = x
    animals[i][1] = y

cnt = 0
for i in range(N):
    if animals[i][1] <= shot_Range:
        radius = shot_Range - animals[i][1]
        start = 0
        end = len(guns) -1
        
        while start <= end:
            mid = (start + end)//2
            if animals[i][0] - radius <= guns[mid] <= animals[i][0] + radius:
                cnt += 1
                break
            elif animals[i][0] + radius < guns[mid]:
                end = mid - 1
            elif guns[mid] < animals[i][0] - radius:
                start = mid + 1

print(cnt)