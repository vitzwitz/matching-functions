'''
FUNC:A_1rpx_5_1_3_1
PDB:1rpx
EC:5.1.3.1
RESI:his,asp,his,asp
LOCI:a-41,43,74,185;
'''
import motifFunctions as cmd
ASP_HISI = { 
	'distances':
		[[9.4, 8.36, 8.33, 7.63, 7.62, 7.13], [8.85, 7.87, 8.14, 6.95, 7.5, 6.69], [9.11, 8.35, 8.82, 7.48, 8.36, 7.5], [8.46, 7.35, 7.64, 6.25, 6.86, 5.89]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HISI', 9.4), ('CB', 'ASP', 'CG', 'HISI', 8.36), ('CB', 'ASP', 'ND1', 'HISI', 8.33), ('CB', 'ASP', 'CD2', 'HISI', 7.63), ('CB', 'ASP', 'CE1', 'HISI', 7.62), ('CB', 'ASP', 'NE2', 'HISI', 7.13)], [('CG', 'ASP', 'CB', 'HISI', 8.85), ('CG', 'ASP', 'CG', 'HISI', 7.87), ('CG', 'ASP', 'ND1', 'HISI', 8.14), ('CG', 'ASP', 'CD2', 'HISI', 6.95), ('CG', 'ASP', 'CE1', 'HISI', 7.5), ('CG', 'ASP', 'NE2', 'HISI', 6.69)], [('OD1', 'ASP', 'CB', 'HISI', 9.11), ('OD1', 'ASP', 'CG', 'HISI', 8.35), ('OD1', 'ASP', 'ND1', 'HISI', 8.82), ('OD1', 'ASP', 'CD2', 'HISI', 7.48), ('OD1', 'ASP', 'CE1', 'HISI', 8.36), ('OD1', 'ASP', 'NE2', 'HISI', 7.5)], [('OD2', 'ASP', 'CB', 'HISI', 8.46), ('OD2', 'ASP', 'CG', 'HISI', 7.35), ('OD2', 'ASP', 'ND1', 'HISI', 7.64), ('OD2', 'ASP', 'CD2', 'HISI', 6.25), ('OD2', 'ASP', 'CE1', 'HISI', 6.86), ('OD2', 'ASP', 'NE2', 'HISI', 5.89)]]}
ASP_HIS = { 
	'distances':
		[[7.4, 7.77, 7.45, 8.78, 8.3, 9.05], [7.06, 7.41, 6.88, 8.56, 7.83, 8.76], [6.15, 6.32, 5.69, 7.49, 6.65, 7.63], [8.0, 8.42, 7.85, 9.64, 8.81, 9.82], [8.73, 8.02, 8.77, 6.93, 8.33, 7.19], [7.75, 6.95, 7.74, 5.74, 7.28, 6.04], [7.82, 6.76, 7.3, 5.45, 6.6, 5.35], [7.23, 6.67, 7.7, 5.55, 7.47, 6.23], [9.36, 8.97, 7.92, 9.8, 8.26, 9.39], [9.1, 8.78, 7.66, 9.74, 8.11, 9.36], [10.14, 9.89, 8.76, 10.88, 9.2, 10.48], [8.02, 7.71, 6.57, 8.71, 7.11, 8.37]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 7.4), ('CB', 'ASP', 'CG', 'HIS', 7.77), ('CB', 'ASP', 'ND1', 'HIS', 7.45), ('CB', 'ASP', 'CD2', 'HIS', 8.78), ('CB', 'ASP', 'CE1', 'HIS', 8.3), ('CB', 'ASP', 'NE2', 'HIS', 9.05)], [('CG', 'ASP', 'CB', 'HIS', 7.06), ('CG', 'ASP', 'CG', 'HIS', 7.41), ('CG', 'ASP', 'ND1', 'HIS', 6.88), ('CG', 'ASP', 'CD2', 'HIS', 8.56), ('CG', 'ASP', 'CE1', 'HIS', 7.83), ('CG', 'ASP', 'NE2', 'HIS', 8.76)], [('OD1', 'ASP', 'CB', 'HIS', 6.15), ('OD1', 'ASP', 'CG', 'HIS', 6.32), ('OD1', 'ASP', 'ND1', 'HIS', 5.69), ('OD1', 'ASP', 'CD2', 'HIS', 7.49), ('OD1', 'ASP', 'CE1', 'HIS', 6.65), ('OD1', 'ASP', 'NE2', 'HIS', 7.63)], [('OD2', 'ASP', 'CB', 'HIS', 8.0), ('OD2', 'ASP', 'CG', 'HIS', 8.42), ('OD2', 'ASP', 'ND1', 'HIS', 7.85), ('OD2', 'ASP', 'CD2', 'HIS', 9.64), ('OD2', 'ASP', 'CE1', 'HIS', 8.81), ('OD2', 'ASP', 'NE2', 'HIS', 9.82)], [('CB', 'ASP', 'CB', 'HIS', 8.73), ('CB', 'ASP', 'CG', 'HIS', 8.02), ('CB', 'ASP', 'ND1', 'HIS', 8.77), ('CB', 'ASP', 'CD2', 'HIS', 6.93), ('CB', 'ASP', 'CE1', 'HIS', 8.33), ('CB', 'ASP', 'NE2', 'HIS', 7.19)], [('CG', 'ASP', 'CB', 'HIS', 7.75), ('CG', 'ASP', 'CG', 'HIS', 6.95), ('CG', 'ASP', 'ND1', 'HIS', 7.74), ('CG', 'ASP', 'CD2', 'HIS', 5.74), ('CG', 'ASP', 'CE1', 'HIS', 7.28), ('CG', 'ASP', 'NE2', 'HIS', 6.04)], [('OD1', 'ASP', 'CB', 'HIS', 7.82), ('OD1', 'ASP', 'CG', 'HIS', 6.76), ('OD1', 'ASP', 'ND1', 'HIS', 7.3), ('OD1', 'ASP', 'CD2', 'HIS', 5.45), ('OD1', 'ASP', 'CE1', 'HIS', 6.6), ('OD1', 'ASP', 'NE2', 'HIS', 5.35)], [('OD2', 'ASP', 'CB', 'HIS', 7.23), ('OD2', 'ASP', 'CG', 'HIS', 6.67), ('OD2', 'ASP', 'ND1', 'HIS', 7.7), ('OD2', 'ASP', 'CD2', 'HIS', 5.55), ('OD2', 'ASP', 'CE1', 'HIS', 7.47), ('OD2', 'ASP', 'NE2', 'HIS', 6.23)], [('CB', 'ASP', 'CB', 'HIS', 9.36), ('CB', 'ASP', 'CG', 'HIS', 8.97), ('CB', 'ASP', 'ND1', 'HIS', 7.92), ('CB', 'ASP', 'CD2', 'HIS', 9.8), ('CB', 'ASP', 'CE1', 'HIS', 8.26), ('CB', 'ASP', 'NE2', 'HIS', 9.39)], [('CG', 'ASP', 'CB', 'HIS', 9.1), ('CG', 'ASP', 'CG', 'HIS', 8.78), ('CG', 'ASP', 'ND1', 'HIS', 7.66), ('CG', 'ASP', 'CD2', 'HIS', 9.74), ('CG', 'ASP', 'CE1', 'HIS', 8.11), ('CG', 'ASP', 'NE2', 'HIS', 9.36)], [('OD1', 'ASP', 'CB', 'HIS', 10.14), ('OD1', 'ASP', 'CG', 'HIS', 9.89), ('OD1', 'ASP', 'ND1', 'HIS', 8.76), ('OD1', 'ASP', 'CD2', 'HIS', 10.88), ('OD1', 'ASP', 'CE1', 'HIS', 9.2), ('OD1', 'ASP', 'NE2', 'HIS', 10.48)], [('OD2', 'ASP', 'CB', 'HIS', 8.02), ('OD2', 'ASP', 'CG', 'HIS', 7.71), ('OD2', 'ASP', 'ND1', 'HIS', 6.57), ('OD2', 'ASP', 'CD2', 'HIS', 8.71), ('OD2', 'ASP', 'CE1', 'HIS', 7.11), ('OD2', 'ASP', 'NE2', 'HIS', 8.37)]]}
HIS_HIS = { 
	'distances':
		[[8.7, 7.35, 6.84, 6.7, 5.78, 5.63], [9.78, 8.35, 7.86, 7.52, 6.64, 6.34], [9.75, 8.31, 7.99, 7.28, 6.73, 6.15], [11.1, 9.67, 9.11, 8.87, 7.88, 7.67], [11.02, 9.57, 9.23, 8.52, 7.95, 7.39], [11.78, 10.32, 9.84, 9.37, 8.55, 8.18], [8.7, 9.78, 9.75, 11.1, 11.02, 11.78], [7.35, 8.35, 8.31, 9.67, 9.57, 10.32], [6.84, 7.86, 7.99, 9.11, 9.23, 9.84], [6.7, 7.52, 7.28, 8.87, 8.52, 9.37], [5.78, 6.64, 6.73, 7.88, 7.95, 8.55], [5.63, 6.34, 6.15, 7.67, 7.39, 8.18]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 8.7), ('CB', 'HIS', 'CG', 'HIS', 7.35), ('CB', 'HIS', 'ND1', 'HIS', 6.84), ('CB', 'HIS', 'CD2', 'HIS', 6.7), ('CB', 'HIS', 'CE1', 'HIS', 5.78), ('CB', 'HIS', 'NE2', 'HIS', 5.63)], [('CG', 'HIS', 'CB', 'HIS', 9.78), ('CG', 'HIS', 'CG', 'HIS', 8.35), ('CG', 'HIS', 'ND1', 'HIS', 7.86), ('CG', 'HIS', 'CD2', 'HIS', 7.52), ('CG', 'HIS', 'CE1', 'HIS', 6.64), ('CG', 'HIS', 'NE2', 'HIS', 6.34)], [('ND1', 'HIS', 'CB', 'HIS', 9.75), ('ND1', 'HIS', 'CG', 'HIS', 8.31), ('ND1', 'HIS', 'ND1', 'HIS', 7.99), ('ND1', 'HIS', 'CD2', 'HIS', 7.28), ('ND1', 'HIS', 'CE1', 'HIS', 6.73), ('ND1', 'HIS', 'NE2', 'HIS', 6.15)], [('CD2', 'HIS', 'CB', 'HIS', 11.1), ('CD2', 'HIS', 'CG', 'HIS', 9.67), ('CD2', 'HIS', 'ND1', 'HIS', 9.11), ('CD2', 'HIS', 'CD2', 'HIS', 8.87), ('CD2', 'HIS', 'CE1', 'HIS', 7.88), ('CD2', 'HIS', 'NE2', 'HIS', 7.67)], [('CE1', 'HIS', 'CB', 'HIS', 11.02), ('CE1', 'HIS', 'CG', 'HIS', 9.57), ('CE1', 'HIS', 'ND1', 'HIS', 9.23), ('CE1', 'HIS', 'CD2', 'HIS', 8.52), ('CE1', 'HIS', 'CE1', 'HIS', 7.95), ('CE1', 'HIS', 'NE2', 'HIS', 7.39)], [('NE2', 'HIS', 'CB', 'HIS', 11.78), ('NE2', 'HIS', 'CG', 'HIS', 10.32), ('NE2', 'HIS', 'ND1', 'HIS', 9.84), ('NE2', 'HIS', 'CD2', 'HIS', 9.37), ('NE2', 'HIS', 'CE1', 'HIS', 8.55), ('NE2', 'HIS', 'NE2', 'HIS', 8.18)], [('CB', 'HIS', 'CB', 'HIS', 8.7), ('CB', 'HIS', 'CG', 'HIS', 9.78), ('CB', 'HIS', 'ND1', 'HIS', 9.75), ('CB', 'HIS', 'CD2', 'HIS', 11.1), ('CB', 'HIS', 'CE1', 'HIS', 11.02), ('CB', 'HIS', 'NE2', 'HIS', 11.78)], [('CG', 'HIS', 'CB', 'HIS', 7.35), ('CG', 'HIS', 'CG', 'HIS', 8.35), ('CG', 'HIS', 'ND1', 'HIS', 8.31), ('CG', 'HIS', 'CD2', 'HIS', 9.67), ('CG', 'HIS', 'CE1', 'HIS', 9.57), ('CG', 'HIS', 'NE2', 'HIS', 10.32)], [('ND1', 'HIS', 'CB', 'HIS', 6.84), ('ND1', 'HIS', 'CG', 'HIS', 7.86), ('ND1', 'HIS', 'ND1', 'HIS', 7.99), ('ND1', 'HIS', 'CD2', 'HIS', 9.11), ('ND1', 'HIS', 'CE1', 'HIS', 9.23), ('ND1', 'HIS', 'NE2', 'HIS', 9.84)], [('CD2', 'HIS', 'CB', 'HIS', 6.7), ('CD2', 'HIS', 'CG', 'HIS', 7.52), ('CD2', 'HIS', 'ND1', 'HIS', 7.28), ('CD2', 'HIS', 'CD2', 'HIS', 8.87), ('CD2', 'HIS', 'CE1', 'HIS', 8.52), ('CD2', 'HIS', 'NE2', 'HIS', 9.37)], [('CE1', 'HIS', 'CB', 'HIS', 5.78), ('CE1', 'HIS', 'CG', 'HIS', 6.64), ('CE1', 'HIS', 'ND1', 'HIS', 6.73), ('CE1', 'HIS', 'CD2', 'HIS', 7.88), ('CE1', 'HIS', 'CE1', 'HIS', 7.95), ('CE1', 'HIS', 'NE2', 'HIS', 8.55)], [('NE2', 'HIS', 'CB', 'HIS', 5.63), ('NE2', 'HIS', 'CG', 'HIS', 6.34), ('NE2', 'HIS', 'ND1', 'HIS', 6.15), ('NE2', 'HIS', 'CD2', 'HIS', 7.67), ('NE2', 'HIS', 'CE1', 'HIS', 7.39), ('NE2', 'HIS', 'NE2', 'HIS', 8.18)]]}
ASP_ASP = { 
	'distances':
		[[10.35, 9.15, 9.49, 8.02], [8.95, 7.73, 8.08, 6.64], [8.11, 7.04, 7.61, 5.85], [8.86, 7.55, 7.67, 6.63], [10.35, 8.95, 8.11, 8.86], [9.15, 7.73, 7.04, 7.55], [9.49, 8.08, 7.61, 7.67], [8.02, 6.64, 5.85, 6.63]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 10.35), ('CB', 'ASP', 'CG', 'ASP', 9.15), ('CB', 'ASP', 'OD1', 'ASP', 9.49), ('CB', 'ASP', 'OD2', 'ASP', 8.02)], [('CG', 'ASP', 'CB', 'ASP', 8.95), ('CG', 'ASP', 'CG', 'ASP', 7.73), ('CG', 'ASP', 'OD1', 'ASP', 8.08), ('CG', 'ASP', 'OD2', 'ASP', 6.64)], [('OD1', 'ASP', 'CB', 'ASP', 8.11), ('OD1', 'ASP', 'CG', 'ASP', 7.04), ('OD1', 'ASP', 'OD1', 'ASP', 7.61), ('OD1', 'ASP', 'OD2', 'ASP', 5.85)], [('OD2', 'ASP', 'CB', 'ASP', 8.86), ('OD2', 'ASP', 'CG', 'ASP', 7.55), ('OD2', 'ASP', 'OD1', 'ASP', 7.67), ('OD2', 'ASP', 'OD2', 'ASP', 6.63)], [('CB', 'ASP', 'CB', 'ASP', 10.35), ('CB', 'ASP', 'CG', 'ASP', 8.95), ('CB', 'ASP', 'OD1', 'ASP', 8.11), ('CB', 'ASP', 'OD2', 'ASP', 8.86)], [('CG', 'ASP', 'CB', 'ASP', 9.15), ('CG', 'ASP', 'CG', 'ASP', 7.73), ('CG', 'ASP', 'OD1', 'ASP', 7.04), ('CG', 'ASP', 'OD2', 'ASP', 7.55)], [('OD1', 'ASP', 'CB', 'ASP', 9.49), ('OD1', 'ASP', 'CG', 'ASP', 8.08), ('OD1', 'ASP', 'OD1', 'ASP', 7.61), ('OD1', 'ASP', 'OD2', 'ASP', 7.67)], [('OD2', 'ASP', 'CB', 'ASP', 8.02), ('OD2', 'ASP', 'CG', 'ASP', 6.64), ('OD2', 'ASP', 'OD1', 'ASP', 5.85), ('OD2', 'ASP', 'OD2', 'ASP', 6.63)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HISI, d, 'A_1rpx_5_1_3_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'A_1rpx_5_1_3_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_HIS, d, 'A_1rpx_5_1_3_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_ASP, d, 'A_1rpx_5_1_3_1')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HISI' :  match1,
		'ASP_HIS' :  match2,
		'HIS_HIS' :  match3,
		'ASP_ASP' :  match4}