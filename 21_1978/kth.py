import math

num = int(input())
dec = list(map(int, input().split()))
dec.sort()
prime = 0

for i in range(num):
    count = 0
    for j in range(2, int(math.sqrt(dec[-1]))+1):
        if dec[i] == 1: 
            count = 1
        elif dec[i] % j == 0 and dec[i] != j:
            count += 1
    if count == 0:
        prime += 1

print(prime)