import sys
matrix1 = []
N , power = map(int,sys.stdin.readline().split())
while N > 0:
    list1_str = input()
    list1 = list1_str.split()
    for i in range(len(list1)):
        list1[i] = int(list1[i])
    matrix1.append(list1)
    N -= 1


def pwer_down(mat, power):
    if power == 1:
        return mat
    if (power != 0) and ((power & (power - 1)) == 0):
        return pwer_down(matrix_multiply(mat,mat), max_po_2(power)//2)
    else:
        return matrix_multiply(pwer_down(matrix_multiply(mat,mat), max_po_2(power)//2), pwer_down(mat, power - (max_po_2(power))))

def max_po_2(num):
    power = 0
    while 2 ** power <= num:
        power += 1
    return 2 ** (power - 1)

def matrix_multiply(mat1, mat2):
    size = len(mat1)
    ret = []
    for _ in range(size):
        ret.append([0]*size)
    val = 0
    temp = 1
    for i in range(size):
        for j in range(size):
            for k in range(size):
                temp = mat1[i][k] * mat2[k][j]
                val += temp
                if k == size -1:
                    ret[i][j] = val%1000
                    val = 0
    return ret


result = pwer_down(matrix1, power)
for i in range(len(matrix1)):
    for j in range(len(matrix1)):
        if j == len(matrix1)-1:
            print(result[i][j]%1000)
        else:
            print(result[i][j]%1000, end=" ")
    