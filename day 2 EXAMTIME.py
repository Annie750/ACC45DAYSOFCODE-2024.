T = int(input())

for _ in range(T):
    x_dsa, x_toc, x_dm = map(int, input().split())
    y_dsa, y_toc, y_dm = map(int, input().split())
    
    x_total = x_dsa + x_toc + x_dm
    y_total = y_dsa + y_toc + y_dm
    
    if x_total > y_total:
        print("Dragon")
    elif y_total > x_total:
        print("Sloth")
    else:
        if x_dsa > y_dsa:
            print("Dragon")
        elif y_dsa > x_dsa:
            print("Sloth")
        else:
            if x_toc > y_toc:
                print("Dragon")
            elif y_toc > x_toc:
                print("Sloth")
            else:
                print("Tie")