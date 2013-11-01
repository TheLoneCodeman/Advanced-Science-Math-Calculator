import math
import os
cont = "y"
angle_type = "d"
while cont not in ["n","N"]:
	pi = math.pi
	angle_type = input("What type of angle is it>>")
	mag,angle = input("Please enter the polar vector>>").split(",")
	mag = float(mag)
	angle = float(angle)
	if angle_type in ["d", "D",""]:
		angle = math.radians(angle)
	x_vec = mag*math.cos(angle)
	y_vec = mag*math.sin(angle)
	print("<",x_vec,",", y_vec,">")
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