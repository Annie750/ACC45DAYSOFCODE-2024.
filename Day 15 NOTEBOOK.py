T = int(input())  
test_cases = []
for _ in range(T):
    N = int(input())  
    test_cases.append(N)
def print_notebooks(test_cases):
    for N in test_cases:
        notebooks = (N * 1000) // 100
        print(notebooks)
print_notebooks(test_cases)
