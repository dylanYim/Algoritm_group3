def bi_search(a, lst):
    first, last = 0, len(lst)-1
    while first <= last:
        mid = (first + last) // 2
        if lst[mid] == a: return 1
        if lst[mid] > a:
            last = mid - 1
        else:
            first = mid + 1
    return 0

n = int(input())
a = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))
a.sort()

for i in range(len(m_lst)):
    ans = bi_search(m_lst[i], a)
    print(ans)