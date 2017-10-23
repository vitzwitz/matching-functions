'''
FUNC:A_1ecl_5_99_1_2
PDB:1ecl
EC:5.99.1.2
RESI:glu,asp,tyr,his
LOCI:a-9,111,319,365;
'''
import motifFunctions as cmd
ASP_HIS = { 
	'distances':
		[[14.33, 13.56, 14.28, 12.27, 13.58, 12.32], [15.09, 14.45, 15.28, 13.2, 14.67, 13.39], [15.3, 14.72, 15.6, 13.48, 15.04, 13.73], [15.61, 15.02, 15.86, 13.81, 15.29, 14.04]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 14.33), ('CB', 'ASP', 'CG', 'HIS', 13.56), ('CB', 'ASP', 'ND1', 'HIS', 14.28), ('CB', 'ASP', 'CD2', 'HIS', 12.27), ('CB', 'ASP', 'CE1', 'HIS', 13.58), ('CB', 'ASP', 'NE2', 'HIS', 12.32)], [('CG', 'ASP', 'CB', 'HIS', 15.09), ('CG', 'ASP', 'CG', 'HIS', 14.45), ('CG', 'ASP', 'ND1', 'HIS', 15.28), ('CG', 'ASP', 'CD2', 'HIS', 13.2), ('CG', 'ASP', 'CE1', 'HIS', 14.67), ('CG', 'ASP', 'NE2', 'HIS', 13.39)], [('OD1', 'ASP', 'CB', 'HIS', 15.3), ('OD1', 'ASP', 'CG', 'HIS', 14.72), ('OD1', 'ASP', 'ND1', 'HIS', 15.6), ('OD1', 'ASP', 'CD2', 'HIS', 13.48), ('OD1', 'ASP', 'CE1', 'HIS', 15.04), ('OD1', 'ASP', 'NE2', 'HIS', 13.73)], [('OD2', 'ASP', 'CB', 'HIS', 15.61), ('OD2', 'ASP', 'CG', 'HIS', 15.02), ('OD2', 'ASP', 'ND1', 'HIS', 15.86), ('OD2', 'ASP', 'CD2', 'HIS', 13.81), ('OD2', 'ASP', 'CE1', 'HIS', 15.29), ('OD2', 'ASP', 'NE2', 'HIS', 14.04)]]}
TYR_ASP = { 
	'distances':
		[[8.78, 8.69, 8.72, 8.92], [7.55, 7.59, 7.84, 7.77], [6.69, 6.46, 6.76, 6.5], [7.6, 7.97, 8.41, 8.19], [5.77, 5.68, 6.31, 5.59], [6.87, 7.42, 8.09, 7.57], [5.89, 6.29, 7.09, 6.29], [5.67, 6.28, 7.31, 6.15]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASP', 8.78), ('CB', 'TYR', 'CG', 'ASP', 8.69), ('CB', 'TYR', 'OD1', 'ASP', 8.72), ('CB', 'TYR', 'OD2', 'ASP', 8.92)], [('CG', 'TYR', 'CB', 'ASP', 7.55), ('CG', 'TYR', 'CG', 'ASP', 7.59), ('CG', 'TYR', 'OD1', 'ASP', 7.84), ('CG', 'TYR', 'OD2', 'ASP', 7.77)], [('CD1', 'TYR', 'CB', 'ASP', 6.69), ('CD1', 'TYR', 'CG', 'ASP', 6.46), ('CD1', 'TYR', 'OD1', 'ASP', 6.76), ('CD1', 'TYR', 'OD2', 'ASP', 6.5)], [('CD2', 'TYR', 'CB', 'ASP', 7.6), ('CD2', 'TYR', 'CG', 'ASP', 7.97), ('CD2', 'TYR', 'OD1', 'ASP', 8.41), ('CD2', 'TYR', 'OD2', 'ASP', 8.19)], [('CE1', 'TYR', 'CB', 'ASP', 5.77), ('CE1', 'TYR', 'CG', 'ASP', 5.68), ('CE1', 'TYR', 'OD1', 'ASP', 6.31), ('CE1', 'TYR', 'OD2', 'ASP', 5.59)], [('CE2', 'TYR', 'CB', 'ASP', 6.87), ('CE2', 'TYR', 'CG', 'ASP', 7.42), ('CE2', 'TYR', 'OD1', 'ASP', 8.09), ('CE2', 'TYR', 'OD2', 'ASP', 7.57)], [('CZ', 'TYR', 'CB', 'ASP', 5.89), ('CZ', 'TYR', 'CG', 'ASP', 6.29), ('CZ', 'TYR', 'OD1', 'ASP', 7.09), ('CZ', 'TYR', 'OD2', 'ASP', 6.29)], [('OH', 'TYR', 'CB', 'ASP', 5.67), ('OH', 'TYR', 'CG', 'ASP', 6.28), ('OH', 'TYR', 'OD1', 'ASP', 7.31), ('OH', 'TYR', 'OD2', 'ASP', 6.15)]]}
ASP_GLU = { 
	'distances':
		[[8.91, 7.57, 6.51, 6.78, 5.79], [8.47, 7.02, 6.16, 6.29, 5.85], [8.56, 7.16, 6.19, 5.97, 6.15], [8.43, 6.92, 6.42, 6.74, 6.21]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 8.91), ('CB', 'ASP', 'CG', 'GLU', 7.57), ('CB', 'ASP', 'CD', 'GLU', 6.51), ('CB', 'ASP', 'OE1', 'GLU', 6.78), ('CB', 'ASP', 'OE2', 'GLU', 5.79)], [('CG', 'ASP', 'CB', 'GLU', 8.47), ('CG', 'ASP', 'CG', 'GLU', 7.02), ('CG', 'ASP', 'CD', 'GLU', 6.16), ('CG', 'ASP', 'OE1', 'GLU', 6.29), ('CG', 'ASP', 'OE2', 'GLU', 5.85)], [('OD1', 'ASP', 'CB', 'GLU', 8.56), ('OD1', 'ASP', 'CG', 'GLU', 7.16), ('OD1', 'ASP', 'CD', 'GLU', 6.19), ('OD1', 'ASP', 'OE1', 'GLU', 5.97), ('OD1', 'ASP', 'OE2', 'GLU', 6.15)], [('OD2', 'ASP', 'CB', 'GLU', 8.43), ('OD2', 'ASP', 'CG', 'GLU', 6.92), ('OD2', 'ASP', 'CD', 'GLU', 6.42), ('OD2', 'ASP', 'OE1', 'GLU', 6.74), ('OD2', 'ASP', 'OE2', 'GLU', 6.21)]]}
TYR_GLU = { 
	'distances':
		[[15.13, 13.66, 12.79, 12.67, 12.42], [14.05, 12.57, 11.73, 11.74, 11.26], [12.85, 11.36, 10.61, 10.65, 10.24], [14.34, 12.9, 12.01, 12.13, 11.38], [11.95, 10.46, 9.77, 9.98, 9.29], [13.57, 12.15, 11.3, 11.57, 10.57], [12.36, 10.92, 10.17, 10.49, 9.49], [11.77, 10.39, 9.72, 10.23, 8.92]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'GLU', 15.13), ('CB', 'TYR', 'CG', 'GLU', 13.66), ('CB', 'TYR', 'CD', 'GLU', 12.79), ('CB', 'TYR', 'OE1', 'GLU', 12.67), ('CB', 'TYR', 'OE2', 'GLU', 12.42)], [('CG', 'TYR', 'CB', 'GLU', 14.05), ('CG', 'TYR', 'CG', 'GLU', 12.57), ('CG', 'TYR', 'CD', 'GLU', 11.73), ('CG', 'TYR', 'OE1', 'GLU', 11.74), ('CG', 'TYR', 'OE2', 'GLU', 11.26)], [('CD1', 'TYR', 'CB', 'GLU', 12.85), ('CD1', 'TYR', 'CG', 'GLU', 11.36), ('CD1', 'TYR', 'CD', 'GLU', 10.61), ('CD1', 'TYR', 'OE1', 'GLU', 10.65), ('CD1', 'TYR', 'OE2', 'GLU', 10.24)], [('CD2', 'TYR', 'CB', 'GLU', 14.34), ('CD2', 'TYR', 'CG', 'GLU', 12.9), ('CD2', 'TYR', 'CD', 'GLU', 12.01), ('CD2', 'TYR', 'OE1', 'GLU', 12.13), ('CD2', 'TYR', 'OE2', 'GLU', 11.38)], [('CE1', 'TYR', 'CB', 'GLU', 11.95), ('CE1', 'TYR', 'CG', 'GLU', 10.46), ('CE1', 'TYR', 'CD', 'GLU', 9.77), ('CE1', 'TYR', 'OE1', 'GLU', 9.98), ('CE1', 'TYR', 'OE2', 'GLU', 9.29)], [('CE2', 'TYR', 'CB', 'GLU', 13.57), ('CE2', 'TYR', 'CG', 'GLU', 12.15), ('CE2', 'TYR', 'CD', 'GLU', 11.3), ('CE2', 'TYR', 'OE1', 'GLU', 11.57), ('CE2', 'TYR', 'OE2', 'GLU', 10.57)], [('CZ', 'TYR', 'CB', 'GLU', 12.36), ('CZ', 'TYR', 'CG', 'GLU', 10.92), ('CZ', 'TYR', 'CD', 'GLU', 10.17), ('CZ', 'TYR', 'OE1', 'GLU', 10.49), ('CZ', 'TYR', 'OE2', 'GLU', 9.49)], [('OH', 'TYR', 'CB', 'GLU', 11.77), ('OH', 'TYR', 'CG', 'GLU', 10.39), ('OH', 'TYR', 'CD', 'GLU', 9.72), ('OH', 'TYR', 'OE1', 'GLU', 10.23), ('OH', 'TYR', 'OE2', 'GLU', 8.92)]]}
TYR_HIS = { 
	'distances':
		[[10.05, 10.09, 11.33, 9.31, 11.39, 10.24], [10.46, 10.26, 11.38, 9.33, 11.25, 10.06], [11.84, 11.57, 12.64, 10.58, 12.43, 11.21], [9.68, 9.32, 10.34, 8.35, 10.14, 8.96], [12.42, 11.99, 12.94, 10.92, 12.58, 11.37], [10.4, 9.85, 10.71, 8.79, 10.33, 9.17], [11.76, 11.19, 12.03, 10.1, 11.6, 10.42], [12.57, 11.87, 12.57, 10.75, 12.01, 10.88]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'HIS', 10.05), ('CB', 'TYR', 'CG', 'HIS', 10.09), ('CB', 'TYR', 'ND1', 'HIS', 11.33), ('CB', 'TYR', 'CD2', 'HIS', 9.31), ('CB', 'TYR', 'CE1', 'HIS', 11.39), ('CB', 'TYR', 'NE2', 'HIS', 10.24)], [('CG', 'TYR', 'CB', 'HIS', 10.46), ('CG', 'TYR', 'CG', 'HIS', 10.26), ('CG', 'TYR', 'ND1', 'HIS', 11.38), ('CG', 'TYR', 'CD2', 'HIS', 9.33), ('CG', 'TYR', 'CE1', 'HIS', 11.25), ('CG', 'TYR', 'NE2', 'HIS', 10.06)], [('CD1', 'TYR', 'CB', 'HIS', 11.84), ('CD1', 'TYR', 'CG', 'HIS', 11.57), ('CD1', 'TYR', 'ND1', 'HIS', 12.64), ('CD1', 'TYR', 'CD2', 'HIS', 10.58), ('CD1', 'TYR', 'CE1', 'HIS', 12.43), ('CD1', 'TYR', 'NE2', 'HIS', 11.21)], [('CD2', 'TYR', 'CB', 'HIS', 9.68), ('CD2', 'TYR', 'CG', 'HIS', 9.32), ('CD2', 'TYR', 'ND1', 'HIS', 10.34), ('CD2', 'TYR', 'CD2', 'HIS', 8.35), ('CD2', 'TYR', 'CE1', 'HIS', 10.14), ('CD2', 'TYR', 'NE2', 'HIS', 8.96)], [('CE1', 'TYR', 'CB', 'HIS', 12.42), ('CE1', 'TYR', 'CG', 'HIS', 11.99), ('CE1', 'TYR', 'ND1', 'HIS', 12.94), ('CE1', 'TYR', 'CD2', 'HIS', 10.92), ('CE1', 'TYR', 'CE1', 'HIS', 12.58), ('CE1', 'TYR', 'NE2', 'HIS', 11.37)], [('CE2', 'TYR', 'CB', 'HIS', 10.4), ('CE2', 'TYR', 'CG', 'HIS', 9.85), ('CE2', 'TYR', 'ND1', 'HIS', 10.71), ('CE2', 'TYR', 'CD2', 'HIS', 8.79), ('CE2', 'TYR', 'CE1', 'HIS', 10.33), ('CE2', 'TYR', 'NE2', 'HIS', 9.17)], [('CZ', 'TYR', 'CB', 'HIS', 11.76), ('CZ', 'TYR', 'CG', 'HIS', 11.19), ('CZ', 'TYR', 'ND1', 'HIS', 12.03), ('CZ', 'TYR', 'CD2', 'HIS', 10.1), ('CZ', 'TYR', 'CE1', 'HIS', 11.6), ('CZ', 'TYR', 'NE2', 'HIS', 10.42)], [('OH', 'TYR', 'CB', 'HIS', 12.57), ('OH', 'TYR', 'CG', 'HIS', 11.87), ('OH', 'TYR', 'ND1', 'HIS', 12.57), ('OH', 'TYR', 'CD2', 'HIS', 10.75), ('OH', 'TYR', 'CE1', 'HIS', 12.01), ('OH', 'TYR', 'NE2', 'HIS', 10.88)]]}
GLU_HIS = { 
	'distances':
		[[21.2, 20.37, 21.0, 19.05, 20.16, 18.95], [19.89, 19.1, 19.78, 17.8, 19.0, 17.76], [18.72, 17.91, 18.57, 16.59, 17.77, 16.53], [18.71, 17.94, 18.66, 16.63, 17.89, 16.63], [17.93, 17.05, 17.65, 15.72, 16.8, 15.59]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 21.2), ('CB', 'GLU', 'CG', 'HIS', 20.37), ('CB', 'GLU', 'ND1', 'HIS', 21.0), ('CB', 'GLU', 'CD2', 'HIS', 19.05), ('CB', 'GLU', 'CE1', 'HIS', 20.16), ('CB', 'GLU', 'NE2', 'HIS', 18.95)], [('CG', 'GLU', 'CB', 'HIS', 19.89), ('CG', 'GLU', 'CG', 'HIS', 19.1), ('CG', 'GLU', 'ND1', 'HIS', 19.78), ('CG', 'GLU', 'CD2', 'HIS', 17.8), ('CG', 'GLU', 'CE1', 'HIS', 19.0), ('CG', 'GLU', 'NE2', 'HIS', 17.76)], [('CD', 'GLU', 'CB', 'HIS', 18.72), ('CD', 'GLU', 'CG', 'HIS', 17.91), ('CD', 'GLU', 'ND1', 'HIS', 18.57), ('CD', 'GLU', 'CD2', 'HIS', 16.59), ('CD', 'GLU', 'CE1', 'HIS', 17.77), ('CD', 'GLU', 'NE2', 'HIS', 16.53)], [('OE1', 'GLU', 'CB', 'HIS', 18.71), ('OE1', 'GLU', 'CG', 'HIS', 17.94), ('OE1', 'GLU', 'ND1', 'HIS', 18.66), ('OE1', 'GLU', 'CD2', 'HIS', 16.63), ('OE1', 'GLU', 'CE1', 'HIS', 17.89), ('OE1', 'GLU', 'NE2', 'HIS', 16.63)], [('OE2', 'GLU', 'CB', 'HIS', 17.93), ('OE2', 'GLU', 'CG', 'HIS', 17.05), ('OE2', 'GLU', 'ND1', 'HIS', 17.65), ('OE2', 'GLU', 'CD2', 'HIS', 15.72), ('OE2', 'GLU', 'CE1', 'HIS', 16.8), ('OE2', 'GLU', 'NE2', 'HIS', 15.59)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HIS, d, 'A_1ecl_5_99_1_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TYR_ASP, d, 'A_1ecl_5_99_1_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_GLU, d, 'A_1ecl_5_99_1_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(TYR_GLU, d, 'A_1ecl_5_99_1_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(TYR_HIS, d, 'A_1ecl_5_99_1_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLU_HIS, d, 'A_1ecl_5_99_1_2')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HIS' :  match1,
		'TYR_ASP' :  match2,
		'ASP_GLU' :  match3,
		'TYR_GLU' :  match4,
		'TYR_HIS' :  match5,
		'GLU_HIS' :  match6}