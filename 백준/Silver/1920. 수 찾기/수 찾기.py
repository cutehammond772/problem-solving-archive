N = int(input())
nums = set(map(int, input().split()))
M = int(input())
lst = list(map(int, input().split()))

for i in lst:
    if i in nums:
        print("1")
    else:
        print("0")