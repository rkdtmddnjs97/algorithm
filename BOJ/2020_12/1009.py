import math

def decide(a,b):
    c =[]
    if b==2:
        c = [2,4,8,6]
    elif b == 3:
        c = [3,9,7,1]
    elif b ==7:
        c = [7,9,3,1]
    return c[a-1]
def getDigit(a,b):
    c = int(str(a)[-1])
    if c == 0:
        return 10
    if c%2 ==0 and c%3 != 0:
        d = math.log2(c)
        return decide(int((d*b)%4),2)
    elif c%3 ==0 and c%2 != 0:
        d =  2 if c/3 == 3 else 1
        return decide(int((d*b)%4),3)
    elif c == 7:
        return decide(int(b%4),7)
    else:
        return c

t = int(input())

for i in range(t):
    a,b =map(int,input().split())
    print(getDigit(a,b))