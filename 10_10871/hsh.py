import sys
N, max = map(int,sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().split()))

for i in num:
    if i < max:
        print(i)