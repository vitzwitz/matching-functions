'''
FUNC:P_1pyd_4_1_1_1
PDB:1pyd
EC:4.1.1.1
RESI:asp,his,his,glu
LOCI:a-28,114,115,477;
'''
import motifFunctions as cmd
GLU_HISI = { 
	'distances':
		[[16.42, 15.01, 14.61, 14.03, 13.35, 12.97], [15.27, 13.91, 13.63, 12.87, 12.41, 11.9], [14.78, 13.46, 13.18, 12.51, 12.02, 11.57], [15.65, 14.37, 14.07, 13.47, 12.96, 12.56], [13.56, 12.25, 11.97, 11.31, 10.82, 10.38]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HISI', 16.42), ('CB', 'GLU', 'CG', 'HISI', 15.01), ('CB', 'GLU', 'ND1', 'HISI', 14.61), ('CB', 'GLU', 'CD2', 'HISI', 14.03), ('CB', 'GLU', 'CE1', 'HISI', 13.35), ('CB', 'GLU', 'NE2', 'HISI', 12.97)], [('CG', 'GLU', 'CB', 'HISI', 15.27), ('CG', 'GLU', 'CG', 'HISI', 13.91), ('CG', 'GLU', 'ND1', 'HISI', 13.63), ('CG', 'GLU', 'CD2', 'HISI', 12.87), ('CG', 'GLU', 'CE1', 'HISI', 12.41), ('CG', 'GLU', 'NE2', 'HISI', 11.9)], [('CD', 'GLU', 'CB', 'HISI', 14.78), ('CD', 'GLU', 'CG', 'HISI', 13.46), ('CD', 'GLU', 'ND1', 'HISI', 13.18), ('CD', 'GLU', 'CD2', 'HISI', 12.51), ('CD', 'GLU', 'CE1', 'HISI', 12.02), ('CD', 'GLU', 'NE2', 'HISI', 11.57)], [('OE1', 'GLU', 'CB', 'HISI', 15.65), ('OE1', 'GLU', 'CG', 'HISI', 14.37), ('OE1', 'GLU', 'ND1', 'HISI', 14.07), ('OE1', 'GLU', 'CD2', 'HISI', 13.47), ('OE1', 'GLU', 'CE1', 'HISI', 12.96), ('OE1', 'GLU', 'NE2', 'HISI', 12.56)], [('OE2', 'GLU', 'CB', 'HISI', 13.56), ('OE2', 'GLU', 'CG', 'HISI', 12.25), ('OE2', 'GLU', 'ND1', 'HISI', 11.97), ('OE2', 'GLU', 'CD2', 'HISI', 11.31), ('OE2', 'GLU', 'CE1', 'HISI', 10.82), ('OE2', 'GLU', 'NE2', 'HISI', 10.38)]]}
HIS_GLU = { 
	'distances':
		[[16.97, 15.94, 16.03, 17.16, 14.94], [16.13, 15.22, 15.38, 16.52, 14.31], [16.58, 15.76, 16.05, 17.21, 15.03], [15.05, 14.18, 14.29, 15.41, 13.21], [15.85, 15.14, 15.46, 16.62, 14.48], [14.89, 14.16, 14.38, 15.52, 13.36], [16.42, 15.27, 14.78, 15.65, 13.56], [15.01, 13.91, 13.46, 14.37, 12.25], [14.61, 13.63, 13.18, 14.07, 11.97], [14.03, 12.87, 12.51, 13.47, 11.31], [13.35, 12.41, 12.02, 12.96, 10.82], [12.97, 11.9, 11.57, 12.56, 10.38]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 16.97), ('CB', 'HIS', 'CG', 'GLU', 15.94), ('CB', 'HIS', 'CD', 'GLU', 16.03), ('CB', 'HIS', 'OE1', 'GLU', 17.16), ('CB', 'HIS', 'OE2', 'GLU', 14.94)], [('CG', 'HIS', 'CB', 'GLU', 16.13), ('CG', 'HIS', 'CG', 'GLU', 15.22), ('CG', 'HIS', 'CD', 'GLU', 15.38), ('CG', 'HIS', 'OE1', 'GLU', 16.52), ('CG', 'HIS', 'OE2', 'GLU', 14.31)], [('ND1', 'HIS', 'CB', 'GLU', 16.58), ('ND1', 'HIS', 'CG', 'GLU', 15.76), ('ND1', 'HIS', 'CD', 'GLU', 16.05), ('ND1', 'HIS', 'OE1', 'GLU', 17.21), ('ND1', 'HIS', 'OE2', 'GLU', 15.03)], [('CD2', 'HIS', 'CB', 'GLU', 15.05), ('CD2', 'HIS', 'CG', 'GLU', 14.18), ('CD2', 'HIS', 'CD', 'GLU', 14.29), ('CD2', 'HIS', 'OE1', 'GLU', 15.41), ('CD2', 'HIS', 'OE2', 'GLU', 13.21)], [('CE1', 'HIS', 'CB', 'GLU', 15.85), ('CE1', 'HIS', 'CG', 'GLU', 15.14), ('CE1', 'HIS', 'CD', 'GLU', 15.46), ('CE1', 'HIS', 'OE1', 'GLU', 16.62), ('CE1', 'HIS', 'OE2', 'GLU', 14.48)], [('NE2', 'HIS', 'CB', 'GLU', 14.89), ('NE2', 'HIS', 'CG', 'GLU', 14.16), ('NE2', 'HIS', 'CD', 'GLU', 14.38), ('NE2', 'HIS', 'OE1', 'GLU', 15.52), ('NE2', 'HIS', 'OE2', 'GLU', 13.36)], [('CB', 'HIS', 'CB', 'GLU', 16.42), ('CB', 'HIS', 'CG', 'GLU', 15.27), ('CB', 'HIS', 'CD', 'GLU', 14.78), ('CB', 'HIS', 'OE1', 'GLU', 15.65), ('CB', 'HIS', 'OE2', 'GLU', 13.56)], [('CG', 'HIS', 'CB', 'GLU', 15.01), ('CG', 'HIS', 'CG', 'GLU', 13.91), ('CG', 'HIS', 'CD', 'GLU', 13.46), ('CG', 'HIS', 'OE1', 'GLU', 14.37), ('CG', 'HIS', 'OE2', 'GLU', 12.25)], [('ND1', 'HIS', 'CB', 'GLU', 14.61), ('ND1', 'HIS', 'CG', 'GLU', 13.63), ('ND1', 'HIS', 'CD', 'GLU', 13.18), ('ND1', 'HIS', 'OE1', 'GLU', 14.07), ('ND1', 'HIS', 'OE2', 'GLU', 11.97)], [('CD2', 'HIS', 'CB', 'GLU', 14.03), ('CD2', 'HIS', 'CG', 'GLU', 12.87), ('CD2', 'HIS', 'CD', 'GLU', 12.51), ('CD2', 'HIS', 'OE1', 'GLU', 13.47), ('CD2', 'HIS', 'OE2', 'GLU', 11.31)], [('CE1', 'HIS', 'CB', 'GLU', 13.35), ('CE1', 'HIS', 'CG', 'GLU', 12.41), ('CE1', 'HIS', 'CD', 'GLU', 12.02), ('CE1', 'HIS', 'OE1', 'GLU', 12.96), ('CE1', 'HIS', 'OE2', 'GLU', 10.82)], [('NE2', 'HIS', 'CB', 'GLU', 12.97), ('NE2', 'HIS', 'CG', 'GLU', 11.9), ('NE2', 'HIS', 'CD', 'GLU', 11.57), ('NE2', 'HIS', 'OE1', 'GLU', 12.56), ('NE2', 'HIS', 'OE2', 'GLU', 10.38)]]}
ASP_HIS = { 
	'distances':
		[[9.92, 9.81, 10.81, 9.15, 10.83, 9.87], [9.38, 9.0, 9.88, 8.18, 9.72, 8.71], [10.36, 9.81, 10.57, 8.9, 10.23, 9.22], [8.15, 7.75, 8.69, 6.92, 8.58, 7.55], [9.27, 8.19, 8.67, 6.88, 7.82, 6.63], [9.18, 7.89, 8.09, 6.61, 7.05, 5.98], [10.21, 8.85, 8.86, 7.63, 7.7, 6.81], [8.23, 6.92, 7.13, 5.65, 6.14, 5.03]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 9.92), ('CB', 'ASP', 'CG', 'HIS', 9.81), ('CB', 'ASP', 'ND1', 'HIS', 10.81), ('CB', 'ASP', 'CD2', 'HIS', 9.15), ('CB', 'ASP', 'CE1', 'HIS', 10.83), ('CB', 'ASP', 'NE2', 'HIS', 9.87)], [('CG', 'ASP', 'CB', 'HIS', 9.38), ('CG', 'ASP', 'CG', 'HIS', 9.0), ('CG', 'ASP', 'ND1', 'HIS', 9.88), ('CG', 'ASP', 'CD2', 'HIS', 8.18), ('CG', 'ASP', 'CE1', 'HIS', 9.72), ('CG', 'ASP', 'NE2', 'HIS', 8.71)], [('OD1', 'ASP', 'CB', 'HIS', 10.36), ('OD1', 'ASP', 'CG', 'HIS', 9.81), ('OD1', 'ASP', 'ND1', 'HIS', 10.57), ('OD1', 'ASP', 'CD2', 'HIS', 8.9), ('OD1', 'ASP', 'CE1', 'HIS', 10.23), ('OD1', 'ASP', 'NE2', 'HIS', 9.22)], [('OD2', 'ASP', 'CB', 'HIS', 8.15), ('OD2', 'ASP', 'CG', 'HIS', 7.75), ('OD2', 'ASP', 'ND1', 'HIS', 8.69), ('OD2', 'ASP', 'CD2', 'HIS', 6.92), ('OD2', 'ASP', 'CE1', 'HIS', 8.58), ('OD2', 'ASP', 'NE2', 'HIS', 7.55)], [('CB', 'ASP', 'CB', 'HIS', 9.27), ('CB', 'ASP', 'CG', 'HIS', 8.19), ('CB', 'ASP', 'ND1', 'HIS', 8.67), ('CB', 'ASP', 'CD2', 'HIS', 6.88), ('CB', 'ASP', 'CE1', 'HIS', 7.82), ('CB', 'ASP', 'NE2', 'HIS', 6.63)], [('CG', 'ASP', 'CB', 'HIS', 9.18), ('CG', 'ASP', 'CG', 'HIS', 7.89), ('CG', 'ASP', 'ND1', 'HIS', 8.09), ('CG', 'ASP', 'CD2', 'HIS', 6.61), ('CG', 'ASP', 'CE1', 'HIS', 7.05), ('CG', 'ASP', 'NE2', 'HIS', 5.98)], [('OD1', 'ASP', 'CB', 'HIS', 10.21), ('OD1', 'ASP', 'CG', 'HIS', 8.85), ('OD1', 'ASP', 'ND1', 'HIS', 8.86), ('OD1', 'ASP', 'CD2', 'HIS', 7.63), ('OD1', 'ASP', 'CE1', 'HIS', 7.7), ('OD1', 'ASP', 'NE2', 'HIS', 6.81)], [('OD2', 'ASP', 'CB', 'HIS', 8.23), ('OD2', 'ASP', 'CG', 'HIS', 6.92), ('OD2', 'ASP', 'ND1', 'HIS', 7.13), ('OD2', 'ASP', 'CD2', 'HIS', 5.65), ('OD2', 'ASP', 'CE1', 'HIS', 6.14), ('OD2', 'ASP', 'NE2', 'HIS', 5.03)]]}
HIS_HIS = { 
	'distances':
		[[7.6, 7.36, 7.84, 7.18, 8.01, 7.63], [8.07, 7.48, 7.62, 7.25, 7.55, 7.31], [9.42, 8.82, 8.81, 8.58, 8.66, 8.51], [7.7, 6.83, 6.72, 6.55, 6.44, 6.32], [9.87, 9.06, 8.81, 8.8, 8.47, 8.45], [8.95, 7.99, 7.64, 7.71, 7.19, 7.23], [7.6, 8.07, 9.42, 7.7, 9.87, 8.95], [7.36, 7.48, 8.82, 6.83, 9.06, 7.99], [7.84, 7.62, 8.81, 6.72, 8.81, 7.64], [7.18, 7.25, 8.58, 6.55, 8.8, 7.71], [8.01, 7.55, 8.66, 6.44, 8.47, 7.19], [7.63, 7.31, 8.51, 6.32, 8.45, 7.23]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 7.6), ('CB', 'HIS', 'CG', 'HIS', 7.36), ('CB', 'HIS', 'ND1', 'HIS', 7.84), ('CB', 'HIS', 'CD2', 'HIS', 7.18), ('CB', 'HIS', 'CE1', 'HIS', 8.01), ('CB', 'HIS', 'NE2', 'HIS', 7.63)], [('CG', 'HIS', 'CB', 'HIS', 8.07), ('CG', 'HIS', 'CG', 'HIS', 7.48), ('CG', 'HIS', 'ND1', 'HIS', 7.62), ('CG', 'HIS', 'CD2', 'HIS', 7.25), ('CG', 'HIS', 'CE1', 'HIS', 7.55), ('CG', 'HIS', 'NE2', 'HIS', 7.31)], [('ND1', 'HIS', 'CB', 'HIS', 9.42), ('ND1', 'HIS', 'CG', 'HIS', 8.82), ('ND1', 'HIS', 'ND1', 'HIS', 8.81), ('ND1', 'HIS', 'CD2', 'HIS', 8.58), ('ND1', 'HIS', 'CE1', 'HIS', 8.66), ('ND1', 'HIS', 'NE2', 'HIS', 8.51)], [('CD2', 'HIS', 'CB', 'HIS', 7.7), ('CD2', 'HIS', 'CG', 'HIS', 6.83), ('CD2', 'HIS', 'ND1', 'HIS', 6.72), ('CD2', 'HIS', 'CD2', 'HIS', 6.55), ('CD2', 'HIS', 'CE1', 'HIS', 6.44), ('CD2', 'HIS', 'NE2', 'HIS', 6.32)], [('CE1', 'HIS', 'CB', 'HIS', 9.87), ('CE1', 'HIS', 'CG', 'HIS', 9.06), ('CE1', 'HIS', 'ND1', 'HIS', 8.81), ('CE1', 'HIS', 'CD2', 'HIS', 8.8), ('CE1', 'HIS', 'CE1', 'HIS', 8.47), ('CE1', 'HIS', 'NE2', 'HIS', 8.45)], [('NE2', 'HIS', 'CB', 'HIS', 8.95), ('NE2', 'HIS', 'CG', 'HIS', 7.99), ('NE2', 'HIS', 'ND1', 'HIS', 7.64), ('NE2', 'HIS', 'CD2', 'HIS', 7.71), ('NE2', 'HIS', 'CE1', 'HIS', 7.19), ('NE2', 'HIS', 'NE2', 'HIS', 7.23)], [('CB', 'HIS', 'CB', 'HIS', 7.6), ('CB', 'HIS', 'CG', 'HIS', 8.07), ('CB', 'HIS', 'ND1', 'HIS', 9.42), ('CB', 'HIS', 'CD2', 'HIS', 7.7), ('CB', 'HIS', 'CE1', 'HIS', 9.87), ('CB', 'HIS', 'NE2', 'HIS', 8.95)], [('CG', 'HIS', 'CB', 'HIS', 7.36), ('CG', 'HIS', 'CG', 'HIS', 7.48), ('CG', 'HIS', 'ND1', 'HIS', 8.82), ('CG', 'HIS', 'CD2', 'HIS', 6.83), ('CG', 'HIS', 'CE1', 'HIS', 9.06), ('CG', 'HIS', 'NE2', 'HIS', 7.99)], [('ND1', 'HIS', 'CB', 'HIS', 7.84), ('ND1', 'HIS', 'CG', 'HIS', 7.62), ('ND1', 'HIS', 'ND1', 'HIS', 8.81), ('ND1', 'HIS', 'CD2', 'HIS', 6.72), ('ND1', 'HIS', 'CE1', 'HIS', 8.81), ('ND1', 'HIS', 'NE2', 'HIS', 7.64)], [('CD2', 'HIS', 'CB', 'HIS', 7.18), ('CD2', 'HIS', 'CG', 'HIS', 7.25), ('CD2', 'HIS', 'ND1', 'HIS', 8.58), ('CD2', 'HIS', 'CD2', 'HIS', 6.55), ('CD2', 'HIS', 'CE1', 'HIS', 8.8), ('CD2', 'HIS', 'NE2', 'HIS', 7.71)], [('CE1', 'HIS', 'CB', 'HIS', 8.01), ('CE1', 'HIS', 'CG', 'HIS', 7.55), ('CE1', 'HIS', 'ND1', 'HIS', 8.66), ('CE1', 'HIS', 'CD2', 'HIS', 6.44), ('CE1', 'HIS', 'CE1', 'HIS', 8.47), ('CE1', 'HIS', 'NE2', 'HIS', 7.19)], [('NE2', 'HIS', 'CB', 'HIS', 7.63), ('NE2', 'HIS', 'CG', 'HIS', 7.31), ('NE2', 'HIS', 'ND1', 'HIS', 8.51), ('NE2', 'HIS', 'CD2', 'HIS', 6.32), ('NE2', 'HIS', 'CE1', 'HIS', 8.45), ('NE2', 'HIS', 'NE2', 'HIS', 7.23)]]}
ASP_GLU = { 
	'distances':
		[[10.82, 9.41, 9.31, 10.33, 8.3], [10.33, 9.07, 9.09, 10.21, 8.04], [9.12, 7.91, 8.03, 9.19, 7.04], [11.36, 10.18, 10.19, 11.31, 9.11]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 10.82), ('CB', 'ASP', 'CG', 'GLU', 9.41), ('CB', 'ASP', 'CD', 'GLU', 9.31), ('CB', 'ASP', 'OE1', 'GLU', 10.33), ('CB', 'ASP', 'OE2', 'GLU', 8.3)], [('CG', 'ASP', 'CB', 'GLU', 10.33), ('CG', 'ASP', 'CG', 'GLU', 9.07), ('CG', 'ASP', 'CD', 'GLU', 9.09), ('CG', 'ASP', 'OE1', 'GLU', 10.21), ('CG', 'ASP', 'OE2', 'GLU', 8.04)], [('OD1', 'ASP', 'CB', 'GLU', 9.12), ('OD1', 'ASP', 'CG', 'GLU', 7.91), ('OD1', 'ASP', 'CD', 'GLU', 8.03), ('OD1', 'ASP', 'OE1', 'GLU', 9.19), ('OD1', 'ASP', 'OE2', 'GLU', 7.04)], [('OD2', 'ASP', 'CB', 'GLU', 11.36), ('OD2', 'ASP', 'CG', 'GLU', 10.18), ('OD2', 'ASP', 'CD', 'GLU', 10.19), ('OD2', 'ASP', 'OE1', 'GLU', 11.31), ('OD2', 'ASP', 'OE2', 'GLU', 9.11)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_HISI, d, 'P_1pyd_4_1_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_GLU, d, 'P_1pyd_4_1_1_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_HIS, d, 'P_1pyd_4_1_1_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_HIS, d, 'P_1pyd_4_1_1_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_GLU, d, 'P_1pyd_4_1_1_1')
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