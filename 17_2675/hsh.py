import sys
trial = int(sys.stdin.readline())

while trial > 0:
    a,b = sys.stdin.readline().split()
    for j in b:
        for i in range(int(a)):
        
            print(j, end = "")
    print("")
    trial -= 1