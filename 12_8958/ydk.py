t = int(input())
ans = []
for _ in range(t):
    s = input()
    total_sum =0
    sum = 0
    for i in range(len(s)):
        if s[i] == 'O':
            sum += 1
            total_sum +=sum
        else:
            sum = 0
    ans.append(total_sum)

print(ans)
