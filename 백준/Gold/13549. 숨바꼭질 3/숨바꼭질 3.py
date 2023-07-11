from queue import Queue

MAX_VAL = 100001
P, Q = map(int, input().split())
ARR_MAX = max(P, Q) + 1

memo = [MAX_VAL] * ARR_MAX
que = Queue()
que.put((P, 0))

while not que.empty():
  idx, count = que.get()
  
  if memo[idx] <= count:
    continue
    
  memo[idx] = count

  # X - 1
  if idx > 0 and memo[idx - 1] > memo[idx]:
    que.put((idx - 1, count + 1))

  # X + 1
  if idx < ARR_MAX - 1 and memo[idx + 1] > memo[idx]:
    que.put((idx + 1, count + 1))

  # 2 * X
  if idx * 2 < ARR_MAX:
    que.put((idx * 2, count))
  else:
    memo[Q] = min(memo[Q], memo[idx] + (idx * 2) - Q)

print(memo[Q])