a = list(map(int,input().split()))
if a[0] == 1:
    flag =True
    for key,value in enumerate(a):
        if key+1 == value:
            flag = True 
        else:
            flag = False
            break
    if flag:
        print("ascending")
    else:
        print("mixed")
elif a[0] == 8:
    flag = True
    for i in range(1,8):
        if a[i-1] -1 == a[i]:
            flag =True
        else:
            flag =False
            break
    if flag:
        print("descending")
    else:
        print("mixed")
else:
    print("mixed")