n= str(input())

if len(n) == 1:
    n = '0'+n
a = int(n[0])+int(n[1]) 
b = str(a)
if len(b) == 1:
    b = '0'+b
p = n[1]+b[1]
count = 1
while p != n:
    a = int(p[0])+int(p[1]) 
    b = str(a)
    if len(b) == 1:
        b = '0'+b
    p = p[1]+b[1]
    count +=1
print(count)