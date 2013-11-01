'''
This is a Chemical equation to molar mass converter.
It was created by Christopher Ferri
For more information contact me at cferri@udel.edu
Currently, the program requires exact chemical notation.
While the numbers do not reflect consistent precision, I tried to use the most precise values currently available could find.
'''
#Modules and variables Initialization
import time
import math
import re
import os
cont = "y"
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
def mol_chunker(molecule):
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
#Main Function
while cont not in ["n","N"]:
	poly_multiply = 1
	total = 0
	mol_string = "0"
	print("This is a Molecular Mass calculator.\nIt will calculate the molar mass of a chemical.\nPlease enter the molecular formula into the text box as you would naturally write it.\nFor Example. H2O")
	print("DO NOT PLACE CHEMICAL COEFFICHENTS FOR CHEMICAL EQUATIONS INTO THIS CALCULATOR!\n")
	print("YOU MUST USE THE PROPER CHEMCIAL ELEMENT NOTATION WITH A CAPITAL LETTER FOR THE FIRST LETTER IN THE SYMBOL!")
	try:
		mol_string = input("Please enter the Molecular Formula>>")
		mol_stack = mol_chunker(mol_string)
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