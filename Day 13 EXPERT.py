T = int(input())  
for _ in range(T):
    X, Y = map(int, input().split())
    if Y * 2 >= X: 
        print("YES")
    else:
        print("NO")