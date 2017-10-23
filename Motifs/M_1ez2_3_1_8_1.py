'''
FUNC:M_1ez2_3_1_8_1
PDB:1ez2
EC:3.1.8.1
RESI:asp,his,asp,zn,zn
LOCI:a-233,254,301,401,402;
'''
import motifFunctions as cmd
ASP_ZN = { 
	'distances':
		[[13.63], [12.47], [11.74], [12.52], [11.66], [10.65], [9.7], [11.08], [6.45], [5.14], [5.3], [4.33], [8.14], [6.85], [6.18], [6.9]],
	'comparisons':
		[[('CB', 'ASP', 'ZN', 'ZN', 13.63)], [('CG', 'ASP', 'ZN', 'ZN', 12.47)], [('OD1', 'ASP', 'ZN', 'ZN', 11.74)], [('OD2', 'ASP', 'ZN', 'ZN', 12.52)], [('CB', 'ASP', 'ZN', 'ZN', 11.66)], [('CG', 'ASP', 'ZN', 'ZN', 10.65)], [('OD1', 'ASP', 'ZN', 'ZN', 9.7)], [('OD2', 'ASP', 'ZN', 'ZN', 11.08)], [('CB', 'ASP', 'ZN', 'ZN', 6.45)], [('CG', 'ASP', 'ZN', 'ZN', 5.14)], [('OD1', 'ASP', 'ZN', 'ZN', 5.3)], [('OD2', 'ASP', 'ZN', 'ZN', 4.33)], [('CB', 'ASP', 'ZN', 'ZN', 8.14)], [('CG', 'ASP', 'ZN', 'ZN', 6.85)], [('OD1', 'ASP', 'ZN', 'ZN', 6.18)], [('OD2', 'ASP', 'ZN', 'ZN', 6.9)]]}
ASP_HIS = { 
	'distances':
		[[7.42, 7.54, 6.76, 8.72, 7.67, 8.76], [6.38, 6.28, 5.36, 7.43, 6.26, 7.4], [6.82, 6.34, 5.16, 7.29, 5.71, 6.95], [5.35, 5.54, 4.91, 6.83, 6.08, 7.07], [7.6, 6.69, 7.44, 5.36, 6.84, 5.52], [8.38, 7.21, 7.61, 5.88, 6.69, 5.46], [8.11, 6.78, 6.91, 5.55, 5.83, 4.75], [9.65, 8.5, 8.88, 7.17, 7.91, 6.73]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 7.42), ('CB', 'ASP', 'CG', 'HIS', 7.54), ('CB', 'ASP', 'ND1', 'HIS', 6.76), ('CB', 'ASP', 'CD2', 'HIS', 8.72), ('CB', 'ASP', 'CE1', 'HIS', 7.67), ('CB', 'ASP', 'NE2', 'HIS', 8.76)], [('CG', 'ASP', 'CB', 'HIS', 6.38), ('CG', 'ASP', 'CG', 'HIS', 6.28), ('CG', 'ASP', 'ND1', 'HIS', 5.36), ('CG', 'ASP', 'CD2', 'HIS', 7.43), ('CG', 'ASP', 'CE1', 'HIS', 6.26), ('CG', 'ASP', 'NE2', 'HIS', 7.4)], [('OD1', 'ASP', 'CB', 'HIS', 6.82), ('OD1', 'ASP', 'CG', 'HIS', 6.34), ('OD1', 'ASP', 'ND1', 'HIS', 5.16), ('OD1', 'ASP', 'CD2', 'HIS', 7.29), ('OD1', 'ASP', 'CE1', 'HIS', 5.71), ('OD1', 'ASP', 'NE2', 'HIS', 6.95)], [('OD2', 'ASP', 'CB', 'HIS', 5.35), ('OD2', 'ASP', 'CG', 'HIS', 5.54), ('OD2', 'ASP', 'ND1', 'HIS', 4.91), ('OD2', 'ASP', 'CD2', 'HIS', 6.83), ('OD2', 'ASP', 'CE1', 'HIS', 6.08), ('OD2', 'ASP', 'NE2', 'HIS', 7.07)], [('CB', 'ASP', 'CB', 'HIS', 7.6), ('CB', 'ASP', 'CG', 'HIS', 6.69), ('CB', 'ASP', 'ND1', 'HIS', 7.44), ('CB', 'ASP', 'CD2', 'HIS', 5.36), ('CB', 'ASP', 'CE1', 'HIS', 6.84), ('CB', 'ASP', 'NE2', 'HIS', 5.52)], [('CG', 'ASP', 'CB', 'HIS', 8.38), ('CG', 'ASP', 'CG', 'HIS', 7.21), ('CG', 'ASP', 'ND1', 'HIS', 7.61), ('CG', 'ASP', 'CD2', 'HIS', 5.88), ('CG', 'ASP', 'CE1', 'HIS', 6.69), ('CG', 'ASP', 'NE2', 'HIS', 5.46)], [('OD1', 'ASP', 'CB', 'HIS', 8.11), ('OD1', 'ASP', 'CG', 'HIS', 6.78), ('OD1', 'ASP', 'ND1', 'HIS', 6.91), ('OD1', 'ASP', 'CD2', 'HIS', 5.55), ('OD1', 'ASP', 'CE1', 'HIS', 5.83), ('OD1', 'ASP', 'NE2', 'HIS', 4.75)], [('OD2', 'ASP', 'CB', 'HIS', 9.65), ('OD2', 'ASP', 'CG', 'HIS', 8.5), ('OD2', 'ASP', 'ND1', 'HIS', 8.88), ('OD2', 'ASP', 'CD2', 'HIS', 7.17), ('OD2', 'ASP', 'CE1', 'HIS', 7.91), ('OD2', 'ASP', 'NE2', 'HIS', 6.73)]]}
HIS_ZN = { 
	'distances':
		[[10.99], [9.71], [9.76], [8.51], [8.63], [7.73], [10.64], [9.25], [8.76], [8.48], [7.57], [7.33]],
	'comparisons':
		[[('CB', 'HIS', 'ZN', 'ZN', 10.99)], [('CG', 'HIS', 'ZN', 'ZN', 9.71)], [('ND1', 'HIS', 'ZN', 'ZN', 9.76)], [('CD2', 'HIS', 'ZN', 'ZN', 8.51)], [('CE1', 'HIS', 'ZN', 'ZN', 8.63)], [('NE2', 'HIS', 'ZN', 'ZN', 7.73)], [('CB', 'HIS', 'ZN', 'ZN', 10.64)], [('CG', 'HIS', 'ZN', 'ZN', 9.25)], [('ND1', 'HIS', 'ZN', 'ZN', 8.76)], [('CD2', 'HIS', 'ZN', 'ZN', 8.48)], [('CE1', 'HIS', 'ZN', 'ZN', 7.57)], [('NE2', 'HIS', 'ZN', 'ZN', 7.33)]]}
ZN_ASPI = { 
	'distances':
		[6.45, 5.14, 5.3, 4.33, 8.14, 6.85, 6.18, 6.9],
	'comparisons':
		[('ZN', 'ZN', 'CB', 'ASPI', 6.45), ('ZN', 'ZN', 'CG', 'ASPI', 5.14), ('ZN', 'ZN', 'OD1', 'ASPI', 5.3), ('ZN', 'ZN', 'OD2', 'ASPI', 4.33), ('ZN', 'ZN', 'CB', 'ASPI', 8.14), ('ZN', 'ZN', 'CG', 'ASPI', 6.85), ('ZN', 'ZN', 'OD1', 'ASPI', 6.18), ('ZN', 'ZN', 'OD2', 'ASPI', 6.9)]}
ZN_ZN = { 
	'distances':
		[5.33, 5.33],
	'comparisons':
		[('ZN', 'ZN', 'ZN', 'ZN', 5.33), ('ZN', 'ZN', 'ZN', 'ZN', 5.33)]}
ASP_ASP = { 
	'distances':
		[[11.92, 12.07, 11.35, 13.25], [10.67, 10.78, 10.02, 11.99], [10.37, 10.28, 9.41, 11.44], [10.18, 10.48, 9.81, 11.74], [11.92, 10.67, 10.37, 10.18], [12.07, 10.78, 10.28, 10.48], [11.35, 10.02, 9.41, 9.81], [13.25, 11.99, 11.44, 11.74]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 11.92), ('CB', 'ASP', 'CG', 'ASP', 12.07), ('CB', 'ASP', 'OD1', 'ASP', 11.35), ('CB', 'ASP', 'OD2', 'ASP', 13.25)], [('CG', 'ASP', 'CB', 'ASP', 10.67), ('CG', 'ASP', 'CG', 'ASP', 10.78), ('CG', 'ASP', 'OD1', 'ASP', 10.02), ('CG', 'ASP', 'OD2', 'ASP', 11.99)], [('OD1', 'ASP', 'CB', 'ASP', 10.37), ('OD1', 'ASP', 'CG', 'ASP', 10.28), ('OD1', 'ASP', 'OD1', 'ASP', 9.41), ('OD1', 'ASP', 'OD2', 'ASP', 11.44)], [('OD2', 'ASP', 'CB', 'ASP', 10.18), ('OD2', 'ASP', 'CG', 'ASP', 10.48), ('OD2', 'ASP', 'OD1', 'ASP', 9.81), ('OD2', 'ASP', 'OD2', 'ASP', 11.74)], [('CB', 'ASP', 'CB', 'ASP', 11.92), ('CB', 'ASP', 'CG', 'ASP', 10.67), ('CB', 'ASP', 'OD1', 'ASP', 10.37), ('CB', 'ASP', 'OD2', 'ASP', 10.18)], [('CG', 'ASP', 'CB', 'ASP', 12.07), ('CG', 'ASP', 'CG', 'ASP', 10.78), ('CG', 'ASP', 'OD1', 'ASP', 10.28), ('CG', 'ASP', 'OD2', 'ASP', 10.48)], [('OD1', 'ASP', 'CB', 'ASP', 11.35), ('OD1', 'ASP', 'CG', 'ASP', 10.02), ('OD1', 'ASP', 'OD1', 'ASP', 9.41), ('OD1', 'ASP', 'OD2', 'ASP', 9.81)], [('OD2', 'ASP', 'CB', 'ASP', 13.25), ('OD2', 'ASP', 'CG', 'ASP', 11.99), ('OD2', 'ASP', 'OD1', 'ASP', 11.44), ('OD2', 'ASP', 'OD2', 'ASP', 11.74)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ZN, d, 'M_1ez2_3_1_8_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'M_1ez2_3_1_8_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ZN, d, 'M_1ez2_3_1_8_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ZN_ASPI, d, 'M_1ez2_3_1_8_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ZN_ZN, d, 'M_1ez2_3_1_8_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ASP_ASP, d, 'M_1ez2_3_1_8_1')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ZN' :  match1,
		'ASP_HIS' :  match2,
		'HIS_ZN' :  match3,
		'ZN_ASPI' :  match4,
		'ZN_ZN' :  match5,
		'ASP_ASP' :  match6}