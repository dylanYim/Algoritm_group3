import sys
a,b,c = map(int,sys.stdin.readline().split())


def multiply(a, b,c):
    if b == 1:
        return a%c
    if (b != 0) and ((b & (b - 1)) == 0):
        return multiply((a*a)%c, max_po_2(b)//2 , c)
    else:
        return (multiply((a*a)%c, max_po_2(b)//2, c) * multiply(a, b - (max_po_2(b)), c)) % c

def max_po_2(num):
    power = 0
    while 2 ** power <= num:
        power += 1
    return 2 ** (power - 1)

print(multiply(a,b,c))