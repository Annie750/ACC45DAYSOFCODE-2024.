T = int(input())
for i in range(T):
    P, Q, R, S = map(int, input().split())
    if P > Q + R + S or Q > P + R + S or R > P + Q + S or S > P + Q + R:
        print("YES")
    else:
        print("NO")