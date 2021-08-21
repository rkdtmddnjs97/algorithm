# def factorial(n):
#     if n == 1:
#         return 1
#     elif n == 0:
#         return 0
#     else:
#         return n*factorial(n-1)  

# def combine(n):
#     return factorial(n)/factorial(2)

# m,n = map(int,input().split())

# universe = []
# for i in range(m):
#     universe.append(list(map(int,input().split())))

# multi_universe = []
# for u in universe:
#     s =[]
#     for i in range(1,len(u)):
#         if (u[i]-u[i-1])>0:
#             s.append(1)    
#         elif (u[i]-u[i-1])==0:
#             s.apppend(2)
#         else:
#             s.append(3)
#     multi_universe.append(s)

# print(multi_universe)
# similar = []
# for m in range(len(multi_universe)):
#     count = 0
#     for n in range(m+1,len(multi_universe)):
#         if multi_universe[m] == multi_universe[n]:
#             count += 1
#         else:
#             pass
#     similar.append(count)

# print(similar)
# result = 0
# for s in similar:
#     result += combine(s)

# print(int(result))

#  좌표압축?????

m,N = map(int,input().split()) 

universe = []
for i in range(m):
    universe.append(list(map(int,input().split()))) 
compress = []
for u in universe:
    l = list(set(u)) 
    l.sort()
    d = {}
    w = ''
    for n in range(len(l)):
        d[l[n]] = n
    for j in u:
        w += str(d[j])
    compress.append(w)


dir = {}
for x in compress:
    if x in dir.keys():
        dir[x] += 1
    else:
        dir[x] = 1
result = 0
for k,v in dir.items():
    result += v*(v-1)//2
print(result)




# compress.sort() # 스트링 정렬해주고
# result = 0
# count = 1
# for c in range(1,len(compress)):  # 리스트를 돌자
#     if compress[c] != compress[c-1]: #바뀌는 부분 있으면
#         result += count*(count-1)//2  # 조합으로 계산때림(몇 쌍인지 구하려고)
#         count = 1
#     else:
#         count +=1
# result += count*(count-1)/2
# print(result)

