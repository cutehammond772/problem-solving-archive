import sys
input = lambda: sys.stdin.readline().rstrip()
mappings = {'H': 0, 'T': 1}

if __name__ == '__main__':
  N = int(input())
  arr = [[mappings[x] for x in input()] for _ in range(N)]
  result = 400

  # 행과 열에 대해, '뒤집는 경우' 또는 '그대로 두는 경우' 두 가지가 존재하므로
  # 총 (2^20) * (2^20)가지가 존재한다.
  # 이때, 열만 모든 조합을 고려하고 행은 뒷면의 개수가 과반수인 경우에만 뒤집으면 된다.
  # -> 20 * (2^20)으로 방법의 수를 줄일 수 있다.
  for subset in range(1 << N):
    count = 0
    matrix = [[arr[row][col] for col in range(N)] for row in range(N)]

    for col in range(N):
      if subset & (1 << col):
        continue

      for row in range(N):
        matrix[row][col] ^= 1

    for row in range(N):
      total = sum(matrix[row])
      count += min(total, N - total)

    result = min(result, count)

  print(result)
