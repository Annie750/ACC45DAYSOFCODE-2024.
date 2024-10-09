def min_time_to_catch_thief(test_cases):
    results = []
    for X, Y in test_cases:
        time_taken = abs(X - Y)  # Since the relative speed is 1
        results.append(time_taken)
    return results
T = int(input())
test_cases = []

for _ in range(T):
    X, Y = map(int, input().split())
    test_cases.append((X, Y))
results = min_time_to_catch_thief(test_cases)
for result in results:
    print(result)

