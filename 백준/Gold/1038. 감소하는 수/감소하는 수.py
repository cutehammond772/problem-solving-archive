def make_arr():
  arr = [0] * 100

  # 1의 자리의 경우 모두 1이다.
  arr[:10] = [1] * 10
  
  for x in range(1, 10):
    for y in range(10):
      if y < x:
        continue
          
      off = (x - 1) * 10
      arr[y + x * 10] = sum(arr[off:(off + y)])
  
  arr[0] = 0
  return arr

def create(N, l):
  if l == 1:
    return [N]
    
  lst = []
  t = N * (10 ** (l - 1))
  
  for i in range(l - 2, N):
    lst += [t + x for x in create(i, l - 1)]
    
  return lst

def solve(N, arr):
  prev = arr[0]
  for i in range(100):
    if prev < N <= prev + arr[i]:
      return create(i % 10, i // 10 + 1)[N - prev - 1]
      
    prev += arr[i]
    
  return -1

if __name__ == "__main__":
  N = int(input())
  
  if N == 0:
    print(0)
  else:
    print(solve(N, make_arr()))
  