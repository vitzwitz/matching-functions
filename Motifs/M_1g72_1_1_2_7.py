'''
FUNC:M_1g72_1_1_2_7
PDB:1g72
EC:1.1.2.7
RESI:glu,asp,ca
LOCI:a-171,297,702;
'''
import motifFunctions as cmd
ASP_CA = { 
	'distances':
		[[7.67], [6.25], [6.29], [5.39]],
	'comparisons':
		[[('CB', 'ASP', 'CA', 'CA', 7.67)], [('CG', 'ASP', 'CA', 'CA', 6.25)], [('OD1', 'ASP', 'CA', 'CA', 6.29)], [('OD2', 'ASP', 'CA', 'CA', 5.39)]]}
GLU_CA = { 
	'distances':
		[[7.31], [6.39], [4.91], [4.62], [4.53]],
	'comparisons':
		[[('CB', 'GLU', 'CA', 'CA', 7.31)], [('CG', 'GLU', 'CA', 'CA', 6.39)], [('CD', 'GLU', 'CA', 'CA', 4.91)], [('OE1', 'GLU', 'CA', 'CA', 4.62)], [('OE2', 'GLU', 'CA', 'CA', 4.53)]]}
GLU_ASP = { 
	'distances':
		[[10.55, 9.52, 9.37, 9.12], [9.17, 8.12, 7.89, 7.85], [8.51, 7.29, 7.15, 6.81], [9.15, 7.79, 7.52, 7.26], [7.6, 6.47, 6.6, 5.85]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 10.55), ('CB', 'GLU', 'CG', 'ASP', 9.52), ('CB', 'GLU', 'OD1', 'ASP', 9.37), ('CB', 'GLU', 'OD2', 'ASP', 9.12)], [('CG', 'GLU', 'CB', 'ASP', 9.17), ('CG', 'GLU', 'CG', 'ASP', 8.12), ('CG', 'GLU', 'OD1', 'ASP', 7.89), ('CG', 'GLU', 'OD2', 'ASP', 7.85)], [('CD', 'GLU', 'CB', 'ASP', 8.51), ('CD', 'GLU', 'CG', 'ASP', 7.29), ('CD', 'GLU', 'OD1', 'ASP', 7.15), ('CD', 'GLU', 'OD2', 'ASP', 6.81)], [('OE1', 'GLU', 'CB', 'ASP', 9.15), ('OE1', 'GLU', 'CG', 'ASP', 7.79), ('OE1', 'GLU', 'OD1', 'ASP', 7.52), ('OE1', 'GLU', 'OD2', 'ASP', 7.26)], [('OE2', 'GLU', 'CB', 'ASP', 7.6), ('OE2', 'GLU', 'CG', 'ASP', 6.47), ('OE2', 'GLU', 'OD1', 'ASP', 6.6), ('OE2', 'GLU', 'OD2', 'ASP', 5.85)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_CA, d, 'M_1g72_1_1_2_7')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_CA, d, 'M_1g72_1_1_2_7')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_ASP, d, 'M_1g72_1_1_2_7')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_CA' :  match1,
		'GLU_CA' :  match2,
		'GLU_ASP' :  match3}