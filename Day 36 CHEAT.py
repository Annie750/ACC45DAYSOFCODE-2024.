def count_tuesdays(T, test_cases):
    results = []
    for N in test_cases:
        full_weeks = N // 7
        extra_days = N % 7
        tuesday_count = full_weeks + (1 if extra_days >= 2 else 0)
        results.append(tuesday_count)
    return results
T = int(input().strip())
test_cases = [int(input().strip()) for _ in range(T)]
results = count_tuesdays(T, test_cases)
for result in results:
    print(result)
