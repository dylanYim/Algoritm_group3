import sys
trial = int(sys.stdin.readline())
while trial > 0:
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)
    trial -= 1
