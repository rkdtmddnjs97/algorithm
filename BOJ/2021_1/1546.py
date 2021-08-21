n = int(input())
a = list(map(int,input().split()))
m = max(a)
for i in range(len(a)):
    a[i] = a[i]/m*100
print(sum(a)/len(a))