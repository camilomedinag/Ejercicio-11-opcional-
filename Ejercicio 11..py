from scipy.optimize import fsolve
import math
x=0
y=0
Miu=0.2
m=100
g=10
a=0.012
def ecuacion(p):
    x,y=p
    return (-Miu*x+m*g*math.sin(y)-m*a,x-m*g*math.cos(x))
(N,O)= fsolve(ecuacion,(0,0))
print ("(","N",",","theta",")","==","(",(N),",",(O),")")