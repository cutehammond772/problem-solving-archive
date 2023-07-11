P, Q = map(int, input().split())

if P == Q:
  print(0)
elif Q - P < 4:
  print(Q - P)
else:
  diff = Q - P
  n = 1
  
  while (n ** 2) < diff:
    n += 1
  
  if n ** 2 == diff:
    print(n * 2 - 1)
  else:
    n -= 1
    result = n * 2 - 1
    diff -= n ** 2
    
    while diff != 0:
      if (diff // n) > 0:
        result += diff // n
        diff %= n
        
      n -= 1
      
    print(result)