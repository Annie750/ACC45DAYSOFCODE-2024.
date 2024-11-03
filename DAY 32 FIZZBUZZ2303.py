T = int(input().strip())
results = []
for _ in range(T):
    N = int(input().strip())
    choices = N * (N - 1)
    results.append(choices)
for result in results:
    print(result)
