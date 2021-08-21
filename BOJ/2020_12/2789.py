n,m = map(int,input().split())

a = [ int(input()) for i in range(n)]

for i in range(len(a)):
    if a[i] > a[i-1]:  
        a[i],a[i-1] = a[i-1],a[i]

print(a)
