T = int(input())
for _ in range(T):
    N = int(input())
    contest_codes = input().split()
    start38_count = contest_codes.count("START38")
    ltime108_count = contest_codes.count("LTIME108")
    print(start38_count, ltime108_count)
