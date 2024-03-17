import sys

N,C = map(int,sys.stdin.readline().split())
M=N
lst1 = []

while M > 0:
    lst1.append(int(sys.stdin.readline()))
    M -= 1

lst1.sort()

