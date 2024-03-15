w, h = map(int, input().split())
t = int(input())
wcp = []
hcp = []
for _ in range(t):
    a, b = map(int,input().split())
    if a == 0 and b not in wcp:
        wcp.append(b)
    elif a == 1 and b not in hcp:
        hcp.append(b)
wcp.append(0)
hcp.append(0)
wcp.sort()
hcp.sort()

lw = []
lh = []
wcp.append(h)
hcp.append(w)

for i in range(len(wcp)-1):
    if i == 0:
        lw.append(wcp[i])
        lw.append(wcp[i + 1] - wcp[i])
    else:
        lw.append(wcp[i + 1] - wcp[i])

for i in range(len(hcp)-1):
    if i == 0:
        lh.append(hcp[i])
        lh.append(hcp[i + 1] - hcp[i])
    else:
        lh.append(hcp[i + 1] - hcp[i])

if len(lw) == 0:
    lw.append(w)
if len(lh) == 0:
    lh.append(h)
print(hcp)
print(wcp)
print(lh)
print(lw)
print(max(lw)*max(lh))