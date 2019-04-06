x = [1.0,1.6,3.4,4.0,5.2]
y = [1.2,2.0,2.4,3.5,3.5]

def suma(w):
    sum = 0
    for i in range(len(w)):
        sum = w[i] + sum
    return sum

print (suma(x))
print (suma(y))

import pandas as pd

x1 = pd.array(x)
print(x1)
y1 = pd.array(y)
print(y1)

xy = x1*y1
print(xy)

x2 = x1*x1
print(x2)

n = len(x)
print(n)

def lin_reg(m,n):
    x = pd.array(m)
    y = pd.array(n)
    n = len(m)
    x2 = x*x
    sumx2 = (suma(x) * suma(x))
    xy=x*y
    arriba1 = (n*(suma(xy))) - (suma(x) * suma(y))
    abajo1 = (n*(suma (x2))) - sumx2

    a = arriba1 / abajo1

    arriba2 = (suma(y) * suma(x2)) - (suma(xy) * suma(x))
    abajo2 = (n*(suma(x2))) - sumx2

    b = arriba2 / abajo2


    return a,b

print (lin_reg (x,y))
