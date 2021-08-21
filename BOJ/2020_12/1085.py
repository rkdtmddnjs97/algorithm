x,y,w,h = map(int,input().split())
def minLen(a,b):
    return b-a if b-a<a else a
print( minLen(x,w) if minLen(x,w)<minLen(y,h) else minLen(y,h) )