import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
    scores = []

    # A Input
    A = int(input())

    for _ in range(A):
        score_a = int(input())
        scores.append((score_a, 0))

    # B Input
    B = int(input())

    for _ in range(B):
        score_b = int(input())
        scores.append((score_b, 1))

    # Sorting
    scores.sort()

    # Result
    scored_during_first_half = 0
    turnarounds = 0

    team_scores = [0, 0]
    leading = -1

    for i in range(len(scores)):
        time, team = scores[i]

        # first half-time
        if time <= 1440:
            scored_during_first_half += 1

        # turnarounds
        if team_scores[0] == team_scores[1]:
            if leading >= 0 and leading != team:
                turnarounds += 1

            leading = team

        team_scores[team] += 1

    print(scored_during_first_half)
    print(turnarounds)

