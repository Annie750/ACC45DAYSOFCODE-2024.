def min_flips_to_same_direction(test_cases):
    results = []
    for N, X in test_cases:
        # Calculate the minimum number of flips required
        flips_to_face_up = N - X  # Flipping all face-down cards
        flips_to_face_down = X     # Flipping all face-up cards
        min_flips = min(flips_to_face_up, flips_to_face_down)
        results.append(min_flips)
    return results
T = int(input())
test_cases = []
for _ in range(T):
    N, X = map(int, input().split())
    test_cases.append((N, X))
results = min_flips_to_same_direction(test_cases)
for result in results:
    print(result)
