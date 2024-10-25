T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    degree = 0
    for i in range(N-1, -1, -1):  # Start from the end of the list
        if A[i] != 0:
            degree = i
            break
    print(degree)

