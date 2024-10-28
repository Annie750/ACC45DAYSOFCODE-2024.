def count_wolverine_minions(N, K, characteristics):
    count = 0
    for value in characteristics:
        new_value = value + K
        if new_value % 7 == 0:
            count += 1
    return count
T = int(input())
results = []
for _ in range(T):
    N, K = map(int, input().split())
    characteristics = list(map(int, input().split()))
    results.append(count_wolverine_minions(N, K, characteristics))
for result in results:
    print(result)
