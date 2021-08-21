# 다리 놓기
def factorial(n):
    return n*factorial(n-1) if n>1 else 1


t =int(input())

for i in range(t):
    a,b = input().split(' ')
    c = int(a)
    d = int(b)
    print(int(factorial(d)/(factorial(d-c)*factorial(c))))

