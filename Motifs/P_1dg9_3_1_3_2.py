'''
FUNC:P_1dg9_3_1_3_2
PDB:1dg9
EC:3.1.3.2
RESI:cys,cys,arg,asp
LOCI:a-12,17,18,129;
'''
import motifFunctions as cmd
ARG_CYSI = { 
	'distances':
		[[6.99, 8.71], [6.67, 8.3], [7.62, 9.05], [7.51, 8.75], [8.61, 9.67], [9.72, 10.8], [8.82, 9.68]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'CYSI', 6.99), ('CB', 'ARG', 'SG', 'CYSI', 8.71)], [('CG', 'ARG', 'CB', 'CYSI', 6.67), ('CG', 'ARG', 'SG', 'CYSI', 8.3)], [('CD', 'ARG', 'CB', 'CYSI', 7.62), ('CD', 'ARG', 'SG', 'CYSI', 9.05)], [('NE', 'ARG', 'CB', 'CYSI', 7.51), ('NE', 'ARG', 'SG', 'CYSI', 8.75)], [('CZ', 'ARG', 'CB', 'CYSI', 8.61), ('CZ', 'ARG', 'SG', 'CYSI', 9.67)], [('NH1', 'ARG', 'CB', 'CYSI', 9.72), ('NH1', 'ARG', 'SG', 'CYSI', 10.8)], [('NH2', 'ARG', 'CB', 'CYSI', 8.82), ('NH2', 'ARG', 'SG', 'CYSI', 9.68)]]}
CYS_CYS = { 
	'distances':
		[[8.99, 10.2], [7.99, 9.11], [8.99, 7.99], [10.2, 9.11]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'CYS', 8.99), ('CB', 'CYS', 'SG', 'CYS', 10.2)], [('SG', 'CYS', 'CB', 'CYS', 7.99), ('SG', 'CYS', 'SG', 'CYS', 9.11)], [('CB', 'CYS', 'CB', 'CYS', 8.99), ('CB', 'CYS', 'SG', 'CYS', 7.99)], [('SG', 'CYS', 'CB', 'CYS', 10.2), ('SG', 'CYS', 'SG', 'CYS', 9.11)]]}
ARG_ASP = { 
	'distances':
		[[8.95, 9.03, 9.67, 8.69], [7.78, 7.99, 8.8, 7.59], [6.74, 7.21, 7.99, 7.13], [6.24, 6.49, 7.03, 6.6], [5.9, 6.31, 6.65, 6.8], [5.99, 6.81, 7.22, 7.45], [6.16, 6.24, 6.22, 6.88]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 8.95), ('CB', 'ARG', 'CG', 'ASP', 9.03), ('CB', 'ARG', 'OD1', 'ASP', 9.67), ('CB', 'ARG', 'OD2', 'ASP', 8.69)], [('CG', 'ARG', 'CB', 'ASP', 7.78), ('CG', 'ARG', 'CG', 'ASP', 7.99), ('CG', 'ARG', 'OD1', 'ASP', 8.8), ('CG', 'ARG', 'OD2', 'ASP', 7.59)], [('CD', 'ARG', 'CB', 'ASP', 6.74), ('CD', 'ARG', 'CG', 'ASP', 7.21), ('CD', 'ARG', 'OD1', 'ASP', 7.99), ('CD', 'ARG', 'OD2', 'ASP', 7.13)], [('NE', 'ARG', 'CB', 'ASP', 6.24), ('NE', 'ARG', 'CG', 'ASP', 6.49), ('NE', 'ARG', 'OD1', 'ASP', 7.03), ('NE', 'ARG', 'OD2', 'ASP', 6.6)], [('CZ', 'ARG', 'CB', 'ASP', 5.9), ('CZ', 'ARG', 'CG', 'ASP', 6.31), ('CZ', 'ARG', 'OD1', 'ASP', 6.65), ('CZ', 'ARG', 'OD2', 'ASP', 6.8)], [('NH1', 'ARG', 'CB', 'ASP', 5.99), ('NH1', 'ARG', 'CG', 'ASP', 6.81), ('NH1', 'ARG', 'OD1', 'ASP', 7.22), ('NH1', 'ARG', 'OD2', 'ASP', 7.45)], [('NH2', 'ARG', 'CB', 'ASP', 6.16), ('NH2', 'ARG', 'CG', 'ASP', 6.24), ('NH2', 'ARG', 'OD1', 'ASP', 6.22), ('NH2', 'ARG', 'OD2', 'ASP', 6.88)]]}
CYS_ASP = { 
	'distances':
		[[9.63, 9.48, 9.48, 9.66], [10.2, 9.76, 9.75, 9.68], [8.95, 8.14, 8.7, 7.08], [9.31, 8.23, 8.63, 7.09]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASP', 9.63), ('CB', 'CYS', 'CG', 'ASP', 9.48), ('CB', 'CYS', 'OD1', 'ASP', 9.48), ('CB', 'CYS', 'OD2', 'ASP', 9.66)], [('SG', 'CYS', 'CB', 'ASP', 10.2), ('SG', 'CYS', 'CG', 'ASP', 9.76), ('SG', 'CYS', 'OD1', 'ASP', 9.75), ('SG', 'CYS', 'OD2', 'ASP', 9.68)], [('CB', 'CYS', 'CB', 'ASP', 8.95), ('CB', 'CYS', 'CG', 'ASP', 8.14), ('CB', 'CYS', 'OD1', 'ASP', 8.7), ('CB', 'CYS', 'OD2', 'ASP', 7.08)], [('SG', 'CYS', 'CB', 'ASP', 9.31), ('SG', 'CYS', 'CG', 'ASP', 8.23), ('SG', 'CYS', 'OD1', 'ASP', 8.63), ('SG', 'CYS', 'OD2', 'ASP', 7.09)]]}
ASP_CYSI = { 
	'distances':
		[[8.95, 9.31], [8.14, 8.23], [8.7, 8.63], [7.08, 7.09]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'CYSI', 8.95), ('CB', 'ASP', 'SG', 'CYSI', 9.31)], [('CG', 'ASP', 'CB', 'CYSI', 8.14), ('CG', 'ASP', 'SG', 'CYSI', 8.23)], [('OD1', 'ASP', 'CB', 'CYSI', 8.7), ('OD1', 'ASP', 'SG', 'CYSI', 8.63)], [('OD2', 'ASP', 'CB', 'CYSI', 7.08), ('OD2', 'ASP', 'SG', 'CYSI', 7.09)]]}
CYS_ARG = { 
	'distances':
		[[6.12, 7.06, 6.89, 5.96, 6.07, 7.03, 5.76], [6.23, 7.28, 7.56, 6.69, 7.14, 8.3, 6.78], [6.99, 6.67, 7.62, 7.51, 8.61, 9.72, 8.82], [8.71, 8.3, 9.05, 8.75, 9.67, 10.8, 9.68]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ARG', 6.12), ('CB', 'CYS', 'CG', 'ARG', 7.06), ('CB', 'CYS', 'CD', 'ARG', 6.89), ('CB', 'CYS', 'NE', 'ARG', 5.96), ('CB', 'CYS', 'CZ', 'ARG', 6.07), ('CB', 'CYS', 'NH1', 'ARG', 7.03), ('CB', 'CYS', 'NH2', 'ARG', 5.76)], [('SG', 'CYS', 'CB', 'ARG', 6.23), ('SG', 'CYS', 'CG', 'ARG', 7.28), ('SG', 'CYS', 'CD', 'ARG', 7.56), ('SG', 'CYS', 'NE', 'ARG', 6.69), ('SG', 'CYS', 'CZ', 'ARG', 7.14), ('SG', 'CYS', 'NH1', 'ARG', 8.3), ('SG', 'CYS', 'NH2', 'ARG', 6.78)], [('CB', 'CYS', 'CB', 'ARG', 6.99), ('CB', 'CYS', 'CG', 'ARG', 6.67), ('CB', 'CYS', 'CD', 'ARG', 7.62), ('CB', 'CYS', 'NE', 'ARG', 7.51), ('CB', 'CYS', 'CZ', 'ARG', 8.61), ('CB', 'CYS', 'NH1', 'ARG', 9.72), ('CB', 'CYS', 'NH2', 'ARG', 8.82)], [('SG', 'CYS', 'CB', 'ARG', 8.71), ('SG', 'CYS', 'CG', 'ARG', 8.3), ('SG', 'CYS', 'CD', 'ARG', 9.05), ('SG', 'CYS', 'NE', 'ARG', 8.75), ('SG', 'CYS', 'CZ', 'ARG', 9.67), ('SG', 'CYS', 'NH1', 'ARG', 10.8), ('SG', 'CYS', 'NH2', 'ARG', 9.68)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_CYSI, d, 'P_1dg9_3_1_3_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_CYS, d, 'P_1dg9_3_1_3_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_ASP, d, 'P_1dg9_3_1_3_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(CYS_ASP, d, 'P_1dg9_3_1_3_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_CYSI, d, 'P_1dg9_3_1_3_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(CYS_ARG, d, 'P_1dg9_3_1_3_2')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_CYSI' :  match1,
		'CYS_CYS' :  match2,
		'ARG_ASP' :  match3,
		'CYS_ASP' :  match4,
		'ASP_CYSI' :  match5,
		'CYS_ARG' :  match6}