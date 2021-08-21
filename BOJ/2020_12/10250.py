t = int(input())

for i in range(t):
    h,w,n = map(int, input().split())
    a =   n//h if n%h == 0 else n//h+1
    b =  h if n%h == 0 else n%h
    print(b*100 + a)
