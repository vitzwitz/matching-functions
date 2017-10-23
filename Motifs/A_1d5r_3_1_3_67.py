'''
FUNC:A_1d5r_3_1_3_67
PDB:1d5r
EC:3.1.3.67
RESI:asp,cys,arg
LOCI:a-92,124,130;
'''
import motifFunctions as cmd
ARG_ASP = { 
	'distances':
		[[9.66, 9.75, 10.87, 8.9], [8.37, 8.61, 9.79, 7.83], [7.36, 7.78, 8.93, 7.23], [6.69, 6.85, 7.9, 6.28], [6.18, 6.45, 7.36, 6.19], [6.32, 6.98, 7.87, 6.99], [6.1, 6.02, 6.71, 5.82]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 9.66), ('CB', 'ARG', 'CG', 'ASP', 9.75), ('CB', 'ARG', 'OD1', 'ASP', 10.87), ('CB', 'ARG', 'OD2', 'ASP', 8.9)], [('CG', 'ARG', 'CB', 'ASP', 8.37), ('CG', 'ARG', 'CG', 'ASP', 8.61), ('CG', 'ARG', 'OD1', 'ASP', 9.79), ('CG', 'ARG', 'OD2', 'ASP', 7.83)], [('CD', 'ARG', 'CB', 'ASP', 7.36), ('CD', 'ARG', 'CG', 'ASP', 7.78), ('CD', 'ARG', 'OD1', 'ASP', 8.93), ('CD', 'ARG', 'OD2', 'ASP', 7.23)], [('NE', 'ARG', 'CB', 'ASP', 6.69), ('NE', 'ARG', 'CG', 'ASP', 6.85), ('NE', 'ARG', 'OD1', 'ASP', 7.9), ('NE', 'ARG', 'OD2', 'ASP', 6.28)], [('CZ', 'ARG', 'CB', 'ASP', 6.18), ('CZ', 'ARG', 'CG', 'ASP', 6.45), ('CZ', 'ARG', 'OD1', 'ASP', 7.36), ('CZ', 'ARG', 'OD2', 'ASP', 6.19)], [('NH1', 'ARG', 'CB', 'ASP', 6.32), ('NH1', 'ARG', 'CG', 'ASP', 6.98), ('NH1', 'ARG', 'OD1', 'ASP', 7.87), ('NH1', 'ARG', 'OD2', 'ASP', 6.99)], [('NH2', 'ARG', 'CB', 'ASP', 6.1), ('NH2', 'ARG', 'CG', 'ASP', 6.02), ('NH2', 'ARG', 'OD1', 'ASP', 6.71), ('NH2', 'ARG', 'OD2', 'ASP', 5.82)]]}
CYS_ASP = { 
	'distances':
		[[10.11, 9.89, 10.65, 9.2], [10.63, 10.15, 10.88, 9.25]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASP', 10.11), ('CB', 'CYS', 'CG', 'ASP', 9.89), ('CB', 'CYS', 'OD1', 'ASP', 10.65), ('CB', 'CYS', 'OD2', 'ASP', 9.2)], [('SG', 'CYS', 'CB', 'ASP', 10.63), ('SG', 'CYS', 'CG', 'ASP', 10.15), ('SG', 'CYS', 'OD1', 'ASP', 10.88), ('SG', 'CYS', 'OD2', 'ASP', 9.25)]]}
CYS_ARG = { 
	'distances':
		[[5.86, 6.67, 6.43, 5.81, 6.18, 6.99, 6.3], [6.02, 6.96, 7.18, 6.53, 7.18, 8.23, 7.16]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ARG', 5.86), ('CB', 'CYS', 'CG', 'ARG', 6.67), ('CB', 'CYS', 'CD', 'ARG', 6.43), ('CB', 'CYS', 'NE', 'ARG', 5.81), ('CB', 'CYS', 'CZ', 'ARG', 6.18), ('CB', 'CYS', 'NH1', 'ARG', 6.99), ('CB', 'CYS', 'NH2', 'ARG', 6.3)], [('SG', 'CYS', 'CB', 'ARG', 6.02), ('SG', 'CYS', 'CG', 'ARG', 6.96), ('SG', 'CYS', 'CD', 'ARG', 7.18), ('SG', 'CYS', 'NE', 'ARG', 6.53), ('SG', 'CYS', 'CZ', 'ARG', 7.18), ('SG', 'CYS', 'NH1', 'ARG', 8.23), ('SG', 'CYS', 'NH2', 'ARG', 7.16)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_ASP, d, 'A_1d5r_3_1_3_67')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_ASP, d, 'A_1d5r_3_1_3_67')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CYS_ARG, d, 'A_1d5r_3_1_3_67')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_ASP' :  match1,
		'CYS_ASP' :  match2,
		'CYS_ARG' :  match3}