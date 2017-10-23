'''
FUNC:A_1ako_3_1_11_2
PDB:1ako
EC:3.1.11.2
RESI:asn,asp,asn,asp,his
LOCI:a-7,151,153,229,259;
'''
import motifFunctions as cmd
ASP_ASP = { 
	'distances':
		[[7.38, 7.64, 7.42, 8.46], [6.51, 6.55, 6.45, 7.19], [5.41, 5.66, 5.84, 6.31], [7.19, 6.88, 6.68, 7.33], [7.38, 6.51, 5.41, 7.19], [7.64, 6.55, 5.66, 6.88], [7.42, 6.45, 5.84, 6.68], [8.46, 7.19, 6.31, 7.33]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 7.38), ('CB', 'ASP', 'CG', 'ASP', 7.64), ('CB', 'ASP', 'OD1', 'ASP', 7.42), ('CB', 'ASP', 'OD2', 'ASP', 8.46)], [('CG', 'ASP', 'CB', 'ASP', 6.51), ('CG', 'ASP', 'CG', 'ASP', 6.55), ('CG', 'ASP', 'OD1', 'ASP', 6.45), ('CG', 'ASP', 'OD2', 'ASP', 7.19)], [('OD1', 'ASP', 'CB', 'ASP', 5.41), ('OD1', 'ASP', 'CG', 'ASP', 5.66), ('OD1', 'ASP', 'OD1', 'ASP', 5.84), ('OD1', 'ASP', 'OD2', 'ASP', 6.31)], [('OD2', 'ASP', 'CB', 'ASP', 7.19), ('OD2', 'ASP', 'CG', 'ASP', 6.88), ('OD2', 'ASP', 'OD1', 'ASP', 6.68), ('OD2', 'ASP', 'OD2', 'ASP', 7.33)], [('CB', 'ASP', 'CB', 'ASP', 7.38), ('CB', 'ASP', 'CG', 'ASP', 6.51), ('CB', 'ASP', 'OD1', 'ASP', 5.41), ('CB', 'ASP', 'OD2', 'ASP', 7.19)], [('CG', 'ASP', 'CB', 'ASP', 7.64), ('CG', 'ASP', 'CG', 'ASP', 6.55), ('CG', 'ASP', 'OD1', 'ASP', 5.66), ('CG', 'ASP', 'OD2', 'ASP', 6.88)], [('OD1', 'ASP', 'CB', 'ASP', 7.42), ('OD1', 'ASP', 'CG', 'ASP', 6.45), ('OD1', 'ASP', 'OD1', 'ASP', 5.84), ('OD1', 'ASP', 'OD2', 'ASP', 6.68)], [('OD2', 'ASP', 'CB', 'ASP', 8.46), ('OD2', 'ASP', 'CG', 'ASP', 7.19), ('OD2', 'ASP', 'OD1', 'ASP', 6.31), ('OD2', 'ASP', 'OD2', 'ASP', 7.33)]]}
HIS_ASP = { 
	'distances':
		[[7.95, 6.76, 6.81, 6.15], [7.91, 6.5, 6.4, 5.85], [6.92, 5.45, 5.39, 4.78], [9.02, 7.56, 7.28, 6.94], [7.65, 6.16, 5.9, 5.57], [8.86, 7.36, 7.0, 6.78], [8.98, 8.62, 9.04, 8.28], [8.04, 7.46, 7.87, 6.99], [7.1, 6.42, 6.66, 6.17], [8.21, 7.46, 7.96, 6.71], [6.68, 5.69, 5.92, 5.23], [7.41, 6.43, 6.84, 5.62]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.95), ('CB', 'HIS', 'CG', 'ASP', 6.76), ('CB', 'HIS', 'OD1', 'ASP', 6.81), ('CB', 'HIS', 'OD2', 'ASP', 6.15)], [('CG', 'HIS', 'CB', 'ASP', 7.91), ('CG', 'HIS', 'CG', 'ASP', 6.5), ('CG', 'HIS', 'OD1', 'ASP', 6.4), ('CG', 'HIS', 'OD2', 'ASP', 5.85)], [('ND1', 'HIS', 'CB', 'ASP', 6.92), ('ND1', 'HIS', 'CG', 'ASP', 5.45), ('ND1', 'HIS', 'OD1', 'ASP', 5.39), ('ND1', 'HIS', 'OD2', 'ASP', 4.78)], [('CD2', 'HIS', 'CB', 'ASP', 9.02), ('CD2', 'HIS', 'CG', 'ASP', 7.56), ('CD2', 'HIS', 'OD1', 'ASP', 7.28), ('CD2', 'HIS', 'OD2', 'ASP', 6.94)], [('CE1', 'HIS', 'CB', 'ASP', 7.65), ('CE1', 'HIS', 'CG', 'ASP', 6.16), ('CE1', 'HIS', 'OD1', 'ASP', 5.9), ('CE1', 'HIS', 'OD2', 'ASP', 5.57)], [('NE2', 'HIS', 'CB', 'ASP', 8.86), ('NE2', 'HIS', 'CG', 'ASP', 7.36), ('NE2', 'HIS', 'OD1', 'ASP', 7.0), ('NE2', 'HIS', 'OD2', 'ASP', 6.78)], [('CB', 'HIS', 'CB', 'ASP', 8.98), ('CB', 'HIS', 'CG', 'ASP', 8.62), ('CB', 'HIS', 'OD1', 'ASP', 9.04), ('CB', 'HIS', 'OD2', 'ASP', 8.28)], [('CG', 'HIS', 'CB', 'ASP', 8.04), ('CG', 'HIS', 'CG', 'ASP', 7.46), ('CG', 'HIS', 'OD1', 'ASP', 7.87), ('CG', 'HIS', 'OD2', 'ASP', 6.99)], [('ND1', 'HIS', 'CB', 'ASP', 7.1), ('ND1', 'HIS', 'CG', 'ASP', 6.42), ('ND1', 'HIS', 'OD1', 'ASP', 6.66), ('ND1', 'HIS', 'OD2', 'ASP', 6.17)], [('CD2', 'HIS', 'CB', 'ASP', 8.21), ('CD2', 'HIS', 'CG', 'ASP', 7.46), ('CD2', 'HIS', 'OD1', 'ASP', 7.96), ('CD2', 'HIS', 'OD2', 'ASP', 6.71)], [('CE1', 'HIS', 'CB', 'ASP', 6.68), ('CE1', 'HIS', 'CG', 'ASP', 5.69), ('CE1', 'HIS', 'OD1', 'ASP', 5.92), ('CE1', 'HIS', 'OD2', 'ASP', 5.23)], [('NE2', 'HIS', 'CB', 'ASP', 7.41), ('NE2', 'HIS', 'CG', 'ASP', 6.43), ('NE2', 'HIS', 'OD1', 'ASP', 6.84), ('NE2', 'HIS', 'OD2', 'ASP', 5.62)]]}
ASN_ASPI = { 
	'distances':
		[[7.86, 6.91, 6.14, 7.29], [7.26, 6.1, 5.54, 6.17], [7.6, 6.23, 5.61, 6.14], [6.77, 5.78, 5.63, 5.7]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ASPI', 7.86), ('CB', 'ASN', 'CG', 'ASPI', 6.91), ('CB', 'ASN', 'OD1', 'ASPI', 6.14), ('CB', 'ASN', 'OD2', 'ASPI', 7.29)], [('CG', 'ASN', 'CB', 'ASPI', 7.26), ('CG', 'ASN', 'CG', 'ASPI', 6.1), ('CG', 'ASN', 'OD1', 'ASPI', 5.54), ('CG', 'ASN', 'OD2', 'ASPI', 6.17)], [('OD1', 'ASN', 'CB', 'ASPI', 7.6), ('OD1', 'ASN', 'CG', 'ASPI', 6.23), ('OD1', 'ASN', 'OD1', 'ASPI', 5.61), ('OD1', 'ASN', 'OD2', 'ASPI', 6.14)], [('ND2', 'ASN', 'CB', 'ASPI', 6.77), ('ND2', 'ASN', 'CG', 'ASPI', 5.78), ('ND2', 'ASN', 'OD1', 'ASPI', 5.63), ('ND2', 'ASN', 'OD2', 'ASPI', 5.7)]]}
ASN_ASP = { 
	'distances':
		[[8.37, 7.15, 6.24, 7.39], [9.58, 8.25, 7.33, 8.36], [10.66, 9.33, 8.47, 9.35], [9.61, 8.25, 7.26, 8.37], [6.57, 6.79, 7.8, 6.34], [6.88, 6.85, 7.94, 6.05], [8.09, 8.02, 9.1, 7.13], [6.11, 5.89, 7.01, 4.95], [11.05, 10.33, 9.91, 10.4], [10.81, 9.87, 9.36, 9.85], [10.64, 9.61, 9.23, 9.4], [11.04, 10.05, 9.35, 10.15]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ASP', 8.37), ('CB', 'ASN', 'CG', 'ASP', 7.15), ('CB', 'ASN', 'OD1', 'ASP', 6.24), ('CB', 'ASN', 'OD2', 'ASP', 7.39)], [('CG', 'ASN', 'CB', 'ASP', 9.58), ('CG', 'ASN', 'CG', 'ASP', 8.25), ('CG', 'ASN', 'OD1', 'ASP', 7.33), ('CG', 'ASN', 'OD2', 'ASP', 8.36)], [('OD1', 'ASN', 'CB', 'ASP', 10.66), ('OD1', 'ASN', 'CG', 'ASP', 9.33), ('OD1', 'ASN', 'OD1', 'ASP', 8.47), ('OD1', 'ASN', 'OD2', 'ASP', 9.35)], [('ND2', 'ASN', 'CB', 'ASP', 9.61), ('ND2', 'ASN', 'CG', 'ASP', 8.25), ('ND2', 'ASN', 'OD1', 'ASP', 7.26), ('ND2', 'ASN', 'OD2', 'ASP', 8.37)], [('CB', 'ASN', 'CB', 'ASP', 6.57), ('CB', 'ASN', 'CG', 'ASP', 6.79), ('CB', 'ASN', 'OD1', 'ASP', 7.8), ('CB', 'ASN', 'OD2', 'ASP', 6.34)], [('CG', 'ASN', 'CB', 'ASP', 6.88), ('CG', 'ASN', 'CG', 'ASP', 6.85), ('CG', 'ASN', 'OD1', 'ASP', 7.94), ('CG', 'ASN', 'OD2', 'ASP', 6.05)], [('OD1', 'ASN', 'CB', 'ASP', 8.09), ('OD1', 'ASN', 'CG', 'ASP', 8.02), ('OD1', 'ASN', 'OD1', 'ASP', 9.1), ('OD1', 'ASN', 'OD2', 'ASP', 7.13)], [('ND2', 'ASN', 'CB', 'ASP', 6.11), ('ND2', 'ASN', 'CG', 'ASP', 5.89), ('ND2', 'ASN', 'OD1', 'ASP', 7.01), ('ND2', 'ASN', 'OD2', 'ASP', 4.95)], [('CB', 'ASN', 'CB', 'ASP', 11.05), ('CB', 'ASN', 'CG', 'ASP', 10.33), ('CB', 'ASN', 'OD1', 'ASP', 9.91), ('CB', 'ASN', 'OD2', 'ASP', 10.4)], [('CG', 'ASN', 'CB', 'ASP', 10.81), ('CG', 'ASN', 'CG', 'ASP', 9.87), ('CG', 'ASN', 'OD1', 'ASP', 9.36), ('CG', 'ASN', 'OD2', 'ASP', 9.85)], [('OD1', 'ASN', 'CB', 'ASP', 10.64), ('OD1', 'ASN', 'CG', 'ASP', 9.61), ('OD1', 'ASN', 'OD1', 'ASP', 9.23), ('OD1', 'ASN', 'OD2', 'ASP', 9.4)], [('ND2', 'ASN', 'CB', 'ASP', 11.04), ('ND2', 'ASN', 'CG', 'ASP', 10.05), ('ND2', 'ASN', 'OD1', 'ASP', 9.35), ('ND2', 'ASN', 'OD2', 'ASP', 10.15)]]}
ASN_HIS = { 
	'distances':
		[[5.94, 5.56, 5.81, 5.7, 6.07, 6.01], [6.67, 5.98, 6.32, 5.57, 6.16, 5.7], [7.03, 6.5, 7.12, 5.91, 7.01, 6.28], [7.38, 6.38, 6.38, 5.82, 5.86, 5.46], [12.8, 11.45, 10.31, 11.21, 9.27, 9.86], [11.76, 10.35, 9.31, 9.96, 8.17, 8.6], [11.13, 9.7, 8.7, 9.27, 7.51, 7.9], [11.73, 10.33, 9.4, 9.86, 8.24, 8.54]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'HIS', 5.94), ('CB', 'ASN', 'CG', 'HIS', 5.56), ('CB', 'ASN', 'ND1', 'HIS', 5.81), ('CB', 'ASN', 'CD2', 'HIS', 5.7), ('CB', 'ASN', 'CE1', 'HIS', 6.07), ('CB', 'ASN', 'NE2', 'HIS', 6.01)], [('CG', 'ASN', 'CB', 'HIS', 6.67), ('CG', 'ASN', 'CG', 'HIS', 5.98), ('CG', 'ASN', 'ND1', 'HIS', 6.32), ('CG', 'ASN', 'CD2', 'HIS', 5.57), ('CG', 'ASN', 'CE1', 'HIS', 6.16), ('CG', 'ASN', 'NE2', 'HIS', 5.7)], [('OD1', 'ASN', 'CB', 'HIS', 7.03), ('OD1', 'ASN', 'CG', 'HIS', 6.5), ('OD1', 'ASN', 'ND1', 'HIS', 7.12), ('OD1', 'ASN', 'CD2', 'HIS', 5.91), ('OD1', 'ASN', 'CE1', 'HIS', 7.01), ('OD1', 'ASN', 'NE2', 'HIS', 6.28)], [('ND2', 'ASN', 'CB', 'HIS', 7.38), ('ND2', 'ASN', 'CG', 'HIS', 6.38), ('ND2', 'ASN', 'ND1', 'HIS', 6.38), ('ND2', 'ASN', 'CD2', 'HIS', 5.82), ('ND2', 'ASN', 'CE1', 'HIS', 5.86), ('ND2', 'ASN', 'NE2', 'HIS', 5.46)], [('CB', 'ASN', 'CB', 'HIS', 12.8), ('CB', 'ASN', 'CG', 'HIS', 11.45), ('CB', 'ASN', 'ND1', 'HIS', 10.31), ('CB', 'ASN', 'CD2', 'HIS', 11.21), ('CB', 'ASN', 'CE1', 'HIS', 9.27), ('CB', 'ASN', 'NE2', 'HIS', 9.86)], [('CG', 'ASN', 'CB', 'HIS', 11.76), ('CG', 'ASN', 'CG', 'HIS', 10.35), ('CG', 'ASN', 'ND1', 'HIS', 9.31), ('CG', 'ASN', 'CD2', 'HIS', 9.96), ('CG', 'ASN', 'CE1', 'HIS', 8.17), ('CG', 'ASN', 'NE2', 'HIS', 8.6)], [('OD1', 'ASN', 'CB', 'HIS', 11.13), ('OD1', 'ASN', 'CG', 'HIS', 9.7), ('OD1', 'ASN', 'ND1', 'HIS', 8.7), ('OD1', 'ASN', 'CD2', 'HIS', 9.27), ('OD1', 'ASN', 'CE1', 'HIS', 7.51), ('OD1', 'ASN', 'NE2', 'HIS', 7.9)], [('ND2', 'ASN', 'CB', 'HIS', 11.73), ('ND2', 'ASN', 'CG', 'HIS', 10.33), ('ND2', 'ASN', 'ND1', 'HIS', 9.4), ('ND2', 'ASN', 'CD2', 'HIS', 9.86), ('ND2', 'ASN', 'CE1', 'HIS', 8.24), ('ND2', 'ASN', 'NE2', 'HIS', 8.54)]]}
ASN_ASN = { 
	'distances':
		[[11.59, 10.5, 10.33, 9.98], [11.31, 10.08, 9.89, 9.43], [12.31, 11.01, 10.78, 10.33], [10.1, 8.85, 8.73, 8.14], [11.59, 11.31, 12.31, 10.1], [10.5, 10.08, 11.01, 8.85], [10.33, 9.89, 10.78, 8.73], [9.98, 9.43, 10.33, 8.14]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ASN', 11.59), ('CB', 'ASN', 'CG', 'ASN', 10.5), ('CB', 'ASN', 'OD1', 'ASN', 10.33), ('CB', 'ASN', 'ND2', 'ASN', 9.98)], [('CG', 'ASN', 'CB', 'ASN', 11.31), ('CG', 'ASN', 'CG', 'ASN', 10.08), ('CG', 'ASN', 'OD1', 'ASN', 9.89), ('CG', 'ASN', 'ND2', 'ASN', 9.43)], [('OD1', 'ASN', 'CB', 'ASN', 12.31), ('OD1', 'ASN', 'CG', 'ASN', 11.01), ('OD1', 'ASN', 'OD1', 'ASN', 10.78), ('OD1', 'ASN', 'ND2', 'ASN', 10.33)], [('ND2', 'ASN', 'CB', 'ASN', 10.1), ('ND2', 'ASN', 'CG', 'ASN', 8.85), ('ND2', 'ASN', 'OD1', 'ASN', 8.73), ('ND2', 'ASN', 'ND2', 'ASN', 8.14)], [('CB', 'ASN', 'CB', 'ASN', 11.59), ('CB', 'ASN', 'CG', 'ASN', 11.31), ('CB', 'ASN', 'OD1', 'ASN', 12.31), ('CB', 'ASN', 'ND2', 'ASN', 10.1)], [('CG', 'ASN', 'CB', 'ASN', 10.5), ('CG', 'ASN', 'CG', 'ASN', 10.08), ('CG', 'ASN', 'OD1', 'ASN', 11.01), ('CG', 'ASN', 'ND2', 'ASN', 8.85)], [('OD1', 'ASN', 'CB', 'ASN', 10.33), ('OD1', 'ASN', 'CG', 'ASN', 9.89), ('OD1', 'ASN', 'OD1', 'ASN', 10.78), ('OD1', 'ASN', 'ND2', 'ASN', 8.73)], [('ND2', 'ASN', 'CB', 'ASN', 9.98), ('ND2', 'ASN', 'CG', 'ASN', 9.43), ('ND2', 'ASN', 'OD1', 'ASN', 10.33), ('ND2', 'ASN', 'ND2', 'ASN', 8.14)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ASP, d, 'A_1ako_3_1_11_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'A_1ako_3_1_11_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASN_ASPI, d, 'A_1ako_3_1_11_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASN_ASP, d, 'A_1ako_3_1_11_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASN_HIS, d, 'A_1ako_3_1_11_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ASN_ASN, d, 'A_1ako_3_1_11_2')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ASP' :  match1,
		'HIS_ASP' :  match2,
		'ASN_ASPI' :  match3,
		'ASN_ASP' :  match4,
		'ASN_HIS' :  match5,
		'ASN_ASN' :  match6}