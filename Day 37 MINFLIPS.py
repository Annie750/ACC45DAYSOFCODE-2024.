def min_flips_to_zero(T, test_cases):
    results = []
    for case in test_cases:
        N, A = case
        array_sum = sum(A)
        if array_sum == 0:
            results.append(0)
        elif abs(array_sum) % 2 != 0:
            results.append(-1)
        else:
            results.append(abs(array_sum) // 2)
    return results

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    test_cases.append((N, A))

results = min_flips_to_zero(T, test_cases)
for result in results:
    print(result)
