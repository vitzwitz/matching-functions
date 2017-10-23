'''
FUNC:Pab_1ah3_1_1_1_21
PDB:1ah3
EC:1.1.1.21
RESI:asp,tyr,lys,his
LOCI:a-43,48,77,110;
'''
import motifFunctions as cmd
LYS_HIS = { 
	'distances':
		[[5.76, 5.69, 5.63, 6.46, 6.34, 6.78], [6.72, 6.33, 6.28, 6.67, 6.58, 6.79], [6.5, 5.74, 5.76, 5.66, 5.7, 5.64], [7.94, 7.05, 6.98, 6.72, 6.61, 6.44], [8.55, 7.46, 7.04, 7.18, 6.46, 6.56]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'HIS', 5.76), ('CB', 'LYS', 'CG', 'HIS', 5.69), ('CB', 'LYS', 'ND1', 'HIS', 5.63), ('CB', 'LYS', 'CD2', 'HIS', 6.46), ('CB', 'LYS', 'CE1', 'HIS', 6.34), ('CB', 'LYS', 'NE2', 'HIS', 6.78)], [('CG', 'LYS', 'CB', 'HIS', 6.72), ('CG', 'LYS', 'CG', 'HIS', 6.33), ('CG', 'LYS', 'ND1', 'HIS', 6.28), ('CG', 'LYS', 'CD2', 'HIS', 6.67), ('CG', 'LYS', 'CE1', 'HIS', 6.58), ('CG', 'LYS', 'NE2', 'HIS', 6.79)], [('CD', 'LYS', 'CB', 'HIS', 6.5), ('CD', 'LYS', 'CG', 'HIS', 5.74), ('CD', 'LYS', 'ND1', 'HIS', 5.76), ('CD', 'LYS', 'CD2', 'HIS', 5.66), ('CD', 'LYS', 'CE1', 'HIS', 5.7), ('CD', 'LYS', 'NE2', 'HIS', 5.64)], [('CE', 'LYS', 'CB', 'HIS', 7.94), ('CE', 'LYS', 'CG', 'HIS', 7.05), ('CE', 'LYS', 'ND1', 'HIS', 6.98), ('CE', 'LYS', 'CD2', 'HIS', 6.72), ('CE', 'LYS', 'CE1', 'HIS', 6.61), ('CE', 'LYS', 'NE2', 'HIS', 6.44)], [('NZ', 'LYS', 'CB', 'HIS', 8.55), ('NZ', 'LYS', 'CG', 'HIS', 7.46), ('NZ', 'LYS', 'ND1', 'HIS', 7.04), ('NZ', 'LYS', 'CD2', 'HIS', 7.18), ('NZ', 'LYS', 'CE1', 'HIS', 6.46), ('NZ', 'LYS', 'NE2', 'HIS', 6.56)]]}
ASP_HIS = { 
	'distances':
		[[13.29, 12.32, 11.95, 11.9, 11.31, 11.29], [11.83, 10.86, 10.56, 10.41, 9.94, 9.85], [11.3, 10.48, 10.32, 10.1, 9.85, 9.72], [11.34, 10.23, 9.87, 9.7, 9.11, 9.01]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 13.29), ('CB', 'ASP', 'CG', 'HIS', 12.32), ('CB', 'ASP', 'ND1', 'HIS', 11.95), ('CB', 'ASP', 'CD2', 'HIS', 11.9), ('CB', 'ASP', 'CE1', 'HIS', 11.31), ('CB', 'ASP', 'NE2', 'HIS', 11.29)], [('CG', 'ASP', 'CB', 'HIS', 11.83), ('CG', 'ASP', 'CG', 'HIS', 10.86), ('CG', 'ASP', 'ND1', 'HIS', 10.56), ('CG', 'ASP', 'CD2', 'HIS', 10.41), ('CG', 'ASP', 'CE1', 'HIS', 9.94), ('CG', 'ASP', 'NE2', 'HIS', 9.85)], [('OD1', 'ASP', 'CB', 'HIS', 11.3), ('OD1', 'ASP', 'CG', 'HIS', 10.48), ('OD1', 'ASP', 'ND1', 'HIS', 10.32), ('OD1', 'ASP', 'CD2', 'HIS', 10.1), ('OD1', 'ASP', 'CE1', 'HIS', 9.85), ('OD1', 'ASP', 'NE2', 'HIS', 9.72)], [('OD2', 'ASP', 'CB', 'HIS', 11.34), ('OD2', 'ASP', 'CG', 'HIS', 10.23), ('OD2', 'ASP', 'ND1', 'HIS', 9.87), ('OD2', 'ASP', 'CD2', 'HIS', 9.7), ('OD2', 'ASP', 'CE1', 'HIS', 9.11), ('OD2', 'ASP', 'NE2', 'HIS', 9.01)]]}
TYR_HIS = { 
	'distances':
		[[12.09, 10.83, 9.57, 10.95, 8.87, 9.81], [11.06, 9.72, 8.53, 9.69, 7.68, 8.51], [10.2, 8.81, 7.64, 8.71, 6.7, 7.49], [11.19, 9.85, 8.76, 9.74, 7.89, 8.59], [9.4, 7.92, 6.9, 7.63, 5.79, 6.36], [10.49, 9.11, 8.17, 8.83, 7.2, 7.69], [9.56, 8.1, 7.21, 7.71, 6.1, 6.49], [9.09, 7.63, 7.0, 7.0, 5.84, 5.85]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'HIS', 12.09), ('CB', 'TYR', 'CG', 'HIS', 10.83), ('CB', 'TYR', 'ND1', 'HIS', 9.57), ('CB', 'TYR', 'CD2', 'HIS', 10.95), ('CB', 'TYR', 'CE1', 'HIS', 8.87), ('CB', 'TYR', 'NE2', 'HIS', 9.81)], [('CG', 'TYR', 'CB', 'HIS', 11.06), ('CG', 'TYR', 'CG', 'HIS', 9.72), ('CG', 'TYR', 'ND1', 'HIS', 8.53), ('CG', 'TYR', 'CD2', 'HIS', 9.69), ('CG', 'TYR', 'CE1', 'HIS', 7.68), ('CG', 'TYR', 'NE2', 'HIS', 8.51)], [('CD1', 'TYR', 'CB', 'HIS', 10.2), ('CD1', 'TYR', 'CG', 'HIS', 8.81), ('CD1', 'TYR', 'ND1', 'HIS', 7.64), ('CD1', 'TYR', 'CD2', 'HIS', 8.71), ('CD1', 'TYR', 'CE1', 'HIS', 6.7), ('CD1', 'TYR', 'NE2', 'HIS', 7.49)], [('CD2', 'TYR', 'CB', 'HIS', 11.19), ('CD2', 'TYR', 'CG', 'HIS', 9.85), ('CD2', 'TYR', 'ND1', 'HIS', 8.76), ('CD2', 'TYR', 'CD2', 'HIS', 9.74), ('CD2', 'TYR', 'CE1', 'HIS', 7.89), ('CD2', 'TYR', 'NE2', 'HIS', 8.59)], [('CE1', 'TYR', 'CB', 'HIS', 9.4), ('CE1', 'TYR', 'CG', 'HIS', 7.92), ('CE1', 'TYR', 'ND1', 'HIS', 6.9), ('CE1', 'TYR', 'CD2', 'HIS', 7.63), ('CE1', 'TYR', 'CE1', 'HIS', 5.79), ('CE1', 'TYR', 'NE2', 'HIS', 6.36)], [('CE2', 'TYR', 'CB', 'HIS', 10.49), ('CE2', 'TYR', 'CG', 'HIS', 9.11), ('CE2', 'TYR', 'ND1', 'HIS', 8.17), ('CE2', 'TYR', 'CD2', 'HIS', 8.83), ('CE2', 'TYR', 'CE1', 'HIS', 7.2), ('CE2', 'TYR', 'NE2', 'HIS', 7.69)], [('CZ', 'TYR', 'CB', 'HIS', 9.56), ('CZ', 'TYR', 'CG', 'HIS', 8.1), ('CZ', 'TYR', 'ND1', 'HIS', 7.21), ('CZ', 'TYR', 'CD2', 'HIS', 7.71), ('CZ', 'TYR', 'CE1', 'HIS', 6.1), ('CZ', 'TYR', 'NE2', 'HIS', 6.49)], [('OH', 'TYR', 'CB', 'HIS', 9.09), ('OH', 'TYR', 'CG', 'HIS', 7.63), ('OH', 'TYR', 'ND1', 'HIS', 7.0), ('OH', 'TYR', 'CD2', 'HIS', 7.0), ('OH', 'TYR', 'CE1', 'HIS', 5.84), ('OH', 'TYR', 'NE2', 'HIS', 5.85)]]}
ASP_TYR = { 
	'distances':
		[[11.25, 10.25, 10.83, 8.87, 10.2, 8.03, 8.81, 8.42], [10.78, 9.62, 10.01, 8.33, 9.22, 7.29, 7.84, 7.27], [11.44, 10.27, 10.57, 9.04, 9.72, 7.98, 8.39, 7.72], [9.93, 8.68, 8.98, 7.43, 8.13, 6.28, 6.74, 6.14]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'TYR', 11.25), ('CB', 'ASP', 'CG', 'TYR', 10.25), ('CB', 'ASP', 'CD1', 'TYR', 10.83), ('CB', 'ASP', 'CD2', 'TYR', 8.87), ('CB', 'ASP', 'CE1', 'TYR', 10.2), ('CB', 'ASP', 'CE2', 'TYR', 8.03), ('CB', 'ASP', 'CZ', 'TYR', 8.81), ('CB', 'ASP', 'OH', 'TYR', 8.42)], [('CG', 'ASP', 'CB', 'TYR', 10.78), ('CG', 'ASP', 'CG', 'TYR', 9.62), ('CG', 'ASP', 'CD1', 'TYR', 10.01), ('CG', 'ASP', 'CD2', 'TYR', 8.33), ('CG', 'ASP', 'CE1', 'TYR', 9.22), ('CG', 'ASP', 'CE2', 'TYR', 7.29), ('CG', 'ASP', 'CZ', 'TYR', 7.84), ('CG', 'ASP', 'OH', 'TYR', 7.27)], [('OD1', 'ASP', 'CB', 'TYR', 11.44), ('OD1', 'ASP', 'CG', 'TYR', 10.27), ('OD1', 'ASP', 'CD1', 'TYR', 10.57), ('OD1', 'ASP', 'CD2', 'TYR', 9.04), ('OD1', 'ASP', 'CE1', 'TYR', 9.72), ('OD1', 'ASP', 'CE2', 'TYR', 7.98), ('OD1', 'ASP', 'CZ', 'TYR', 8.39), ('OD1', 'ASP', 'OH', 'TYR', 7.72)], [('OD2', 'ASP', 'CB', 'TYR', 9.93), ('OD2', 'ASP', 'CG', 'TYR', 8.68), ('OD2', 'ASP', 'CD1', 'TYR', 8.98), ('OD2', 'ASP', 'CD2', 'TYR', 7.43), ('OD2', 'ASP', 'CE1', 'TYR', 8.13), ('OD2', 'ASP', 'CE2', 'TYR', 6.28), ('OD2', 'ASP', 'CZ', 'TYR', 6.74), ('OD2', 'ASP', 'OH', 'TYR', 6.14)]]}
ASP_LYS = { 
	'distances':
		[[10.54, 9.08, 8.81, 7.4, 6.91], [9.24, 7.74, 7.35, 5.91, 5.54], [8.59, 7.05, 6.81, 5.44, 5.49], [9.06, 7.64, 6.99, 5.56, 4.92]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 10.54), ('CB', 'ASP', 'CG', 'LYS', 9.08), ('CB', 'ASP', 'CD', 'LYS', 8.81), ('CB', 'ASP', 'CE', 'LYS', 7.4), ('CB', 'ASP', 'NZ', 'LYS', 6.91)], [('CG', 'ASP', 'CB', 'LYS', 9.24), ('CG', 'ASP', 'CG', 'LYS', 7.74), ('CG', 'ASP', 'CD', 'LYS', 7.35), ('CG', 'ASP', 'CE', 'LYS', 5.91), ('CG', 'ASP', 'NZ', 'LYS', 5.54)], [('OD1', 'ASP', 'CB', 'LYS', 8.59), ('OD1', 'ASP', 'CG', 'LYS', 7.05), ('OD1', 'ASP', 'CD', 'LYS', 6.81), ('OD1', 'ASP', 'CE', 'LYS', 5.44), ('OD1', 'ASP', 'NZ', 'LYS', 5.49)], [('OD2', 'ASP', 'CB', 'LYS', 9.06), ('OD2', 'ASP', 'CG', 'LYS', 7.64), ('OD2', 'ASP', 'CD', 'LYS', 6.99), ('OD2', 'ASP', 'CE', 'LYS', 5.56), ('OD2', 'ASP', 'NZ', 'LYS', 4.92)]]}
TYR_LYS = { 
	'distances':
		[[10.8, 10.66, 10.33, 10.24, 8.9], [9.85, 9.57, 9.07, 8.92, 7.59], [9.55, 9.39, 8.71, 8.73, 7.55], [9.54, 9.01, 8.52, 8.12, 6.71], [8.89, 8.59, 7.71, 7.68, 6.61], [8.89, 8.18, 7.49, 6.95, 5.56], [8.53, 7.94, 7.02, 6.69, 5.49], [8.22, 7.45, 6.3, 5.84, 4.88]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'LYS', 10.8), ('CB', 'TYR', 'CG', 'LYS', 10.66), ('CB', 'TYR', 'CD', 'LYS', 10.33), ('CB', 'TYR', 'CE', 'LYS', 10.24), ('CB', 'TYR', 'NZ', 'LYS', 8.9)], [('CG', 'TYR', 'CB', 'LYS', 9.85), ('CG', 'TYR', 'CG', 'LYS', 9.57), ('CG', 'TYR', 'CD', 'LYS', 9.07), ('CG', 'TYR', 'CE', 'LYS', 8.92), ('CG', 'TYR', 'NZ', 'LYS', 7.59)], [('CD1', 'TYR', 'CB', 'LYS', 9.55), ('CD1', 'TYR', 'CG', 'LYS', 9.39), ('CD1', 'TYR', 'CD', 'LYS', 8.71), ('CD1', 'TYR', 'CE', 'LYS', 8.73), ('CD1', 'TYR', 'NZ', 'LYS', 7.55)], [('CD2', 'TYR', 'CB', 'LYS', 9.54), ('CD2', 'TYR', 'CG', 'LYS', 9.01), ('CD2', 'TYR', 'CD', 'LYS', 8.52), ('CD2', 'TYR', 'CE', 'LYS', 8.12), ('CD2', 'TYR', 'NZ', 'LYS', 6.71)], [('CE1', 'TYR', 'CB', 'LYS', 8.89), ('CE1', 'TYR', 'CG', 'LYS', 8.59), ('CE1', 'TYR', 'CD', 'LYS', 7.71), ('CE1', 'TYR', 'CE', 'LYS', 7.68), ('CE1', 'TYR', 'NZ', 'LYS', 6.61)], [('CE2', 'TYR', 'CB', 'LYS', 8.89), ('CE2', 'TYR', 'CG', 'LYS', 8.18), ('CE2', 'TYR', 'CD', 'LYS', 7.49), ('CE2', 'TYR', 'CE', 'LYS', 6.95), ('CE2', 'TYR', 'NZ', 'LYS', 5.56)], [('CZ', 'TYR', 'CB', 'LYS', 8.53), ('CZ', 'TYR', 'CG', 'LYS', 7.94), ('CZ', 'TYR', 'CD', 'LYS', 7.02), ('CZ', 'TYR', 'CE', 'LYS', 6.69), ('CZ', 'TYR', 'NZ', 'LYS', 5.49)], [('OH', 'TYR', 'CB', 'LYS', 8.22), ('OH', 'TYR', 'CG', 'LYS', 7.45), ('OH', 'TYR', 'CD', 'LYS', 6.3), ('OH', 'TYR', 'CE', 'LYS', 5.84), ('OH', 'TYR', 'NZ', 'LYS', 4.88)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_HIS, d, 'Pab_1ah3_1_1_1_21')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'Pab_1ah3_1_1_1_21')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_HIS, d, 'Pab_1ah3_1_1_1_21')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_TYR, d, 'Pab_1ah3_1_1_1_21')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_LYS, d, 'Pab_1ah3_1_1_1_21')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(TYR_LYS, d, 'Pab_1ah3_1_1_1_21')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_HIS' :  match1,
		'ASP_HIS' :  match2,
		'TYR_HIS' :  match3,
		'ASP_TYR' :  match4,
		'ASP_LYS' :  match5,
		'TYR_LYS' :  match6}