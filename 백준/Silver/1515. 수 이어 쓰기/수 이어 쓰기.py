import sys
input = lambda: sys.stdin.readline().rstrip()


if __name__ == '__main__':
    # Counting
    nums = [*input()]
    nums.reverse()

    # 1, 2, ...,
    for x in range(1, 1000000):
        candidate = x

        x = [*str(x)]
        x.reverse()

        while x and nums:
            num = x.pop()

            if num == nums[-1]:
                nums.pop()

        if not nums:
            print(candidate)
            break
