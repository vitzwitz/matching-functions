'''
FUNC:P_2dnj_3_1_21_1
PDB:2dnj
EC:3.1.21.1
RESI:glu,his,asp,his
LOCI:a-78,134,212,252;
'''
import motifFunctions as cmd
GLU_ASP = { 
	'distances':
		[[17.05, 16.06, 16.59, 14.88], [16.69, 15.6, 16.01, 14.46], [15.34, 14.24, 14.64, 13.13], [14.47, 13.45, 13.93, 12.32], [15.28, 14.11, 14.38, 13.05]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 17.05), ('CB', 'GLU', 'CG', 'ASP', 16.06), ('CB', 'GLU', 'OD1', 'ASP', 16.59), ('CB', 'GLU', 'OD2', 'ASP', 14.88)], [('CG', 'GLU', 'CB', 'ASP', 16.69), ('CG', 'GLU', 'CG', 'ASP', 15.6), ('CG', 'GLU', 'OD1', 'ASP', 16.01), ('CG', 'GLU', 'OD2', 'ASP', 14.46)], [('CD', 'GLU', 'CB', 'ASP', 15.34), ('CD', 'GLU', 'CG', 'ASP', 14.24), ('CD', 'GLU', 'OD1', 'ASP', 14.64), ('CD', 'GLU', 'OD2', 'ASP', 13.13)], [('OE1', 'GLU', 'CB', 'ASP', 14.47), ('OE1', 'GLU', 'CG', 'ASP', 13.45), ('OE1', 'GLU', 'OD1', 'ASP', 13.93), ('OE1', 'GLU', 'OD2', 'ASP', 12.32)], [('OE2', 'GLU', 'CB', 'ASP', 15.28), ('OE2', 'GLU', 'CG', 'ASP', 14.11), ('OE2', 'GLU', 'OD1', 'ASP', 14.38), ('OE2', 'GLU', 'OD2', 'ASP', 13.05)]]}
HIS_ASP = { 
	'distances':
		[[11.54, 10.81, 11.51, 9.77], [11.48, 10.57, 11.09, 9.55], [12.5, 11.48, 11.89, 10.43], [10.79, 9.82, 10.21, 8.91], [12.49, 11.35, 11.6, 10.38], [11.49, 10.38, 10.59, 9.5], [7.79, 6.45, 5.88, 6.28], [7.8, 6.34, 5.67, 6.12], [6.9, 5.46, 4.7, 5.41], [8.95, 7.45, 6.83, 7.1], [7.7, 6.3, 5.62, 6.16], [8.85, 7.39, 6.75, 7.08]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 11.54), ('CB', 'HIS', 'CG', 'ASP', 10.81), ('CB', 'HIS', 'OD1', 'ASP', 11.51), ('CB', 'HIS', 'OD2', 'ASP', 9.77)], [('CG', 'HIS', 'CB', 'ASP', 11.48), ('CG', 'HIS', 'CG', 'ASP', 10.57), ('CG', 'HIS', 'OD1', 'ASP', 11.09), ('CG', 'HIS', 'OD2', 'ASP', 9.55)], [('ND1', 'HIS', 'CB', 'ASP', 12.5), ('ND1', 'HIS', 'CG', 'ASP', 11.48), ('ND1', 'HIS', 'OD1', 'ASP', 11.89), ('ND1', 'HIS', 'OD2', 'ASP', 10.43)], [('CD2', 'HIS', 'CB', 'ASP', 10.79), ('CD2', 'HIS', 'CG', 'ASP', 9.82), ('CD2', 'HIS', 'OD1', 'ASP', 10.21), ('CD2', 'HIS', 'OD2', 'ASP', 8.91)], [('CE1', 'HIS', 'CB', 'ASP', 12.49), ('CE1', 'HIS', 'CG', 'ASP', 11.35), ('CE1', 'HIS', 'OD1', 'ASP', 11.6), ('CE1', 'HIS', 'OD2', 'ASP', 10.38)], [('NE2', 'HIS', 'CB', 'ASP', 11.49), ('NE2', 'HIS', 'CG', 'ASP', 10.38), ('NE2', 'HIS', 'OD1', 'ASP', 10.59), ('NE2', 'HIS', 'OD2', 'ASP', 9.5)], [('CB', 'HIS', 'CB', 'ASP', 7.79), ('CB', 'HIS', 'CG', 'ASP', 6.45), ('CB', 'HIS', 'OD1', 'ASP', 5.88), ('CB', 'HIS', 'OD2', 'ASP', 6.28)], [('CG', 'HIS', 'CB', 'ASP', 7.8), ('CG', 'HIS', 'CG', 'ASP', 6.34), ('CG', 'HIS', 'OD1', 'ASP', 5.67), ('CG', 'HIS', 'OD2', 'ASP', 6.12)], [('ND1', 'HIS', 'CB', 'ASP', 6.9), ('ND1', 'HIS', 'CG', 'ASP', 5.46), ('ND1', 'HIS', 'OD1', 'ASP', 4.7), ('ND1', 'HIS', 'OD2', 'ASP', 5.41)], [('CD2', 'HIS', 'CB', 'ASP', 8.95), ('CD2', 'HIS', 'CG', 'ASP', 7.45), ('CD2', 'HIS', 'OD1', 'ASP', 6.83), ('CD2', 'HIS', 'OD2', 'ASP', 7.1)], [('CE1', 'HIS', 'CB', 'ASP', 7.7), ('CE1', 'HIS', 'CG', 'ASP', 6.3), ('CE1', 'HIS', 'OD1', 'ASP', 5.62), ('CE1', 'HIS', 'OD2', 'ASP', 6.16)], [('NE2', 'HIS', 'CB', 'ASP', 8.85), ('NE2', 'HIS', 'CG', 'ASP', 7.39), ('NE2', 'HIS', 'OD1', 'ASP', 6.75), ('NE2', 'HIS', 'OD2', 'ASP', 7.08)]]}
HIS_HIS = { 
	'distances':
		[[12.06, 11.26, 10.87, 11.0, 10.4, 10.47], [11.36, 10.43, 10.08, 9.99, 9.47, 9.39], [11.68, 10.73, 10.56, 10.12, 9.89, 9.59], [10.65, 9.59, 9.12, 9.12, 8.38, 8.37], [11.21, 10.15, 10.0, 9.39, 9.19, 8.77], [10.58, 9.42, 9.09, 8.74, 8.22, 7.96], [12.06, 11.36, 11.68, 10.65, 11.21, 10.58], [11.26, 10.43, 10.73, 9.59, 10.15, 9.42], [10.87, 10.08, 10.56, 9.12, 10.0, 9.09], [11.0, 9.99, 10.12, 9.12, 9.39, 8.74], [10.4, 9.47, 9.89, 8.38, 9.19, 8.22], [10.47, 9.39, 9.59, 8.37, 8.77, 7.96]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 12.06), ('CB', 'HIS', 'CG', 'HIS', 11.26), ('CB', 'HIS', 'ND1', 'HIS', 10.87), ('CB', 'HIS', 'CD2', 'HIS', 11.0), ('CB', 'HIS', 'CE1', 'HIS', 10.4), ('CB', 'HIS', 'NE2', 'HIS', 10.47)], [('CG', 'HIS', 'CB', 'HIS', 11.36), ('CG', 'HIS', 'CG', 'HIS', 10.43), ('CG', 'HIS', 'ND1', 'HIS', 10.08), ('CG', 'HIS', 'CD2', 'HIS', 9.99), ('CG', 'HIS', 'CE1', 'HIS', 9.47), ('CG', 'HIS', 'NE2', 'HIS', 9.39)], [('ND1', 'HIS', 'CB', 'HIS', 11.68), ('ND1', 'HIS', 'CG', 'HIS', 10.73), ('ND1', 'HIS', 'ND1', 'HIS', 10.56), ('ND1', 'HIS', 'CD2', 'HIS', 10.12), ('ND1', 'HIS', 'CE1', 'HIS', 9.89), ('ND1', 'HIS', 'NE2', 'HIS', 9.59)], [('CD2', 'HIS', 'CB', 'HIS', 10.65), ('CD2', 'HIS', 'CG', 'HIS', 9.59), ('CD2', 'HIS', 'ND1', 'HIS', 9.12), ('CD2', 'HIS', 'CD2', 'HIS', 9.12), ('CD2', 'HIS', 'CE1', 'HIS', 8.38), ('CD2', 'HIS', 'NE2', 'HIS', 8.37)], [('CE1', 'HIS', 'CB', 'HIS', 11.21), ('CE1', 'HIS', 'CG', 'HIS', 10.15), ('CE1', 'HIS', 'ND1', 'HIS', 10.0), ('CE1', 'HIS', 'CD2', 'HIS', 9.39), ('CE1', 'HIS', 'CE1', 'HIS', 9.19), ('CE1', 'HIS', 'NE2', 'HIS', 8.77)], [('NE2', 'HIS', 'CB', 'HIS', 10.58), ('NE2', 'HIS', 'CG', 'HIS', 9.42), ('NE2', 'HIS', 'ND1', 'HIS', 9.09), ('NE2', 'HIS', 'CD2', 'HIS', 8.74), ('NE2', 'HIS', 'CE1', 'HIS', 8.22), ('NE2', 'HIS', 'NE2', 'HIS', 7.96)], [('CB', 'HIS', 'CB', 'HIS', 12.06), ('CB', 'HIS', 'CG', 'HIS', 11.36), ('CB', 'HIS', 'ND1', 'HIS', 11.68), ('CB', 'HIS', 'CD2', 'HIS', 10.65), ('CB', 'HIS', 'CE1', 'HIS', 11.21), ('CB', 'HIS', 'NE2', 'HIS', 10.58)], [('CG', 'HIS', 'CB', 'HIS', 11.26), ('CG', 'HIS', 'CG', 'HIS', 10.43), ('CG', 'HIS', 'ND1', 'HIS', 10.73), ('CG', 'HIS', 'CD2', 'HIS', 9.59), ('CG', 'HIS', 'CE1', 'HIS', 10.15), ('CG', 'HIS', 'NE2', 'HIS', 9.42)], [('ND1', 'HIS', 'CB', 'HIS', 10.87), ('ND1', 'HIS', 'CG', 'HIS', 10.08), ('ND1', 'HIS', 'ND1', 'HIS', 10.56), ('ND1', 'HIS', 'CD2', 'HIS', 9.12), ('ND1', 'HIS', 'CE1', 'HIS', 10.0), ('ND1', 'HIS', 'NE2', 'HIS', 9.09)], [('CD2', 'HIS', 'CB', 'HIS', 11.0), ('CD2', 'HIS', 'CG', 'HIS', 9.99), ('CD2', 'HIS', 'ND1', 'HIS', 10.12), ('CD2', 'HIS', 'CD2', 'HIS', 9.12), ('CD2', 'HIS', 'CE1', 'HIS', 9.39), ('CD2', 'HIS', 'NE2', 'HIS', 8.74)], [('CE1', 'HIS', 'CB', 'HIS', 10.4), ('CE1', 'HIS', 'CG', 'HIS', 9.47), ('CE1', 'HIS', 'ND1', 'HIS', 9.89), ('CE1', 'HIS', 'CD2', 'HIS', 8.38), ('CE1', 'HIS', 'CE1', 'HIS', 9.19), ('CE1', 'HIS', 'NE2', 'HIS', 8.22)], [('NE2', 'HIS', 'CB', 'HIS', 10.47), ('NE2', 'HIS', 'CG', 'HIS', 9.39), ('NE2', 'HIS', 'ND1', 'HIS', 9.59), ('NE2', 'HIS', 'CD2', 'HIS', 8.37), ('NE2', 'HIS', 'CE1', 'HIS', 8.77), ('NE2', 'HIS', 'NE2', 'HIS', 7.96)]]}
GLU_HIS = { 
	'distances':
		[[8.3, 8.28, 7.3, 9.44, 8.06, 9.29], [8.25, 7.86, 6.67, 8.84, 7.13, 8.43], [7.01, 6.44, 5.19, 7.35, 5.64, 6.93], [5.89, 5.54, 4.48, 6.63, 5.33, 6.5], [7.43, 6.55, 5.17, 7.17, 5.14, 6.45], [15.66, 15.03, 15.21, 14.34, 14.7, 14.17], [14.91, 14.19, 14.41, 13.39, 13.82, 13.19], [13.71, 12.92, 13.05, 12.13, 12.43, 11.85], [13.27, 12.51, 12.55, 11.85, 11.99, 11.54], [13.35, 12.46, 12.6, 11.57, 11.88, 11.22]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 8.3), ('CB', 'GLU', 'CG', 'HIS', 8.28), ('CB', 'GLU', 'ND1', 'HIS', 7.3), ('CB', 'GLU', 'CD2', 'HIS', 9.44), ('CB', 'GLU', 'CE1', 'HIS', 8.06), ('CB', 'GLU', 'NE2', 'HIS', 9.29)], [('CG', 'GLU', 'CB', 'HIS', 8.25), ('CG', 'GLU', 'CG', 'HIS', 7.86), ('CG', 'GLU', 'ND1', 'HIS', 6.67), ('CG', 'GLU', 'CD2', 'HIS', 8.84), ('CG', 'GLU', 'CE1', 'HIS', 7.13), ('CG', 'GLU', 'NE2', 'HIS', 8.43)], [('CD', 'GLU', 'CB', 'HIS', 7.01), ('CD', 'GLU', 'CG', 'HIS', 6.44), ('CD', 'GLU', 'ND1', 'HIS', 5.19), ('CD', 'GLU', 'CD2', 'HIS', 7.35), ('CD', 'GLU', 'CE1', 'HIS', 5.64), ('CD', 'GLU', 'NE2', 'HIS', 6.93)], [('OE1', 'GLU', 'CB', 'HIS', 5.89), ('OE1', 'GLU', 'CG', 'HIS', 5.54), ('OE1', 'GLU', 'ND1', 'HIS', 4.48), ('OE1', 'GLU', 'CD2', 'HIS', 6.63), ('OE1', 'GLU', 'CE1', 'HIS', 5.33), ('OE1', 'GLU', 'NE2', 'HIS', 6.5)], [('OE2', 'GLU', 'CB', 'HIS', 7.43), ('OE2', 'GLU', 'CG', 'HIS', 6.55), ('OE2', 'GLU', 'ND1', 'HIS', 5.17), ('OE2', 'GLU', 'CD2', 'HIS', 7.17), ('OE2', 'GLU', 'CE1', 'HIS', 5.14), ('OE2', 'GLU', 'NE2', 'HIS', 6.45)], [('CB', 'GLU', 'CB', 'HIS', 15.66), ('CB', 'GLU', 'CG', 'HIS', 15.03), ('CB', 'GLU', 'ND1', 'HIS', 15.21), ('CB', 'GLU', 'CD2', 'HIS', 14.34), ('CB', 'GLU', 'CE1', 'HIS', 14.7), ('CB', 'GLU', 'NE2', 'HIS', 14.17)], [('CG', 'GLU', 'CB', 'HIS', 14.91), ('CG', 'GLU', 'CG', 'HIS', 14.19), ('CG', 'GLU', 'ND1', 'HIS', 14.41), ('CG', 'GLU', 'CD2', 'HIS', 13.39), ('CG', 'GLU', 'CE1', 'HIS', 13.82), ('CG', 'GLU', 'NE2', 'HIS', 13.19)], [('CD', 'GLU', 'CB', 'HIS', 13.71), ('CD', 'GLU', 'CG', 'HIS', 12.92), ('CD', 'GLU', 'ND1', 'HIS', 13.05), ('CD', 'GLU', 'CD2', 'HIS', 12.13), ('CD', 'GLU', 'CE1', 'HIS', 12.43), ('CD', 'GLU', 'NE2', 'HIS', 11.85)], [('OE1', 'GLU', 'CB', 'HIS', 13.27), ('OE1', 'GLU', 'CG', 'HIS', 12.51), ('OE1', 'GLU', 'ND1', 'HIS', 12.55), ('OE1', 'GLU', 'CD2', 'HIS', 11.85), ('OE1', 'GLU', 'CE1', 'HIS', 11.99), ('OE1', 'GLU', 'NE2', 'HIS', 11.54)], [('OE2', 'GLU', 'CB', 'HIS', 13.35), ('OE2', 'GLU', 'CG', 'HIS', 12.46), ('OE2', 'GLU', 'ND1', 'HIS', 12.6), ('OE2', 'GLU', 'CD2', 'HIS', 11.57), ('OE2', 'GLU', 'CE1', 'HIS', 11.88), ('OE2', 'GLU', 'NE2', 'HIS', 11.22)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_ASP, d, 'P_2dnj_3_1_21_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'P_2dnj_3_1_21_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_HIS, d, 'P_2dnj_3_1_21_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_HIS, d, 'P_2dnj_3_1_21_1')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_ASP' :  match1,
		'HIS_ASP' :  match2,
		'HIS_HIS' :  match3,
		'GLU_HIS' :  match4}