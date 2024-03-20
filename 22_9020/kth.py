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
  for i in range(2, a//2 + 1):
    if chk[i] and chk[a-i]:
      f = chk[i]
      s = chk[a-i]

  print(f'{f} {s}')

  lst = [x for x in range(a+1) if chk[x]]
  return lst

t = int(input())
lst =[]

for i in range(t):
  a = 0
  b = 0
  num = int(input())
  lst = prime_list(num)
  for j in range(len(prime_list(int(num/2)))):
    if (num - lst[j]) in lst:
      a = lst[j]
      b = num - lst[j] 
  print(f"{a} {b}")
