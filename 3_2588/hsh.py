import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
b1, b2, b3 = [int(digit) for digit in str(b)]
print(a * b3)
print(a * b2)
print(a * b1)
print(a* b)
