C = int(input())

a =[]
for c in range(C):
    inp = list(map(int,input().split()))
    del inp[0]
    a.append(inp)
for i in a:
    avg = sum(i)/len(i)
    cnt = 0
    for j in i:
        if avg < j:
            cnt +=1
    print(format(round((cnt/len(i))*100,3),".3f")+"%")
