import sys,math
trial = int(sys.stdin.readline())

while trial > 0:
    even = int(sys.stdin.readline())

    primeList = [True] * (even +1)
    # primeList[0] = primeList[1] = False

    for i in range(2, int(math.sqrt(even))+1):
        if primeList[i] == True: #추가됨.
            for j in range(2*i, even+1, i):
                primeList[j] = False
        
    for i in range(even//2, 1, -1):
        if primeList[i] == True and primeList[even-i] == True:
            a = i
            b = even-i
            break
    
    print(f"{a} {b}")

    trial -= 1