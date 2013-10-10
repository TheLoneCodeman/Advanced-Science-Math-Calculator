#this is a calculator for exponentials using the number e.  It uses the Taylor series definition to find the approximate number.
import math
import time
total = 0
print("This is a calculator for exponentials using the number e.\nIt uses the Taylor series definition to find the approximate number.")
itterations = input("How many degrees of the polynomial would you like to use>>")
power = input("To what power do you wish to raise e>>")
power = float(power)
itt_num = int(itterations)
for itter in range(itt_num):
	term_sum = power**itter/math.factorial(itter)
	total = total+term_sum
print(total)
time.sleep(4)