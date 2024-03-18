import sys
n = int(sys.stdin.readline())

# n개의 점을 입력 받아 2차원 리스트로 저장
dots = []
for _ in range(n):
    dots.append(list(map(int, sys.stdin.readline().split())))

dots.sort()  # x좌표를 기준으로 정렬


def get_dist(a, b):  # 두 점 사이의 거리를 구하는 함수
    return (a[0]-b[0])**2+(a[1]-b[1])**2

def get_min(dots, start, end):
    

    if start == end:
        return sys.maxsize
    elif end - start == 1:
        return get_dist(dots[start], dots[end])
    else:
        mid = (start + end) //2
        min_dist = min(get_min(dots, start, mid), get_min(dots, mid+1, end))

    centers = []
    for i in range(start, end+1): #개중요 난 range(len(dots))했음
        if (dots[i][0]-dots[mid][0])**2 <min_dist:
            centers.append(dots[i])

    centers.sort(key=lambda x: x[1])

    for i in range(len(centers)-1):
        for j in range(i+1, len(centers)): # 이거때메 엄밀해짐
            if (centers[i][1] -centers[j][1])**2< min_dist:
                min_dist = min(min_dist, get_dist(centers[i], centers[j]))
            else:
                break
    
    return min_dist

print(get_min(dots, 0, len(dots)-1))
