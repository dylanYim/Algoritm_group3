import sys,math
trial = int(sys.stdin.readline())
while trial > 0:
    even = int(sys.stdin.readline())

    fullList = [True] * (even +1)
    #fullList[0] = fullList[1] = False

    for i in range(2, int(math.sqrt(even)+1)):
        for j in range(2*i,even+1,i):
            fullList[j]=False
        
    for i in range(2, even//2 +1):
        if fullList[i] == True and fullList[even-i] == True:
            a = i
            b = even-i
    
    print(f"{a} {b}")

    trial -= 1