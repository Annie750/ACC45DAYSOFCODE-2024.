T = int(input().strip())
results = []
for _ in range(T):
    N = int(input().strip())
    # Check if N is divisible by 4
    if N % 4 == 0:
        results.append("Good")
    else:
        results.append("Not Good")
print("\n".join(results))
