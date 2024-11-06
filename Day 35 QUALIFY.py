T = int(input())
for _ in range(T):
    X, A, B = map(int, input().split())
    total_score = A * 1 + B * 2
    if total_score >= X:
        print("Qualify")
    else:
        print("NotQualify")
