def find_server(t, cases):
    results = []
    for p, q in cases:
        total_points = p + q
        if (total_points // 2) % 2 == 0:
            results.append("Alice")
        else:
            results.append("Bob")
    return results
T = int(input())
cases = [tuple(map(int, input().split())) for _ in range(T)]
results = find_server(T, cases)
for result in results:
    print(result)
