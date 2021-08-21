
T = int(input())

for t in range(T):
    k = int(input())
    n = int(input())
    l = []
    cl = []
    for i in range(k+1):
        for j in range(n):
            if i == 0:
                l.append(j+1)
            else:
                d = sum(cl[:j+1])
                l.append(d)
        cl = l
        l=[]
    print(cl[-1])
