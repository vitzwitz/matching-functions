'''
FUNC:P_1cy8_5_99_1_2
PDB:1cy8
EC:5.99.1.2
RESI:glu,asp,tyr,his
LOCI:a-9,111,319,365;
'''
import motifFunctions as cmd
ASP_HIS = { 
	'distances':
		[[14.16, 13.36, 13.41, 12.7, 12.81, 12.35], [15.0, 14.33, 14.46, 13.73, 13.97, 13.51], [15.16, 14.56, 14.82, 13.91, 14.37, 13.8], [15.64, 15.0, 15.06, 14.5, 14.61, 14.25]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 14.16), ('CB', 'ASP', 'CG', 'HIS', 13.36), ('CB', 'ASP', 'ND1', 'HIS', 13.41), ('CB', 'ASP', 'CD2', 'HIS', 12.7), ('CB', 'ASP', 'CE1', 'HIS', 12.81), ('CB', 'ASP', 'NE2', 'HIS', 12.35)], [('CG', 'ASP', 'CB', 'HIS', 15.0), ('CG', 'ASP', 'CG', 'HIS', 14.33), ('CG', 'ASP', 'ND1', 'HIS', 14.46), ('CG', 'ASP', 'CD2', 'HIS', 13.73), ('CG', 'ASP', 'CE1', 'HIS', 13.97), ('CG', 'ASP', 'NE2', 'HIS', 13.51)], [('OD1', 'ASP', 'CB', 'HIS', 15.16), ('OD1', 'ASP', 'CG', 'HIS', 14.56), ('OD1', 'ASP', 'ND1', 'HIS', 14.82), ('OD1', 'ASP', 'CD2', 'HIS', 13.91), ('OD1', 'ASP', 'CE1', 'HIS', 14.37), ('OD1', 'ASP', 'NE2', 'HIS', 13.8)], [('OD2', 'ASP', 'CB', 'HIS', 15.64), ('OD2', 'ASP', 'CG', 'HIS', 15.0), ('OD2', 'ASP', 'ND1', 'HIS', 15.06), ('OD2', 'ASP', 'CD2', 'HIS', 14.5), ('OD2', 'ASP', 'CE1', 'HIS', 14.61), ('OD2', 'ASP', 'NE2', 'HIS', 14.25)]]}
GLU_TYR = { 
	'distances':
		[[15.15, 14.08, 12.86, 14.41, 11.93, 13.61, 12.36, 11.69], [13.65, 12.59, 11.35, 12.96, 10.45, 12.21, 10.93, 10.33], [12.82, 11.78, 10.63, 12.11, 9.78, 11.4, 10.22, 9.7], [12.82, 11.91, 10.8, 12.35, 10.12, 11.78, 10.66, 10.31], [12.35, 11.21, 10.15, 11.4, 9.19, 10.58, 9.44, 8.82]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'TYR', 15.15), ('CB', 'GLU', 'CG', 'TYR', 14.08), ('CB', 'GLU', 'CD1', 'TYR', 12.86), ('CB', 'GLU', 'CD2', 'TYR', 14.41), ('CB', 'GLU', 'CE1', 'TYR', 11.93), ('CB', 'GLU', 'CE2', 'TYR', 13.61), ('CB', 'GLU', 'CZ', 'TYR', 12.36), ('CB', 'GLU', 'OH', 'TYR', 11.69)], [('CG', 'GLU', 'CB', 'TYR', 13.65), ('CG', 'GLU', 'CG', 'TYR', 12.59), ('CG', 'GLU', 'CD1', 'TYR', 11.35), ('CG', 'GLU', 'CD2', 'TYR', 12.96), ('CG', 'GLU', 'CE1', 'TYR', 10.45), ('CG', 'GLU', 'CE2', 'TYR', 12.21), ('CG', 'GLU', 'CZ', 'TYR', 10.93), ('CG', 'GLU', 'OH', 'TYR', 10.33)], [('CD', 'GLU', 'CB', 'TYR', 12.82), ('CD', 'GLU', 'CG', 'TYR', 11.78), ('CD', 'GLU', 'CD1', 'TYR', 10.63), ('CD', 'GLU', 'CD2', 'TYR', 12.11), ('CD', 'GLU', 'CE1', 'TYR', 9.78), ('CD', 'GLU', 'CE2', 'TYR', 11.4), ('CD', 'GLU', 'CZ', 'TYR', 10.22), ('CD', 'GLU', 'OH', 'TYR', 9.7)], [('OE1', 'GLU', 'CB', 'TYR', 12.82), ('OE1', 'GLU', 'CG', 'TYR', 11.91), ('OE1', 'GLU', 'CD1', 'TYR', 10.8), ('OE1', 'GLU', 'CD2', 'TYR', 12.35), ('OE1', 'GLU', 'CE1', 'TYR', 10.12), ('OE1', 'GLU', 'CE2', 'TYR', 11.78), ('OE1', 'GLU', 'CZ', 'TYR', 10.66), ('OE1', 'GLU', 'OH', 'TYR', 10.31)], [('OE2', 'GLU', 'CB', 'TYR', 12.35), ('OE2', 'GLU', 'CG', 'TYR', 11.21), ('OE2', 'GLU', 'CD1', 'TYR', 10.15), ('OE2', 'GLU', 'CD2', 'TYR', 11.4), ('OE2', 'GLU', 'CE1', 'TYR', 9.19), ('OE2', 'GLU', 'CE2', 'TYR', 10.58), ('OE2', 'GLU', 'CZ', 'TYR', 9.44), ('OE2', 'GLU', 'OH', 'TYR', 8.82)]]}
GLU_ASP = { 
	'distances':
		[[9.05, 8.46, 8.61, 8.22], [7.71, 6.99, 7.17, 6.72], [6.66, 6.14, 6.23, 6.24], [7.0, 6.41, 6.15, 6.75], [5.86, 5.7, 6.07, 5.86]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 9.05), ('CB', 'GLU', 'CG', 'ASP', 8.46), ('CB', 'GLU', 'OD1', 'ASP', 8.61), ('CB', 'GLU', 'OD2', 'ASP', 8.22)], [('CG', 'GLU', 'CB', 'ASP', 7.71), ('CG', 'GLU', 'CG', 'ASP', 6.99), ('CG', 'GLU', 'OD1', 'ASP', 7.17), ('CG', 'GLU', 'OD2', 'ASP', 6.72)], [('CD', 'GLU', 'CB', 'ASP', 6.66), ('CD', 'GLU', 'CG', 'ASP', 6.14), ('CD', 'GLU', 'OD1', 'ASP', 6.23), ('CD', 'GLU', 'OD2', 'ASP', 6.24)], [('OE1', 'GLU', 'CB', 'ASP', 7.0), ('OE1', 'GLU', 'CG', 'ASP', 6.41), ('OE1', 'GLU', 'OD1', 'ASP', 6.15), ('OE1', 'GLU', 'OD2', 'ASP', 6.75)], [('OE2', 'GLU', 'CB', 'ASP', 5.86), ('OE2', 'GLU', 'CG', 'ASP', 5.7), ('OE2', 'GLU', 'OD1', 'ASP', 6.07), ('OE2', 'GLU', 'OD2', 'ASP', 5.86)]]}
ASP_TYR = { 
	'distances':
		[[8.69, 7.49, 6.61, 7.58, 5.7, 6.85, 5.85, 5.6], [8.73, 7.64, 6.5, 8.06, 5.7, 7.5, 6.33, 6.23], [8.7, 7.84, 6.72, 8.46, 6.27, 8.14, 7.09, 7.25], [9.12, 7.97, 6.7, 8.38, 5.75, 7.72, 6.4, 6.12]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'TYR', 8.69), ('CB', 'ASP', 'CG', 'TYR', 7.49), ('CB', 'ASP', 'CD1', 'TYR', 6.61), ('CB', 'ASP', 'CD2', 'TYR', 7.58), ('CB', 'ASP', 'CE1', 'TYR', 5.7), ('CB', 'ASP', 'CE2', 'TYR', 6.85), ('CB', 'ASP', 'CZ', 'TYR', 5.85), ('CB', 'ASP', 'OH', 'TYR', 5.6)], [('CG', 'ASP', 'CB', 'TYR', 8.73), ('CG', 'ASP', 'CG', 'TYR', 7.64), ('CG', 'ASP', 'CD1', 'TYR', 6.5), ('CG', 'ASP', 'CD2', 'TYR', 8.06), ('CG', 'ASP', 'CE1', 'TYR', 5.7), ('CG', 'ASP', 'CE2', 'TYR', 7.5), ('CG', 'ASP', 'CZ', 'TYR', 6.33), ('CG', 'ASP', 'OH', 'TYR', 6.23)], [('OD1', 'ASP', 'CB', 'TYR', 8.7), ('OD1', 'ASP', 'CG', 'TYR', 7.84), ('OD1', 'ASP', 'CD1', 'TYR', 6.72), ('OD1', 'ASP', 'CD2', 'TYR', 8.46), ('OD1', 'ASP', 'CE1', 'TYR', 6.27), ('OD1', 'ASP', 'CE2', 'TYR', 8.14), ('OD1', 'ASP', 'CZ', 'TYR', 7.09), ('OD1', 'ASP', 'OH', 'TYR', 7.25)], [('OD2', 'ASP', 'CB', 'TYR', 9.12), ('OD2', 'ASP', 'CG', 'TYR', 7.97), ('OD2', 'ASP', 'CD1', 'TYR', 6.7), ('OD2', 'ASP', 'CD2', 'TYR', 8.38), ('OD2', 'ASP', 'CE1', 'TYR', 5.75), ('OD2', 'ASP', 'CE2', 'TYR', 7.72), ('OD2', 'ASP', 'CZ', 'TYR', 6.4), ('OD2', 'ASP', 'OH', 'TYR', 6.12)]]}
TYR_HIS = { 
	'distances':
		[[9.83, 9.85, 10.35, 9.77, 10.57, 10.23], [10.28, 10.05, 10.35, 9.91, 10.39, 10.13], [11.64, 11.35, 11.6, 11.13, 11.54, 11.26], [9.55, 9.17, 9.29, 9.06, 9.26, 9.12], [12.3, 11.84, 11.92, 11.58, 11.72, 11.5], [10.36, 9.78, 9.69, 9.61, 9.48, 9.42], [11.71, 11.13, 11.05, 10.88, 10.77, 10.66], [12.62, 11.91, 11.68, 11.63, 11.27, 11.23]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'HIS', 9.83), ('CB', 'TYR', 'CG', 'HIS', 9.85), ('CB', 'TYR', 'ND1', 'HIS', 10.35), ('CB', 'TYR', 'CD2', 'HIS', 9.77), ('CB', 'TYR', 'CE1', 'HIS', 10.57), ('CB', 'TYR', 'NE2', 'HIS', 10.23)], [('CG', 'TYR', 'CB', 'HIS', 10.28), ('CG', 'TYR', 'CG', 'HIS', 10.05), ('CG', 'TYR', 'ND1', 'HIS', 10.35), ('CG', 'TYR', 'CD2', 'HIS', 9.91), ('CG', 'TYR', 'CE1', 'HIS', 10.39), ('CG', 'TYR', 'NE2', 'HIS', 10.13)], [('CD1', 'TYR', 'CB', 'HIS', 11.64), ('CD1', 'TYR', 'CG', 'HIS', 11.35), ('CD1', 'TYR', 'ND1', 'HIS', 11.6), ('CD1', 'TYR', 'CD2', 'HIS', 11.13), ('CD1', 'TYR', 'CE1', 'HIS', 11.54), ('CD1', 'TYR', 'NE2', 'HIS', 11.26)], [('CD2', 'TYR', 'CB', 'HIS', 9.55), ('CD2', 'TYR', 'CG', 'HIS', 9.17), ('CD2', 'TYR', 'ND1', 'HIS', 9.29), ('CD2', 'TYR', 'CD2', 'HIS', 9.06), ('CD2', 'TYR', 'CE1', 'HIS', 9.26), ('CD2', 'TYR', 'NE2', 'HIS', 9.12)], [('CE1', 'TYR', 'CB', 'HIS', 12.3), ('CE1', 'TYR', 'CG', 'HIS', 11.84), ('CE1', 'TYR', 'ND1', 'HIS', 11.92), ('CE1', 'TYR', 'CD2', 'HIS', 11.58), ('CE1', 'TYR', 'CE1', 'HIS', 11.72), ('CE1', 'TYR', 'NE2', 'HIS', 11.5)], [('CE2', 'TYR', 'CB', 'HIS', 10.36), ('CE2', 'TYR', 'CG', 'HIS', 9.78), ('CE2', 'TYR', 'ND1', 'HIS', 9.69), ('CE2', 'TYR', 'CD2', 'HIS', 9.61), ('CE2', 'TYR', 'CE1', 'HIS', 9.48), ('CE2', 'TYR', 'NE2', 'HIS', 9.42)], [('CZ', 'TYR', 'CB', 'HIS', 11.71), ('CZ', 'TYR', 'CG', 'HIS', 11.13), ('CZ', 'TYR', 'ND1', 'HIS', 11.05), ('CZ', 'TYR', 'CD2', 'HIS', 10.88), ('CZ', 'TYR', 'CE1', 'HIS', 10.77), ('CZ', 'TYR', 'NE2', 'HIS', 10.66)], [('OH', 'TYR', 'CB', 'HIS', 12.62), ('OH', 'TYR', 'CG', 'HIS', 11.91), ('OH', 'TYR', 'ND1', 'HIS', 11.68), ('OH', 'TYR', 'CD2', 'HIS', 11.63), ('OH', 'TYR', 'CE1', 'HIS', 11.27), ('OH', 'TYR', 'NE2', 'HIS', 11.23)]]}
GLU_HIS = { 
	'distances':
		[[21.19, 20.35, 20.35, 19.59, 19.64, 19.15], [19.85, 19.07, 19.1, 18.36, 18.44, 17.97], [18.72, 17.9, 17.97, 17.12, 17.28, 16.74], [18.74, 17.95, 18.13, 17.13, 17.45, 16.81], [17.9, 17.01, 17.02, 16.24, 16.28, 15.78]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 21.19), ('CB', 'GLU', 'CG', 'HIS', 20.35), ('CB', 'GLU', 'ND1', 'HIS', 20.35), ('CB', 'GLU', 'CD2', 'HIS', 19.59), ('CB', 'GLU', 'CE1', 'HIS', 19.64), ('CB', 'GLU', 'NE2', 'HIS', 19.15)], [('CG', 'GLU', 'CB', 'HIS', 19.85), ('CG', 'GLU', 'CG', 'HIS', 19.07), ('CG', 'GLU', 'ND1', 'HIS', 19.1), ('CG', 'GLU', 'CD2', 'HIS', 18.36), ('CG', 'GLU', 'CE1', 'HIS', 18.44), ('CG', 'GLU', 'NE2', 'HIS', 17.97)], [('CD', 'GLU', 'CB', 'HIS', 18.72), ('CD', 'GLU', 'CG', 'HIS', 17.9), ('CD', 'GLU', 'ND1', 'HIS', 17.97), ('CD', 'GLU', 'CD2', 'HIS', 17.12), ('CD', 'GLU', 'CE1', 'HIS', 17.28), ('CD', 'GLU', 'NE2', 'HIS', 16.74)], [('OE1', 'GLU', 'CB', 'HIS', 18.74), ('OE1', 'GLU', 'CG', 'HIS', 17.95), ('OE1', 'GLU', 'ND1', 'HIS', 18.13), ('OE1', 'GLU', 'CD2', 'HIS', 17.13), ('OE1', 'GLU', 'CE1', 'HIS', 17.45), ('OE1', 'GLU', 'NE2', 'HIS', 16.81)], [('OE2', 'GLU', 'CB', 'HIS', 17.9), ('OE2', 'GLU', 'CG', 'HIS', 17.01), ('OE2', 'GLU', 'ND1', 'HIS', 17.02), ('OE2', 'GLU', 'CD2', 'HIS', 16.24), ('OE2', 'GLU', 'CE1', 'HIS', 16.28), ('OE2', 'GLU', 'NE2', 'HIS', 15.78)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HIS, d, 'P_1cy8_5_99_1_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_TYR, d, 'P_1cy8_5_99_1_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_ASP, d, 'P_1cy8_5_99_1_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_TYR, d, 'P_1cy8_5_99_1_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(TYR_HIS, d, 'P_1cy8_5_99_1_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLU_HIS, d, 'P_1cy8_5_99_1_2')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HIS' :  match1,
		'GLU_TYR' :  match2,
		'GLU_ASP' :  match3,
		'ASP_TYR' :  match4,
		'TYR_HIS' :  match5,
		'GLU_HIS' :  match6}