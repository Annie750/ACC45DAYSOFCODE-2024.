def minimum_coins_required(T, test_cases):
    results = []
    for N in test_cases:
        coins = (N // 5) * 4 + (N % 5)
        results.append(coins)
    return results
if __name__ == "__main__":
    T = int(input()) 
    test_cases = [int(input()) for _ in range(T)]
    results = minimum_coins_required(T, test_cases)
    for result in results:
        print(result)
