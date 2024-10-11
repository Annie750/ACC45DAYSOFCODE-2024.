T = int(input())
for _ in range(T):
    a, b, c, d = map(int, input().split())
    option1 = a + c
    option2 = a + d
    option3 = b + c
    option4 = b + d
    print(max(option1, option2, option3, option4))

