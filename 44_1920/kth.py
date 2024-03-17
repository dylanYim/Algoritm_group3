n = int(input())
a = list(map(int, input().split(' ')))
m = int(input())
m_lst = list(map(int, input().split(' ')))


a.sort()
for i in range(len(m_lst)):
    for j in range(len(a)):
        if m_lst[i] == a[j]:
            search = 1
            break
        else:
            search = 0
    print(search)