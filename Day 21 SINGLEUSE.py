T = int(input())
for _ in range(T):
    H, X, Y = map(int, input().split())
    normal_attacks = (H + X - 1) // X  
    remaining_health = H - Y
    if remaining_health > 0:
        special_attacks = 1 + (remaining_health + X - 1) // X
    else:
        special_attacks = 1
    print(min(normal_attacks, special_attacks))
