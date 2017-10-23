'''
FUNC:P_1dj9_2_3_1_47
PDB:1dj9
EC:2.3.1.47
RESI:his,glu,asp,lys
LOCI:a-133,175,204,236;
'''
import motifFunctions as cmd
GLU_LYS = { 
	'distances':
		[[14.3, 13.7, 12.56, 12.21, 13.31], [14.4, 13.64, 12.44, 11.89, 12.85], [13.69, 12.81, 11.67, 10.99, 11.95], [12.85, 12.02, 10.98, 10.38, 11.45], [14.09, 13.09, 11.94, 11.09, 11.9]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LYS', 14.3), ('CB', 'GLU', 'CG', 'LYS', 13.7), ('CB', 'GLU', 'CD', 'LYS', 12.56), ('CB', 'GLU', 'CE', 'LYS', 12.21), ('CB', 'GLU', 'NZ', 'LYS', 13.31)], [('CG', 'GLU', 'CB', 'LYS', 14.4), ('CG', 'GLU', 'CG', 'LYS', 13.64), ('CG', 'GLU', 'CD', 'LYS', 12.44), ('CG', 'GLU', 'CE', 'LYS', 11.89), ('CG', 'GLU', 'NZ', 'LYS', 12.85)], [('CD', 'GLU', 'CB', 'LYS', 13.69), ('CD', 'GLU', 'CG', 'LYS', 12.81), ('CD', 'GLU', 'CD', 'LYS', 11.67), ('CD', 'GLU', 'CE', 'LYS', 10.99), ('CD', 'GLU', 'NZ', 'LYS', 11.95)], [('OE1', 'GLU', 'CB', 'LYS', 12.85), ('OE1', 'GLU', 'CG', 'LYS', 12.02), ('OE1', 'GLU', 'CD', 'LYS', 10.98), ('OE1', 'GLU', 'CE', 'LYS', 10.38), ('OE1', 'GLU', 'NZ', 'LYS', 11.45)], [('OE2', 'GLU', 'CB', 'LYS', 14.09), ('OE2', 'GLU', 'CG', 'LYS', 13.09), ('OE2', 'GLU', 'CD', 'LYS', 11.94), ('OE2', 'GLU', 'CE', 'LYS', 11.09), ('OE2', 'GLU', 'NZ', 'LYS', 11.9)]]}
HIS_ASP = { 
	'distances':
		[[8.07, 7.38, 8.05, 6.36], [8.81, 7.86, 8.36, 6.73], [9.04, 8.06, 8.61, 6.84], [9.69, 8.59, 8.88, 7.56], [9.99, 8.86, 9.23, 7.67], [10.37, 9.17, 9.39, 8.08]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 8.07), ('CB', 'HIS', 'CG', 'ASP', 7.38), ('CB', 'HIS', 'OD1', 'ASP', 8.05), ('CB', 'HIS', 'OD2', 'ASP', 6.36)], [('CG', 'HIS', 'CB', 'ASP', 8.81), ('CG', 'HIS', 'CG', 'ASP', 7.86), ('CG', 'HIS', 'OD1', 'ASP', 8.36), ('CG', 'HIS', 'OD2', 'ASP', 6.73)], [('ND1', 'HIS', 'CB', 'ASP', 9.04), ('ND1', 'HIS', 'CG', 'ASP', 8.06), ('ND1', 'HIS', 'OD1', 'ASP', 8.61), ('ND1', 'HIS', 'OD2', 'ASP', 6.84)], [('CD2', 'HIS', 'CB', 'ASP', 9.69), ('CD2', 'HIS', 'CG', 'ASP', 8.59), ('CD2', 'HIS', 'OD1', 'ASP', 8.88), ('CD2', 'HIS', 'OD2', 'ASP', 7.56)], [('CE1', 'HIS', 'CB', 'ASP', 9.99), ('CE1', 'HIS', 'CG', 'ASP', 8.86), ('CE1', 'HIS', 'OD1', 'ASP', 9.23), ('CE1', 'HIS', 'OD2', 'ASP', 7.67)], [('NE2', 'HIS', 'CB', 'ASP', 10.37), ('NE2', 'HIS', 'CG', 'ASP', 9.17), ('NE2', 'HIS', 'OD1', 'ASP', 9.39), ('NE2', 'HIS', 'OD2', 'ASP', 8.08)]]}
GLU_ASP = { 
	'distances':
		[[6.89, 7.34, 7.67, 7.81], [6.46, 6.79, 7.35, 6.95], [7.22, 7.12, 7.55, 7.04], [7.8, 7.53, 7.69, 7.57], [7.63, 7.42, 7.97, 7.04]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 6.89), ('CB', 'GLU', 'CG', 'ASP', 7.34), ('CB', 'GLU', 'OD1', 'ASP', 7.67), ('CB', 'GLU', 'OD2', 'ASP', 7.81)], [('CG', 'GLU', 'CB', 'ASP', 6.46), ('CG', 'GLU', 'CG', 'ASP', 6.79), ('CG', 'GLU', 'OD1', 'ASP', 7.35), ('CG', 'GLU', 'OD2', 'ASP', 6.95)], [('CD', 'GLU', 'CB', 'ASP', 7.22), ('CD', 'GLU', 'CG', 'ASP', 7.12), ('CD', 'GLU', 'OD1', 'ASP', 7.55), ('CD', 'GLU', 'OD2', 'ASP', 7.04)], [('OE1', 'GLU', 'CB', 'ASP', 7.8), ('OE1', 'GLU', 'CG', 'ASP', 7.53), ('OE1', 'GLU', 'OD1', 'ASP', 7.69), ('OE1', 'GLU', 'OD2', 'ASP', 7.57)], [('OE2', 'GLU', 'CB', 'ASP', 7.63), ('OE2', 'GLU', 'CG', 'ASP', 7.42), ('OE2', 'GLU', 'OD1', 'ASP', 7.97), ('OE2', 'GLU', 'OD2', 'ASP', 7.04)]]}
ASP_LYS = { 
	'distances':
		[[13.51, 12.92, 11.47, 11.15, 11.8], [12.26, 11.59, 10.11, 9.72, 10.32], [11.13, 10.55, 9.08, 8.85, 9.53], [12.49, 11.66, 10.18, 9.56, 10.01]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 13.51), ('CB', 'ASP', 'CG', 'LYS', 12.92), ('CB', 'ASP', 'CD', 'LYS', 11.47), ('CB', 'ASP', 'CE', 'LYS', 11.15), ('CB', 'ASP', 'NZ', 'LYS', 11.8)], [('CG', 'ASP', 'CB', 'LYS', 12.26), ('CG', 'ASP', 'CG', 'LYS', 11.59), ('CG', 'ASP', 'CD', 'LYS', 10.11), ('CG', 'ASP', 'CE', 'LYS', 9.72), ('CG', 'ASP', 'NZ', 'LYS', 10.32)], [('OD1', 'ASP', 'CB', 'LYS', 11.13), ('OD1', 'ASP', 'CG', 'LYS', 10.55), ('OD1', 'ASP', 'CD', 'LYS', 9.08), ('OD1', 'ASP', 'CE', 'LYS', 8.85), ('OD1', 'ASP', 'NZ', 'LYS', 9.53)], [('OD2', 'ASP', 'CB', 'LYS', 12.49), ('OD2', 'ASP', 'CG', 'LYS', 11.66), ('OD2', 'ASP', 'CD', 'LYS', 10.18), ('OD2', 'ASP', 'CE', 'LYS', 9.56), ('OD2', 'ASP', 'NZ', 'LYS', 10.01)]]}
HIS_LYS = { 
	'distances':
		[[13.94, 12.73, 11.5, 10.35, 10.7], [13.36, 12.06, 10.88, 9.59, 9.73], [13.71, 12.41, 11.19, 9.9, 9.8], [12.61, 11.24, 10.18, 8.8, 8.9], [13.25, 11.89, 10.75, 9.38, 9.08], [12.55, 11.14, 10.11, 8.67, 8.47]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'LYS', 13.94), ('CB', 'HIS', 'CG', 'LYS', 12.73), ('CB', 'HIS', 'CD', 'LYS', 11.5), ('CB', 'HIS', 'CE', 'LYS', 10.35), ('CB', 'HIS', 'NZ', 'LYS', 10.7)], [('CG', 'HIS', 'CB', 'LYS', 13.36), ('CG', 'HIS', 'CG', 'LYS', 12.06), ('CG', 'HIS', 'CD', 'LYS', 10.88), ('CG', 'HIS', 'CE', 'LYS', 9.59), ('CG', 'HIS', 'NZ', 'LYS', 9.73)], [('ND1', 'HIS', 'CB', 'LYS', 13.71), ('ND1', 'HIS', 'CG', 'LYS', 12.41), ('ND1', 'HIS', 'CD', 'LYS', 11.19), ('ND1', 'HIS', 'CE', 'LYS', 9.9), ('ND1', 'HIS', 'NZ', 'LYS', 9.8)], [('CD2', 'HIS', 'CB', 'LYS', 12.61), ('CD2', 'HIS', 'CG', 'LYS', 11.24), ('CD2', 'HIS', 'CD', 'LYS', 10.18), ('CD2', 'HIS', 'CE', 'LYS', 8.8), ('CD2', 'HIS', 'NZ', 'LYS', 8.9)], [('CE1', 'HIS', 'CB', 'LYS', 13.25), ('CE1', 'HIS', 'CG', 'LYS', 11.89), ('CE1', 'HIS', 'CD', 'LYS', 10.75), ('CE1', 'HIS', 'CE', 'LYS', 9.38), ('CE1', 'HIS', 'NZ', 'LYS', 9.08)], [('NE2', 'HIS', 'CB', 'LYS', 12.55), ('NE2', 'HIS', 'CG', 'LYS', 11.14), ('NE2', 'HIS', 'CD', 'LYS', 10.11), ('NE2', 'HIS', 'CE', 'LYS', 8.67), ('NE2', 'HIS', 'NZ', 'LYS', 8.47)]]}
HIS_GLU = { 
	'distances':
		[[8.48, 7.08, 6.22, 6.89, 5.19], [9.7, 8.38, 7.44, 7.9, 6.5], [10.68, 9.35, 8.57, 9.11, 7.67], [10.29, 9.08, 7.94, 8.15, 7.08], [11.68, 10.41, 9.53, 9.9, 8.67], [11.49, 10.29, 9.23, 9.42, 8.39]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 8.48), ('CB', 'HIS', 'CG', 'GLU', 7.08), ('CB', 'HIS', 'CD', 'GLU', 6.22), ('CB', 'HIS', 'OE1', 'GLU', 6.89), ('CB', 'HIS', 'OE2', 'GLU', 5.19)], [('CG', 'HIS', 'CB', 'GLU', 9.7), ('CG', 'HIS', 'CG', 'GLU', 8.38), ('CG', 'HIS', 'CD', 'GLU', 7.44), ('CG', 'HIS', 'OE1', 'GLU', 7.9), ('CG', 'HIS', 'OE2', 'GLU', 6.5)], [('ND1', 'HIS', 'CB', 'GLU', 10.68), ('ND1', 'HIS', 'CG', 'GLU', 9.35), ('ND1', 'HIS', 'CD', 'GLU', 8.57), ('ND1', 'HIS', 'OE1', 'GLU', 9.11), ('ND1', 'HIS', 'OE2', 'GLU', 7.67)], [('CD2', 'HIS', 'CB', 'GLU', 10.29), ('CD2', 'HIS', 'CG', 'GLU', 9.08), ('CD2', 'HIS', 'CD', 'GLU', 7.94), ('CD2', 'HIS', 'OE1', 'GLU', 8.15), ('CD2', 'HIS', 'OE2', 'GLU', 7.08)], [('CE1', 'HIS', 'CB', 'GLU', 11.68), ('CE1', 'HIS', 'CG', 'GLU', 10.41), ('CE1', 'HIS', 'CD', 'GLU', 9.53), ('CE1', 'HIS', 'OE1', 'GLU', 9.9), ('CE1', 'HIS', 'OE2', 'GLU', 8.67)], [('NE2', 'HIS', 'CB', 'GLU', 11.49), ('NE2', 'HIS', 'CG', 'GLU', 10.29), ('NE2', 'HIS', 'CD', 'GLU', 9.23), ('NE2', 'HIS', 'OE1', 'GLU', 9.42), ('NE2', 'HIS', 'OE2', 'GLU', 8.39)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_LYS, d, 'P_1dj9_2_3_1_47')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'P_1dj9_2_3_1_47')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_ASP, d, 'P_1dj9_2_3_1_47')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_LYS, d, 'P_1dj9_2_3_1_47')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_LYS, d, 'P_1dj9_2_3_1_47')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(HIS_GLU, d, 'P_1dj9_2_3_1_47')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_LYS' :  match1,
		'HIS_ASP' :  match2,
		'GLU_ASP' :  match3,
		'ASP_LYS' :  match4,
		'HIS_LYS' :  match5,
		'HIS_GLU' :  match6}