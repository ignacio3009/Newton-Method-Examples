import numpy as np
a=100
def f(x):
    return a*(x[1]-x[0]**2)**2 + (1-x[0])**2

def df(x):
    return np.array([4*a*(x[0]**3 - x[0]*x[1]) + 2*x[0]-2, 2*a*(x[1]-x[0]**2)])

def d2f(x):
    return 4*a*np.array([[3*x[0]**2 - x[1] + 1/(2*a), -x[0]],[-x[0], 1/2]])

def Hinv(x):
    return np.linalg.inv(d2f(x))

def magL(x):
    return np.linalg.norm(df(x))

x0 = np.array([-1.9,2])
kmax = 100
epsilon=0.001
x1 = x0 - Hinv(x0).dot(df(x0))
Lm = magL(x1)
k=0

while(Lm>epsilon and k<kmax):
    x0=x1
    x1 = x0 - Hinv(x0).dot(df(x0))
    Lm = magL(x1)
    k=k+1
print('Iterations = ',k)
print('Solution =',x1)
