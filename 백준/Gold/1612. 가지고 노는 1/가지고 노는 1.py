impossibles = [2, 4, 5, 6, 8, 0]

def is_impossible(N):
  return (N % 10) in [2, 4, 5, 6, 8, 0]

def solve(N):
  length = len(str(N))
  accu = int('1' * length) # 처음에는 N의 자리수와 맞춤
  
  while accu % N != 0:
    accu = (accu % N) * 10 + 1
    length += 1
  
  return length

N = int(input())
  
if is_impossible(N):
  print(-1)
else:
  print(solve(N))