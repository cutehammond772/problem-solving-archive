data = [
  { 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 }, # 1
  { 2, 4, 6, 8, 0 }, # 2
  { 3, 6, 9, 2, 5, 8, 1, 4, 7, 0 }, # 3
  { 4, 8, 2, 6, 0 }, # 4
  { 5, 0 }, # 5
  { 6, 2, 8, 4, 0 }, # 6
  { 7, 4, 1, 8, 5, 2, 9, 6, 3, 0 }, # 7
  { 8, 6, 4, 2, 0 }, # 8
  { 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 } # 9
] # 각 제수에 의해 나누어떨어질 수 있는 마지막 자리수

IMPOSSIBLE = 2 ** 63 - 1

def possible_dividend(N, divisors):
  for divisor in divisors:
    if int(N) % divisor != 0:
      return IMPOSSIBLE

  return int(N)

def solve(N, divisors, possibles, length):
  min_val = IMPOSSIBLE

  for n in range(10 ** length):
    for x in possibles:
      if length > 0:
        extra = ('0' * (length - len(str(n)))) + str(n)
      else:
        extra = ''
      min_val = min(min_val, possible_dividend(N + extra + str(x), divisors))

  if min_val == IMPOSSIBLE:
    return solve(N, divisors, possibles, length + 1)

  return min_val

N = input()
divisors = sorted(list(set(int(x) for x in N).difference({ 0 }))) # 한자리 수의 제수

lst = [data[x - 1] for x in divisors]
possibles = lst[0]

for x in range(1, len(lst)):
  possibles = possibles.intersection(lst[x])

possibles = sorted(list(possibles)) # 각 제수에 의해 나누어떨어질 수 있는 공통된 마지막 자리수
result = possible_dividend(int(N), divisors)

if result != IMPOSSIBLE:
  print(result) # 주어진 수가 바로 가능한 경우
else:
  result = solve(N, divisors, possibles, 0)
  print(result)