# 2차원 행렬 만들기
import sys
N = int(sys.stdin.readline())
mat = []
for _ in range(N):
    r = sys.stdin.readline()
    tmp = []
    for j in range(N):
        tmp.append(int(r[j])) # input에 따라 조절 필요
    mat.append(tmp)


def splitting(N, mat):
    if N == 1:
        if mat[0][0] == 0:
            print(0, end = "")
            return
        else:
            print(1, end = "")
            return
    
    flag = 0
    for i in range(N):
        for j in range(N):
            if mat[0][0] != mat[i][j]:
                flag = 1
                print("(", end = "")
                mat1 = mat[:N//2]
                for i in range(N//2):
                    mat1[i] = mat1[i][:N//2]
                splitting(N//2, mat1)

                mat2 = mat[:N//2]
                for i in range(N//2):
                    mat2[i] = mat2[i][N//2:]
                splitting(N//2, mat2)

                mat3 = mat[N//2:]
                for i in range(N//2):
                    mat3[i] = mat3[i][:N//2]
                splitting(N//2, mat3)

                mat4 = mat[N//2:]
                for i in range(N//2):
                    mat4[i] = mat4[i][N//2:]
                splitting(N//2, mat4)
           
                print(")", end = "")
                break
        if flag == 1:
            break

    if flag == 0:
        if mat[0][0] == 0:
            print(0, end = "")
            return
        else:
            print(1, end = "")
            return
        
        
splitting(N, mat)