import sys
trial = int(sys.stdin.readline())

while trial > 0:

    trial -= 1

# 1 10  -> a = 1, b = 10
a, b = map(int,sys.stdin.readline().split())

# str str -> ["str", "str"]
list1_str = sys.stdin.readline()
list1 = list1_str.split()

# 1 10 4 9  -> [1, 10, 4, 9]
num = list(map(int, sys.stdin.readline().split()))


import itertools
nCr = list(itertools.combinations(mbti_lst, 3))
# -> [(), (), ...]

# 2차원 행렬 만들기
import sys
N = int(sys.stdin.readline())
mat = []
for _ in range(N):
    r = sys.stdin.readline()
    tmp = []
    for j in range(N):
        tmp.append(int(r[j])) # input에 따라 조절 필요
    mat.append(tmp)