test = int(input())

score = []

for i in range(test):
    text = input()
    total_sum = 0
    sum = 0
    for i in range(len(text)):
        if text[i] == "O":
            sum += 1
            total_sum += sum
        else:
            sum = 0
    print(total_sum)