T = int(input())  
for _ in range(T):
    N = int(input())  
    S = input()  
    
    if N < 4:
        print("YES")  
    else:
        consecutive_consonants = 0
        
        for char in S:
            if char in "aeiou":
                consecutive_consonants = 0
            else:
                consecutive_consonants += 1
                if consecutive_consonants >= 4:
                    print("NO")
                    break
        else:
            print("YES")
