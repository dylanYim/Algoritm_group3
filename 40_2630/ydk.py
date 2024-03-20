N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0

def cutting(n,x, y):
    global white, blue
    length = n
    val = data[x][y]
    if n == 1:
        if val == 1:
            blue += 1
        else:
            white += 1
    else:
        val = data[x][y]
        if check_square(length, x, y,val):
            if val == 1:
                blue += 1
            else:
                white += 1
        else:
            cutting(length//2, x, y)
            cutting(length//2, x, y + length//2)
            cutting(length//2, x + length//2, y)
            cutting(length//2, x + length//2, y + length//2)

def check_square(n,x, y,val):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if data[i][j] != val:
                return False
    return True

cutting(N, 0, 0)
print(white)
print(blue)