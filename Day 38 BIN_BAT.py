import math
T= int(input())
for _ in range(T):
    N, A, B = map(int, input().split())
    R = int(math.log2(N))
    total_time = R * A + (R - 1) * B
    print(total_time)