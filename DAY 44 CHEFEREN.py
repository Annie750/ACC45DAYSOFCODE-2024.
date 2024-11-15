import math
def calculate_total_duration(T, test_cases):
    results = []
    for i in range(T):
        N, A, B = test_cases[i]
        odd_count = (N + 1) // 2  
        even_count = N // 2       
        total_duration = (odd_count * B) + (even_count * A)
        results.append(total_duration)
    return results
if __name__ == "__main__":
    T = int(input())
    test_cases = []
    for _ in range(T):
        parts = input().strip().split()
        while len(parts) < 3:
            parts += input().strip().split()
        N, A, B = map(int, parts[:3])
        test_cases.append((N, A, B))
    results = calculate_total_duration(T, test_cases)
    for res in results:
        print(res)
