test = int(input())
lst = []

for _ in range(test):
    case = list(map(int, input().split(' ')))
    sum = 0
    for i in range(1, len(case)):
        sum += case[i]
    avg = sum/case[0]
    count = 0
    for i in range(1, len(case)):
        if case[i] > avg:
            count += 1
    print(f"{count/case[0]:.3%}")