import sys
trial = int(sys.stdin.readline())

garo = [True] * trial
sero = [True] * trial
diagonal_17 = [True] * (trial*2-1) 
diagonal_115 = [True] * (trial*2-1) 

cnt = 0

def set(i):
    global cnt 
    for j in range(trial):
        if garo[j] and diagonal_17[i+j] and diagonal_115[(i-j+(trial-1))]:
            sero[i] = j
            if i == trial-1:
               cnt +=1
                
            else:
                garo[j] = diagonal_17[i+j] = diagonal_115[(i-j+(trial-1))] = False
                set(i+1)
                garo[j] = diagonal_17[i+j] = diagonal_115[(i-j+(trial-1))] = True
    return cnt

print(set(0))
