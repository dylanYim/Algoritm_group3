x, y, w, h = map(int, input().split())

reach = min(x, y, w-x, h-y)

print(reach)