import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, truths, parties):
  # 진실을 아는 사람이 없는 경우
  if len(truths) == 0:
    return M

  # 진실을 아는 파티의 인덱스이다.
  known = set()

  # 진실이 최대한 퍼지도록 파티 수만큼 반복한다.
  for _ in range(M):
    if len(known) == M:
      break
      
    for idx in range(M):
      if idx in known:
        continue

      # 진실을 아는 사람이 존재할 경우 파티원이 모두 알도록 한다.
      if len(truths.intersection(parties[idx])) > 0:
        known.add(idx)
        truths.update(parties[idx])
        
  return M - len(known)

if __name__ == '__main__':
  N, M = map(int, input().split())
  truths = set(map(int, input().split()[1:]))
  parties = [set(map(int, input().split()[1:])) for _ in range(M)]
  
  print(solve(N, M, truths, parties))