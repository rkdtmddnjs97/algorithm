# 평행사변형 둘레
import math
xa,ya,xb,yb,xc,yc = input().split(' ')

dot_a = [float(xa),float(ya)]
dot_b = [float(xb),float(yb)]
dot_c = [float(xc),float(yc)]

def side(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
line = [side(dot_a,dot_b), side(dot_b,dot_c), side(dot_a,dot_c)]
if (dot_a[0]-dot_b[0])*(dot_b[1]-dot_c[1]) == (dot_a[1]-dot_b[1])*(dot_b[0]-dot_c[0]):
    print(-1)
else:
    print(2*(max(line)-min(line)))