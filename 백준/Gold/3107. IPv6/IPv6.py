import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(A):
	# 생략 그룹에 대한 전처리
	if "::" in A:
		if A.startswith("::"):
			A = A.replace("::", "_:")
		
		elif A.endswith("::"):
			A = A.replace("::", ":_")
		
		else:
			A = A.replace("::", ":_:")
	
	groups = A.split(":")
	result = []
	
	for group in groups:
		if group == '_':
			result.append(":".join(["0000"] * (8 - len(groups) + 1)))
		
		else:
			result.append(("0" * (4 - len(group))) + group)
	
	return ":".join(result)

if __name__ == "__main__":
	A = input()
	print(solve(A))
	