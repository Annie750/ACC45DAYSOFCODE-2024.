T=int(input())
for i in range(T):
    B1,B2,B3= map(int, input().split())
    if(B1==B2==B3==0):
        print("water filling time")
    elif(B1==B2==B3==1):
        print("Not now")
    elif(B1==B2==1):
        print("Not now")
    elif(B1==B3==1):
        print("Not now")
    elif(B3==B2==1):
        print("Not now")
    elif(B3==B2==0):
        print("water filling time")
    elif(B3==B1==0):
        print("water filling time")
    else:
        print("water filling time")