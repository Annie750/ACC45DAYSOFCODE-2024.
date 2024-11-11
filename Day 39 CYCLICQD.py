T = int(input())
results = []
for _ in range(T):
    A, B, C, D = map(int, input().split())
    if (A + C == 180 and B + D == 180):
        results.append("YES")
    else:
        results.append("NO")
print("\n".join(results))

