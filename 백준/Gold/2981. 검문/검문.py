import sys
input = sys.stdin.readline

def gcd(p, q):
  if p < q:
    p, q = q, p

  if q == 0:
    return p
    
  return gcd(q, p % q)

def measures(n):
  lst = [n]
  for x in range(2, int(n ** 0.5) + 1):
    if n % x != 0:
      continue

    p, q = x, n // x
    lst.append(p)

    if p != q:
      lst.append(n // x)

  return sorted(lst)
  
N = int(input())
lst = sorted([int(input()) for _ in range(N)])
diff = [lst[x] - lst[x-1] for x in range(1, len(lst))]

if len(diff) == 1:
  print(*measures(diff[0]))
else:
  num = gcd(diff[0], diff[1])
  for x in range(2, len(diff)):
    num = gcd(num, diff[x])

  print(*measures(num))