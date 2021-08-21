# 이항계수 1
def factorial(n):
    return n*factorial(n-1) if n>1 else 1
n,k = map(int,input().split())
print(int(factorial(n)/(factorial(n-k)*factorial(k))))