def revese_num(x: int) -> int:
    revesed_list = reversed(list(str(x)))
    join_list = ''.join(revesed_list)
    return join_list

a, b = input().split()
z = revese_num(a)
x = revese_num(b)

if (z >= x):
    print(z)
else:
    print(x)