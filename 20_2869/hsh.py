import sys, math
A,B,V = map(int,sys.stdin.readline().split())

days = math.ceil((V-A)/(A-B)) + 1 
print(days)

