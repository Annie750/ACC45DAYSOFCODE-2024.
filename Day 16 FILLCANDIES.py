import math
def min_bags_needed(N, K, M):
    capacity_per_bag = K * M
    return math.ceil(N / capacity_per_bag)
T = int(input()) 
for _ in range(T):
    N, K, M = map(int, input().split())
    print(min_bags_needed(N, K, M))

