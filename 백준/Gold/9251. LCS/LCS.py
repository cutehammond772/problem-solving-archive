P, Q = input(), input()
arr = [[0] * (len(Q) + 1) for _ in range(len(P) + 1)]

for p in range(1, len(P) + 1):
  for q in range(1, len(Q) + 1):
    ch_p, ch_q = P[p - 1], Q[q - 1]
    
    if ch_p == ch_q:
      arr[p][q] = arr[p - 1][q - 1] + 1
    else:
      arr[p][q] = max(arr[p][q - 1], arr[p - 1][q])
      
print(arr[len(P)][len(Q)])