def find_fastest_transport(T, test_cases):
    results = []
    for x, y in test_cases:
        if x < y:
            results.append("BIKE")
        elif x > y:
            results.append("CAR")
        else:
            results.append("SAME")
    return results
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]
results = find_fastest_transport(T, test_cases)
for result in results:
    print(result)


