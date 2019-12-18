#!/usr/bin/python
import subprocess
import sys
import math
#Get input files
file1 = sys.argv[1]
file2 = sys.argv[2]
#Grab atoms
variable = "cp "+str(file1)+" PDB1"
output = subprocess.check_output(['bash', '-c', variable])
variable = "cp "+str(file2)+" PDB2"
output = subprocess.check_output(['bash', '-c', variable])
variable = "cat PDB1 | grep ATOM | grep -v REMARK > temp_ATOMS1"
output = subprocess.check_output(['bash', '-c', variable])
variable = "cat PDB2 | grep ATOM | grep -v REMARK > temp_ATOMS2"
output = subprocess.check_output(['bash', '-c', variable])
#Grab X coordinates
X1 = []
variable = "cat temp_ATOMS1 | awk '{print $7}' > X"
output = subprocess.check_output(['bash', '-c', variable])
with open("X", "r+") as text:
	COOR = text.readlines()
	for i in COOR:
		X1.append(i)
	text.close()
X1 = [x[:-1] for x in X1]
variable = "rm -f X"
output = subprocess.check_output(['bash', '-c', variable])
X2 = []
variable = "cat temp_ATOMS2 | awk '{print $7}' > X"
output = subprocess.check_output(['bash', '-c', variable])
with open("X", "r+") as text:
	COOR = text.readlines()
	for i in COOR:
		X2.append(i)
	text.close()
X2 = [x[:-1] for x in X2]
variable = "rm -f X"
output = subprocess.check_output(['bash', '-c', variable])
#Grab Y coordinates
Y1 = []
variable = "cat temp_ATOMS1 | awk '{print $8}' > Y"
output = subprocess.check_output(['bash', '-c', variable])
with open("Y", "r+") as text:
	COOR = text.readlines()
	for i in COOR:
		Y1.append(i)
	text.close()
Y1 = [x[:-1] for x in Y1]
variable = "rm -f Y"
output = subprocess.check_output(['bash', '-c', variable])
Y2 = []
variable = "cat temp_ATOMS2 | awk '{print $8}' > Y"
output = subprocess.check_output(['bash', '-c', variable])
with open("Y", "r+") as text:
	COOR = text.readlines()
	for i in COOR:
		Y2.append(i)
	text.close()
Y2 = [x[:-1] for x in Y2]
variable = "rm -f Y"
output = subprocess.check_output(['bash', '-c', variable])
#Grab Z coordinates
Z1 = []
variable = "cat temp_ATOMS1 | awk '{print $9}' > Z"
output = subprocess.check_output(['bash', '-c', variable])
with open("Z", "r+") as text:
	COOR = text.readlines()
	for i in COOR:
		Z1.append(i)
	text.close()
Z1 = [x[:-1] for x in Z1]
variable = "rm -f Z"
output = subprocess.check_output(['bash', '-c', variable])
Z2 = []
variable = "cat temp_ATOMS2 | awk '{print $9}' > Z"
output = subprocess.check_output(['bash', '-c', variable])
with open("Z", "r+") as text:
	COOR = text.readlines()
	for i in COOR:
		Z2.append(i)
	text.close()
Z2 = [x[:-1] for x in Z2]
variable = "rm -f Z"
output = subprocess.check_output(['bash', '-c', variable])
#Build cosine array
cosine = ['1.000', '0.996', '0.985', '0.966', '0.940', '0.907', '0.866', '0.819', '0.766', '0.707', '0.643', '0.574', '0.500', '0.423', '0.342', '0.259', '0.174', '0.087', '0.000', '-0.0872', '-0.174', '-0.259', '-0.342', '-0.423', '-0.500', '-0.574', '-0.643', '-0.707', '-0.766', '-0.819', '-0.866', '-0.907', '-0.940', '-0.966', '-0.985', '-0.996', '-1']
#Build sine array
sine = ['0.000', '0.0872', '0.174', '0.259', '0.342', '0.423', '0.500', '0.574', '0.643', '0.707', '0.766', '0.819', '0.866', '0.906', '0.940', '0.966', '0.985', '0.997', '1.000', '-0.996', '-0.985', '-0.966', '-0.940', '-0.906', '-0.866', '-0.819', '-0.766', '-0.707', '-0.643', '-0.574', '-0.500', '-0.423', '-0.342', '-0.259', '-0.174', '-0.0872', '0.000']
#Build tangent array
tan = ['0.000', '0.0875', '0.176', '0.268', '0.364', '0.466', '0.577', '0.700', '0.849', '1.000', '1.192', '1.428', '1.732', '2.145', '2.747', '3.732', '5.761', '11.430']
#Multiply cosine array
#X
X1_multiples = []
for i in range(len(cosine)):
	empty = []
	X1_multiples.append(empty)
	for j in range(len(X1)):
		product = float(cosine[i]) * float(X1[j])
		X1_multiples[i].append(product)
X2_multiples = []
for i in range(len(cosine)):
	empty = []
	X2_multiples.append(empty)
	for j in range(len(X2)):
		product = float(cosine[i]) * float(X2[j])
		X2_multiples[i].append(product)
#Y
Y1_multiples = []
for i in range(len(cosine)):
	empty = []
	Y1_multiples.append(empty)
	for j in range(len(Y1)):
		product = float(cosine[i]) * float(Y1[j])
		Y1_multiples[i].append(product)			
Y2_multiples = []
for i in range(len(cosine)):
	empty = []
	Y2_multiples.append(empty)
	for j in range(len(Y2)):
		product = float(cosine[i]) * float(Y2[j])
		Y2_multiples[i].append(product)			
#Z
Z1_multiples = []
for i in range(len(cosine)):
	empty = []
	Z1_multiples.append(empty)
	for j in range(len(Z1)):
		product = float(cosine[i]) * float(Z1[j])
		Z1_multiples[i].append(product)			
Z2_multiples = []
for i in range(len(cosine)):
	empty = []
	Z2_multiples.append(empty)
	for j in range(len(Z2)):
		product = float(cosine[i]) * float(Z2[j])
		Z2_multiples[i].append(product)			
#Multiply sine array
#X
X1_multiples_sin = []
k = 0
while (k<len(X1_multiples)):
	empty = []
	X1_multiples_sin.append(empty)
	k = k + 1
k = 0
while (k<len(X1_multiples)):
	for i in range(len(sine)):
		empty = []
		X1_multiples_sin[k].append(empty)
		for j in range(len(X1_multiples[k])):
			product = float(sine[i]) * float(X1_multiples[k][j])
			X1_multiples_sin[k][i].append(product)
	k = k + 1								#
X2_multiples_sin = []
k = 0
while (k<len(X2_multiples)):
	empty = []
	X2_multiples_sin.append(empty)
	k = k + 1
k = 0
while (k<len(X2_multiples)):
	for i in range(len(sine)):
		empty = []
		X2_multiples_sin[k].append(empty)
		for j in range(len(X2_multiples[k])):
			product = float(sine[i]) * float(X2_multiples[k][j])
			X2_multiples_sin[k][i].append(product)
	k = k + 1	
#Y
Y1_multiples_sin = []
k = 0
while (k<len(Y1_multiples)):
	empty = []
	Y1_multiples_sin.append(empty)
	k = k + 1
k = 0
while (k<len(Y1_multiples)):
	for i in range(len(sine)):
		empty = []
		Y1_multiples_sin[k].append(empty)
		for j in range(len(Y1_multiples[k])):
			product = float(sine[i]) * float(Y1_multiples[k][j])
			Y1_multiples_sin[k][i].append(product)
	k = k + 1								
Y2_multiples_sin = []
k = 0
while (k<len(Y2_multiples)):
	empty = []
	Y2_multiples_sin.append(empty)
	k = k + 1
k = 0
while (k<len(Y2_multiples)):
	for i in range(len(sine)):
		empty = []
		Y2_multiples_sin[k].append(empty)
		for j in range(len(Y2_multiples[k])):
			product = float(sine[i]) * float(Y2_multiples[k][j])
			Y2_multiples_sin[k][i].append(product)
	k = k + 1								
#Z
Z1_multiples_sin = []
k = 0
while (k<len(Z1_multiples)):
	empty = []
	Z1_multiples_sin.append(empty)
	k = k + 1
k = 0
while (k<len(Z1_multiples)):
	for i in range(len(sine)):
		empty = []
		Z1_multiples_sin[k].append(empty)
		for j in range(len(Z1_multiples[k])):
			product = float(sine[i]) * float(Z1_multiples[k][j])
			Z1_multiples_sin[k][i].append(product)
	k = k + 1								
Z2_multiples_sin = []
k = 0
while (k<len(Z2_multiples)):
	empty = []
	Z2_multiples_sin.append(empty)
	k = k + 1
k = 0
while (k<len(Z2_multiples)):
	for i in range(len(sine)):
		empty = []
		Z2_multiples_sin[k].append(empty)
		for j in range(len(Z2_multiples[k])):
			product = float(sine[i]) * float(Z2_multiples[k][j])
			Z2_multiples_sin[k][i].append(product)
	k = k + 1	
#Multiply tangent array
#X
"""
print X1_multiples_sin[0][0]
print Y1_multiples_sin[0][0]
print Z1_multiples_sin[0][0]
X1_multiples_tan = []
k = 0
while (k<len(X1_multiples_sin)):
	empty = []
	X1_multiples_tan.append(empty)
	k = k + 1
k = 0
while (k<len(X1_multiples_sin)):
	for i in range(len(tan)):
		empty = []
		X1_multiples_tan[k].append(empty)
		for j in range(len(X1_multiples_sin[k])):
			sub = []
			for l in range(len(X1_multiples_sin[k][j])):
				product = float(tan[i]) * float(X1_multiples_sin[k][j][l])
				sub.append(product)
			X1_multiples_tan[k][i].append(sub)
	k = k + 1									#
X2_multiples_tan = []
k = 0
while (k<len(X2_multiples_sin)):
	empty = []
	X2_multiples_tan.append(empty)
	k = k + 1
k = 0
while (k<len(X2_multiples_sin)):
	for i in range(len(tan)):
		empty = []
		X2_multiples_tan[k].append(empty)
		for j in range(len(X2_multiples_sin[k])):
			sub = []
			for l in range(len(X2_multiples_sin[k][j])):
				product = float(tan[i]) * float(X2_multiples_sin[k][j][l])
				sub.append(product)
			X2_multiples_tan[k][i].append(sub)
	k = k + 1									
Y1_multiples_tan = []
k = 0
while (k<len(Y1_multiples_sin)):
	empty = []
	Y1_multiples_tan.append(empty)
	k = k + 1
k = 0
while (k<len(Y1_multiples_sin)):
	for i in range(len(tan)):
		empty = []
		Y1_multiples_tan[k].append(empty)
		for j in range(len(Y1_multiples_sin[k])):
			sub = []
			for l in range(len(Y1_multiples_sin[k][j])):
				product = float(tan[i]) * float(Y1_multiples_sin[k][j][l])
				sub.append(product)
			Y1_multiples_tan[k][i].append(product)
	k = k + 1									
Y2_multiples_tan = []
k = 0
while (k<len(Y2_multiples_sin)):
	empty = []
	Y2_multiples_tan.append(empty)
	k = k + 1
k = 0
while (k<len(Y2_multiples_sin)):
	for i in range(len(tan)):
		empty = []
		Y2_multiples_tan[k].append(empty)
		for j in range(len(Y2_multiples_sin[k])):
			sub = []
			for l in range(len(Y2_multiples_sin[k][j])):
				product = float(tan[i]) * float(Y2_multiples_sin[k][j][l])
				sub.append(product)
			Y2_multiples_tan[k][i].append(product)
	k = k + 1									
Z1_multiples_tan = []
k = 0
while (k<len(Z1_multiples_sin)):
	empty = []
	Z1_multiples_tan.append(empty)
	k = k + 1
k = 0
while (k<len(Z1_multiples_sin)):
	for i in range(len(tan)):
		empty = []
		Z1_multiples_tan[k].append(empty)
		for j in range(len(Z1_multiples_sin[k])):
			sub = []
			for l in range(len(Z1_multiples_sin[k][j])):
				product = float(tan[i]) * float(Z1_multiples_sin[k][j][l])
				sub.append(product)
			Z1_multiples_tan[k][i].append(product)
	k = k + 1									
Z2_multiples_tan = []
k = 0
while (k<len(Z2_multiples_sin)):
	empty = []
	Z2_multiples_tan.append(empty)
	k = k + 1
k = 0
while (k<len(Z2_multiples_sin)):
	for i in range(len(tan)):
		empty = []
		Z2_multiples_tan[k].append(empty)
		for j in range(len(Z2_multiples_sin[k])):
			sub = []
			for l in range(len(Z2_multiples_sin[k][j])):
				product = float(tan[i]) * float(Z2_multiples_sin[k][j][l])
				sub.append(product)
			Z2_multiples_tan[k][i].append(product)
	k = k + 1							"""		
#Calculate distances
distancesx = []
k = 0

while (k<len(X1_multiples_sin)):
	for i in range(len(X1_multiples_sin[k])):
		for l in range(len(X1_multiples_sin[k][i])):
			for j in X2:
				dist = float(X1_multiples_sin[k][i][l]) - float(j)		#x1 - x2
				distancesx.append(dist)
	k = k + 1	
distancesy = []
k = 0
while (k<len(Y1_multiples_sin)):
	for i in range(len(Y1_multiples_sin[k])):
		for l in range(len(Y1_multiples_sin[k][i])):
			for j in Y2:
				dist = float(Y1_multiples_sin[k][i][l]) - float(j)		#x1 - x2
				distancesy.append(dist)
	k = k + 1												
distancesz = []
k = 0
while (k<len(Z1_multiples_sin)):
	for i in range(len(Z1_multiples_sin[k])):
		for l in range(len(Z1_multiples_sin[k][i])):
			for j in Z2:
				dist = float(Z1_multiples_sin[k][i][l]) - float(j)		#x1 - x2
				distancesz.append(dist)
	k = k + 1												
#Transform coordinates
transposex = []
for i in distancesx:
	for k in range(len(X1_multiples_sin)):
		for j in range(len(X1_multiples_sin[k])):
			empty = []
			for l in range(len(X1_multiples_sin[k][j])):
				temp = float(X1_multiples_sin[k][j][l]) + float(i)
				empty.append(temp)	
			transposex.append(empty)						#
transposey = []
for i in distancesy:
	for k in range(len(Y1_multiples_sin)):
		for j in range(len(Y1_multiples_sin[k])):
			empty = []
			for l in range(len(Y1_multiples_sin[k][j])):
				temp = float(Y1_multiples_sin[k][j][l]) + float(i)
				empty.append(temp)	
			transposey.append(empty)						
transposez = []
for i in distancesz:
	for k in range(len(Z1_multiples_sin)):
		for j in range(len(Z1_multiples_sin[k])):
			empty = []
			for l in range(len(Z1_multiples_sin[k][j])):
				temp = float(Z1_multiples_sin[k][j][l]) + float(i)
				empty.append(temp)	
			transposez.append(empty)						#
#Score
print transposex[0]
k = 0
alignments = ["30"]
while (k < len(transposex)):
	scores = []
	for i,j in zip(tranposex[k], X2):
		dist = float(i) - float(j)
		dist_2 = dist**2
		scores.append(dist_2)
	total = 0
	for i in scores:
		total = float(total) + float(i)
	arg = float(total) / float(len(scores)+1)
	RMSD = math.sqrt(arg)
	if (RMSD < min(alignments)):
		pdbx = transposex[k]
	alignments.append(RMSD)
	k = k + 1
print pdbx
print X2
	
		

