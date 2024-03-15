# 입력 제한 조건을 수행하지 못 함.

x, y, w, h = input("숫자 입력(x, y, w, h / 공백으로 구분): ").split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)

reach = 0

# print(min(x, y, w-x, h-y))

if (w-x >= x):
    if (y <= x):
        reach = y
    elif (h-y <= x):
        reach = h-y
    else:
        reach = x
elif (w-x <= x):
    if (w-x >= y):
        reach = y
    elif (w-x >= h-y):
        reach = h-y
    else:
        reach = w-x
elif (h-y <= y):
    if (w-x >= y):
        reach = y
    elif (x <= y):
        reach = x
    else:
        reach = h-y
else:
    if (h-y >= x):
        reach = x
    elif (h-y >= w-x):
        reach = w-x
    else:
        reach = y

print(reach)
