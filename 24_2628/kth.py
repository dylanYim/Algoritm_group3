x, y = map(int, input().split())
cut = int(input())
x_list = [0, x]
y_list = [0, y]
x_reach = 0
y_reach = 0


for _ in range(cut):
    cut_coor, cut_loc = map(int, input().split())
    if cut_coor == 0:
        y_list.append(cut_loc)
    else:
        x_list.append(cut_loc)

x_list.sort()
y_list.sort()
    
for j in range(len(x_list)-1):
    if x_reach < x_list[j+1] - x_list[j]:
        x_reach = x_list[j+1] - x_list[j]

for j in range(len(y_list)-1):
    if y_reach < y_list[j+1] - y_list[j]:
        y_reach = y_list[j+1] - y_list[j]

print(x_reach * y_reach)