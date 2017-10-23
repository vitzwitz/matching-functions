'''
FUNC:A_1mrq_1_3_1_20
PDB:1mrq
EC:1.3.1.20
RESI:asp,tyr,lys,his
LOCI:a-50,55,84,117;
'''
import motifFunctions as cmd
LYS_ASP = { 
	'distances':
		[[10.65, 9.39, 9.13, 8.79], [9.21, 7.92, 7.74, 7.28], [9.02, 7.59, 7.2, 7.02], [7.65, 6.17, 5.8, 5.63], [6.84, 5.45, 4.8, 5.35]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASP', 10.65), ('CB', 'LYS', 'CG', 'ASP', 9.39), ('CB', 'LYS', 'OD1', 'ASP', 9.13), ('CB', 'LYS', 'OD2', 'ASP', 8.79)], [('CG', 'LYS', 'CB', 'ASP', 9.21), ('CG', 'LYS', 'CG', 'ASP', 7.92), ('CG', 'LYS', 'OD1', 'ASP', 7.74), ('CG', 'LYS', 'OD2', 'ASP', 7.28)], [('CD', 'LYS', 'CB', 'ASP', 9.02), ('CD', 'LYS', 'CG', 'ASP', 7.59), ('CD', 'LYS', 'OD1', 'ASP', 7.2), ('CD', 'LYS', 'OD2', 'ASP', 7.02)], [('CE', 'LYS', 'CB', 'ASP', 7.65), ('CE', 'LYS', 'CG', 'ASP', 6.17), ('CE', 'LYS', 'OD1', 'ASP', 5.8), ('CE', 'LYS', 'OD2', 'ASP', 5.63)], [('NZ', 'LYS', 'CB', 'ASP', 6.84), ('NZ', 'LYS', 'CG', 'ASP', 5.45), ('NZ', 'LYS', 'OD1', 'ASP', 4.8), ('NZ', 'LYS', 'OD2', 'ASP', 5.35)]]}
HIS_ASP = { 
	'distances':
		[[13.39, 11.95, 11.38, 11.45], [12.39, 10.96, 10.26, 10.61], [12.06, 10.71, 9.95, 10.5], [11.85, 10.39, 9.61, 10.1], [11.33, 10.01, 9.12, 9.95], [11.17, 9.78, 8.87, 9.68]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 13.39), ('CB', 'HIS', 'CG', 'ASP', 11.95), ('CB', 'HIS', 'OD1', 'ASP', 11.38), ('CB', 'HIS', 'OD2', 'ASP', 11.45)], [('CG', 'HIS', 'CB', 'ASP', 12.39), ('CG', 'HIS', 'CG', 'ASP', 10.96), ('CG', 'HIS', 'OD1', 'ASP', 10.26), ('CG', 'HIS', 'OD2', 'ASP', 10.61)], [('ND1', 'HIS', 'CB', 'ASP', 12.06), ('ND1', 'HIS', 'CG', 'ASP', 10.71), ('ND1', 'HIS', 'OD1', 'ASP', 9.95), ('ND1', 'HIS', 'OD2', 'ASP', 10.5)], [('CD2', 'HIS', 'CB', 'ASP', 11.85), ('CD2', 'HIS', 'CG', 'ASP', 10.39), ('CD2', 'HIS', 'OD1', 'ASP', 9.61), ('CD2', 'HIS', 'OD2', 'ASP', 10.1)], [('CE1', 'HIS', 'CB', 'ASP', 11.33), ('CE1', 'HIS', 'CG', 'ASP', 10.01), ('CE1', 'HIS', 'OD1', 'ASP', 9.12), ('CE1', 'HIS', 'OD2', 'ASP', 9.95)], [('NE2', 'HIS', 'CB', 'ASP', 11.17), ('NE2', 'HIS', 'CG', 'ASP', 9.78), ('NE2', 'HIS', 'OD1', 'ASP', 8.87), ('NE2', 'HIS', 'OD2', 'ASP', 9.68)]]}
ASP_TYR = { 
	'distances':
		[[11.03, 10.05, 10.67, 8.66, 10.11, 7.9, 8.74, 8.47], [10.59, 9.44, 9.86, 8.11, 9.14, 7.12, 7.75, 7.29], [9.65, 8.42, 8.76, 7.13, 7.99, 6.05, 6.6, 6.14], [11.3, 10.11, 10.44, 8.83, 9.62, 7.79, 8.26, 7.65]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'TYR', 11.03), ('CB', 'ASP', 'CG', 'TYR', 10.05), ('CB', 'ASP', 'CD1', 'TYR', 10.67), ('CB', 'ASP', 'CD2', 'TYR', 8.66), ('CB', 'ASP', 'CE1', 'TYR', 10.11), ('CB', 'ASP', 'CE2', 'TYR', 7.9), ('CB', 'ASP', 'CZ', 'TYR', 8.74), ('CB', 'ASP', 'OH', 'TYR', 8.47)], [('CG', 'ASP', 'CB', 'TYR', 10.59), ('CG', 'ASP', 'CG', 'TYR', 9.44), ('CG', 'ASP', 'CD1', 'TYR', 9.86), ('CG', 'ASP', 'CD2', 'TYR', 8.11), ('CG', 'ASP', 'CE1', 'TYR', 9.14), ('CG', 'ASP', 'CE2', 'TYR', 7.12), ('CG', 'ASP', 'CZ', 'TYR', 7.75), ('CG', 'ASP', 'OH', 'TYR', 7.29)], [('OD1', 'ASP', 'CB', 'TYR', 9.65), ('OD1', 'ASP', 'CG', 'TYR', 8.42), ('OD1', 'ASP', 'CD1', 'TYR', 8.76), ('OD1', 'ASP', 'CD2', 'TYR', 7.13), ('OD1', 'ASP', 'CE1', 'TYR', 7.99), ('OD1', 'ASP', 'CE2', 'TYR', 6.05), ('OD1', 'ASP', 'CZ', 'TYR', 6.6), ('OD1', 'ASP', 'OH', 'TYR', 6.14)], [('OD2', 'ASP', 'CB', 'TYR', 11.3), ('OD2', 'ASP', 'CG', 'TYR', 10.11), ('OD2', 'ASP', 'CD1', 'TYR', 10.44), ('OD2', 'ASP', 'CD2', 'TYR', 8.83), ('OD2', 'ASP', 'CE1', 'TYR', 9.62), ('OD2', 'ASP', 'CE2', 'TYR', 7.79), ('OD2', 'ASP', 'CZ', 'TYR', 8.26), ('OD2', 'ASP', 'OH', 'TYR', 7.65)]]}
LYS_TYR = { 
	'distances':
		[[10.63, 9.59, 9.34, 9.22, 8.67, 8.55, 8.26, 7.96], [10.46, 9.31, 9.16, 8.69, 8.37, 7.84, 7.66, 7.2], [10.34, 9.02, 8.68, 8.41, 7.66, 7.35, 6.91, 6.17], [10.32, 8.94, 8.74, 8.09, 7.67, 6.89, 6.63, 5.73], [9.02, 7.65, 7.63, 6.69, 6.67, 5.48, 5.47, 4.81]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'TYR', 10.63), ('CB', 'LYS', 'CG', 'TYR', 9.59), ('CB', 'LYS', 'CD1', 'TYR', 9.34), ('CB', 'LYS', 'CD2', 'TYR', 9.22), ('CB', 'LYS', 'CE1', 'TYR', 8.67), ('CB', 'LYS', 'CE2', 'TYR', 8.55), ('CB', 'LYS', 'CZ', 'TYR', 8.26), ('CB', 'LYS', 'OH', 'TYR', 7.96)], [('CG', 'LYS', 'CB', 'TYR', 10.46), ('CG', 'LYS', 'CG', 'TYR', 9.31), ('CG', 'LYS', 'CD1', 'TYR', 9.16), ('CG', 'LYS', 'CD2', 'TYR', 8.69), ('CG', 'LYS', 'CE1', 'TYR', 8.37), ('CG', 'LYS', 'CE2', 'TYR', 7.84), ('CG', 'LYS', 'CZ', 'TYR', 7.66), ('CG', 'LYS', 'OH', 'TYR', 7.2)], [('CD', 'LYS', 'CB', 'TYR', 10.34), ('CD', 'LYS', 'CG', 'TYR', 9.02), ('CD', 'LYS', 'CD1', 'TYR', 8.68), ('CD', 'LYS', 'CD2', 'TYR', 8.41), ('CD', 'LYS', 'CE1', 'TYR', 7.66), ('CD', 'LYS', 'CE2', 'TYR', 7.35), ('CD', 'LYS', 'CZ', 'TYR', 6.91), ('CD', 'LYS', 'OH', 'TYR', 6.17)], [('CE', 'LYS', 'CB', 'TYR', 10.32), ('CE', 'LYS', 'CG', 'TYR', 8.94), ('CE', 'LYS', 'CD1', 'TYR', 8.74), ('CE', 'LYS', 'CD2', 'TYR', 8.09), ('CE', 'LYS', 'CE1', 'TYR', 7.67), ('CE', 'LYS', 'CE2', 'TYR', 6.89), ('CE', 'LYS', 'CZ', 'TYR', 6.63), ('CE', 'LYS', 'OH', 'TYR', 5.73)], [('NZ', 'LYS', 'CB', 'TYR', 9.02), ('NZ', 'LYS', 'CG', 'TYR', 7.65), ('NZ', 'LYS', 'CD1', 'TYR', 7.63), ('NZ', 'LYS', 'CD2', 'TYR', 6.69), ('NZ', 'LYS', 'CE1', 'TYR', 6.67), ('NZ', 'LYS', 'CE2', 'TYR', 5.48), ('NZ', 'LYS', 'CZ', 'TYR', 5.47), ('NZ', 'LYS', 'OH', 'TYR', 4.81)]]}
HIS_TYR = { 
	'distances':
		[[11.89, 10.79, 9.94, 10.88, 9.09, 10.14, 9.22, 8.71], [10.63, 9.46, 8.55, 9.55, 7.63, 8.78, 7.78, 7.28], [9.39, 8.3, 7.44, 8.51, 6.7, 7.92, 6.99, 6.81], [10.58, 9.28, 8.3, 9.29, 7.18, 8.36, 7.23, 6.5], [8.5, 7.3, 6.35, 7.5, 5.46, 6.84, 5.79, 5.62], [9.31, 7.98, 6.97, 8.03, 5.82, 7.13, 5.93, 5.33]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'TYR', 11.89), ('CB', 'HIS', 'CG', 'TYR', 10.79), ('CB', 'HIS', 'CD1', 'TYR', 9.94), ('CB', 'HIS', 'CD2', 'TYR', 10.88), ('CB', 'HIS', 'CE1', 'TYR', 9.09), ('CB', 'HIS', 'CE2', 'TYR', 10.14), ('CB', 'HIS', 'CZ', 'TYR', 9.22), ('CB', 'HIS', 'OH', 'TYR', 8.71)], [('CG', 'HIS', 'CB', 'TYR', 10.63), ('CG', 'HIS', 'CG', 'TYR', 9.46), ('CG', 'HIS', 'CD1', 'TYR', 8.55), ('CG', 'HIS', 'CD2', 'TYR', 9.55), ('CG', 'HIS', 'CE1', 'TYR', 7.63), ('CG', 'HIS', 'CE2', 'TYR', 8.78), ('CG', 'HIS', 'CZ', 'TYR', 7.78), ('CG', 'HIS', 'OH', 'TYR', 7.28)], [('ND1', 'HIS', 'CB', 'TYR', 9.39), ('ND1', 'HIS', 'CG', 'TYR', 8.3), ('ND1', 'HIS', 'CD1', 'TYR', 7.44), ('ND1', 'HIS', 'CD2', 'TYR', 8.51), ('ND1', 'HIS', 'CE1', 'TYR', 6.7), ('ND1', 'HIS', 'CE2', 'TYR', 7.92), ('ND1', 'HIS', 'CZ', 'TYR', 6.99), ('ND1', 'HIS', 'OH', 'TYR', 6.81)], [('CD2', 'HIS', 'CB', 'TYR', 10.58), ('CD2', 'HIS', 'CG', 'TYR', 9.28), ('CD2', 'HIS', 'CD1', 'TYR', 8.3), ('CD2', 'HIS', 'CD2', 'TYR', 9.29), ('CD2', 'HIS', 'CE1', 'TYR', 7.18), ('CD2', 'HIS', 'CE2', 'TYR', 8.36), ('CD2', 'HIS', 'CZ', 'TYR', 7.23), ('CD2', 'HIS', 'OH', 'TYR', 6.5)], [('CE1', 'HIS', 'CB', 'TYR', 8.5), ('CE1', 'HIS', 'CG', 'TYR', 7.3), ('CE1', 'HIS', 'CD1', 'TYR', 6.35), ('CE1', 'HIS', 'CD2', 'TYR', 7.5), ('CE1', 'HIS', 'CE1', 'TYR', 5.46), ('CE1', 'HIS', 'CE2', 'TYR', 6.84), ('CE1', 'HIS', 'CZ', 'TYR', 5.79), ('CE1', 'HIS', 'OH', 'TYR', 5.62)], [('NE2', 'HIS', 'CB', 'TYR', 9.31), ('NE2', 'HIS', 'CG', 'TYR', 7.98), ('NE2', 'HIS', 'CD1', 'TYR', 6.97), ('NE2', 'HIS', 'CD2', 'TYR', 8.03), ('NE2', 'HIS', 'CE1', 'TYR', 5.82), ('NE2', 'HIS', 'CE2', 'TYR', 7.13), ('NE2', 'HIS', 'CZ', 'TYR', 5.93), ('NE2', 'HIS', 'OH', 'TYR', 5.33)]]}
HIS_LYS = { 
	'distances':
		[[5.88, 6.79, 6.44, 7.86, 8.62], [5.77, 6.38, 5.73, 7.01, 7.55], [5.63, 6.3, 5.86, 7.08, 7.27], [6.48, 6.65, 5.59, 6.55, 7.08], [6.27, 6.53, 5.82, 6.71, 6.62], [6.74, 6.73, 5.65, 6.36, 6.47]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'LYS', 5.88), ('CB', 'HIS', 'CG', 'LYS', 6.79), ('CB', 'HIS', 'CD', 'LYS', 6.44), ('CB', 'HIS', 'CE', 'LYS', 7.86), ('CB', 'HIS', 'NZ', 'LYS', 8.62)], [('CG', 'HIS', 'CB', 'LYS', 5.77), ('CG', 'HIS', 'CG', 'LYS', 6.38), ('CG', 'HIS', 'CD', 'LYS', 5.73), ('CG', 'HIS', 'CE', 'LYS', 7.01), ('CG', 'HIS', 'NZ', 'LYS', 7.55)], [('ND1', 'HIS', 'CB', 'LYS', 5.63), ('ND1', 'HIS', 'CG', 'LYS', 6.3), ('ND1', 'HIS', 'CD', 'LYS', 5.86), ('ND1', 'HIS', 'CE', 'LYS', 7.08), ('ND1', 'HIS', 'NZ', 'LYS', 7.27)], [('CD2', 'HIS', 'CB', 'LYS', 6.48), ('CD2', 'HIS', 'CG', 'LYS', 6.65), ('CD2', 'HIS', 'CD', 'LYS', 5.59), ('CD2', 'HIS', 'CE', 'LYS', 6.55), ('CD2', 'HIS', 'NZ', 'LYS', 7.08)], [('CE1', 'HIS', 'CB', 'LYS', 6.27), ('CE1', 'HIS', 'CG', 'LYS', 6.53), ('CE1', 'HIS', 'CD', 'LYS', 5.82), ('CE1', 'HIS', 'CE', 'LYS', 6.71), ('CE1', 'HIS', 'NZ', 'LYS', 6.62)], [('NE2', 'HIS', 'CB', 'LYS', 6.74), ('NE2', 'HIS', 'CG', 'LYS', 6.73), ('NE2', 'HIS', 'CD', 'LYS', 5.65), ('NE2', 'HIS', 'CE', 'LYS', 6.36), ('NE2', 'HIS', 'NZ', 'LYS', 6.47)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_ASP, d, 'A_1mrq_1_3_1_20')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'A_1mrq_1_3_1_20')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_TYR, d, 'A_1mrq_1_3_1_20')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(LYS_TYR, d, 'A_1mrq_1_3_1_20')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_TYR, d, 'A_1mrq_1_3_1_20')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(HIS_LYS, d, 'A_1mrq_1_3_1_20')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_ASP' :  match1,
		'HIS_ASP' :  match2,
		'ASP_TYR' :  match3,
		'LYS_TYR' :  match4,
		'HIS_TYR' :  match5,
		'HIS_LYS' :  match6}