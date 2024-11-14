T = int(input().strip())
results = []
for _ in range(T):
    N = int(input().strip())
    playlist = list(map(int, input().strip().split()))
    K = int(input().strip()) - 1 
    uncle_johny_length = playlist[K]
    sorted_playlist = sorted(playlist)
    new_position = sorted_playlist.index(uncle_johny_length) + 1
    results.append(new_position)
for result in results:
    print(result)
