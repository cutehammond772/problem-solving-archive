import sys
input = lambda: sys.stdin.readline().rstrip()

# 마트료시카를 구성할 때, 최대 크기가 가장 큰 인형부터 구성하여
# 최대한 한 인형 안에 많은 인형을 넣는 것이 이득이다.
# (예시) 10, 9, 8, ... 과 같이 인형이 존재할 때,
# 10, 9, 8을 따로따로 구성하는 대신 같이 구성하면 10, 10, 10과 다름없는 셈이 된다.
def solve(X):
	count = [0] * 100001
	result = 0
	
	for size in X:
		count[size] += 1
	
	for x in range(100000, 0, -1):
		if count[x] == 0:
			continue
		
		y = x
		value = count[y]
		
		while y > 0 and count[y] > 0:
			value = min(value, count[y])
			
			result += x * value
			count[y] -= value
			y -= 1
		
	return result

if __name__ == '__main__':
	N = int(input())
	X = [*map(int, input().split())]
	
	print(solve(X))
	