import sys, itertools
N = int(sys.stdin.readline())

result = []
for i in range(1, 11):
    for j in itertools.combinations(range(10),i):
        num = int(''.join(list(map(str,reversed(list(j))))))
        result.append(num)

result.sort()
if N >= len(result):
    print(-1)
else:
    print(result[N])