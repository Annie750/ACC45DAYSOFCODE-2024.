def can_reach_target_score(A, B, C, D):
    if C >= A and D >= B:
        return "POSSIBLE"
    else:
        return "IMPOSSIBLE"
T = int(input())
results = []
for _ in range(T):
    A, B = map(int, input().split())
    C, D = map(int, input().split())
    results.append(can_reach_target_score(A, B, C, D))
print("\n".join(results))
