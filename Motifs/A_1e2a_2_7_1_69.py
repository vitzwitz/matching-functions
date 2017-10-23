'''
FUNC:A_1e2a_2_7_1_69
PDB:1e2a
EC:2.7.1.69
RESI:his,gln,asp,his
LOCI:a-78,80,81,82;
'''
import motifFunctions as cmd
ASP_GLN = { 
	'distances':
		[[7.41, 8.86, 9.74, 9.94, 10.55], [7.41, 8.84, 9.89, 10.07, 10.82], [7.17, 8.59, 9.6, 9.63, 10.66], [8.09, 9.41, 10.6, 10.91, 11.48]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLN', 7.41), ('CB', 'ASP', 'CG', 'GLN', 8.86), ('CB', 'ASP', 'CD', 'GLN', 9.74), ('CB', 'ASP', 'OE1', 'GLN', 9.94), ('CB', 'ASP', 'NE2', 'GLN', 10.55)], [('CG', 'ASP', 'CB', 'GLN', 7.41), ('CG', 'ASP', 'CG', 'GLN', 8.84), ('CG', 'ASP', 'CD', 'GLN', 9.89), ('CG', 'ASP', 'OE1', 'GLN', 10.07), ('CG', 'ASP', 'NE2', 'GLN', 10.82)], [('OD1', 'ASP', 'CB', 'GLN', 7.17), ('OD1', 'ASP', 'CG', 'GLN', 8.59), ('OD1', 'ASP', 'CD', 'GLN', 9.6), ('OD1', 'ASP', 'OE1', 'GLN', 9.63), ('OD1', 'ASP', 'NE2', 'GLN', 10.66)], [('OD2', 'ASP', 'CB', 'GLN', 8.09), ('OD2', 'ASP', 'CG', 'GLN', 9.41), ('OD2', 'ASP', 'CD', 'GLN', 10.6), ('OD2', 'ASP', 'OE1', 'GLN', 10.91), ('OD2', 'ASP', 'NE2', 'GLN', 11.48)]]}
GLN_HISI = { 
	'distances':
		[[9.16, 10.01, 10.4, 10.84, 11.37, 11.62], [9.87, 10.84, 11.41, 11.59, 12.39, 12.5], [11.03, 11.88, 12.45, 12.5, 13.32, 13.36], [11.9, 12.68, 13.13, 13.33, 13.99, 14.11], [11.23, 12.06, 12.76, 12.54, 13.57, 13.46]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'HISI', 9.16), ('CB', 'GLN', 'CG', 'HISI', 10.01), ('CB', 'GLN', 'ND1', 'HISI', 10.4), ('CB', 'GLN', 'CD2', 'HISI', 10.84), ('CB', 'GLN', 'CE1', 'HISI', 11.37), ('CB', 'GLN', 'NE2', 'HISI', 11.62)], [('CG', 'GLN', 'CB', 'HISI', 9.87), ('CG', 'GLN', 'CG', 'HISI', 10.84), ('CG', 'GLN', 'ND1', 'HISI', 11.41), ('CG', 'GLN', 'CD2', 'HISI', 11.59), ('CG', 'GLN', 'CE1', 'HISI', 12.39), ('CG', 'GLN', 'NE2', 'HISI', 12.5)], [('CD', 'GLN', 'CB', 'HISI', 11.03), ('CD', 'GLN', 'CG', 'HISI', 11.88), ('CD', 'GLN', 'ND1', 'HISI', 12.45), ('CD', 'GLN', 'CD2', 'HISI', 12.5), ('CD', 'GLN', 'CE1', 'HISI', 13.32), ('CD', 'GLN', 'NE2', 'HISI', 13.36)], [('OE1', 'GLN', 'CB', 'HISI', 11.9), ('OE1', 'GLN', 'CG', 'HISI', 12.68), ('OE1', 'GLN', 'ND1', 'HISI', 13.13), ('OE1', 'GLN', 'CD2', 'HISI', 13.33), ('OE1', 'GLN', 'CE1', 'HISI', 13.99), ('OE1', 'GLN', 'NE2', 'HISI', 14.11)], [('NE2', 'GLN', 'CB', 'HISI', 11.23), ('NE2', 'GLN', 'CG', 'HISI', 12.06), ('NE2', 'GLN', 'ND1', 'HISI', 12.76), ('NE2', 'GLN', 'CD2', 'HISI', 12.54), ('NE2', 'GLN', 'CE1', 'HISI', 13.57), ('NE2', 'GLN', 'NE2', 'HISI', 13.46)]]}
HIS_ASP = { 
	'distances':
		[[7.28, 8.72, 9.49, 9.27], [7.65, 9.08, 10.0, 9.43], [8.49, 9.94, 10.86, 10.31], [7.72, 9.02, 10.08, 9.14], [9.0, 10.37, 11.39, 10.56], [8.59, 9.86, 10.96, 9.9], [7.54, 7.77, 8.84, 7.16], [7.57, 8.08, 9.26, 7.53], [7.01, 7.55, 8.79, 6.96], [8.53, 9.23, 10.41, 8.77], [7.75, 8.48, 9.73, 7.99], [8.6, 9.41, 10.64, 8.98]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.28), ('CB', 'HIS', 'CG', 'ASP', 8.72), ('CB', 'HIS', 'OD1', 'ASP', 9.49), ('CB', 'HIS', 'OD2', 'ASP', 9.27)], [('CG', 'HIS', 'CB', 'ASP', 7.65), ('CG', 'HIS', 'CG', 'ASP', 9.08), ('CG', 'HIS', 'OD1', 'ASP', 10.0), ('CG', 'HIS', 'OD2', 'ASP', 9.43)], [('ND1', 'HIS', 'CB', 'ASP', 8.49), ('ND1', 'HIS', 'CG', 'ASP', 9.94), ('ND1', 'HIS', 'OD1', 'ASP', 10.86), ('ND1', 'HIS', 'OD2', 'ASP', 10.31)], [('CD2', 'HIS', 'CB', 'ASP', 7.72), ('CD2', 'HIS', 'CG', 'ASP', 9.02), ('CD2', 'HIS', 'OD1', 'ASP', 10.08), ('CD2', 'HIS', 'OD2', 'ASP', 9.14)], [('CE1', 'HIS', 'CB', 'ASP', 9.0), ('CE1', 'HIS', 'CG', 'ASP', 10.37), ('CE1', 'HIS', 'OD1', 'ASP', 11.39), ('CE1', 'HIS', 'OD2', 'ASP', 10.56)], [('NE2', 'HIS', 'CB', 'ASP', 8.59), ('NE2', 'HIS', 'CG', 'ASP', 9.86), ('NE2', 'HIS', 'OD1', 'ASP', 10.96), ('NE2', 'HIS', 'OD2', 'ASP', 9.9)], [('CB', 'HIS', 'CB', 'ASP', 7.54), ('CB', 'HIS', 'CG', 'ASP', 7.77), ('CB', 'HIS', 'OD1', 'ASP', 8.84), ('CB', 'HIS', 'OD2', 'ASP', 7.16)], [('CG', 'HIS', 'CB', 'ASP', 7.57), ('CG', 'HIS', 'CG', 'ASP', 8.08), ('CG', 'HIS', 'OD1', 'ASP', 9.26), ('CG', 'HIS', 'OD2', 'ASP', 7.53)], [('ND1', 'HIS', 'CB', 'ASP', 7.01), ('ND1', 'HIS', 'CG', 'ASP', 7.55), ('ND1', 'HIS', 'OD1', 'ASP', 8.79), ('ND1', 'HIS', 'OD2', 'ASP', 6.96)], [('CD2', 'HIS', 'CB', 'ASP', 8.53), ('CD2', 'HIS', 'CG', 'ASP', 9.23), ('CD2', 'HIS', 'OD1', 'ASP', 10.41), ('CD2', 'HIS', 'OD2', 'ASP', 8.77)], [('CE1', 'HIS', 'CB', 'ASP', 7.75), ('CE1', 'HIS', 'CG', 'ASP', 8.48), ('CE1', 'HIS', 'OD1', 'ASP', 9.73), ('CE1', 'HIS', 'OD2', 'ASP', 7.99)], [('NE2', 'HIS', 'CB', 'ASP', 8.6), ('NE2', 'HIS', 'CG', 'ASP', 9.41), ('NE2', 'HIS', 'OD1', 'ASP', 10.64), ('NE2', 'HIS', 'OD2', 'ASP', 8.98)]]}
HIS_GLN = { 
	'distances':
		[[9.16, 10.12, 10.32, 10.69, 10.4], [10.29, 11.29, 11.62, 12.05, 11.7], [11.51, 12.55, 12.82, 13.17, 12.91], [10.56, 11.54, 12.04, 12.59, 12.11], [12.37, 13.42, 13.81, 14.22, 13.9], [11.88, 12.89, 13.41, 13.93, 13.49], [9.16, 9.87, 11.03, 11.9, 11.23], [10.01, 10.84, 11.88, 12.68, 12.06], [10.4, 11.41, 12.45, 13.13, 12.76], [10.84, 11.59, 12.5, 13.33, 12.54], [11.37, 12.39, 13.32, 13.99, 13.57], [11.62, 12.5, 13.36, 14.11, 13.46]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLN', 9.16), ('CB', 'HIS', 'CG', 'GLN', 10.12), ('CB', 'HIS', 'CD', 'GLN', 10.32), ('CB', 'HIS', 'OE1', 'GLN', 10.69), ('CB', 'HIS', 'NE2', 'GLN', 10.4)], [('CG', 'HIS', 'CB', 'GLN', 10.29), ('CG', 'HIS', 'CG', 'GLN', 11.29), ('CG', 'HIS', 'CD', 'GLN', 11.62), ('CG', 'HIS', 'OE1', 'GLN', 12.05), ('CG', 'HIS', 'NE2', 'GLN', 11.7)], [('ND1', 'HIS', 'CB', 'GLN', 11.51), ('ND1', 'HIS', 'CG', 'GLN', 12.55), ('ND1', 'HIS', 'CD', 'GLN', 12.82), ('ND1', 'HIS', 'OE1', 'GLN', 13.17), ('ND1', 'HIS', 'NE2', 'GLN', 12.91)], [('CD2', 'HIS', 'CB', 'GLN', 10.56), ('CD2', 'HIS', 'CG', 'GLN', 11.54), ('CD2', 'HIS', 'CD', 'GLN', 12.04), ('CD2', 'HIS', 'OE1', 'GLN', 12.59), ('CD2', 'HIS', 'NE2', 'GLN', 12.11)], [('CE1', 'HIS', 'CB', 'GLN', 12.37), ('CE1', 'HIS', 'CG', 'GLN', 13.42), ('CE1', 'HIS', 'CD', 'GLN', 13.81), ('CE1', 'HIS', 'OE1', 'GLN', 14.22), ('CE1', 'HIS', 'NE2', 'GLN', 13.9)], [('NE2', 'HIS', 'CB', 'GLN', 11.88), ('NE2', 'HIS', 'CG', 'GLN', 12.89), ('NE2', 'HIS', 'CD', 'GLN', 13.41), ('NE2', 'HIS', 'OE1', 'GLN', 13.93), ('NE2', 'HIS', 'NE2', 'GLN', 13.49)], [('CB', 'HIS', 'CB', 'GLN', 9.16), ('CB', 'HIS', 'CG', 'GLN', 9.87), ('CB', 'HIS', 'CD', 'GLN', 11.03), ('CB', 'HIS', 'OE1', 'GLN', 11.9), ('CB', 'HIS', 'NE2', 'GLN', 11.23)], [('CG', 'HIS', 'CB', 'GLN', 10.01), ('CG', 'HIS', 'CG', 'GLN', 10.84), ('CG', 'HIS', 'CD', 'GLN', 11.88), ('CG', 'HIS', 'OE1', 'GLN', 12.68), ('CG', 'HIS', 'NE2', 'GLN', 12.06)], [('ND1', 'HIS', 'CB', 'GLN', 10.4), ('ND1', 'HIS', 'CG', 'GLN', 11.41), ('ND1', 'HIS', 'CD', 'GLN', 12.45), ('ND1', 'HIS', 'OE1', 'GLN', 13.13), ('ND1', 'HIS', 'NE2', 'GLN', 12.76)], [('CD2', 'HIS', 'CB', 'GLN', 10.84), ('CD2', 'HIS', 'CG', 'GLN', 11.59), ('CD2', 'HIS', 'CD', 'GLN', 12.5), ('CD2', 'HIS', 'OE1', 'GLN', 13.33), ('CD2', 'HIS', 'NE2', 'GLN', 12.54)], [('CE1', 'HIS', 'CB', 'GLN', 11.37), ('CE1', 'HIS', 'CG', 'GLN', 12.39), ('CE1', 'HIS', 'CD', 'GLN', 13.32), ('CE1', 'HIS', 'OE1', 'GLN', 13.99), ('CE1', 'HIS', 'NE2', 'GLN', 13.57)], [('NE2', 'HIS', 'CB', 'GLN', 11.62), ('NE2', 'HIS', 'CG', 'GLN', 12.5), ('NE2', 'HIS', 'CD', 'GLN', 13.36), ('NE2', 'HIS', 'OE1', 'GLN', 14.11), ('NE2', 'HIS', 'NE2', 'GLN', 13.46)]]}
HIS_HIS = { 
	'distances':
		[[8.51, 7.87, 7.83, 7.72, 7.69, 7.6], [8.27, 7.32, 7.14, 6.98, 6.69, 6.57], [9.41, 8.32, 7.95, 7.87, 7.27, 7.19], [7.31, 6.2, 6.04, 5.72, 5.47, 5.22], [9.31, 8.04, 7.57, 7.45, 6.65, 6.54], [8.11, 6.79, 6.41, 6.15, 5.46, 5.23], [8.51, 8.27, 9.41, 7.31, 9.31, 8.11], [7.87, 7.32, 8.32, 6.2, 8.04, 6.79], [7.83, 7.14, 7.95, 6.04, 7.57, 6.41], [7.72, 6.98, 7.87, 5.72, 7.45, 6.15], [7.69, 6.69, 7.27, 5.47, 6.65, 5.46], [7.6, 6.57, 7.19, 5.22, 6.54, 5.23]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 8.51), ('CB', 'HIS', 'CG', 'HIS', 7.87), ('CB', 'HIS', 'ND1', 'HIS', 7.83), ('CB', 'HIS', 'CD2', 'HIS', 7.72), ('CB', 'HIS', 'CE1', 'HIS', 7.69), ('CB', 'HIS', 'NE2', 'HIS', 7.6)], [('CG', 'HIS', 'CB', 'HIS', 8.27), ('CG', 'HIS', 'CG', 'HIS', 7.32), ('CG', 'HIS', 'ND1', 'HIS', 7.14), ('CG', 'HIS', 'CD2', 'HIS', 6.98), ('CG', 'HIS', 'CE1', 'HIS', 6.69), ('CG', 'HIS', 'NE2', 'HIS', 6.57)], [('ND1', 'HIS', 'CB', 'HIS', 9.41), ('ND1', 'HIS', 'CG', 'HIS', 8.32), ('ND1', 'HIS', 'ND1', 'HIS', 7.95), ('ND1', 'HIS', 'CD2', 'HIS', 7.87), ('ND1', 'HIS', 'CE1', 'HIS', 7.27), ('ND1', 'HIS', 'NE2', 'HIS', 7.19)], [('CD2', 'HIS', 'CB', 'HIS', 7.31), ('CD2', 'HIS', 'CG', 'HIS', 6.2), ('CD2', 'HIS', 'ND1', 'HIS', 6.04), ('CD2', 'HIS', 'CD2', 'HIS', 5.72), ('CD2', 'HIS', 'CE1', 'HIS', 5.47), ('CD2', 'HIS', 'NE2', 'HIS', 5.22)], [('CE1', 'HIS', 'CB', 'HIS', 9.31), ('CE1', 'HIS', 'CG', 'HIS', 8.04), ('CE1', 'HIS', 'ND1', 'HIS', 7.57), ('CE1', 'HIS', 'CD2', 'HIS', 7.45), ('CE1', 'HIS', 'CE1', 'HIS', 6.65), ('CE1', 'HIS', 'NE2', 'HIS', 6.54)], [('NE2', 'HIS', 'CB', 'HIS', 8.11), ('NE2', 'HIS', 'CG', 'HIS', 6.79), ('NE2', 'HIS', 'ND1', 'HIS', 6.41), ('NE2', 'HIS', 'CD2', 'HIS', 6.15), ('NE2', 'HIS', 'CE1', 'HIS', 5.46), ('NE2', 'HIS', 'NE2', 'HIS', 5.23)], [('CB', 'HIS', 'CB', 'HIS', 8.51), ('CB', 'HIS', 'CG', 'HIS', 8.27), ('CB', 'HIS', 'ND1', 'HIS', 9.41), ('CB', 'HIS', 'CD2', 'HIS', 7.31), ('CB', 'HIS', 'CE1', 'HIS', 9.31), ('CB', 'HIS', 'NE2', 'HIS', 8.11)], [('CG', 'HIS', 'CB', 'HIS', 7.87), ('CG', 'HIS', 'CG', 'HIS', 7.32), ('CG', 'HIS', 'ND1', 'HIS', 8.32), ('CG', 'HIS', 'CD2', 'HIS', 6.2), ('CG', 'HIS', 'CE1', 'HIS', 8.04), ('CG', 'HIS', 'NE2', 'HIS', 6.79)], [('ND1', 'HIS', 'CB', 'HIS', 7.83), ('ND1', 'HIS', 'CG', 'HIS', 7.14), ('ND1', 'HIS', 'ND1', 'HIS', 7.95), ('ND1', 'HIS', 'CD2', 'HIS', 6.04), ('ND1', 'HIS', 'CE1', 'HIS', 7.57), ('ND1', 'HIS', 'NE2', 'HIS', 6.41)], [('CD2', 'HIS', 'CB', 'HIS', 7.72), ('CD2', 'HIS', 'CG', 'HIS', 6.98), ('CD2', 'HIS', 'ND1', 'HIS', 7.87), ('CD2', 'HIS', 'CD2', 'HIS', 5.72), ('CD2', 'HIS', 'CE1', 'HIS', 7.45), ('CD2', 'HIS', 'NE2', 'HIS', 6.15)], [('CE1', 'HIS', 'CB', 'HIS', 7.69), ('CE1', 'HIS', 'CG', 'HIS', 6.69), ('CE1', 'HIS', 'ND1', 'HIS', 7.27), ('CE1', 'HIS', 'CD2', 'HIS', 5.47), ('CE1', 'HIS', 'CE1', 'HIS', 6.65), ('CE1', 'HIS', 'NE2', 'HIS', 5.46)], [('NE2', 'HIS', 'CB', 'HIS', 7.6), ('NE2', 'HIS', 'CG', 'HIS', 6.57), ('NE2', 'HIS', 'ND1', 'HIS', 7.19), ('NE2', 'HIS', 'CD2', 'HIS', 5.22), ('NE2', 'HIS', 'CE1', 'HIS', 6.54), ('NE2', 'HIS', 'NE2', 'HIS', 5.23)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_GLN, d, 'A_1e2a_2_7_1_69')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLN_HISI, d, 'A_1e2a_2_7_1_69')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASP, d, 'A_1e2a_2_7_1_69')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_GLN, d, 'A_1e2a_2_7_1_69')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_HIS, d, 'A_1e2a_2_7_1_69')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_GLN' :  match1,
		'GLN_HISI' :  match2,
		'HIS_ASP' :  match3,
		'HIS_GLN' :  match4,
		'HIS_HIS' :  match5}