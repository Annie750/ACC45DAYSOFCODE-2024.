T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    score_A_first = (500 - 2 * X) + (1000 - 4 * (X + Y))
    score_B_first = (1000 - 4 * Y) + (500 - 2 * (X + Y))
    max_score = max(score_A_first, score_B_first)
    print(max_score)