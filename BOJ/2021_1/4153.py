while True:
    a,b,c = map(int,input().split())
    flag = False
    if a == 0 and b == 0 and c == 0:
        break
    if a**2 == b**2+c**2:
        flag = True
    if b**2 == a**2+c**2:
        flag = True
    if c**2 == a**2+b**2:
        flag = True
    if flag:
        print("right")
    else:
        print("wrong")
    