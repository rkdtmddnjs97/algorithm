a = int(input())
b= input()
result = 0
for i in range(a):
    o = ord(b[i])-96
    result += o*(31**i)
print(result%1234567891)
