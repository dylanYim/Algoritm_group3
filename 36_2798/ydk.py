n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort(reverse=True)
answer = []
for i in range(len(cards)-2):
    find = False
    if cards[i] >= m:
        continue
    for j in range(i+1, len(cards)-1):
        if cards[i] + cards[j] >= m:
            continue
        for k in range(j+1, len(cards)):
            if cards[i] + cards[j] + cards[k] > m:
                continue
            else:
                answer.append(cards[i] + cards[j] + cards[k])
answer.sort(reverse=True)
print(answer[0])