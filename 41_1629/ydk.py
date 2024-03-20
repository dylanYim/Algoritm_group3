def mod(a,b,c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (mod(a, b//2, c) ** 2) % c
    else:
        return ((mod(a, b//2, c) ** 2) * a) % c

A,B,C = map(int,input().split())

print(mod(A,B,C))