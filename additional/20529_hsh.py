import sys
import itertools
trial = int(sys.stdin.readline())

def dist(mbti1, mbti2):
    result = 0

    for i in range(len(mbti1)):
        if mbti1[i] != mbti2[i]:
            result += 1
    
    return result


while trial > 0:
    N = int(sys.stdin.readline())
    mbti_lst = list(map(str, sys.stdin.readline().split()))
    if N > 32:
        print(0)
        trial -= 1
        continue
    
    nCr = list(itertools.combinations(mbti_lst, 3))
    min = 0
    for i in range(len(nCr)):
        sum_dist = 0
        sum_dist += dist(nCr[i][0], nCr[i][1])
        sum_dist += dist(nCr[i][1], nCr[i][2])
        sum_dist += dist(nCr[i][2], nCr[i][0])
        if sum_dist < min or min == 0:
            min = sum_dist
    print(min)

    trial -= 1

