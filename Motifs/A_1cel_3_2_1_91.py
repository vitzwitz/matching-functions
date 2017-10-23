'''
FUNC:A_1cel_3_2_1_91
PDB:1cel
EC:3.2.1.91
RESI:glu,asp,glu,his
LOCI:a-212,214,217,228;
'''
import motifFunctions as cmd
GLU_ASP = { 
	'distances':
		[[8.26, 7.21, 6.93, 7.01], [7.18, 6.03, 5.54, 6.03], [7.3, 5.9, 5.42, 5.66], [8.26, 6.84, 6.53, 6.32], [6.77, 5.32, 4.65, 5.26], [7.21, 7.65, 8.0, 8.06], [6.11, 6.33, 6.55, 6.82], [6.09, 5.91, 6.29, 6.04], [7.1, 6.64, 6.82, 6.64], [5.5, 5.38, 6.09, 5.26]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 8.26), ('CB', 'GLU', 'CG', 'ASP', 7.21), ('CB', 'GLU', 'OD1', 'ASP', 6.93), ('CB', 'GLU', 'OD2', 'ASP', 7.01)], [('CG', 'GLU', 'CB', 'ASP', 7.18), ('CG', 'GLU', 'CG', 'ASP', 6.03), ('CG', 'GLU', 'OD1', 'ASP', 5.54), ('CG', 'GLU', 'OD2', 'ASP', 6.03)], [('CD', 'GLU', 'CB', 'ASP', 7.3), ('CD', 'GLU', 'CG', 'ASP', 5.9), ('CD', 'GLU', 'OD1', 'ASP', 5.42), ('CD', 'GLU', 'OD2', 'ASP', 5.66)], [('OE1', 'GLU', 'CB', 'ASP', 8.26), ('OE1', 'GLU', 'CG', 'ASP', 6.84), ('OE1', 'GLU', 'OD1', 'ASP', 6.53), ('OE1', 'GLU', 'OD2', 'ASP', 6.32)], [('OE2', 'GLU', 'CB', 'ASP', 6.77), ('OE2', 'GLU', 'CG', 'ASP', 5.32), ('OE2', 'GLU', 'OD1', 'ASP', 4.65), ('OE2', 'GLU', 'OD2', 'ASP', 5.26)], [('CB', 'GLU', 'CB', 'ASP', 7.21), ('CB', 'GLU', 'CG', 'ASP', 7.65), ('CB', 'GLU', 'OD1', 'ASP', 8.0), ('CB', 'GLU', 'OD2', 'ASP', 8.06)], [('CG', 'GLU', 'CB', 'ASP', 6.11), ('CG', 'GLU', 'CG', 'ASP', 6.33), ('CG', 'GLU', 'OD1', 'ASP', 6.55), ('CG', 'GLU', 'OD2', 'ASP', 6.82)], [('CD', 'GLU', 'CB', 'ASP', 6.09), ('CD', 'GLU', 'CG', 'ASP', 5.91), ('CD', 'GLU', 'OD1', 'ASP', 6.29), ('CD', 'GLU', 'OD2', 'ASP', 6.04)], [('OE1', 'GLU', 'CB', 'ASP', 7.1), ('OE1', 'GLU', 'CG', 'ASP', 6.64), ('OE1', 'GLU', 'OD1', 'ASP', 6.82), ('OE1', 'GLU', 'OD2', 'ASP', 6.64)], [('OE2', 'GLU', 'CB', 'ASP', 5.5), ('OE2', 'GLU', 'CG', 'ASP', 5.38), ('OE2', 'GLU', 'OD1', 'ASP', 6.09), ('OE2', 'GLU', 'OD2', 'ASP', 5.26)]]}
GLU_GLU = { 
	'distances':
		[[12.76, 11.35, 10.71, 10.99, 10.18], [11.45, 10.0, 9.44, 9.71, 9.04], [10.9, 9.45, 8.69, 8.75, 8.35], [11.65, 10.25, 9.31, 9.25, 8.92], [9.86, 8.39, 7.67, 7.67, 7.5], [12.76, 11.45, 10.9, 11.65, 9.86], [11.35, 10.0, 9.45, 10.25, 8.39], [10.71, 9.44, 8.69, 9.31, 7.67], [10.99, 9.71, 8.75, 9.25, 7.67], [10.18, 9.04, 8.35, 8.92, 7.5]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 12.76), ('CB', 'GLU', 'CG', 'GLU', 11.35), ('CB', 'GLU', 'CD', 'GLU', 10.71), ('CB', 'GLU', 'OE1', 'GLU', 10.99), ('CB', 'GLU', 'OE2', 'GLU', 10.18)], [('CG', 'GLU', 'CB', 'GLU', 11.45), ('CG', 'GLU', 'CG', 'GLU', 10.0), ('CG', 'GLU', 'CD', 'GLU', 9.44), ('CG', 'GLU', 'OE1', 'GLU', 9.71), ('CG', 'GLU', 'OE2', 'GLU', 9.04)], [('CD', 'GLU', 'CB', 'GLU', 10.9), ('CD', 'GLU', 'CG', 'GLU', 9.45), ('CD', 'GLU', 'CD', 'GLU', 8.69), ('CD', 'GLU', 'OE1', 'GLU', 8.75), ('CD', 'GLU', 'OE2', 'GLU', 8.35)], [('OE1', 'GLU', 'CB', 'GLU', 11.65), ('OE1', 'GLU', 'CG', 'GLU', 10.25), ('OE1', 'GLU', 'CD', 'GLU', 9.31), ('OE1', 'GLU', 'OE1', 'GLU', 9.25), ('OE1', 'GLU', 'OE2', 'GLU', 8.92)], [('OE2', 'GLU', 'CB', 'GLU', 9.86), ('OE2', 'GLU', 'CG', 'GLU', 8.39), ('OE2', 'GLU', 'CD', 'GLU', 7.67), ('OE2', 'GLU', 'OE1', 'GLU', 7.67), ('OE2', 'GLU', 'OE2', 'GLU', 7.5)], [('CB', 'GLU', 'CB', 'GLU', 12.76), ('CB', 'GLU', 'CG', 'GLU', 11.45), ('CB', 'GLU', 'CD', 'GLU', 10.9), ('CB', 'GLU', 'OE1', 'GLU', 11.65), ('CB', 'GLU', 'OE2', 'GLU', 9.86)], [('CG', 'GLU', 'CB', 'GLU', 11.35), ('CG', 'GLU', 'CG', 'GLU', 10.0), ('CG', 'GLU', 'CD', 'GLU', 9.45), ('CG', 'GLU', 'OE1', 'GLU', 10.25), ('CG', 'GLU', 'OE2', 'GLU', 8.39)], [('CD', 'GLU', 'CB', 'GLU', 10.71), ('CD', 'GLU', 'CG', 'GLU', 9.44), ('CD', 'GLU', 'CD', 'GLU', 8.69), ('CD', 'GLU', 'OE1', 'GLU', 9.31), ('CD', 'GLU', 'OE2', 'GLU', 7.67)], [('OE1', 'GLU', 'CB', 'GLU', 10.99), ('OE1', 'GLU', 'CG', 'GLU', 9.71), ('OE1', 'GLU', 'CD', 'GLU', 8.75), ('OE1', 'GLU', 'OE1', 'GLU', 9.25), ('OE1', 'GLU', 'OE2', 'GLU', 7.67)], [('OE2', 'GLU', 'CB', 'GLU', 10.18), ('OE2', 'GLU', 'CG', 'GLU', 9.04), ('OE2', 'GLU', 'CD', 'GLU', 8.35), ('OE2', 'GLU', 'OE1', 'GLU', 8.92), ('OE2', 'GLU', 'OE2', 'GLU', 7.5)]]}
HIS_ASP = { 
	'distances':
		[[9.19, 8.48, 9.03, 7.63], [8.19, 7.46, 8.15, 6.46], [8.78, 8.0, 8.74, 6.84], [6.84, 6.16, 6.94, 5.18], [8.02, 7.25, 8.09, 6.03], [6.74, 6.02, 6.92, 4.84]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 9.19), ('CB', 'HIS', 'CG', 'ASP', 8.48), ('CB', 'HIS', 'OD1', 'ASP', 9.03), ('CB', 'HIS', 'OD2', 'ASP', 7.63)], [('CG', 'HIS', 'CB', 'ASP', 8.19), ('CG', 'HIS', 'CG', 'ASP', 7.46), ('CG', 'HIS', 'OD1', 'ASP', 8.15), ('CG', 'HIS', 'OD2', 'ASP', 6.46)], [('ND1', 'HIS', 'CB', 'ASP', 8.78), ('ND1', 'HIS', 'CG', 'ASP', 8.0), ('ND1', 'HIS', 'OD1', 'ASP', 8.74), ('ND1', 'HIS', 'OD2', 'ASP', 6.84)], [('CD2', 'HIS', 'CB', 'ASP', 6.84), ('CD2', 'HIS', 'CG', 'ASP', 6.16), ('CD2', 'HIS', 'OD1', 'ASP', 6.94), ('CD2', 'HIS', 'OD2', 'ASP', 5.18)], [('CE1', 'HIS', 'CB', 'ASP', 8.02), ('CE1', 'HIS', 'CG', 'ASP', 7.25), ('CE1', 'HIS', 'OD1', 'ASP', 8.09), ('CE1', 'HIS', 'OD2', 'ASP', 6.03)], [('NE2', 'HIS', 'CB', 'ASP', 6.74), ('NE2', 'HIS', 'CG', 'ASP', 6.02), ('NE2', 'HIS', 'OD1', 'ASP', 6.92), ('NE2', 'HIS', 'OD2', 'ASP', 4.84)]]}
GLU_HIS = { 
	'distances':
		[[6.31, 6.53, 7.57, 6.32, 7.95, 7.29], [7.16, 6.96, 7.87, 6.37, 7.91, 7.07], [7.4, 6.9, 7.48, 6.33, 7.34, 6.65], [7.02, 6.6, 6.99, 6.34, 6.99, 6.61], [8.33, 7.62, 8.07, 6.83, 7.66, 6.88], [13.5, 12.17, 12.15, 10.93, 10.95, 10.09], [12.39, 11.11, 11.18, 9.85, 10.03, 9.1], [11.45, 10.1, 10.02, 8.92, 8.82, 8.03], [11.86, 10.51, 10.31, 9.43, 9.11, 8.47], [10.47, 9.09, 8.99, 7.91, 7.78, 6.96]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 6.31), ('CB', 'GLU', 'CG', 'HIS', 6.53), ('CB', 'GLU', 'ND1', 'HIS', 7.57), ('CB', 'GLU', 'CD2', 'HIS', 6.32), ('CB', 'GLU', 'CE1', 'HIS', 7.95), ('CB', 'GLU', 'NE2', 'HIS', 7.29)], [('CG', 'GLU', 'CB', 'HIS', 7.16), ('CG', 'GLU', 'CG', 'HIS', 6.96), ('CG', 'GLU', 'ND1', 'HIS', 7.87), ('CG', 'GLU', 'CD2', 'HIS', 6.37), ('CG', 'GLU', 'CE1', 'HIS', 7.91), ('CG', 'GLU', 'NE2', 'HIS', 7.07)], [('CD', 'GLU', 'CB', 'HIS', 7.4), ('CD', 'GLU', 'CG', 'HIS', 6.9), ('CD', 'GLU', 'ND1', 'HIS', 7.48), ('CD', 'GLU', 'CD2', 'HIS', 6.33), ('CD', 'GLU', 'CE1', 'HIS', 7.34), ('CD', 'GLU', 'NE2', 'HIS', 6.65)], [('OE1', 'GLU', 'CB', 'HIS', 7.02), ('OE1', 'GLU', 'CG', 'HIS', 6.6), ('OE1', 'GLU', 'ND1', 'HIS', 6.99), ('OE1', 'GLU', 'CD2', 'HIS', 6.34), ('OE1', 'GLU', 'CE1', 'HIS', 6.99), ('OE1', 'GLU', 'NE2', 'HIS', 6.61)], [('OE2', 'GLU', 'CB', 'HIS', 8.33), ('OE2', 'GLU', 'CG', 'HIS', 7.62), ('OE2', 'GLU', 'ND1', 'HIS', 8.07), ('OE2', 'GLU', 'CD2', 'HIS', 6.83), ('OE2', 'GLU', 'CE1', 'HIS', 7.66), ('OE2', 'GLU', 'NE2', 'HIS', 6.88)], [('CB', 'GLU', 'CB', 'HIS', 13.5), ('CB', 'GLU', 'CG', 'HIS', 12.17), ('CB', 'GLU', 'ND1', 'HIS', 12.15), ('CB', 'GLU', 'CD2', 'HIS', 10.93), ('CB', 'GLU', 'CE1', 'HIS', 10.95), ('CB', 'GLU', 'NE2', 'HIS', 10.09)], [('CG', 'GLU', 'CB', 'HIS', 12.39), ('CG', 'GLU', 'CG', 'HIS', 11.11), ('CG', 'GLU', 'ND1', 'HIS', 11.18), ('CG', 'GLU', 'CD2', 'HIS', 9.85), ('CG', 'GLU', 'CE1', 'HIS', 10.03), ('CG', 'GLU', 'NE2', 'HIS', 9.1)], [('CD', 'GLU', 'CB', 'HIS', 11.45), ('CD', 'GLU', 'CG', 'HIS', 10.1), ('CD', 'GLU', 'ND1', 'HIS', 10.02), ('CD', 'GLU', 'CD2', 'HIS', 8.92), ('CD', 'GLU', 'CE1', 'HIS', 8.82), ('CD', 'GLU', 'NE2', 'HIS', 8.03)], [('OE1', 'GLU', 'CB', 'HIS', 11.86), ('OE1', 'GLU', 'CG', 'HIS', 10.51), ('OE1', 'GLU', 'ND1', 'HIS', 10.31), ('OE1', 'GLU', 'CD2', 'HIS', 9.43), ('OE1', 'GLU', 'CE1', 'HIS', 9.11), ('OE1', 'GLU', 'NE2', 'HIS', 8.47)], [('OE2', 'GLU', 'CB', 'HIS', 10.47), ('OE2', 'GLU', 'CG', 'HIS', 9.09), ('OE2', 'GLU', 'ND1', 'HIS', 8.99), ('OE2', 'GLU', 'CD2', 'HIS', 7.91), ('OE2', 'GLU', 'CE1', 'HIS', 7.78), ('OE2', 'GLU', 'NE2', 'HIS', 6.96)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_ASP, d, 'A_1cel_3_2_1_91')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_GLU, d, 'A_1cel_3_2_1_91')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASP, d, 'A_1cel_3_2_1_91')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_HIS, d, 'A_1cel_3_2_1_91')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_ASP' :  match1,
		'GLU_GLU' :  match2,
		'HIS_ASP' :  match3,
		'GLU_HIS' :  match4}