import sys
from queue import deque
input = lambda: sys.stdin.readline().rstrip()

MAX_ARR = 100001

def backtrack(N, K, route):
  result = []
  current = K
  
  while current != MAX_ARR:
    result.append(current)
    current = route[current]
    
  return result[::-1]

def solve(N, K):
  # 수빈이 동생과 같이 있거나 뒤에 있는 경우
  if N >= K:
    return N - K, range(N, K - 1, -1)

  time = [MAX_ARR] * MAX_ARR
  route = [MAX_ARR] * MAX_ARR

  # (현재 위치, 누적 시간)
  que = deque([(N, 0)])

  # 초기 설정
  time[N] = 0
  
  while que:
    idx, ctime = que.popleft()

    # 동생 위치에 도착 시
    if idx == K:
      continue

    next = ctime + 1
      
    # 뒤로 가는 경우
    if idx > 0 and min(time[idx - 1], time[K]) > next:
      time[idx - 1], route[idx - 1] = next, idx
      que.append((idx - 1, next))
      
    # 앞으로 가는 경우 (최대를 K로 잡는다.)
    if idx < K and min(time[idx + 1], time[K]) > next:
      time[idx + 1], route[idx + 1] = next, idx
      que.append((idx + 1, next))

    # 2배의 위치로 이동하는 경우
    if idx * 2 < MAX_ARR:
      # K를 넘기는 경우
      if idx * 2 > K:
        if next + (idx * 2 - K) < time[K]:
          time[idx * 2], route[idx * 2] = next, idx
          time[K], route[K] = time[idx * 2] + (idx * 2 - K), idx * 2
      elif min(time[idx * 2], time[K]) > next:
        time[idx * 2], route[idx * 2] = next, idx
        que.append((idx * 2, next))

  return time[K], backtrack(N, K, route)
  

if __name__ == '__main__':
  N, K = map(int, input().split())
  time, route = solve(N, K)

  print(time)
  print(*route)