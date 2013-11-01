"""
This is a calculator program.
It is designed to act as a graphical level calculator.
It implements the Sympy modules for calculations that require more advanced computation than the standard math module can handle.
It was designed by Christopher Ferri
It is for Python v. 3.3
It was written on a Windows platform
Any questions, comments, or suggestions should be submitted on the GitHub page.
"""
#Key runtime Modules
import time
import os
import sys
#Python 3.x Test 
min_ver = (3,0)
if sys.version_info < min_ver:
	print ("Your version of Python is incompatible with this program.\nYou must have Python version 3.0 or greater.")
	time.sleep(3)
	sys.exit()
#Standard Library math and misc modules
import math
import cmath
import re
import webbrowser
#Global Variables
global cont
global pi
global e
global sympy_im
global numpy_im
pi = math.pi
e = math.e
#Outside Modules, test if they are installed on operating system
#Sympy Module load
try:
	import sympy
	from sympy import Symbol, var, pprint, Function, sympify, oo, sin, cos, tan, asin, acos, atan, exp, log, ln
	sympy_im = True
except:
	sympy_im = False
	print("Sympy library is not installed.\nThis will limit the functionality of the calculator.\nHowever, the calculator will not be totally inoperable.\n")
	time.sleep(1)
	print("This program will now open a link to the Sympy main page.")
	time.sleep(2)
	webbrowser.open("http://sympy.org/en/index.html",2)
	time.sleep(2)
#Main Menu
def start():
	time.sleep(1)
	while True:
		try:
			os.system('cls')
			global cont
			cont = "y"
			func = ""
			print("If you wish to exit the program, type 'E' at the main prompt\nPlease enter the number associated with the function you wish to access.")
			print("Here are the following function choices:\n")
			print("1.Add-Subtract-Multiply-Divide, 2.Quadratic formula, 3.Modulo, 4.Sine,\n")
			print("5.Cosine, 6.Tangent, 7.Arcsine, 8.Arccosine, 9.Arctangent, 10.Law of cosines,\n")
			print("10.Degree to Radian, 11.Radian to Degree, 12.Law of Cosines, 13.Heron's formula,")
			print("14.Area of a Polygon, 15.Partial sum for x, 16.Distance Formula, 17.Derivative\n") 
			print("18.Gamma function, 19.Factor, 20.Factorial, 21.Compound Interest,\n")
			print("22.Polar to Rectangular Vector, 23.Dot Product, 24.Cross Product, 25.Molar Mass,")
			print("26. Console, 27.Kinetic Energy, 42.???")
			func = input("Choose a function>>")
			if func in ["e","E"]:
				break
			else:
				func = int(func)
			if func == 1:
				addsub()
			if func == 2:
				quadratic()
			if func == 3:
				remain()
			if func == 4:
				sin()
			if func == 5:
				cos()
			if func == 6:
				tan()
			if func == 7:
				arcsin()
			if func == 8:
				arccos()
			if func == 9:
				arctan()
			if func == 10:
				degree()
			if func == 11:
				radian()
			if func == 12:
				lawcos()
			if func == 13:
				heron()
			if func == 14:
				polyarea()
			if func == 15:
				partsum()
			if func == 16:
				distance()
			if func == 17:
				derivitive()
			if func == 18:
				gamma()
			if func == 19:
				factor()
			if func == 20:
				factorial()
			if func == 21:
				compinter()
			if func == 22:
				pol_rec()
			if func == 23:
				dot_product()
			if func == 24:
				cross_product()
			if func == 25:
				molar_mass()
			if func == 26:
				console()
			if func == 27:
				kin_energy()
			if func == 42:
				thematrix()
			elif cont in ["n","N",]:
				pass
			else:
				print("Error: Unknown Function")
				time.sleep(1)
		except:
			print("Error: invalid input")
			time.sleep(1)
#Addition/subtract function
def addsub():
	os.system('cls')
	global pi
	global e
	global cont
	print("This calculator does not follow the rules of mathematical order or PEMDAS,\nuse brackets() frequently!")
	time.sleep(1)
	while cont not in ["n","N"]:
		print("When you have entered all the numbers you wish to compute, type exit or the '=' symbol.")
		time.sleep(1)
		print("If you wish to subtract a number, enter the'-' symbol before the number.")
		num_in = 0
		total_add = 0
		while True:
			num_in = input(">>")
			if num_in in ["exit","Exit","="]:
				break
			try:
				nnum_in = eval(num_in)
				total_add = nnum_in+total_add
				print("\n", total_add)
			except:
				print("Error: invalid input")
				time.sleep(1)
				os.system('cls')
		print(total_add)
		time.sleep(1)
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
#Quadratic equation solver
def quadratic():
	os.system('cls')
	global pi
	global e
	global cont
	print("All complex solutions are expressed as complex numbers, j=i")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			try:
				print("Please enter the coefficients of the polynomial as shown in the equation below.")
				print("ax^2+bx+c")
				time.sleep(1)
				a = float(input("Enter coefficient a>>"))
				b = float(input("Enter coefficient b>>"))
				c = float(input("Enter coefficient c>>"))
				determinate_base = ((b**2)-4*a*c)
				if determinate_base == 0:
					zero_1 = ((((-1)*b))/(2*a))
				elif determinate_base<0:
					determinate = cmath.sqrt(determinate_base)
					zero_1 = ((((-1)*b)+determinate)/(2*a))
					zero_2 = ((((-1)*b)-determinate)/(2*a))
				else:
					determinate = math.sqrt(determinate_base)
					zero_1 = ((((-1)*b)+determinate)/(2*a))
					zero_2 = ((((-1)*b)-determinate)/(2*a))
				print(zero_1)
				if determinate_base != 0:
					print(zero_2)
				break
			except:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		os.system('cls')	
#Sine function
def sin():
	os.system('cls')
	global pi
	global e
	global cont
	print("This calculator operates in radian mode!")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			try:
				os.system('cls')
				print("Please enter the angle you wish to compute the sine of.")
				time.sleep(1)
				ang_1 = float(input("Enter angle>>"))
				total = math.sin(ang_1)
				print(total)
				time.sleep(1)
				break
			except:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		os.system('cls')
#Cosine Function
def cos():
	os.system('cls')
	global pi
	global e
	global cont
	print("This calculator operates in radian mode!")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			try:
				os.system('cls')
				print("Please enter the angle you wish to compute the cosine of.")
				time.sleep(1)
				ang_1 = float(input("Enter angle>>"))
				total = math.cos(ang_1)
				print(total)
				time.sleep(1)
				break
			except:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		os.system('cls')
#Tangent Function
def tan():
	os.system('cls')
	global pi
	global e
	global cont
	print("This calculator operates in radian mode!")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			try:
				os.system('cls')
				print("Please enter the angle you wish to compute the tangent of.")
				time.sleep(1)
				ang_1 = float(input("Enter angle>>"))
				total = math.tan(ang_1)
				print(total)
				time.sleep(1)
				break
			except:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		os.system('cls')
#Arcsine Function
def arcsin():
	os.system('cls')
	global pi
	global e
	global cont
	print("This calculator operates in radian mode!")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			try:
				os.system('cls')
				print("Please enter the sine you wish to compute the angle of.")
				time.sleep(1)
				ang_1 = float(input("Enter sine>>"))
				total = math.arcsin(ang_1)
				print(total)
				time.sleep(1)
				break
			except:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
#Arccosine Function
def arccos():
	os.system('cls')
	global pi
	global e
	global cont
	print("This calculator operates in radian mode!")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			try:
				os.system('cls')
				print("Please enter the cosine you wish to compute the angle of.")
				time.sleep(1)
				ang_1 = float(input("Enter cos>>"))
				total = math.arccos(ang_1)
				print(total)
				time.sleep(1)
				break
			except:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		os.system('cls')
#Arctan Function
def arctan():
	os.system('cls')
	global pi
	global e
	global cont
	print("This calculator operates in radian mode!")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			try:
				os.system('cls')
				print("Please enter the tangent you wish to compute the angle of.")
				time.sleep(1)
				ang_1 = float(input("Enter tan>>"))
				total = math.arctan(ang_1)
				print(total)
				time.sleep(1)
				break
			except:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		os.system('cls')
#Heron's Formula script
'''
While this is not the Heron's formula that everyone is use to, it is a different, more accurate version than the more common version.
The common version is numerically unstable with triangles that have extremely small angles.
For more information, a mathematical paper by Prof. W. Kahan of UC Berkeley on this such problem.
http://www.cs.berkeley.edu/~wkahan/Triangle.pdf
'''
def heron():
	os.system('cls')
	global pi
	global e
	global cont
	print("This is a calculator of the area of a triangle using Heron's formula")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			try:
				print("Enter the lengths of the sides in order of least to greatest")
				side_a = float(input("Please enter the first side of triangle>>"))
				side_b = float(input("Please enter the second side of triangle>>"))
				if side_a>side_b:
					print("Error: The first side is larger than the second side.")
					time.sleep(1)
				else:
					break
			except:
				print("Error: Invalid Input")
				time.sleep(1)
		while True:
			side_c = float(input("Please enter the third side of triangle>>"))
			if side_b>side_c or side_a>side_c:
				print("Error: The third side is not the largest side of the triangle.")
				time.sleep(1)
			else:
				if (side_a+side_b)>side_c and (side_c+side_a)>side_b and (side_b+side_c)>side_a:
					area = (math.sqrt((side_a+(side_b+side_c))*(side_c-(side_a-side_b))*(side_c+(side_a-side_b))*(side_a+(side_b-side_c))))/4
					print(area)
					time.sleep(1)
					while True:
						cont = input("Do you wish to continue:Y or N?>>")
						if cont in ["y","Y"]:
							break
						elif cont in ["n", "N"]:
							break
						else:
							print("Error: Invalid Input!")
							time.sleep(1)
							os.system('cls')
					break
				else:
					print("Error: Impossible Triangle")
					time.sleep(1)
					os.system('cls')
					break
		os.system('cls')
#Area of a Regular polygon script
def polyarea():
	os.system('cls')
	global pi
	global e
	global cont
	print("This is a calculator for the area of a REGULAR polygon.")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			try:
				nsides = input("Please enter the number of sides the polygon contains>>")
				nsides = int(nsides)
				if nsides<=2:
					print("Error: Not a polygon!")
					time.sleep(1)
				else:
					break
			except:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		while True:
			try:
				radius = float(input("Please enter the radius of the polygon, from the center to a vertex>>"))
				total_area = ((radius**2)*(nsides)*(math.sin((2*math.pi)/nsides)))/2
				print(total_area)
				time.sleep(1)
				break
			except:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		os.system('cls')
#Summation Calculator
def partsum():
	os.system('cls')
	global pi
	global e
	global cont
	print("This is a partial sum calculator from 0 to x.")
	while cont not in ["n","N"]:
		while True:
			try:
				sum_i = int(input("Enter the amount of times you wish to sum>>"))
				sum_total = int((sum_i*(sum_i+1))/2)
				print(sum_total)
				time.sleep(1)
				break
			except:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		os.system('cls')
#Easter egg
def thematrix():
	os.system('cls')
	global cont
	while cont not in ["n","N"]:
		pill_c = input("Take the blue pill, and you wake up in your room, thinking this was all a dream.\nTake the red pill, and I show you how far down the rabbit hole goes.\n>>")
		if pill_c in ["blue","Blue","b","B","blue pill","Blue pill","blue Pill","Blue Pill"]:
			cont = "n"
		elif pill_c in ["red","Red","r","R","red pill","Red pill","red Pill","Red Pill"]:
			print("What is the Matrix?")
			time.sleep(1)
			print("The Matrix is a neural-active simulation that is meant to enslave you and turn you into this: a battery.")
			time.sleep(1)
			cont = "n"
		else:
			print("Error: Invalid Input!")
			time.sleep(1)
			os.system('cls')
#distance formula
def distance():
	os.system('cls')
	global pi
	global e
	global cont
	print("This is a Cartesian point to point distance calculator for two dimensions.")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			try:
				x_1,y_1 = input("Please enter the first point with the x and y values separated by a comma>>").split(",")
				x_2,y_2 = input("Please enter the first point with the x and y values separated by a comma>>").split(",")
				y_1 = float(y_1)
				y_2 = float(y_2)
				x_1 = float(x_1)
				x_2 = float(x_2)
				dist = math.sqrt((((x_2)-(x_1))**2)+(((y_2)-(y_1))**2))
				print(dist)
				time.sleep(1)
				break
			except ValueError:
				print("Error: Non-real distance!")
				time.sleep(1)
				os.system('cls')
			except:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		os.system('cls')
#Law of Cosines
def lawcos():
	os.system('cls')
	global pi
	global e
	global cont
	print("This is a calculator using the Law of Cosines.\nALL ANGLES ARE IN RADIANS!")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			ang_leng = input("Do you wish to find an angle or a distance?>>")
			if ang_leng in ["distance","Distance","d","D","Angle","angle","a","A"]:
				break
			else:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		while True:
			if ang_leng in ["distance","Distance","d","D"]:
				print("To find the distance of a side, you must have the distances of the two other sides and the corresponding angle to the side you wish to compute.")
				time.sleep(1)
				try:
					side_a = input("Please enter the first side>>")
					side_b = input("Please enter the second side>>")
					angl_c = input("Please enter the corresponding angle to the distance you wish to compute>>")
					side_a = float(side_a)
					side_b = float(side_b)
					angl_c = float(angl_c)
					side_c = math.sqrt((side_a**2)+(side_b**2)-(2*side_a*side_b*(math.cos(angl_c))))
					if (side_a+side_b)>side_c and (side_c+side_a)>side_b and (side_b+side_c)>side_a:
						print(side_c)
						time.sleep(1)
						break
					else:
						print("Error: Impossible Triangle!")
						time.sleep(1)
						os.system('cls')
				except:
					print("Error: Invalid Input!")
					time.sleep(1)
					os.system('cls')
			elif ang_leng in ["Angle","angle","a","A"]:
				print("To find an angle of a triangle, you must have the lengths of each side of the triangle.")
				time.sleep(1)
				try:
					side_a = input("Please enter the first side>>")
					side_b = input("Please enter the second side>>")
					side_c = input("Please enter the distance of the corresponding side to the angle you wish to compute>>")
					side_a = float(side_a)
					side_b = float(side_b)
					side_c = float(side_c)
					if (side_a+side_b)>side_c and (side_c+side_a)>side_b and (side_b+side_c)>side_a:
						angl_c = math.acos(((side_c**2)-(side_a**2)-(side_b**2))/((-2)*(side_a)*(side_b)))
						print(angl_c)
						time.sleep(1)
						break
					else:
						print("Error: Impossible Triangle!")
						time.sleep(1)
						os.system('cls')
				except:
					print("Error: Invalid Input!")
					time.sleep(1)
					os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		os.system('cls')
#Degree to Radian Script
def degree():
	os.system('cls')
	global pi
	global e
	global cont
	print("This is a Degree to Radian converter.")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			try:
				deg = input("Please enter the degree you wish to convert to radians>>")
				deg = float(deg)
				rad = math.radians(deg)
				print(rad)
				break
			except:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		os.system('cls')
#Radian to Degree Script
def radian():
	os.system('cls')
	global pi
	global e
	global cont
	print("This is a Radian to Degree converter.")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			try:
				deg = input("Please enter the radian you wish to convert to radians>>")
				deg = float(deg)
				rad = math.degree(deg)
				print(rad)
				break
			except:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		os.system('cls')
#Console script
def console():
	os.system('cls')
	global pi
	global e
	global cont
	print("This is a python console built into the program.\nIt uses Python version 3.3.")
	time.sleep(1)
	print("THIS IS ONLY FOR THOSE WHO KNOW THE PYTHON LANGUAGE!\nDO NOT USE IF YOU ARE NOT EXPERENCED WITH THIS LANGUAGE!")
	time.sleep(1)
	print("To exit, type exit or escape in the console.")
	time.sleep(1)
	cons_in = 0
	while cons_in not in ["exit","Exit","escape","e","E"]:
		try:
			cons_in = input("Please enter the command you wish to execute>>")
			exec(cons_in)
		except:
			print("Error: Invalid Command!")
	cont = "n"
#Derivative Script
def derivitive():
	os.system('cls')
	global pi
	global e
	global cont
	if sympy_im == False:
		print("Error: Sympy not installed.\nPlease install sympy to use this function!")
		time.sleep(1)
	elif sympy_im == True:
		from sympy import diff
		from sympy.abc import a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
		print("This is a derivative calculator, it will output an equation.")
		time.sleep(1)
		while cont not in ["n","N"]:
			while True:
				try:
					print("Equation, independent variable, nth derivative you wish to take")
					print("Please split all inputs by a comma!")
					time.sleep(1)
					print("DO NOT USE SPACES!")
					equ, vari, n_th = input("Please enter the information in the exact order listed above>>").split(",")
					sym_string = "{} = Symbol('{}')".format(vari, vari)
					exec(sym_string)
					deriv = diff(equ,vari,n_th)
					pprint(deriv)
					time.sleep(1)
					break
				except:
					print("Error: Invalid Input!")
					time.sleep(1)
			while True:
				cont = input("Do you wish to continue:Y or N?>>")
				if cont in ["y","Y"]:
					break
				elif cont in ["n", "N"]:
					break
				else:
					print("Error: Invalid Input!")
					time.sleep(1)
					os.system('cls')
			os.system('cls')
#Derivative Script
def gamma():
	os.system('cls')
	global pi
	global e
	global cont
	print("This is a gamma function calculator")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			try:
				gam_in = input("Please type the number you wish to find the gamma of>>")
				gam_in = float(gam_in)
				gamma = math.gamma(gam_in)
				print(gamma)
				time.sleep(1)
				break
			except:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		os.system('cls')
#Remander script
def remain():
	os.system('cls')
	global pi
	global e
	global cont
	print("This is a Modulo (a.k.a Remainder) calculator.")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			try:
				print("5,3")
				num_1, num_2 = input("Please enter the numbers you wish to find the modulo of\nin the format shown above>>").split(',')
				num_1 = float(num_1)
				num_2 = float(num_2)
				print(num_1%num_2)
				time.sleep(1)
				break
			except:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		os.system('cls')
#Factorial Script
def factorial():
	os.system('cls')
	global pi
	global e
	global cont
	print("This is a factorial calculator.")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			try:
				fac_num = input("Please enter the integer number that you wish to find the factorial of>>")
				fac_num = int(fac_num)
				fac = math.factorial(fac_num)
				print(fac)
				time.sleep(1)
				break
			except:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		os.system('cls')
#Factoring Script
def factor():
	os.system('cls')
	global pi
	global e
	global cont
	if sympy_im == False:
		print("Error: Sympy is not installed.\nPlease install sympy to use this function!")
		time.sleep(1)
	elif sympy_im == True:
		from sympy import factor, sqrt
		from sympy.abc import a, b, c, d, e, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
		print("This is a polynomial factoring program.")
		time.sleep(1)
		print("Warning!: Polynomials of degree greater than three produce error!  Functionality will be added!")
		time.sleep(1)
		while cont not in ["n","N"]:
			while True:
				try:
					poly_n = input("Please enter the polynomial you wish to factor.>>")
					factor_p = factor(poly_n)
					pprint(factor_p)
					time.sleep(1)
					break
				except:
					print("Error: Invalid Input!")
					time.sleep(1)
					os.system('cls')
			while True:
				cont = input("Do you wish to continue:Y or N?>>")
				if cont in ["y","Y"]:
					break
				elif cont in ["n", "N"]:
					break
				else:
					print("Error: Invalid Input!")
					time.sleep(1)
					os.system('cls')
			os.system('cls')
#Compound Interest
def compinter():
	os.system('cls')
	global pi
	global e
	global cont
	print("This is a compound interest calculator.")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			try:
				princ = input("Enter the amount of the principal investment>>")
				princ = float(princ)
				interrate = input("Enter the interest rate in the form of a percentage>>")
				interrate = float(interrate)
				compt = input("Enter how many times the sum is compounded per year>>")
				compt = int(compt)
				year = input("Enter how many years the sum will accrue interest>>")
				year = float(year)
				finalsum = ((princ)*((1+(interrate/compt))^(compt*year)))
				print(finalsum)
				break
			except:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		os.system('cls')
# Polar to Rectangular vector
def pol_rec():
	os.system('cls')
	global pi
	global e
	global cont
	print("This is a polar to rectangular vector converter.")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			try:
				angle_type = input("Is the angle in radians: y or n>>")
				print("Enter the vector in the format shown below:\n magnitude,angle")
				mag,angle= input("Please enter the polar vector>>").split(',')
				mag = float(mag)
				angle = float(angle)
				if angle_type in ["n","N","no","No"]:
					angle = math.radians(angle)
				x_vec = mag*math.cos(angle)
				y_vec = mag*math.sin(angle)
				print("<{},{}>".format(x_vec,y_vec))
				break
			except:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		os.sys('cls')
# Dot Product function
def dot_product():
	os.system('cls')
	global pi
	global e
	global cont
	print("This is a dot product calculator!")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			try:
				x_1 = 0.0
				y_1 = 0.0
				z_1 = 0.0
				x_2 = 0.0
				y_2 = 0.0
				z_2 = 0.0
				print("Enter vectors in this format: x,y,z,\nAll vector components must be separated by a comma!")
				x_1,y_1,z_1 = input("Please enter the first vector in the format shown above>>").split(',')
				x_1 = float(x_1)
				y_1 = float(y_1)
				z_1 = float(z_1)
				x_2,y_2,z_2 = input("Please enter the second vector in the format shown above>>").split(',')
				x_2 = float(x_2)
				y_2 = float(y_2)
				z_2 = float(z_2)
				total_dot = (x_1*x_2)+(y_1*y_2)+(z_1*z_2)
				print(total_dot)
				time.sleep(1)
			except:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		os.system('cls')
# Cross Product function
def cross_product():
	os.system('cls')
	global pi
	global e
	global cont
	print("This is a cross product calculator!")
	time.sleep(1)
	while cont not in ["n","N"]:
		while True:
			try:
				x_1 = 0.0
				y_1 = 0.0
				z_1 = 0.0
				x_2 = 0.0
				y_2 = 0.0
				z_2 = 0.0
				print("Enter vectors in this format: x,y,z,\nAll vector components must be separated by a comma!")
				x_1,y_1,z_1 = input("Please enter the first vector in the format shown above>>").split(',')
				x_1 = float(x_1)
				y_1 = float(y_1)
				z_1 = float(z_1)
				x_2,y_2,z_2 = input("Please enter the second vector in the format shown above>>").split(',')
				x_2 = float(x_2)
				y_2 = float(y_2)
				z_2 = float(z_2)
				x_cross = (y_1*z_2)-(y_2*z_1)
				y_cross = (x_1*z_2)-(x_2*z_1)
				z_cross = (x_1*y_2)-(x_2*y_1)
				print("<%f,%f,%f>" % (x_cross,y_cross,z_cross))
				time.sleep(1)
			except:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		os.system('cls')
#Molar Mass module
def molar_mass():
	'''
	This is a Chemical equation to molar mass converter.
	Currently, the program requires exact chemical notation.
	While the numbers do not reflect consistent precision, I tried to use the most precise values currently available could find.
	'''
	os.system('cls')
	global cont
	#Element Dictionary
	element = dict()
	element['H'] = 1.00794
	element['He'] = 4.002602
	element['Li'] = 6.941
	element['Be'] = 9.012182
	element['B'] = 10.811
	element['C'] = 12.0107
	element['N'] = 14.0067
	element['O'] = 15.9994
	element['F'] = 18.9984032
	element['Ne'] = 20.1797
	element['Na'] = 22.98976928
	element['Mg'] = 24.3050
	element['Al'] = 26.9815386
	element['Si'] = 28.0855
	element['P'] = 30.973762
	element['S'] = 32.065
	element['Cl'] = 35.453
	element['Ar'] = 39.948
	element['K'] = 39.0983
	element['Ca'] = 40.078
	element['Sc'] = 44.955912
	element['Ti'] = 47.867
	element['V'] = 50.9415
	element['Cr'] = 51.9961
	element['Mn'] = 54.938045
	element['Fe'] = 55.845
	element['Co'] = 58.933195
	element['Ni'] = 58.6934
	element['Cu'] = 63.546
	element['Zn'] = 65.38
	element['Ga'] = 69.723
	element['Ge'] = 72.63
	element['As'] = 74.92160
	element['Se'] = 78.96
	element['Br'] = 79.904
	element['Kr'] = 83.798
	element['Rb'] = 85.4678
	element['Sr'] = 87.62
	element['Y'] = 88.90585
	element['Zr'] = 91.224
	element['Nb'] = 92.90638
	element['Mo'] = 95.96
	element['Tc'] = 98.00
	element['Ru'] = 101.07
	element['Rh'] = 102.90550
	element['Pd'] = 106.42
	element['Ag'] = 107.8682
	element['Cd'] = 112.411
	element['In'] = 114.818
	element['Sn'] = 118.71
	element['Sb'] = 121.760
	element['Te'] = 127.60
	element['I'] = 126.90447
	element['Xe'] = 131.293
	element['Cs'] = 132.9054519
	element['Ba'] = 137.327
	element['La'] = 138.90547
	element['Ce'] = 140.116
	element['Pr'] = 140.90765
	element['Nd'] = 144.242
	element['Pm'] = 145.00
	element['Sm'] = 150.36
	element['Eu'] = 151.964
	element['Gd'] = 157.25
	element['Tb'] = 158.92535
	element['Dy'] = 162.500
	element['Ho'] = 164.93032
	element['Er'] = 167.259
	element['Tm'] = 168.93421
	element['Yb'] = 173.054
	element['Lu'] = 174.9668
	element['Hf'] = 178.49
	element['Ta'] = 180.94788
	element['W'] = 183.84
	element['Re'] = 186.207
	element['Os'] = 190.23
	element['Ir'] = 192.217
	element['Pt'] = 195.084
	element['Au'] = 196.966569
	element['Hg'] = 200.59
	element['Tl'] = 204.3833
	element['Pb'] = 207.2
	element['Bi'] = 208.98040
	element['Po'] = 210.00
	element['At'] = 210.00
	element['Rn'] = 222.00
	element['Fr'] = 223.00
	element['Ra'] = 226.00
	element['Ac'] = 227.00
	element['Th'] = 232.03806
	element['Pa'] = 231.03588
	element['U'] = 238.02891
	element['Np'] = 237.00
	element['Pu'] = 244.00
	element['Am'] = 243.00
	element['Cm'] = 247.00
	element['Bk'] = 247.00
	element['Cf'] = 251.00
	element['Es'] = 252.00
	element['Fm'] = 257.00
	element['Md'] = 258.00
	element['No'] = 259.00
	element['Lr'] = 262.00
	element['Rf'] = 267.00
	element['Db'] = 268.00
	element['Sg'] = 269.00
	element['Bh'] = 270.00
	element['Hs'] = 269.00
	element['Mt'] = 278.00
	element['Ds'] = 281.00
	element['Rg'] = 281.00
	element['Cn'] = 285.00
	element['Uut'] = 286.00
	element['Fl'] = 289.00
	element['Uup'] = 288.00
	element['Lv'] = 293.00
	element['Uus'] = 294.00
	element['Uuo'] = 294.00
	#Element mass function
	def element_mass(element_sym,element_amount=1):
		try:
			mass = element[element_sym]
			element_total_mass = mass*element_amount
			return element_total_mass
		except:
			raise RuntimeError()
	#Splitting Function
	def mol_parse(molecule):
		run_num = 0
		out_stack = []
		pre_stack = re.split('(\d+)',molecule)
		pre_stack_total = len(pre_stack)
		while pre_stack_total > run_num:
			stack_pop = pre_stack.pop()
			try:
				stack_append = int(stack_pop)
				out_stack.append(stack_append)
			except:
				stack_extend = re.findall('[A-Z][^A-Z]*', stack_pop)
				out_stack.extend(stack_extend)
			run_num = run_num+1
		return out_stack
	print("This is a Molecular Mass calculator.\nIt will calculate the molar mass of a chemical.\n")
	time.sleep(1)
	#Main Function
	while cont not in ["n","N"]:
		poly_multiply = 1
		total = 0
		mol_string = "0"
		print("Please enter the molecular formula into the text box as you would naturally write it.\nFor Example. H2O")
		print("Any number placed at the beginning of the chemical will be used as a polymer multiplier\n")
		print("YOU MUST USE THE PROPER CHEMCIAL ELEMENT NOTATION WITH A CAPITAL LETTER FOR THE FIRST LETTER IN THE SYMBOL!")
		try:
			mol_string = input("Please enter the Molecular Formula>>")
			mol_stack = mol_parse(mol_string)
			poly_multiply = mol_stack.pop()
			try:
				poly_muliply = int(poly_multiply)
			except:
				mol_stack.append(poly_multiply)
				poly_multiply = 1
			stack_total = len(mol_stack)
			while stack_total != 0:
				chem_num = 1
				mol_pop = mol_stack.pop()
				try:
					chem_num = int(mol_pop)
				except:
					elem = mol_pop
				stack_totcheck = len(mol_stack)
				if stack_totcheck > 0:
					mol_pop_1 = mol_stack.pop()
					try:
						chem_num = int(mol_pop_1)
					except:
						mol_stack.append(mol_pop_1)
				total = element_mass(elem,chem_num)+total
				stack_total = len(mol_stack)
			total = total*poly_multiply
			print(total,"g/mol")
		except:
			print("Error: Invalid Input!")
			time.sleep(1)
			os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		os.system('cls')
#Kinetic Energy Script
def kin_energy():
	def rel_kin(m,v):
		c_2 = (299792458)**2
		try:
			rel_mult = (1/math.sqrt(1.0-((v**2)/c_2)))-1
			ke = (m*c_2)*(rel_mult)
			return ke
		except ZeroDivisionError:
			print("Sorry Han Solo, according to Einstein, nothing with mass can go the speed of light!")
			time.sleep(2)
			os.system('cls')
		except:
			raise SyntaxError
	def non_rel_kin(m,v):
		try:
			ke = (m*(v**2))/2
			return ke
		except:
			raise SyntaxError
	os.system('cls')
	global pi
	global e
	global cont
	print("This is a Kinetic Energy Calculator.")
	print("It is in the units of Kg, m/s, and J")
	time.sleep(2)
	while cont not in ["n","N"]:
		while True:
			try:
				kin_en = 0.0
				kin_type = input("Do you wish to use the relativistic kinetic energy equation: y or n>>")
				print("\nMass,Velocity")
				mass,velc = input("Please enter the mass and velocity separated as shown above >>").split(',')
				mass = float(mass)
				velc = float(velc)
				if kin_type in ['y','Y']:
					kin_en = rel_kin(mass,velc)
				else:
					kin_en = non_rel_kin(mass,velc)
				print(kin_en,"J")
				time.sleep(1)
				break
			except:
				print("Error: Invalid Input!")
				time.sleep(1)
				os.system('cls')
		while True:
			cont = input("Do you wish to continue:Y or N?>>")
			if cont in ["y","Y"]:
				break
			elif cont in ["n", "N"]:
				break
			else:
				print("Error: Invalid Input")
				time.sleep(1)
				os.system('cls')
		os.system('cls')
#Landing Script
#This is where the program runs
cont = "y"
print("Welcome to the Advanced Math Calculator")
time.sleep(1)
print("This program is intended for those who have an\nhigh-school understanding of mathematics or higher!")
time.sleep(1)
start()
#Exit Script
time.sleep(1)
os.system('cls')
time.sleep(1)
print("This program was designed by Christopher Ferri")
time.sleep(1)
print("He was assisted by Mr. Milton McDonald, who without his general programming experience and Math expertise, this would have never been made!")
time.sleep(1)
print("Thank you for using this program, please feel free to comment, edit, and let me know of any changes or additions you wish for me to add.")
time.sleep(1)
time.sleep(1)
print("Have a good day!")
time.sleep(1)