import sys
trial = int(sys.stdin.readline())
choice = int(sys.stdin.readline())
hand = []
result = []
while trial > 0:
    card = int(sys.stdin.readline())
    hand.append(card)

    trial -= 1

print()

while True:

    if c == 6:
        if b == 5:
            if a == 4:
                break
            else:
                a+=1
                b=a+1
                c=b+1
        else:
            b+=1
            c= b+1
    else:
        c += 1



