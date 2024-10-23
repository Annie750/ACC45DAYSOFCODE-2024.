T = int(input())
for _ in range(T):
    decisions = list(map(int, input().split()))
    if all(r == 0 for r in decisions):
        print("IN")
    else:
        print("OUT")
