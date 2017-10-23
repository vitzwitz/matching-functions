'''
FUNC:P_1gpi_3_2_1_91
PDB:1gpi
EC:3.2.1.91
RESI:glu,asp,glu,his
LOCI:a-207,209,212,223;
'''
import motifFunctions as cmd
ASP_HIS = { 
	'distances':
		[[8.92, 8.05, 8.74, 6.73, 8.08, 6.77], [8.15, 7.28, 7.9, 6.05, 7.29, 6.08], [8.56, 7.87, 8.54, 6.79, 8.06, 6.95], [7.39, 6.35, 6.8, 5.14, 6.1, 4.95]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 8.92), ('CB', 'ASP', 'CG', 'HIS', 8.05), ('CB', 'ASP', 'ND1', 'HIS', 8.74), ('CB', 'ASP', 'CD2', 'HIS', 6.73), ('CB', 'ASP', 'CE1', 'HIS', 8.08), ('CB', 'ASP', 'NE2', 'HIS', 6.77)], [('CG', 'ASP', 'CB', 'HIS', 8.15), ('CG', 'ASP', 'CG', 'HIS', 7.28), ('CG', 'ASP', 'ND1', 'HIS', 7.9), ('CG', 'ASP', 'CD2', 'HIS', 6.05), ('CG', 'ASP', 'CE1', 'HIS', 7.29), ('CG', 'ASP', 'NE2', 'HIS', 6.08)], [('OD1', 'ASP', 'CB', 'HIS', 8.56), ('OD1', 'ASP', 'CG', 'HIS', 7.87), ('OD1', 'ASP', 'ND1', 'HIS', 8.54), ('OD1', 'ASP', 'CD2', 'HIS', 6.79), ('OD1', 'ASP', 'CE1', 'HIS', 8.06), ('OD1', 'ASP', 'NE2', 'HIS', 6.95)], [('OD2', 'ASP', 'CB', 'HIS', 7.39), ('OD2', 'ASP', 'CG', 'HIS', 6.35), ('OD2', 'ASP', 'ND1', 'HIS', 6.8), ('OD2', 'ASP', 'CD2', 'HIS', 5.14), ('OD2', 'ASP', 'CE1', 'HIS', 6.1), ('OD2', 'ASP', 'NE2', 'HIS', 4.95)]]}
HIS_GLUI = { 
	'distances':
		[[13.33, 12.32, 11.24, 10.35, 11.5], [12.1, 11.16, 10.01, 9.08, 10.28], [12.17, 11.31, 10.03, 9.1, 10.17], [10.82, 9.9, 8.82, 7.85, 9.2], [11.03, 10.24, 8.91, 7.97, 9.06], [10.08, 9.26, 8.04, 7.04, 8.36]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLUI', 13.33), ('CB', 'HIS', 'CG', 'GLUI', 12.32), ('CB', 'HIS', 'CD', 'GLUI', 11.24), ('CB', 'HIS', 'OE1', 'GLUI', 10.35), ('CB', 'HIS', 'OE2', 'GLUI', 11.5)], [('CG', 'HIS', 'CB', 'GLUI', 12.1), ('CG', 'HIS', 'CG', 'GLUI', 11.16), ('CG', 'HIS', 'CD', 'GLUI', 10.01), ('CG', 'HIS', 'OE1', 'GLUI', 9.08), ('CG', 'HIS', 'OE2', 'GLUI', 10.28)], [('ND1', 'HIS', 'CB', 'GLUI', 12.17), ('ND1', 'HIS', 'CG', 'GLUI', 11.31), ('ND1', 'HIS', 'CD', 'GLUI', 10.03), ('ND1', 'HIS', 'OE1', 'GLUI', 9.1), ('ND1', 'HIS', 'OE2', 'GLUI', 10.17)], [('CD2', 'HIS', 'CB', 'GLUI', 10.82), ('CD2', 'HIS', 'CG', 'GLUI', 9.9), ('CD2', 'HIS', 'CD', 'GLUI', 8.82), ('CD2', 'HIS', 'OE1', 'GLUI', 7.85), ('CD2', 'HIS', 'OE2', 'GLUI', 9.2)], [('CE1', 'HIS', 'CB', 'GLUI', 11.03), ('CE1', 'HIS', 'CG', 'GLUI', 10.24), ('CE1', 'HIS', 'CD', 'GLUI', 8.91), ('CE1', 'HIS', 'OE1', 'GLUI', 7.97), ('CE1', 'HIS', 'OE2', 'GLUI', 9.06)], [('NE2', 'HIS', 'CB', 'GLUI', 10.08), ('NE2', 'HIS', 'CG', 'GLUI', 9.26), ('NE2', 'HIS', 'CD', 'GLUI', 8.04), ('NE2', 'HIS', 'OE1', 'GLUI', 7.04), ('NE2', 'HIS', 'OE2', 'GLUI', 8.36)]]}
GLU_HIS = { 
	'distances':
		[[6.26, 6.69, 7.67, 6.68, 8.16, 7.66], [6.96, 6.96, 7.85, 6.57, 8.03, 7.33], [7.19, 6.9, 7.46, 6.51, 7.46, 6.92], [6.89, 6.66, 7.01, 6.59, 7.14, 6.92], [8.1, 7.58, 8.03, 6.95, 7.76, 7.11], [13.33, 12.1, 12.17, 10.82, 11.03, 10.08], [12.32, 11.16, 11.31, 9.9, 10.24, 9.26], [11.24, 10.01, 10.03, 8.82, 8.91, 8.04], [10.35, 9.08, 9.1, 7.85, 7.97, 7.04], [11.5, 10.28, 10.17, 9.2, 9.06, 8.36]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 6.26), ('CB', 'GLU', 'CG', 'HIS', 6.69), ('CB', 'GLU', 'ND1', 'HIS', 7.67), ('CB', 'GLU', 'CD2', 'HIS', 6.68), ('CB', 'GLU', 'CE1', 'HIS', 8.16), ('CB', 'GLU', 'NE2', 'HIS', 7.66)], [('CG', 'GLU', 'CB', 'HIS', 6.96), ('CG', 'GLU', 'CG', 'HIS', 6.96), ('CG', 'GLU', 'ND1', 'HIS', 7.85), ('CG', 'GLU', 'CD2', 'HIS', 6.57), ('CG', 'GLU', 'CE1', 'HIS', 8.03), ('CG', 'GLU', 'NE2', 'HIS', 7.33)], [('CD', 'GLU', 'CB', 'HIS', 7.19), ('CD', 'GLU', 'CG', 'HIS', 6.9), ('CD', 'GLU', 'ND1', 'HIS', 7.46), ('CD', 'GLU', 'CD2', 'HIS', 6.51), ('CD', 'GLU', 'CE1', 'HIS', 7.46), ('CD', 'GLU', 'NE2', 'HIS', 6.92)], [('OE1', 'GLU', 'CB', 'HIS', 6.89), ('OE1', 'GLU', 'CG', 'HIS', 6.66), ('OE1', 'GLU', 'ND1', 'HIS', 7.01), ('OE1', 'GLU', 'CD2', 'HIS', 6.59), ('OE1', 'GLU', 'CE1', 'HIS', 7.14), ('OE1', 'GLU', 'NE2', 'HIS', 6.92)], [('OE2', 'GLU', 'CB', 'HIS', 8.1), ('OE2', 'GLU', 'CG', 'HIS', 7.58), ('OE2', 'GLU', 'ND1', 'HIS', 8.03), ('OE2', 'GLU', 'CD2', 'HIS', 6.95), ('OE2', 'GLU', 'CE1', 'HIS', 7.76), ('OE2', 'GLU', 'NE2', 'HIS', 7.11)], [('CB', 'GLU', 'CB', 'HIS', 13.33), ('CB', 'GLU', 'CG', 'HIS', 12.1), ('CB', 'GLU', 'ND1', 'HIS', 12.17), ('CB', 'GLU', 'CD2', 'HIS', 10.82), ('CB', 'GLU', 'CE1', 'HIS', 11.03), ('CB', 'GLU', 'NE2', 'HIS', 10.08)], [('CG', 'GLU', 'CB', 'HIS', 12.32), ('CG', 'GLU', 'CG', 'HIS', 11.16), ('CG', 'GLU', 'ND1', 'HIS', 11.31), ('CG', 'GLU', 'CD2', 'HIS', 9.9), ('CG', 'GLU', 'CE1', 'HIS', 10.24), ('CG', 'GLU', 'NE2', 'HIS', 9.26)], [('CD', 'GLU', 'CB', 'HIS', 11.24), ('CD', 'GLU', 'CG', 'HIS', 10.01), ('CD', 'GLU', 'ND1', 'HIS', 10.03), ('CD', 'GLU', 'CD2', 'HIS', 8.82), ('CD', 'GLU', 'CE1', 'HIS', 8.91), ('CD', 'GLU', 'NE2', 'HIS', 8.04)], [('OE1', 'GLU', 'CB', 'HIS', 10.35), ('OE1', 'GLU', 'CG', 'HIS', 9.08), ('OE1', 'GLU', 'ND1', 'HIS', 9.1), ('OE1', 'GLU', 'CD2', 'HIS', 7.85), ('OE1', 'GLU', 'CE1', 'HIS', 7.97), ('OE1', 'GLU', 'NE2', 'HIS', 7.04)], [('OE2', 'GLU', 'CB', 'HIS', 11.5), ('OE2', 'GLU', 'CG', 'HIS', 10.28), ('OE2', 'GLU', 'ND1', 'HIS', 10.17), ('OE2', 'GLU', 'CD2', 'HIS', 9.2), ('OE2', 'GLU', 'CE1', 'HIS', 9.06), ('OE2', 'GLU', 'NE2', 'HIS', 8.36)]]}
GLU_GLU = { 
	'distances':
		[[12.78, 11.42, 10.65, 10.23, 10.76], [11.43, 10.04, 9.34, 9.02, 9.45], [10.89, 9.48, 8.6, 8.38, 8.5], [11.67, 10.31, 9.27, 9.01, 9.04], [9.86, 8.42, 7.59, 7.53, 7.44], [12.78, 11.43, 10.89, 11.67, 9.86], [11.42, 10.04, 9.48, 10.31, 8.42], [10.65, 9.34, 8.6, 9.27, 7.59], [10.23, 9.02, 8.38, 9.01, 7.53], [10.76, 9.45, 8.5, 9.04, 7.44]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 12.78), ('CB', 'GLU', 'CG', 'GLU', 11.42), ('CB', 'GLU', 'CD', 'GLU', 10.65), ('CB', 'GLU', 'OE1', 'GLU', 10.23), ('CB', 'GLU', 'OE2', 'GLU', 10.76)], [('CG', 'GLU', 'CB', 'GLU', 11.43), ('CG', 'GLU', 'CG', 'GLU', 10.04), ('CG', 'GLU', 'CD', 'GLU', 9.34), ('CG', 'GLU', 'OE1', 'GLU', 9.02), ('CG', 'GLU', 'OE2', 'GLU', 9.45)], [('CD', 'GLU', 'CB', 'GLU', 10.89), ('CD', 'GLU', 'CG', 'GLU', 9.48), ('CD', 'GLU', 'CD', 'GLU', 8.6), ('CD', 'GLU', 'OE1', 'GLU', 8.38), ('CD', 'GLU', 'OE2', 'GLU', 8.5)], [('OE1', 'GLU', 'CB', 'GLU', 11.67), ('OE1', 'GLU', 'CG', 'GLU', 10.31), ('OE1', 'GLU', 'CD', 'GLU', 9.27), ('OE1', 'GLU', 'OE1', 'GLU', 9.01), ('OE1', 'GLU', 'OE2', 'GLU', 9.04)], [('OE2', 'GLU', 'CB', 'GLU', 9.86), ('OE2', 'GLU', 'CG', 'GLU', 8.42), ('OE2', 'GLU', 'CD', 'GLU', 7.59), ('OE2', 'GLU', 'OE1', 'GLU', 7.53), ('OE2', 'GLU', 'OE2', 'GLU', 7.44)], [('CB', 'GLU', 'CB', 'GLU', 12.78), ('CB', 'GLU', 'CG', 'GLU', 11.43), ('CB', 'GLU', 'CD', 'GLU', 10.89), ('CB', 'GLU', 'OE1', 'GLU', 11.67), ('CB', 'GLU', 'OE2', 'GLU', 9.86)], [('CG', 'GLU', 'CB', 'GLU', 11.42), ('CG', 'GLU', 'CG', 'GLU', 10.04), ('CG', 'GLU', 'CD', 'GLU', 9.48), ('CG', 'GLU', 'OE1', 'GLU', 10.31), ('CG', 'GLU', 'OE2', 'GLU', 8.42)], [('CD', 'GLU', 'CB', 'GLU', 10.65), ('CD', 'GLU', 'CG', 'GLU', 9.34), ('CD', 'GLU', 'CD', 'GLU', 8.6), ('CD', 'GLU', 'OE1', 'GLU', 9.27), ('CD', 'GLU', 'OE2', 'GLU', 7.59)], [('OE1', 'GLU', 'CB', 'GLU', 10.23), ('OE1', 'GLU', 'CG', 'GLU', 9.02), ('OE1', 'GLU', 'CD', 'GLU', 8.38), ('OE1', 'GLU', 'OE1', 'GLU', 9.01), ('OE1', 'GLU', 'OE2', 'GLU', 7.53)], [('OE2', 'GLU', 'CB', 'GLU', 10.76), ('OE2', 'GLU', 'CG', 'GLU', 9.45), ('OE2', 'GLU', 'CD', 'GLU', 8.5), ('OE2', 'GLU', 'OE1', 'GLU', 9.04), ('OE2', 'GLU', 'OE2', 'GLU', 7.44)]]}
GLU_ASP = { 
	'distances':
		[[8.2, 7.15, 6.66, 7.03], [7.07, 5.94, 5.27, 5.99], [7.22, 5.84, 5.19, 5.6], [8.22, 6.81, 6.34, 6.3], [6.71, 5.3, 4.5, 5.2], [7.3, 7.75, 8.23, 8.1], [6.31, 6.54, 6.86, 6.96], [6.07, 5.93, 6.38, 6.0], [5.45, 5.4, 6.18, 5.29], [6.99, 6.54, 6.78, 6.45]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 8.2), ('CB', 'GLU', 'CG', 'ASP', 7.15), ('CB', 'GLU', 'OD1', 'ASP', 6.66), ('CB', 'GLU', 'OD2', 'ASP', 7.03)], [('CG', 'GLU', 'CB', 'ASP', 7.07), ('CG', 'GLU', 'CG', 'ASP', 5.94), ('CG', 'GLU', 'OD1', 'ASP', 5.27), ('CG', 'GLU', 'OD2', 'ASP', 5.99)], [('CD', 'GLU', 'CB', 'ASP', 7.22), ('CD', 'GLU', 'CG', 'ASP', 5.84), ('CD', 'GLU', 'OD1', 'ASP', 5.19), ('CD', 'GLU', 'OD2', 'ASP', 5.6)], [('OE1', 'GLU', 'CB', 'ASP', 8.22), ('OE1', 'GLU', 'CG', 'ASP', 6.81), ('OE1', 'GLU', 'OD1', 'ASP', 6.34), ('OE1', 'GLU', 'OD2', 'ASP', 6.3)], [('OE2', 'GLU', 'CB', 'ASP', 6.71), ('OE2', 'GLU', 'CG', 'ASP', 5.3), ('OE2', 'GLU', 'OD1', 'ASP', 4.5), ('OE2', 'GLU', 'OD2', 'ASP', 5.2)], [('CB', 'GLU', 'CB', 'ASP', 7.3), ('CB', 'GLU', 'CG', 'ASP', 7.75), ('CB', 'GLU', 'OD1', 'ASP', 8.23), ('CB', 'GLU', 'OD2', 'ASP', 8.1)], [('CG', 'GLU', 'CB', 'ASP', 6.31), ('CG', 'GLU', 'CG', 'ASP', 6.54), ('CG', 'GLU', 'OD1', 'ASP', 6.86), ('CG', 'GLU', 'OD2', 'ASP', 6.96)], [('CD', 'GLU', 'CB', 'ASP', 6.07), ('CD', 'GLU', 'CG', 'ASP', 5.93), ('CD', 'GLU', 'OD1', 'ASP', 6.38), ('CD', 'GLU', 'OD2', 'ASP', 6.0)], [('OE1', 'GLU', 'CB', 'ASP', 5.45), ('OE1', 'GLU', 'CG', 'ASP', 5.4), ('OE1', 'GLU', 'OD1', 'ASP', 6.18), ('OE1', 'GLU', 'OD2', 'ASP', 5.29)], [('OE2', 'GLU', 'CB', 'ASP', 6.99), ('OE2', 'GLU', 'CG', 'ASP', 6.54), ('OE2', 'GLU', 'OD1', 'ASP', 6.78), ('OE2', 'GLU', 'OD2', 'ASP', 6.45)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HIS, d, 'P_1gpi_3_2_1_91')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_GLUI, d, 'P_1gpi_3_2_1_91')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_HIS, d, 'P_1gpi_3_2_1_91')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_GLU, d, 'P_1gpi_3_2_1_91')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLU_ASP, d, 'P_1gpi_3_2_1_91')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HIS' :  match1,
		'HIS_GLUI' :  match2,
		'GLU_HIS' :  match3,
		'GLU_GLU' :  match4,
		'GLU_ASP' :  match5}