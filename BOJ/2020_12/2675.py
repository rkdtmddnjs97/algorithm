t = int(input())

for i in range(t):
    a,b = input().split()
    c =''
    for j in b:
        c += j*int(a)    
    print(c)
            
