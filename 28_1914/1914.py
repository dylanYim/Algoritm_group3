def times(n):
    if n ==1:
        return 1
    else:
        return 1+2*(times(n-1))

def Hanoi(N, base, goal, otherhand=None):
    otherhand = (6-base-goal)
    if N == 1:
        print(f"{base} {goal}")
        return
    

    Hanoi(N-1, base, otherhand)
    print(f"{base} {goal}")
    Hanoi(N-1, otherhand, goal)

import sys
trial = int(sys.stdin.readline())

print(times(trial))

if trial<=20:
    Hanoi(trial, 1, 3)