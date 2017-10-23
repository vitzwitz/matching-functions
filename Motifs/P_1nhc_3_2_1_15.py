'''
FUNC:P_1nhc_3_2_1_15
PDB:1nhc
EC:3.2.1.15
RESI:asp,asp,asp,his
LOCI:a-186,207,208,229;
'''
import motifFunctions as cmd
ASP_ASPI = { 
	'distances':
		[[7.12, 7.51, 8.37, 7.36], [6.45, 6.45, 7.2, 6.23], [7.31, 7.0, 7.67, 6.49], [5.57, 5.54, 6.14, 5.62]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASPI', 7.12), ('CB', 'ASP', 'CG', 'ASPI', 7.51), ('CB', 'ASP', 'OD1', 'ASPI', 8.37), ('CB', 'ASP', 'OD2', 'ASPI', 7.36)], [('CG', 'ASP', 'CB', 'ASPI', 6.45), ('CG', 'ASP', 'CG', 'ASPI', 6.45), ('CG', 'ASP', 'OD1', 'ASPI', 7.2), ('CG', 'ASP', 'OD2', 'ASPI', 6.23)], [('OD1', 'ASP', 'CB', 'ASPI', 7.31), ('OD1', 'ASP', 'CG', 'ASPI', 7.0), ('OD1', 'ASP', 'OD1', 'ASPI', 7.67), ('OD1', 'ASP', 'OD2', 'ASPI', 6.49)], [('OD2', 'ASP', 'CB', 'ASPI', 5.57), ('OD2', 'ASP', 'CG', 'ASPI', 5.54), ('OD2', 'ASP', 'OD1', 'ASPI', 6.14), ('OD2', 'ASP', 'OD2', 'ASPI', 5.62)]]}
HIS_ASP = { 
	'distances':
		[[7.03, 6.5, 7.22, 5.76], [7.91, 7.4, 7.9, 6.88], [7.99, 7.36, 7.56, 7.05], [9.09, 8.71, 9.22, 8.2], [9.16, 8.62, 8.74, 8.37], [9.76, 9.33, 9.64, 8.96], [7.4, 7.16, 7.89, 6.71], [6.92, 6.61, 7.06, 6.46], [6.59, 5.89, 6.09, 5.75], [7.32, 7.22, 7.51, 7.37], [6.84, 6.2, 6.04, 6.43], [7.28, 7.0, 6.95, 7.34], [10.69, 10.05, 10.3, 9.71], [10.91, 10.15, 10.49, 9.59], [10.65, 9.68, 9.95, 9.02], [11.7, 10.99, 11.47, 10.32], [11.3, 10.31, 10.67, 9.48], [11.92, 11.07, 11.55, 10.25]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.03), ('CB', 'HIS', 'CG', 'ASP', 6.5), ('CB', 'HIS', 'OD1', 'ASP', 7.22), ('CB', 'HIS', 'OD2', 'ASP', 5.76)], [('CG', 'HIS', 'CB', 'ASP', 7.91), ('CG', 'HIS', 'CG', 'ASP', 7.4), ('CG', 'HIS', 'OD1', 'ASP', 7.9), ('CG', 'HIS', 'OD2', 'ASP', 6.88)], [('ND1', 'HIS', 'CB', 'ASP', 7.99), ('ND1', 'HIS', 'CG', 'ASP', 7.36), ('ND1', 'HIS', 'OD1', 'ASP', 7.56), ('ND1', 'HIS', 'OD2', 'ASP', 7.05)], [('CD2', 'HIS', 'CB', 'ASP', 9.09), ('CD2', 'HIS', 'CG', 'ASP', 8.71), ('CD2', 'HIS', 'OD1', 'ASP', 9.22), ('CD2', 'HIS', 'OD2', 'ASP', 8.2)], [('CE1', 'HIS', 'CB', 'ASP', 9.16), ('CE1', 'HIS', 'CG', 'ASP', 8.62), ('CE1', 'HIS', 'OD1', 'ASP', 8.74), ('CE1', 'HIS', 'OD2', 'ASP', 8.37)], [('NE2', 'HIS', 'CB', 'ASP', 9.76), ('NE2', 'HIS', 'CG', 'ASP', 9.33), ('NE2', 'HIS', 'OD1', 'ASP', 9.64), ('NE2', 'HIS', 'OD2', 'ASP', 8.96)], [('CB', 'HIS', 'CB', 'ASP', 7.4), ('CB', 'HIS', 'CG', 'ASP', 7.16), ('CB', 'HIS', 'OD1', 'ASP', 7.89), ('CB', 'HIS', 'OD2', 'ASP', 6.71)], [('CG', 'HIS', 'CB', 'ASP', 6.92), ('CG', 'HIS', 'CG', 'ASP', 6.61), ('CG', 'HIS', 'OD1', 'ASP', 7.06), ('CG', 'HIS', 'OD2', 'ASP', 6.46)], [('ND1', 'HIS', 'CB', 'ASP', 6.59), ('ND1', 'HIS', 'CG', 'ASP', 5.89), ('ND1', 'HIS', 'OD1', 'ASP', 6.09), ('ND1', 'HIS', 'OD2', 'ASP', 5.75)], [('CD2', 'HIS', 'CB', 'ASP', 7.32), ('CD2', 'HIS', 'CG', 'ASP', 7.22), ('CD2', 'HIS', 'OD1', 'ASP', 7.51), ('CD2', 'HIS', 'OD2', 'ASP', 7.37)], [('CE1', 'HIS', 'CB', 'ASP', 6.84), ('CE1', 'HIS', 'CG', 'ASP', 6.2), ('CE1', 'HIS', 'OD1', 'ASP', 6.04), ('CE1', 'HIS', 'OD2', 'ASP', 6.43)], [('NE2', 'HIS', 'CB', 'ASP', 7.28), ('NE2', 'HIS', 'CG', 'ASP', 7.0), ('NE2', 'HIS', 'OD1', 'ASP', 6.95), ('NE2', 'HIS', 'OD2', 'ASP', 7.34)], [('CB', 'HIS', 'CB', 'ASP', 10.69), ('CB', 'HIS', 'CG', 'ASP', 10.05), ('CB', 'HIS', 'OD1', 'ASP', 10.3), ('CB', 'HIS', 'OD2', 'ASP', 9.71)], [('CG', 'HIS', 'CB', 'ASP', 10.91), ('CG', 'HIS', 'CG', 'ASP', 10.15), ('CG', 'HIS', 'OD1', 'ASP', 10.49), ('CG', 'HIS', 'OD2', 'ASP', 9.59)], [('ND1', 'HIS', 'CB', 'ASP', 10.65), ('ND1', 'HIS', 'CG', 'ASP', 9.68), ('ND1', 'HIS', 'OD1', 'ASP', 9.95), ('ND1', 'HIS', 'OD2', 'ASP', 9.02)], [('CD2', 'HIS', 'CB', 'ASP', 11.7), ('CD2', 'HIS', 'CG', 'ASP', 10.99), ('CD2', 'HIS', 'OD1', 'ASP', 11.47), ('CD2', 'HIS', 'OD2', 'ASP', 10.32)], [('CE1', 'HIS', 'CB', 'ASP', 11.3), ('CE1', 'HIS', 'CG', 'ASP', 10.31), ('CE1', 'HIS', 'OD1', 'ASP', 10.67), ('CE1', 'HIS', 'OD2', 'ASP', 9.48)], [('NE2', 'HIS', 'CB', 'ASP', 11.92), ('NE2', 'HIS', 'CG', 'ASP', 11.07), ('NE2', 'HIS', 'OD1', 'ASP', 11.55), ('NE2', 'HIS', 'OD2', 'ASP', 10.25)]]}
ASP_ASP = { 
	'distances':
		[[7.24, 7.07, 8.23, 6.07], [7.73, 7.19, 8.18, 6.02], [7.96, 7.15, 7.96, 5.89], [8.26, 7.74, 8.69, 6.64], [7.09, 6.74, 6.64, 7.18], [8.27, 7.62, 7.32, 7.9], [8.31, 7.42, 6.89, 7.68], [9.39, 8.77, 8.54, 8.95], [7.24, 7.73, 7.96, 8.26], [7.07, 7.19, 7.15, 7.74], [8.23, 8.18, 7.96, 8.69], [6.07, 6.02, 5.89, 6.64], [7.12, 6.45, 7.31, 5.57], [7.51, 6.45, 7.0, 5.54], [8.37, 7.2, 7.67, 6.14], [7.36, 6.23, 6.49, 5.62], [7.09, 8.27, 8.31, 9.39], [6.74, 7.62, 7.42, 8.77], [6.64, 7.32, 6.89, 8.54], [7.18, 7.9, 7.68, 8.95]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 7.24), ('CB', 'ASP', 'CG', 'ASP', 7.07), ('CB', 'ASP', 'OD1', 'ASP', 8.23), ('CB', 'ASP', 'OD2', 'ASP', 6.07)], [('CG', 'ASP', 'CB', 'ASP', 7.73), ('CG', 'ASP', 'CG', 'ASP', 7.19), ('CG', 'ASP', 'OD1', 'ASP', 8.18), ('CG', 'ASP', 'OD2', 'ASP', 6.02)], [('OD1', 'ASP', 'CB', 'ASP', 7.96), ('OD1', 'ASP', 'CG', 'ASP', 7.15), ('OD1', 'ASP', 'OD1', 'ASP', 7.96), ('OD1', 'ASP', 'OD2', 'ASP', 5.89)], [('OD2', 'ASP', 'CB', 'ASP', 8.26), ('OD2', 'ASP', 'CG', 'ASP', 7.74), ('OD2', 'ASP', 'OD1', 'ASP', 8.69), ('OD2', 'ASP', 'OD2', 'ASP', 6.64)], [('CB', 'ASP', 'CB', 'ASP', 7.09), ('CB', 'ASP', 'CG', 'ASP', 6.74), ('CB', 'ASP', 'OD1', 'ASP', 6.64), ('CB', 'ASP', 'OD2', 'ASP', 7.18)], [('CG', 'ASP', 'CB', 'ASP', 8.27), ('CG', 'ASP', 'CG', 'ASP', 7.62), ('CG', 'ASP', 'OD1', 'ASP', 7.32), ('CG', 'ASP', 'OD2', 'ASP', 7.9)], [('OD1', 'ASP', 'CB', 'ASP', 8.31), ('OD1', 'ASP', 'CG', 'ASP', 7.42), ('OD1', 'ASP', 'OD1', 'ASP', 6.89), ('OD1', 'ASP', 'OD2', 'ASP', 7.68)], [('OD2', 'ASP', 'CB', 'ASP', 9.39), ('OD2', 'ASP', 'CG', 'ASP', 8.77), ('OD2', 'ASP', 'OD1', 'ASP', 8.54), ('OD2', 'ASP', 'OD2', 'ASP', 8.95)], [('CB', 'ASP', 'CB', 'ASP', 7.24), ('CB', 'ASP', 'CG', 'ASP', 7.73), ('CB', 'ASP', 'OD1', 'ASP', 7.96), ('CB', 'ASP', 'OD2', 'ASP', 8.26)], [('CG', 'ASP', 'CB', 'ASP', 7.07), ('CG', 'ASP', 'CG', 'ASP', 7.19), ('CG', 'ASP', 'OD1', 'ASP', 7.15), ('CG', 'ASP', 'OD2', 'ASP', 7.74)], [('OD1', 'ASP', 'CB', 'ASP', 8.23), ('OD1', 'ASP', 'CG', 'ASP', 8.18), ('OD1', 'ASP', 'OD1', 'ASP', 7.96), ('OD1', 'ASP', 'OD2', 'ASP', 8.69)], [('OD2', 'ASP', 'CB', 'ASP', 6.07), ('OD2', 'ASP', 'CG', 'ASP', 6.02), ('OD2', 'ASP', 'OD1', 'ASP', 5.89), ('OD2', 'ASP', 'OD2', 'ASP', 6.64)], [('CB', 'ASP', 'CB', 'ASP', 7.12), ('CB', 'ASP', 'CG', 'ASP', 6.45), ('CB', 'ASP', 'OD1', 'ASP', 7.31), ('CB', 'ASP', 'OD2', 'ASP', 5.57)], [('CG', 'ASP', 'CB', 'ASP', 7.51), ('CG', 'ASP', 'CG', 'ASP', 6.45), ('CG', 'ASP', 'OD1', 'ASP', 7.0), ('CG', 'ASP', 'OD2', 'ASP', 5.54)], [('OD1', 'ASP', 'CB', 'ASP', 8.37), ('OD1', 'ASP', 'CG', 'ASP', 7.2), ('OD1', 'ASP', 'OD1', 'ASP', 7.67), ('OD1', 'ASP', 'OD2', 'ASP', 6.14)], [('OD2', 'ASP', 'CB', 'ASP', 7.36), ('OD2', 'ASP', 'CG', 'ASP', 6.23), ('OD2', 'ASP', 'OD1', 'ASP', 6.49), ('OD2', 'ASP', 'OD2', 'ASP', 5.62)], [('CB', 'ASP', 'CB', 'ASP', 7.09), ('CB', 'ASP', 'CG', 'ASP', 8.27), ('CB', 'ASP', 'OD1', 'ASP', 8.31), ('CB', 'ASP', 'OD2', 'ASP', 9.39)], [('CG', 'ASP', 'CB', 'ASP', 6.74), ('CG', 'ASP', 'CG', 'ASP', 7.62), ('CG', 'ASP', 'OD1', 'ASP', 7.42), ('CG', 'ASP', 'OD2', 'ASP', 8.77)], [('OD1', 'ASP', 'CB', 'ASP', 6.64), ('OD1', 'ASP', 'CG', 'ASP', 7.32), ('OD1', 'ASP', 'OD1', 'ASP', 6.89), ('OD1', 'ASP', 'OD2', 'ASP', 8.54)], [('OD2', 'ASP', 'CB', 'ASP', 7.18), ('OD2', 'ASP', 'CG', 'ASP', 7.9), ('OD2', 'ASP', 'OD1', 'ASP', 7.68), ('OD2', 'ASP', 'OD2', 'ASP', 8.95)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ASPI, d, 'P_1nhc_3_2_1_15')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'P_1nhc_3_2_1_15')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_ASP, d, 'P_1nhc_3_2_1_15')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ASPI' :  match1,
		'HIS_ASP' :  match2,
		'ASP_ASP' :  match3}