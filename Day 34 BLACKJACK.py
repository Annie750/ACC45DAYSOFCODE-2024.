T = int(input().strip())
results = []
for _ in range(T):
    A, B = map(int, input().strip().split())
    C = 21 - (A + B)
    if 1 <= C <= 10:
        results.append(str(C))
    else:
        results.append("-1")
print("\n".join(results))
