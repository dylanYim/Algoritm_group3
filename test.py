import sys
trial = int(sys.stdin.readline())

# 1 10  -> a=1, b=10
a,b = map(int,sys.stdin.readline().split())

# str str -> ["str", "str"]
list1_str = sys.stdin.readline()
list1 = list1_str.split()

# 1 10 4 9  -> [1, 10, 4, 9]
num = list(map(int, sys.stdin.readline().split()))

# 빈 2차원 행렬 만들기
animals = []
for _ in range(N):
    animals.append([0]*2) # 2 or N