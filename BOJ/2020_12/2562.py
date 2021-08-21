a = [ int(input()) for i in range(9)]
b = max(a)
print(b)
for key,value in enumerate(a):
    if value == b:
        print(key+1)