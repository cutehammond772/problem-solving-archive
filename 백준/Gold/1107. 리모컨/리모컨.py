channel = str(int(input()))

N = int(input())
buttons = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def f(cnt):
    if cnt == 0:
        return 0

    return int("1" * cnt)

# 고장난 버튼이 존재할 경우
if N != 0:
    buttons = list(map(int, input().split()))
    buttons = [x for x in range(10) if x not in buttons]
    buttons.sort()

# +, - 버튼만을 이용한 경우
result = abs(int(channel) - 100)

def solve(calc, pos, buttons):
    global result, channel

    if pos == len(channel):
        result = min(result, pos)
        return

    digit = int(channel[pos])

    # digit에 가까운 수 순서대로 (나머지는 오름차순)
    buttons.sort()
    buttons.sort(key = lambda x: abs(x - digit))

    # 동일한 자리에 동일한 숫자가 매치되는 경우
    if buttons[0] == digit:
        solve(calc * 10 + digit, pos + 1, buttons.copy())

        if len(buttons) > 2:
            p, q = buttons[1], buttons[2]
            # k - n, k + n 동시에 연산
            if abs(p - digit) == abs(q - digit) == 1:
                if not (p == 0 and pos == 0):
                    result = min(result, len(channel) + abs(int(channel) - ((calc * 10 + p) * (10 ** (len(channel) - pos - 1)) + f(len(channel) - pos - 1) * max(buttons))))

                result = min(result, len(channel) + abs(int(channel) - ((calc * 10 + q) * (10 ** (len(channel) - pos - 1)) + f(len(channel) - pos - 1) * min(buttons))))
                return
            else:
                # k와의 격차가 더 작은 쪽
                target = p if abs(p - digit) < abs(q - digit) else q
                target = target if not (target == 0 and pos == 0) else (p + q)
                if abs(target - digit) != 1:
                    return

                result = min(result, len(channel) + abs(int(channel) - ((calc * 10 + target) * (10 ** (len(channel) - pos - 1)) + f(len(channel) - pos - 1) * (max(buttons) if target < digit else min(buttons)))))
                return
        else:
            x = buttons[1]
            if abs(x - digit) != 1:
                return

            result = min(result, len(channel) + abs(int(channel) - ((calc * 10 + x) * (10 ** (len(channel) - pos - 1)) + f(len(channel) - pos - 1) * (max(buttons) if x < digit else min(buttons)))))
            return
    else:
        p, q = buttons[0], buttons[1]
        # k - n, k + n 동시에 연산
        if abs(p - digit) == abs(q - digit):
            if not (p == 0 and pos == 0):
                result = min(result, len(channel) + abs(int(channel) - ((calc * 10 + p) * (10 ** (len(channel) - pos - 1)) + f(len(channel) - pos - 1) * max(buttons))))

            result = min(result, len(channel) + abs(int(channel) - ((calc * 10 + q) * (10 ** (len(channel) - pos - 1)) + f(len(channel) - pos - 1) * min(buttons))))
            return
        else:
            # k와의 격차가 더 작은 쪽
            target = p if abs(p - digit) < abs(q - digit) else q
            target = target if not (target == 0 and pos == 0) else (p + q)
            result = min(result, len(channel) + abs(int(channel) - ((calc * 10 + target) * (10 ** (len(channel) - pos - 1)) + f(len(channel) - pos - 1) * (max(buttons) if target < digit else min(buttons)))))
            return

if len(buttons) != 0:
    # 0ch에서 시작하는 경우의 수
    if buttons[0] == 0:
        result = min(result, 1 + int(channel))

    # 1자리에서 (n - 1)자리까지는 숫자 버튼 중 max로만 구성 (단, 숫자가 0만 있는 경우 의미 없으므로 제외)
    if not (len(buttons) == 1 and buttons[0] == 0):
        m = max(buttons)
        for i in range(1, len(channel)):
            result = min(result, i + abs(int(channel) - m * f(i)))
    
    # 버튼이 하나만 있는 경우 (0은 제외)
    if len(buttons) == 1:
        if buttons[0] != 0:
            result = min(result, len(channel) + abs(int(channel) - buttons[0] * f(len(channel))))
    else:
        # n자리의 경우 맨 앞 자리부터 체크 (0 ~ n-1)
        solve(0, 0, buttons.copy())

    # (n + 1)자리의 경우 (맨 앞자리는 0 제외)
    if not (len(buttons) == 1 and buttons[0] == 0):
        min_num = min([x for x in buttons if x != 0])
        result = min(result, (len(channel) + 1) + abs(int(channel) - (min_num * (10 ** len(channel)) + min(buttons) * f(len(channel)))))

# 결과 출력
print(result)