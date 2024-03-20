natural_num = []
for i in range(10001):
    natural_num.append(i)

not_self = []
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    if i not in not_self:
        not_self.append(i)

for i in range(1, 10001):
    if i not in not_self:
        print(i)
    