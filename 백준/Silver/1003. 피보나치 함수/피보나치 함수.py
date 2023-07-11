T = int(input())
cases = [int(input()) for _ in range(T)]
fibs = [(1, 0), (0, 1)]

for i in range(2, max(cases) + 1):
  z1, o1 = fibs[-1]
  z2, o2 = fibs[-2]
  fibs.append(((z1 + z2), (o1 + o2)))

for x in cases:
  print(*fibs[x])