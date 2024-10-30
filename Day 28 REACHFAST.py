T = int(input().strip())
results = []
for _ in range(T):
    A, B, K = map(int, input().split())
    distance = abs(B - A)
    if distance == 0:
        results.append(0)
    else:
        steps = distance // K
        if distance % K != 0:
            steps += 1
        results.append(steps)
for result in results:
    print(result)
