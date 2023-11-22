import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(preorder, inorder):
	# root는 preorder의 첫번째 글자이다.
	root = preorder[0]

	# inorder의 root의 위치를 기준으로 죄측, 우측의 문자열의 길이를 구한다.
	left_size = inorder.index(root)
	right_size = len(inorder) - left_size - 1

	pre_left, pre_right = preorder[1:(left_size + 1)], preorder[(left_size + 1):]
	in_left, in_right = inorder[:left_size], inorder[(left_size + 1):]

	left = solve(pre_left, in_left) if left_size else ''
	right = solve(pre_right, in_right) if right_size else ''

	return left + right + root

if __name__ == '__main__':
	while data := input():
		preorder, inorder = data.split()
		print(solve(preorder, inorder))
