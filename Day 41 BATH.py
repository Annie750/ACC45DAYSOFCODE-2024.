T = int(input().strip())
results = []
for _ in range(T):
    X, Y = map(int, input().strip().split())
    water_per_person = 2 * Y
    people = X // water_per_person
    results.append(people)
for result in results:
    print(result)
