def prime_list(a):
  chk = [True] * (a+1)
  lst = []
  chk[0], chk[1] = False, False
  for i in range(2, int(a**(1/2))+1):
    if chk[i]:
      lst.append(i)
      j = 2
      while i*j <= a:
        chk[i*j] = False
        j += 1

  for i in range(2, (a//2)+1):
    if chk[i] and chk[a-i]:
      f = i
      s = a-i
  print(f'{f} {s}')

t = int(input())
ans = []

for i in range(t):
  num = int(input())
  ans.append(num)

for j in ans:
  prime_list(j)