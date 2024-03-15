import sys
N,y,x = map(int,sys.stdin.readline().split())

def Z(n,x,y):
    X1 = 0
    Y1 = 0
    if n == 1:
        return (x + 2*y)

    if x+1 > 2**(n-1):
        x = x- (2**(n-1))
        X1 = 1
    
    if y+1 > 2**(n-1):
        y= y- (2**(n-1))
        Y1 = 1

    return X1*(2**(2*(n-1))) + Y1*(2**((2*n)-1)) + Z(n-1,x,y)

print(Z(N, x, y))