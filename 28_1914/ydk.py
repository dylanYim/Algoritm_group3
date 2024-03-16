import sys
n = int(sys.stdin.readline().rstrip())

def move(no, a, b):
    if no > 1:
        move(no-1, a, 6-a-b)
    sys.stdout.write(str(a) + ' ' + str(b) + '\n')
    if no > 1:
        move(no-1,6-a-b, b)


sys.stdout.write(str(2**n-1)+'\n')
if n <= 20:
    move(n, 1, 3)