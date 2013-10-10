#This is a pi calculator based on the Gauss-Legendre algorithm
#For more information visit this link
import time
import math
itter = 0
a = 1
b = 1/math.sqrt(2)
t = 0.25
p = 1
#Base iterative algorithms
def afunc(x,y):
	a_new = (x+y)/2
	return a_new
def bfunc(x,y):
	b_new = math.sqrt(x*y)
	return b_new
def tfunc(x,y,z,z1):
	t_new = x-(y*((z-z1)**2))
	return t_new
def pfunc(x):
	p_new = 2*x
	return p_new
#Base runtime component
print("This is a pi calculating program using the Gauss-Legendre algorithm\nFor more info, search on Wikipedia.")
itter_choice = input("Please enter the amount of iterations you desire>>")
itter_choice = int(itter_choice)
while itter < itter_choice:
	a1 = afunc(a,b)
	b1 = bfunc(b,a)
	t = tfunc(t,p,a,a1)
	p = pfunc(p)
	a = a1
	b = b1
	itter = itter+1
#a1 = afunc(a,b)
#t = tfunc(t,p,a,a1)
pi = ((a+b)**2)/(4*t)
print(pi)
pi_diff = abs(math.pi-pi)
print("Difference from actual value>>",pi_diff)
time.sleep(5)