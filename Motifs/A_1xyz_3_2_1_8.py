'''
FUNC:A_1xyz_3_2_1_8
PDB:1xyz
EC:3.2.1.8
RESI:glu,his,glu,asp
LOCI:a-645,723,754,756;
'''
import motifFunctions as cmd
HIS_GLU = { 
	'distances':
		[[8.25, 9.4, 9.29, 8.4, 10.34], [6.95, 8.05, 7.89, 6.96, 8.97], [6.43, 7.7, 7.7, 6.79, 8.89], [6.41, 7.23, 6.84, 5.88, 7.82], [5.48, 6.61, 6.52, 5.59, 7.72], [5.43, 6.23, 5.84, 4.81, 6.92], [13.02, 11.77, 11.2, 11.88, 10.26], [12.37, 11.03, 10.39, 11.12, 9.33], [13.21, 11.81, 11.09, 11.8, 9.94], [11.13, 9.74, 9.13, 9.92, 8.05], [12.63, 11.18, 10.43, 11.18, 9.22], [11.34, 9.89, 9.19, 9.99, 8.0]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 8.25), ('CB', 'HIS', 'CG', 'GLU', 9.4), ('CB', 'HIS', 'CD', 'GLU', 9.29), ('CB', 'HIS', 'OE1', 'GLU', 8.4), ('CB', 'HIS', 'OE2', 'GLU', 10.34)], [('CG', 'HIS', 'CB', 'GLU', 6.95), ('CG', 'HIS', 'CG', 'GLU', 8.05), ('CG', 'HIS', 'CD', 'GLU', 7.89), ('CG', 'HIS', 'OE1', 'GLU', 6.96), ('CG', 'HIS', 'OE2', 'GLU', 8.97)], [('ND1', 'HIS', 'CB', 'GLU', 6.43), ('ND1', 'HIS', 'CG', 'GLU', 7.7), ('ND1', 'HIS', 'CD', 'GLU', 7.7), ('ND1', 'HIS', 'OE1', 'GLU', 6.79), ('ND1', 'HIS', 'OE2', 'GLU', 8.89)], [('CD2', 'HIS', 'CB', 'GLU', 6.41), ('CD2', 'HIS', 'CG', 'GLU', 7.23), ('CD2', 'HIS', 'CD', 'GLU', 6.84), ('CD2', 'HIS', 'OE1', 'GLU', 5.88), ('CD2', 'HIS', 'OE2', 'GLU', 7.82)], [('CE1', 'HIS', 'CB', 'GLU', 5.48), ('CE1', 'HIS', 'CG', 'GLU', 6.61), ('CE1', 'HIS', 'CD', 'GLU', 6.52), ('CE1', 'HIS', 'OE1', 'GLU', 5.59), ('CE1', 'HIS', 'OE2', 'GLU', 7.72)], [('NE2', 'HIS', 'CB', 'GLU', 5.43), ('NE2', 'HIS', 'CG', 'GLU', 6.23), ('NE2', 'HIS', 'CD', 'GLU', 5.84), ('NE2', 'HIS', 'OE1', 'GLU', 4.81), ('NE2', 'HIS', 'OE2', 'GLU', 6.92)], [('CB', 'HIS', 'CB', 'GLU', 13.02), ('CB', 'HIS', 'CG', 'GLU', 11.77), ('CB', 'HIS', 'CD', 'GLU', 11.2), ('CB', 'HIS', 'OE1', 'GLU', 11.88), ('CB', 'HIS', 'OE2', 'GLU', 10.26)], [('CG', 'HIS', 'CB', 'GLU', 12.37), ('CG', 'HIS', 'CG', 'GLU', 11.03), ('CG', 'HIS', 'CD', 'GLU', 10.39), ('CG', 'HIS', 'OE1', 'GLU', 11.12), ('CG', 'HIS', 'OE2', 'GLU', 9.33)], [('ND1', 'HIS', 'CB', 'GLU', 13.21), ('ND1', 'HIS', 'CG', 'GLU', 11.81), ('ND1', 'HIS', 'CD', 'GLU', 11.09), ('ND1', 'HIS', 'OE1', 'GLU', 11.8), ('ND1', 'HIS', 'OE2', 'GLU', 9.94)], [('CD2', 'HIS', 'CB', 'GLU', 11.13), ('CD2', 'HIS', 'CG', 'GLU', 9.74), ('CD2', 'HIS', 'CD', 'GLU', 9.13), ('CD2', 'HIS', 'OE1', 'GLU', 9.92), ('CD2', 'HIS', 'OE2', 'GLU', 8.05)], [('CE1', 'HIS', 'CB', 'GLU', 12.63), ('CE1', 'HIS', 'CG', 'GLU', 11.18), ('CE1', 'HIS', 'CD', 'GLU', 10.43), ('CE1', 'HIS', 'OE1', 'GLU', 11.18), ('CE1', 'HIS', 'OE2', 'GLU', 9.22)], [('NE2', 'HIS', 'CB', 'GLU', 11.34), ('NE2', 'HIS', 'CG', 'GLU', 9.89), ('NE2', 'HIS', 'CD', 'GLU', 9.19), ('NE2', 'HIS', 'OE1', 'GLU', 9.99), ('NE2', 'HIS', 'OE2', 'GLU', 8.0)]]}
GLU_GLU = { 
	'distances':
		[[12.71, 11.2, 10.85, 11.86, 9.66], [11.92, 10.43, 10.18, 11.24, 9.05], [10.62, 9.13, 8.77, 9.79, 7.62], [10.39, 8.88, 8.31, 9.24, 7.08], [9.99, 8.56, 8.32, 9.36, 7.29], [12.71, 11.92, 10.62, 10.39, 9.99], [11.2, 10.43, 9.13, 8.88, 8.56], [10.85, 10.18, 8.77, 8.31, 8.32], [11.86, 11.24, 9.79, 9.24, 9.36], [9.66, 9.05, 7.62, 7.08, 7.29]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 12.71), ('CB', 'GLU', 'CG', 'GLU', 11.2), ('CB', 'GLU', 'CD', 'GLU', 10.85), ('CB', 'GLU', 'OE1', 'GLU', 11.86), ('CB', 'GLU', 'OE2', 'GLU', 9.66)], [('CG', 'GLU', 'CB', 'GLU', 11.92), ('CG', 'GLU', 'CG', 'GLU', 10.43), ('CG', 'GLU', 'CD', 'GLU', 10.18), ('CG', 'GLU', 'OE1', 'GLU', 11.24), ('CG', 'GLU', 'OE2', 'GLU', 9.05)], [('CD', 'GLU', 'CB', 'GLU', 10.62), ('CD', 'GLU', 'CG', 'GLU', 9.13), ('CD', 'GLU', 'CD', 'GLU', 8.77), ('CD', 'GLU', 'OE1', 'GLU', 9.79), ('CD', 'GLU', 'OE2', 'GLU', 7.62)], [('OE1', 'GLU', 'CB', 'GLU', 10.39), ('OE1', 'GLU', 'CG', 'GLU', 8.88), ('OE1', 'GLU', 'CD', 'GLU', 8.31), ('OE1', 'GLU', 'OE1', 'GLU', 9.24), ('OE1', 'GLU', 'OE2', 'GLU', 7.08)], [('OE2', 'GLU', 'CB', 'GLU', 9.99), ('OE2', 'GLU', 'CG', 'GLU', 8.56), ('OE2', 'GLU', 'CD', 'GLU', 8.32), ('OE2', 'GLU', 'OE1', 'GLU', 9.36), ('OE2', 'GLU', 'OE2', 'GLU', 7.29)], [('CB', 'GLU', 'CB', 'GLU', 12.71), ('CB', 'GLU', 'CG', 'GLU', 11.92), ('CB', 'GLU', 'CD', 'GLU', 10.62), ('CB', 'GLU', 'OE1', 'GLU', 10.39), ('CB', 'GLU', 'OE2', 'GLU', 9.99)], [('CG', 'GLU', 'CB', 'GLU', 11.2), ('CG', 'GLU', 'CG', 'GLU', 10.43), ('CG', 'GLU', 'CD', 'GLU', 9.13), ('CG', 'GLU', 'OE1', 'GLU', 8.88), ('CG', 'GLU', 'OE2', 'GLU', 8.56)], [('CD', 'GLU', 'CB', 'GLU', 10.85), ('CD', 'GLU', 'CG', 'GLU', 10.18), ('CD', 'GLU', 'CD', 'GLU', 8.77), ('CD', 'GLU', 'OE1', 'GLU', 8.31), ('CD', 'GLU', 'OE2', 'GLU', 8.32)], [('OE1', 'GLU', 'CB', 'GLU', 11.86), ('OE1', 'GLU', 'CG', 'GLU', 11.24), ('OE1', 'GLU', 'CD', 'GLU', 9.79), ('OE1', 'GLU', 'OE1', 'GLU', 9.24), ('OE1', 'GLU', 'OE2', 'GLU', 9.36)], [('OE2', 'GLU', 'CB', 'GLU', 9.66), ('OE2', 'GLU', 'CG', 'GLU', 9.05), ('OE2', 'GLU', 'CD', 'GLU', 7.62), ('OE2', 'GLU', 'OE1', 'GLU', 7.08), ('OE2', 'GLU', 'OE2', 'GLU', 7.29)]]}
ASP_HIS = { 
	'distances':
		[[8.08, 7.82, 6.69, 8.85, 7.27, 8.54], [6.84, 6.47, 5.31, 7.49, 5.95, 7.21], [5.74, 5.63, 4.73, 6.81, 5.72, 6.83], [7.26, 6.6, 5.3, 7.41, 5.58, 6.88]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 8.08), ('CB', 'ASP', 'CG', 'HIS', 7.82), ('CB', 'ASP', 'ND1', 'HIS', 6.69), ('CB', 'ASP', 'CD2', 'HIS', 8.85), ('CB', 'ASP', 'CE1', 'HIS', 7.27), ('CB', 'ASP', 'NE2', 'HIS', 8.54)], [('CG', 'ASP', 'CB', 'HIS', 6.84), ('CG', 'ASP', 'CG', 'HIS', 6.47), ('CG', 'ASP', 'ND1', 'HIS', 5.31), ('CG', 'ASP', 'CD2', 'HIS', 7.49), ('CG', 'ASP', 'CE1', 'HIS', 5.95), ('CG', 'ASP', 'NE2', 'HIS', 7.21)], [('OD1', 'ASP', 'CB', 'HIS', 5.74), ('OD1', 'ASP', 'CG', 'HIS', 5.63), ('OD1', 'ASP', 'ND1', 'HIS', 4.73), ('OD1', 'ASP', 'CD2', 'HIS', 6.81), ('OD1', 'ASP', 'CE1', 'HIS', 5.72), ('OD1', 'ASP', 'NE2', 'HIS', 6.83)], [('OD2', 'ASP', 'CB', 'HIS', 7.26), ('OD2', 'ASP', 'CG', 'HIS', 6.6), ('OD2', 'ASP', 'ND1', 'HIS', 5.3), ('OD2', 'ASP', 'CD2', 'HIS', 7.41), ('OD2', 'ASP', 'CE1', 'HIS', 5.58), ('OD2', 'ASP', 'NE2', 'HIS', 6.88)]]}
ASP_GLU = { 
	'distances':
		[[8.94, 10.46, 11.06, 10.46, 12.32], [8.19, 9.67, 10.07, 9.33, 11.32], [8.25, 9.73, 10.05, 9.26, 11.3], [7.91, 9.28, 9.56, 8.77, 10.79], [17.85, 16.41, 15.66, 16.34, 14.47], [16.46, 15.04, 14.24, 14.89, 13.06], [15.89, 14.51, 13.76, 14.41, 12.63], [16.06, 14.64, 13.75, 14.34, 12.54]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 8.94), ('CB', 'ASP', 'CG', 'GLU', 10.46), ('CB', 'ASP', 'CD', 'GLU', 11.06), ('CB', 'ASP', 'OE1', 'GLU', 10.46), ('CB', 'ASP', 'OE2', 'GLU', 12.32)], [('CG', 'ASP', 'CB', 'GLU', 8.19), ('CG', 'ASP', 'CG', 'GLU', 9.67), ('CG', 'ASP', 'CD', 'GLU', 10.07), ('CG', 'ASP', 'OE1', 'GLU', 9.33), ('CG', 'ASP', 'OE2', 'GLU', 11.32)], [('OD1', 'ASP', 'CB', 'GLU', 8.25), ('OD1', 'ASP', 'CG', 'GLU', 9.73), ('OD1', 'ASP', 'CD', 'GLU', 10.05), ('OD1', 'ASP', 'OE1', 'GLU', 9.26), ('OD1', 'ASP', 'OE2', 'GLU', 11.3)], [('OD2', 'ASP', 'CB', 'GLU', 7.91), ('OD2', 'ASP', 'CG', 'GLU', 9.28), ('OD2', 'ASP', 'CD', 'GLU', 9.56), ('OD2', 'ASP', 'OE1', 'GLU', 8.77), ('OD2', 'ASP', 'OE2', 'GLU', 10.79)], [('CB', 'ASP', 'CB', 'GLU', 17.85), ('CB', 'ASP', 'CG', 'GLU', 16.41), ('CB', 'ASP', 'CD', 'GLU', 15.66), ('CB', 'ASP', 'OE1', 'GLU', 16.34), ('CB', 'ASP', 'OE2', 'GLU', 14.47)], [('CG', 'ASP', 'CB', 'GLU', 16.46), ('CG', 'ASP', 'CG', 'GLU', 15.04), ('CG', 'ASP', 'CD', 'GLU', 14.24), ('CG', 'ASP', 'OE1', 'GLU', 14.89), ('CG', 'ASP', 'OE2', 'GLU', 13.06)], [('OD1', 'ASP', 'CB', 'GLU', 15.89), ('OD1', 'ASP', 'CG', 'GLU', 14.51), ('OD1', 'ASP', 'CD', 'GLU', 13.76), ('OD1', 'ASP', 'OE1', 'GLU', 14.41), ('OD1', 'ASP', 'OE2', 'GLU', 12.63)], [('OD2', 'ASP', 'CB', 'GLU', 16.06), ('OD2', 'ASP', 'CG', 'GLU', 14.64), ('OD2', 'ASP', 'CD', 'GLU', 13.75), ('OD2', 'ASP', 'OE1', 'GLU', 14.34), ('OD2', 'ASP', 'OE2', 'GLU', 12.54)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_GLU, d, 'A_1xyz_3_2_1_8')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_GLU, d, 'A_1xyz_3_2_1_8')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_HIS, d, 'A_1xyz_3_2_1_8')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_GLU, d, 'A_1xyz_3_2_1_8')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_GLU' :  match1,
		'GLU_GLU' :  match2,
		'ASP_HIS' :  match3,
		'ASP_GLU' :  match4}