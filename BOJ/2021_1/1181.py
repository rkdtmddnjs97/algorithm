def wordsort(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            for k in range(len(l[i])):
                if ord(l[i][k]) > ord(l[j][k]):
                        l[i],l[j] = l[j],l[i]
                        break
                if ord(l[i][k]) == ord(l[j][k]):
                    pass
                else:
                    break
    return l
T = int(input())

l = [ input() for _ in range(T)]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if len(l[i]) > len(l[j]):
            l[i],l[j] = l[j],l[i]
print(l)
a =[]
dex = []
for i in range(len(l)):
    d =[]
    if i in dex:
        pass
    else:
        dex.append(l[i])
        same = len(l[i])
        for j in range(i,len(l)):
            if len(l[j]) == same:
                d.append(l[j])
                dex.append(j)
            else: 
                break
        print("d:",d)
        a += wordsort(d)
            
for i in range(len(a)):
    if a[i] ==a[i-1]:
        pass
    else:
        print(a[i])

            