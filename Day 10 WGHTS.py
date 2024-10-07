def can_measure_weight(test_cases):
    results = []
    for W, X, Y, Z in test_cases:
        if (W == X or W == Y or W == Z or
            W == (X + Y) or W == (X + Z) or W == (Y + Z) or
            W == (X + Y + Z)):
            results.append("YES")
        else:
            results.append("NO")
    return results
T = int(input())
test_cases = []
for _ in range(T):
    W, X, Y, Z = map(int, input().split())
    test_cases.append((W, X, Y, Z))
results = can_measure_weight(test_cases)
for result in results:
    print(result)

