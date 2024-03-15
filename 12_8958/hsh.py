import sys
trial = int(sys.stdin.readline())
while trial > 0:
    OX = (sys.stdin.readline())
    score = 0
    O_score = 1
    for i in range(len(OX)):
        if OX[i] == "O":
            if i == 0:
                score += 1
            else:
                if OX[i-1] == "O":
                    O_score += 1
                    score += O_score
                else:
                    score +=1
                    O_score = 1
        else:
            O_score = 0
    print(score)


    trial -= 1