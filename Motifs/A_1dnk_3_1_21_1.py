'''
FUNC:A_1dnk_3_1_21_1
PDB:1dnk
EC:3.1.21.1
RESI:glu,his,asp,his
LOCI:a-78,134,212,252;
'''
import motifFunctions as cmd
GLU_HISI = { 
	'distances':
		[[8.36, 8.31, 7.36, 9.5, 8.16, 9.39], [8.45, 8.04, 6.87, 9.04, 7.38, 8.67], [7.17, 6.59, 5.38, 7.54, 5.87, 7.16], [6.13, 5.77, 4.74, 6.91, 5.6, 6.79], [7.57, 6.7, 5.39, 7.38, 5.46, 6.74]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HISI', 8.36), ('CB', 'GLU', 'CG', 'HISI', 8.31), ('CB', 'GLU', 'ND1', 'HISI', 7.36), ('CB', 'GLU', 'CD2', 'HISI', 9.5), ('CB', 'GLU', 'CE1', 'HISI', 8.16), ('CB', 'GLU', 'NE2', 'HISI', 9.39)], [('CG', 'GLU', 'CB', 'HISI', 8.45), ('CG', 'GLU', 'CG', 'HISI', 8.04), ('CG', 'GLU', 'ND1', 'HISI', 6.87), ('CG', 'GLU', 'CD2', 'HISI', 9.04), ('CG', 'GLU', 'CE1', 'HISI', 7.38), ('CG', 'GLU', 'NE2', 'HISI', 8.67)], [('CD', 'GLU', 'CB', 'HISI', 7.17), ('CD', 'GLU', 'CG', 'HISI', 6.59), ('CD', 'GLU', 'ND1', 'HISI', 5.38), ('CD', 'GLU', 'CD2', 'HISI', 7.54), ('CD', 'GLU', 'CE1', 'HISI', 5.87), ('CD', 'GLU', 'NE2', 'HISI', 7.16)], [('OE1', 'GLU', 'CB', 'HISI', 6.13), ('OE1', 'GLU', 'CG', 'HISI', 5.77), ('OE1', 'GLU', 'ND1', 'HISI', 4.74), ('OE1', 'GLU', 'CD2', 'HISI', 6.91), ('OE1', 'GLU', 'CE1', 'HISI', 5.6), ('OE1', 'GLU', 'NE2', 'HISI', 6.79)], [('OE2', 'GLU', 'CB', 'HISI', 7.57), ('OE2', 'GLU', 'CG', 'HISI', 6.7), ('OE2', 'GLU', 'ND1', 'HISI', 5.39), ('OE2', 'GLU', 'CD2', 'HISI', 7.38), ('OE2', 'GLU', 'CE1', 'HISI', 5.46), ('OE2', 'GLU', 'NE2', 'HISI', 6.74)]]}
HIS_GLU = { 
	'distances':
		[[15.46, 14.85, 13.65, 13.22, 13.38], [14.87, 14.17, 12.9, 12.52, 12.53], [15.13, 14.46, 13.1, 12.66, 12.73], [14.18, 13.36, 12.1, 11.84, 11.62], [14.68, 13.92, 12.52, 12.15, 12.05], [14.09, 13.23, 11.88, 11.63, 11.33], [8.36, 8.45, 7.17, 6.13, 7.57], [8.31, 8.04, 6.59, 5.77, 6.7], [7.36, 6.87, 5.38, 4.74, 5.39], [9.5, 9.04, 7.54, 6.91, 7.38], [8.16, 7.38, 5.87, 5.6, 5.46], [9.39, 8.67, 7.16, 6.79, 6.74]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 15.46), ('CB', 'HIS', 'CG', 'GLU', 14.85), ('CB', 'HIS', 'CD', 'GLU', 13.65), ('CB', 'HIS', 'OE1', 'GLU', 13.22), ('CB', 'HIS', 'OE2', 'GLU', 13.38)], [('CG', 'HIS', 'CB', 'GLU', 14.87), ('CG', 'HIS', 'CG', 'GLU', 14.17), ('CG', 'HIS', 'CD', 'GLU', 12.9), ('CG', 'HIS', 'OE1', 'GLU', 12.52), ('CG', 'HIS', 'OE2', 'GLU', 12.53)], [('ND1', 'HIS', 'CB', 'GLU', 15.13), ('ND1', 'HIS', 'CG', 'GLU', 14.46), ('ND1', 'HIS', 'CD', 'GLU', 13.1), ('ND1', 'HIS', 'OE1', 'GLU', 12.66), ('ND1', 'HIS', 'OE2', 'GLU', 12.73)], [('CD2', 'HIS', 'CB', 'GLU', 14.18), ('CD2', 'HIS', 'CG', 'GLU', 13.36), ('CD2', 'HIS', 'CD', 'GLU', 12.1), ('CD2', 'HIS', 'OE1', 'GLU', 11.84), ('CD2', 'HIS', 'OE2', 'GLU', 11.62)], [('CE1', 'HIS', 'CB', 'GLU', 14.68), ('CE1', 'HIS', 'CG', 'GLU', 13.92), ('CE1', 'HIS', 'CD', 'GLU', 12.52), ('CE1', 'HIS', 'OE1', 'GLU', 12.15), ('CE1', 'HIS', 'OE2', 'GLU', 12.05)], [('NE2', 'HIS', 'CB', 'GLU', 14.09), ('NE2', 'HIS', 'CG', 'GLU', 13.23), ('NE2', 'HIS', 'CD', 'GLU', 11.88), ('NE2', 'HIS', 'OE1', 'GLU', 11.63), ('NE2', 'HIS', 'OE2', 'GLU', 11.33)], [('CB', 'HIS', 'CB', 'GLU', 8.36), ('CB', 'HIS', 'CG', 'GLU', 8.45), ('CB', 'HIS', 'CD', 'GLU', 7.17), ('CB', 'HIS', 'OE1', 'GLU', 6.13), ('CB', 'HIS', 'OE2', 'GLU', 7.57)], [('CG', 'HIS', 'CB', 'GLU', 8.31), ('CG', 'HIS', 'CG', 'GLU', 8.04), ('CG', 'HIS', 'CD', 'GLU', 6.59), ('CG', 'HIS', 'OE1', 'GLU', 5.77), ('CG', 'HIS', 'OE2', 'GLU', 6.7)], [('ND1', 'HIS', 'CB', 'GLU', 7.36), ('ND1', 'HIS', 'CG', 'GLU', 6.87), ('ND1', 'HIS', 'CD', 'GLU', 5.38), ('ND1', 'HIS', 'OE1', 'GLU', 4.74), ('ND1', 'HIS', 'OE2', 'GLU', 5.39)], [('CD2', 'HIS', 'CB', 'GLU', 9.5), ('CD2', 'HIS', 'CG', 'GLU', 9.04), ('CD2', 'HIS', 'CD', 'GLU', 7.54), ('CD2', 'HIS', 'OE1', 'GLU', 6.91), ('CD2', 'HIS', 'OE2', 'GLU', 7.38)], [('CE1', 'HIS', 'CB', 'GLU', 8.16), ('CE1', 'HIS', 'CG', 'GLU', 7.38), ('CE1', 'HIS', 'CD', 'GLU', 5.87), ('CE1', 'HIS', 'OE1', 'GLU', 5.6), ('CE1', 'HIS', 'OE2', 'GLU', 5.46)], [('NE2', 'HIS', 'CB', 'GLU', 9.39), ('NE2', 'HIS', 'CG', 'GLU', 8.67), ('NE2', 'HIS', 'CD', 'GLU', 7.16), ('NE2', 'HIS', 'OE1', 'GLU', 6.79), ('NE2', 'HIS', 'OE2', 'GLU', 6.74)]]}
ASP_HIS = { 
	'distances':
		[[7.94, 7.92, 7.03, 9.03, 7.81, 8.95], [6.62, 6.47, 5.58, 7.53, 6.39, 7.47], [6.11, 5.79, 4.75, 6.86, 5.58, 6.73], [6.47, 6.33, 5.65, 7.29, 6.41, 7.32], [11.61, 11.51, 12.41, 10.78, 12.31, 11.35], [10.8, 10.52, 11.3, 9.74, 11.1, 10.17], [11.34, 10.87, 11.56, 9.95, 11.19, 10.21], [9.83, 9.59, 10.34, 8.93, 10.24, 9.41]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 7.94), ('CB', 'ASP', 'CG', 'HIS', 7.92), ('CB', 'ASP', 'ND1', 'HIS', 7.03), ('CB', 'ASP', 'CD2', 'HIS', 9.03), ('CB', 'ASP', 'CE1', 'HIS', 7.81), ('CB', 'ASP', 'NE2', 'HIS', 8.95)], [('CG', 'ASP', 'CB', 'HIS', 6.62), ('CG', 'ASP', 'CG', 'HIS', 6.47), ('CG', 'ASP', 'ND1', 'HIS', 5.58), ('CG', 'ASP', 'CD2', 'HIS', 7.53), ('CG', 'ASP', 'CE1', 'HIS', 6.39), ('CG', 'ASP', 'NE2', 'HIS', 7.47)], [('OD1', 'ASP', 'CB', 'HIS', 6.11), ('OD1', 'ASP', 'CG', 'HIS', 5.79), ('OD1', 'ASP', 'ND1', 'HIS', 4.75), ('OD1', 'ASP', 'CD2', 'HIS', 6.86), ('OD1', 'ASP', 'CE1', 'HIS', 5.58), ('OD1', 'ASP', 'NE2', 'HIS', 6.73)], [('OD2', 'ASP', 'CB', 'HIS', 6.47), ('OD2', 'ASP', 'CG', 'HIS', 6.33), ('OD2', 'ASP', 'ND1', 'HIS', 5.65), ('OD2', 'ASP', 'CD2', 'HIS', 7.29), ('OD2', 'ASP', 'CE1', 'HIS', 6.41), ('OD2', 'ASP', 'NE2', 'HIS', 7.32)], [('CB', 'ASP', 'CB', 'HIS', 11.61), ('CB', 'ASP', 'CG', 'HIS', 11.51), ('CB', 'ASP', 'ND1', 'HIS', 12.41), ('CB', 'ASP', 'CD2', 'HIS', 10.78), ('CB', 'ASP', 'CE1', 'HIS', 12.31), ('CB', 'ASP', 'NE2', 'HIS', 11.35)], [('CG', 'ASP', 'CB', 'HIS', 10.8), ('CG', 'ASP', 'CG', 'HIS', 10.52), ('CG', 'ASP', 'ND1', 'HIS', 11.3), ('CG', 'ASP', 'CD2', 'HIS', 9.74), ('CG', 'ASP', 'CE1', 'HIS', 11.1), ('CG', 'ASP', 'NE2', 'HIS', 10.17)], [('OD1', 'ASP', 'CB', 'HIS', 11.34), ('OD1', 'ASP', 'CG', 'HIS', 10.87), ('OD1', 'ASP', 'ND1', 'HIS', 11.56), ('OD1', 'ASP', 'CD2', 'HIS', 9.95), ('OD1', 'ASP', 'CE1', 'HIS', 11.19), ('OD1', 'ASP', 'NE2', 'HIS', 10.21)], [('OD2', 'ASP', 'CB', 'HIS', 9.83), ('OD2', 'ASP', 'CG', 'HIS', 9.59), ('OD2', 'ASP', 'ND1', 'HIS', 10.34), ('OD2', 'ASP', 'CD2', 'HIS', 8.93), ('OD2', 'ASP', 'CE1', 'HIS', 10.24), ('OD2', 'ASP', 'NE2', 'HIS', 9.41)]]}
HIS_HIS = { 
	'distances':
		[[12.0, 11.21, 11.34, 10.51, 10.81, 10.27], [11.21, 10.3, 10.44, 9.46, 9.79, 9.14], [10.87, 10.02, 10.35, 9.04, 9.7, 8.85], [10.92, 9.85, 9.82, 8.98, 9.02, 8.44], [10.43, 9.44, 9.74, 8.34, 8.96, 8.03], [10.45, 9.31, 9.38, 8.28, 8.49, 7.72], [12.0, 11.21, 10.87, 10.92, 10.43, 10.45], [11.21, 10.3, 10.02, 9.85, 9.44, 9.31], [11.34, 10.44, 10.35, 9.82, 9.74, 9.38], [10.51, 9.46, 9.04, 8.98, 8.34, 8.28], [10.81, 9.79, 9.7, 9.02, 8.96, 8.49], [10.27, 9.14, 8.85, 8.44, 8.03, 7.72]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 12.0), ('CB', 'HIS', 'CG', 'HIS', 11.21), ('CB', 'HIS', 'ND1', 'HIS', 11.34), ('CB', 'HIS', 'CD2', 'HIS', 10.51), ('CB', 'HIS', 'CE1', 'HIS', 10.81), ('CB', 'HIS', 'NE2', 'HIS', 10.27)], [('CG', 'HIS', 'CB', 'HIS', 11.21), ('CG', 'HIS', 'CG', 'HIS', 10.3), ('CG', 'HIS', 'ND1', 'HIS', 10.44), ('CG', 'HIS', 'CD2', 'HIS', 9.46), ('CG', 'HIS', 'CE1', 'HIS', 9.79), ('CG', 'HIS', 'NE2', 'HIS', 9.14)], [('ND1', 'HIS', 'CB', 'HIS', 10.87), ('ND1', 'HIS', 'CG', 'HIS', 10.02), ('ND1', 'HIS', 'ND1', 'HIS', 10.35), ('ND1', 'HIS', 'CD2', 'HIS', 9.04), ('ND1', 'HIS', 'CE1', 'HIS', 9.7), ('ND1', 'HIS', 'NE2', 'HIS', 8.85)], [('CD2', 'HIS', 'CB', 'HIS', 10.92), ('CD2', 'HIS', 'CG', 'HIS', 9.85), ('CD2', 'HIS', 'ND1', 'HIS', 9.82), ('CD2', 'HIS', 'CD2', 'HIS', 8.98), ('CD2', 'HIS', 'CE1', 'HIS', 9.02), ('CD2', 'HIS', 'NE2', 'HIS', 8.44)], [('CE1', 'HIS', 'CB', 'HIS', 10.43), ('CE1', 'HIS', 'CG', 'HIS', 9.44), ('CE1', 'HIS', 'ND1', 'HIS', 9.74), ('CE1', 'HIS', 'CD2', 'HIS', 8.34), ('CE1', 'HIS', 'CE1', 'HIS', 8.96), ('CE1', 'HIS', 'NE2', 'HIS', 8.03)], [('NE2', 'HIS', 'CB', 'HIS', 10.45), ('NE2', 'HIS', 'CG', 'HIS', 9.31), ('NE2', 'HIS', 'ND1', 'HIS', 9.38), ('NE2', 'HIS', 'CD2', 'HIS', 8.28), ('NE2', 'HIS', 'CE1', 'HIS', 8.49), ('NE2', 'HIS', 'NE2', 'HIS', 7.72)], [('CB', 'HIS', 'CB', 'HIS', 12.0), ('CB', 'HIS', 'CG', 'HIS', 11.21), ('CB', 'HIS', 'ND1', 'HIS', 10.87), ('CB', 'HIS', 'CD2', 'HIS', 10.92), ('CB', 'HIS', 'CE1', 'HIS', 10.43), ('CB', 'HIS', 'NE2', 'HIS', 10.45)], [('CG', 'HIS', 'CB', 'HIS', 11.21), ('CG', 'HIS', 'CG', 'HIS', 10.3), ('CG', 'HIS', 'ND1', 'HIS', 10.02), ('CG', 'HIS', 'CD2', 'HIS', 9.85), ('CG', 'HIS', 'CE1', 'HIS', 9.44), ('CG', 'HIS', 'NE2', 'HIS', 9.31)], [('ND1', 'HIS', 'CB', 'HIS', 11.34), ('ND1', 'HIS', 'CG', 'HIS', 10.44), ('ND1', 'HIS', 'ND1', 'HIS', 10.35), ('ND1', 'HIS', 'CD2', 'HIS', 9.82), ('ND1', 'HIS', 'CE1', 'HIS', 9.74), ('ND1', 'HIS', 'NE2', 'HIS', 9.38)], [('CD2', 'HIS', 'CB', 'HIS', 10.51), ('CD2', 'HIS', 'CG', 'HIS', 9.46), ('CD2', 'HIS', 'ND1', 'HIS', 9.04), ('CD2', 'HIS', 'CD2', 'HIS', 8.98), ('CD2', 'HIS', 'CE1', 'HIS', 8.34), ('CD2', 'HIS', 'NE2', 'HIS', 8.28)], [('CE1', 'HIS', 'CB', 'HIS', 10.81), ('CE1', 'HIS', 'CG', 'HIS', 9.79), ('CE1', 'HIS', 'ND1', 'HIS', 9.7), ('CE1', 'HIS', 'CD2', 'HIS', 9.02), ('CE1', 'HIS', 'CE1', 'HIS', 8.96), ('CE1', 'HIS', 'NE2', 'HIS', 8.49)], [('NE2', 'HIS', 'CB', 'HIS', 10.27), ('NE2', 'HIS', 'CG', 'HIS', 9.14), ('NE2', 'HIS', 'ND1', 'HIS', 8.85), ('NE2', 'HIS', 'CD2', 'HIS', 8.44), ('NE2', 'HIS', 'CE1', 'HIS', 8.03), ('NE2', 'HIS', 'NE2', 'HIS', 7.72)]]}
ASP_GLU = { 
	'distances':
		[[17.11, 16.9, 15.53, 14.7, 15.53], [16.05, 15.74, 14.37, 13.61, 14.3], [16.44, 16.01, 14.61, 13.95, 14.42], [14.94, 14.69, 13.35, 12.55, 13.34]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 17.11), ('CB', 'ASP', 'CG', 'GLU', 16.9), ('CB', 'ASP', 'CD', 'GLU', 15.53), ('CB', 'ASP', 'OE1', 'GLU', 14.7), ('CB', 'ASP', 'OE2', 'GLU', 15.53)], [('CG', 'ASP', 'CB', 'GLU', 16.05), ('CG', 'ASP', 'CG', 'GLU', 15.74), ('CG', 'ASP', 'CD', 'GLU', 14.37), ('CG', 'ASP', 'OE1', 'GLU', 13.61), ('CG', 'ASP', 'OE2', 'GLU', 14.3)], [('OD1', 'ASP', 'CB', 'GLU', 16.44), ('OD1', 'ASP', 'CG', 'GLU', 16.01), ('OD1', 'ASP', 'CD', 'GLU', 14.61), ('OD1', 'ASP', 'OE1', 'GLU', 13.95), ('OD1', 'ASP', 'OE2', 'GLU', 14.42)], [('OD2', 'ASP', 'CB', 'GLU', 14.94), ('OD2', 'ASP', 'CG', 'GLU', 14.69), ('OD2', 'ASP', 'CD', 'GLU', 13.35), ('OD2', 'ASP', 'OE1', 'GLU', 12.55), ('OD2', 'ASP', 'OE2', 'GLU', 13.34)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_HISI, d, 'A_1dnk_3_1_21_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_GLU, d, 'A_1dnk_3_1_21_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_HIS, d, 'A_1dnk_3_1_21_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_HIS, d, 'A_1dnk_3_1_21_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_GLU, d, 'A_1dnk_3_1_21_1')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_HISI' :  match1,
		'HIS_GLU' :  match2,
		'ASP_HIS' :  match3,
		'HIS_HIS' :  match4,
		'ASP_GLU' :  match5}