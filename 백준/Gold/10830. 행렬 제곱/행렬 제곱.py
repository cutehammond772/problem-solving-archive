import sys
input = lambda: sys.stdin.readline().rstrip()

# N * N 행렬곱을 수행한다.
def mul(N, ma, mb):
  matrix = [[0] * N for _ in range(N)]
  
  for r in range(N):
    for c in range(N):
      for k in range(N):
        matrix[r][c] = (matrix[r][c] + ma[r][k] * mb[k][c]) % 1000
        
  return matrix

# B는 1 이상이다.
def analyze(B):
  bit_length = 0
  has_bits = []
  
  while B != 0:
    if B & (1 << bit_length) > 0:
      has_bits.append(True)
      B -= 2 ** bit_length
    else:
      has_bits.append(False)
      
    bit_length += 1
    
  return bit_length, has_bits

if __name__ == '__main__':
  N, B = map(int, input().split())
  matrix = [list(map(int, input().split())) for _ in range(N)]

  # 항등 행렬
  result = [[1 if x == y else 0 for x in range(N)] for y in range(N)]
  
  # B의 이진수 비트 정보를 가져온다.
  bit_length, has_bits = analyze(B)
  
  # 행렬 B의 (2 ** 0)제곱부터 (2 ** (bit_length - 1))제곱까지 구한다.
  memo = [matrix]
  for i in range(1, bit_length):
    memo.append(mul(N, memo[i - 1], memo[i - 1]))

  # 특정 비트를 체크하여 계속 곱한다.
  for i in range(bit_length):
    if has_bits[i]:
      result = mul(N, result, memo[i])

  # 결과를 출력한다.
  for r in range(N):
    print(*result[r])