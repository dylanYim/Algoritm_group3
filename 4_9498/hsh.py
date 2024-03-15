import sys
grade = int(sys.stdin.readline())

if 90<= grade <=100:
    print("A")
elif 80<= grade:
    print("B")
elif 70<=grade:
    print("C")
elif 60<=grade:
    print("D")
else:
    print("F")

