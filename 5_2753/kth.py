while True:
    year = int(input())
    if (1 <= year <= 4000):
        break

if (year % 4 == 0):
    if(year % 100 == 0 and year % 400 != 0):
        print(0)
    else:
        print(1)
else:
    print(0)