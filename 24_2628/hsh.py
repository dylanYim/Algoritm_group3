import sys
a, b = map(int,sys.stdin.readline().split())
hori_list = [0, a]
verti_list = [0, b]

trial = int(sys.stdin.readline())

while trial > 0:
    idx, cut = map(int,sys.stdin.readline().split())

    if idx == 0:
        verti_list.append(cut)

    elif idx == 1:
        hori_list.append(cut)
    
    trial -= 1

verti_list.sort()
hori_list.sort()

real_hori = []
real_verti = []

for i in range(0, len(hori_list)-1):
    real_hori.append(hori_list[i+1]-hori_list[i])
for i in range(0, len(verti_list)-1):
    real_verti.append(verti_list[i+1]-verti_list[i])

# if len(real_hori) == 0:
#     real_hori = [a]
# if len(real_verti) == 0:
#     real_verti = [b]

print(max(real_hori) * max(real_verti))    