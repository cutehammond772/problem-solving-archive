A, B, C = map(int, input().split())

memo = [0] * 31

# A ^ (2 ^ 0) % C
memo[0] = A % C

# 2 ^ (i - 1) + 2 ^ (i - 1) = 2 ^ i
for i in range(1, 31):
  memo[i] = (memo[i - 1] * memo[i - 1]) % C

# bit masking
result = 1
for shift in range(31):
  if B & (1 << shift) > 0:
    result = (result * memo[shift]) % C

print(result)