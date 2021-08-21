t = int(input())
for i in range(t):
    a = input()
    l = 0
    point = 0
    for j in a:
        if j == 'O':
            point = point + l +1
            l +=1
        else: 
            l = 0
    print(point)