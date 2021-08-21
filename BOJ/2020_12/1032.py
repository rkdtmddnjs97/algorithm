a = int(input())
b = [ input() for i in range(0,a)]
e = []
for j in range(len(b[0])):
    for k in b:
        d = True
        if b.index(k) == 0:
            c = k[j]
        else:
            if c == k[j]:
                d = True
                c = k[j]
            else:
                d = False
                break
    if d:
        e.append(c)
    else:
        e.append("?")
        d = True
    
print(''.join(e))