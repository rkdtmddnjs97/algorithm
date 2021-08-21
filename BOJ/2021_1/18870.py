n = int(input())
l = list(map(int,input().split()))
c = list(set(l))
c.sort()
d = {}
for i in range(len(c)):
    d[c[i]] =i  

for j in l:
    print(d[j], end=" ")
