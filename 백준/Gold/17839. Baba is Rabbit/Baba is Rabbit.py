import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

class Converter:
  def __init__(self):
    self.id = 1
    self.id_maps = dict()
    self.name_maps = [None]

  def get_id(self, name):
    if name not in self.id_maps:
      self.id_maps[name] = self.id
      self.name_maps.append(name)
      self.id += 1

    return self.id_maps[name]

  def get_name(self, id):
    if id >= len(self.name_maps):
      return 0

    return self.name_maps[id]

def solve(converter, graph):
  result = []
  BABA_ID = converter.get_id("Baba")

  check = [False] * 200001
  queue = deque([BABA_ID])

  check[BABA_ID] = True

  while queue:
    node = queue.popleft()

    for next in graph[node]:
      if check[next]:
        continue

      result.append(converter.get_name(next))
      check[next] = True

      queue.append(next)

  result.sort()
  return result

if __name__ == "__main__":
  N = int(input())
  converter = Converter()
  graph = [set() for _ in range(200001)]

  for _ in range(N):
    P, _, Q = input().split()
    pid, qid = converter.get_id(P), converter.get_id(Q)

    graph[pid].add(qid)

  result = solve(converter, graph)

  if result:
    print(*result, sep='\n')
