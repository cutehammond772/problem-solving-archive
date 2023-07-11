import sys
input = lambda: sys.stdin.readline().rstrip()

# N은 13 이하이다.
def combination(N, R):
  result = []
  for comb in range(2 ** N):
    accumulation = set()
    for idx in range(N):
      if (1 << idx) & comb > 0:
        accumulation.add(idx)
        
      if len(accumulation) == R:
        result.append(accumulation)
        break

  return result        

def solve(matrix, N, M, houses, chickens):
  result = 2 ** 63 - 1
  
  # 치킨 거리를 먼저 구한다.
  dist = [[0] * len(chickens) for _ in range(len(houses))]

  for house_idx in range(len(houses)):
    for chicken_idx in range(len(chickens)):
      house = houses[house_idx]
      chicken = chickens[chicken_idx]
      dist[house_idx][chicken_idx] = abs(house // N - chicken //
                                         N) + abs(house % N - chicken % N)

  for r in range(M, 0, -1):
    for ch in combination(len(chickens), M):
      accumulation = 0
      for i in range(len(houses)):
        if accumulation > result:
          break
          
        accumulation += min([dist[i][j] for j in range(len(chickens)) if j in ch])
        
      result = min(result, accumulation)

  return result


if __name__ == '__main__':
  N, M = map(int, input().split())
  matrix = [list(map(int, input().split())) for _ in range(N)]
  houses, chickens = [], []
  
  # 집과 치킨집의 위치를 알아낸다.
  for row in range(N):
    for col in range(N):
      if matrix[row][col] == 1:
        houses.append(row * N + col)
      if matrix[row][col] == 2:
        chickens.append(row * N + col)

  print(solve(matrix, N, M, houses, chickens))