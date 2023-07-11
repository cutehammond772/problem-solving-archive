MAX_VAL = (10 ** 6) + 1
INIT, ADD, DOUBLE, TRIPLE = -1, 0, 1, 2

def forward_index(behavior, idx):
  if behavior == ADD:
    return idx + 1
    
  if behavior == DOUBLE:
    return idx * 2
    
  if behavior == TRIPLE:
    return idx * 3
    
  return -1

def backward_index(behavior, idx):
  if behavior == ADD:
    return idx - 1
    
  if behavior == DOUBLE:
    return idx // 2
    
  if behavior == TRIPLE:
    return idx // 3
    
  return -1

def solve(memo, cur_idx, behavior):
  cur_count, _ = memo[cur_idx]

  next_idx = forward_index(behavior, cur_idx)
  next_count, _ = memo[next_idx]

  if cur_count + 1 < next_count:
    memo[next_idx] = (cur_count + 1, behavior)

def track(memo, idx):
  _, behavior = memo[idx]
  result = [idx]
  
  while behavior != INIT:
    back_idx = backward_index(behavior, idx)
    _, back_behavior = memo[back_idx]
    
    result.append(back_idx)
    
    idx = back_idx
    behavior = back_behavior
    
  return result
    
if __name__ == "__main__":
  N = int(input())
  memo = [(MAX_VAL, INIT)] * (N + 1)
  
  # (count, sequence)
  memo[1] = (0, INIT)
  
  for idx in range(1, N):
    if forward_index(ADD, idx) <= N:
      solve(memo, idx, ADD)
      
    if forward_index(DOUBLE, idx) <= N:
      solve(memo, idx, DOUBLE)
      
    if forward_index(TRIPLE, idx) <= N:
      solve(memo, idx, TRIPLE)

  count, behavior = memo[N]
  
  print(count)
  print(*track(memo, N))