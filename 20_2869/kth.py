a, b, v = map(int, input().split(' '))

reach = 0
day = 0

while True:
    day += 1
    # print(f'{day}째 날')
    reach += a
    if (reach >= v):
        print(day)
        break
    # print(f'{reach}m 아침')
    reach -= b
    # print(f'{reach}m 저녁')