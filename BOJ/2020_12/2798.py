n,m = map(int,input().split())
a = list(map(int,input().split()))
b =[]
for i in range(len(a)-2):
    for j in range(i+1,len(a)-1):
        for k in range(j+1,len(a)):
            if m - (a[i]+a[j]+a[k]) >= 0:
                b.append(a[i]+a[j]+a[k])
            else:
                continue
print(max(b))


