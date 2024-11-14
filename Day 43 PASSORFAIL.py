T = int(input().strip())
results = []
for _ in range(T):
    N, X, P = map(int, input().strip().split())
    score = 3 * X - (N - X)
    if score >= P:
        results.append("PASS")
    else:
        results.append("FAIL")
print("\n".join(results))
