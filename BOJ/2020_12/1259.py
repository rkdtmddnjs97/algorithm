while True:
    a = input()
    if a[0] == '0':
        break
    flag = True
    l = len(a)      
    for i in range(int(l/2)):
        if a[i] != a[l-i-1]:
            flag = False
            break
        else: 
            flag = True
    
    print("yes" if flag else "no")
    
