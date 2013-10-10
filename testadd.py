import time
import math
print("This calculator does not follow the rules of mathmatical order or PEMDAS!")
time.sleep(1)
print("When you have entered all the numbers you wish to compute, type e or the '=' symbol.")
time.sleep(1)
print("If you wish to subtract a number, enter the'-' symbol before the number")
num_in = 0
total_add = 0
while num_in not in ["e","E","="]:
	num_in = input(">>")
	if num_in not in ["e","E","="]:
		num_in = float(num_in)
		total_add = num_in+total_add
print(total_add)
cont = input("Do you wish to continue:Y or N?>>")
if cont in ["y","Y"]:
	add()
elif cont in ["n", "N"]:
	start()