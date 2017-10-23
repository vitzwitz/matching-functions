'''
FUNC:A_1els_4_2_1_11
PDB:1els
EC:4.2.1.11
RESI:glu,glu,his,lys
LOCI:a-168,211,373,396;
'''
import motifFunctions as cmd
LYS_HIS = { 
	'distances':
		[[8.33, 7.69, 6.83, 8.1, 6.86, 7.63], [8.17, 7.23, 6.17, 7.5, 5.88, 6.75], [9.01, 8.09, 6.86, 8.48, 6.59, 7.67], [9.06, 7.99, 6.67, 8.29, 6.18, 7.32], [9.9, 8.97, 7.63, 9.44, 7.33, 8.56]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'HIS', 8.33), ('CB', 'LYS', 'CG', 'HIS', 7.69), ('CB', 'LYS', 'ND1', 'HIS', 6.83), ('CB', 'LYS', 'CD2', 'HIS', 8.1), ('CB', 'LYS', 'CE1', 'HIS', 6.86), ('CB', 'LYS', 'NE2', 'HIS', 7.63)], [('CG', 'LYS', 'CB', 'HIS', 8.17), ('CG', 'LYS', 'CG', 'HIS', 7.23), ('CG', 'LYS', 'ND1', 'HIS', 6.17), ('CG', 'LYS', 'CD2', 'HIS', 7.5), ('CG', 'LYS', 'CE1', 'HIS', 5.88), ('CG', 'LYS', 'NE2', 'HIS', 6.75)], [('CD', 'LYS', 'CB', 'HIS', 9.01), ('CD', 'LYS', 'CG', 'HIS', 8.09), ('CD', 'LYS', 'ND1', 'HIS', 6.86), ('CD', 'LYS', 'CD2', 'HIS', 8.48), ('CD', 'LYS', 'CE1', 'HIS', 6.59), ('CD', 'LYS', 'NE2', 'HIS', 7.67)], [('CE', 'LYS', 'CB', 'HIS', 9.06), ('CE', 'LYS', 'CG', 'HIS', 7.99), ('CE', 'LYS', 'ND1', 'HIS', 6.67), ('CE', 'LYS', 'CD2', 'HIS', 8.29), ('CE', 'LYS', 'CE1', 'HIS', 6.18), ('CE', 'LYS', 'NE2', 'HIS', 7.32)], [('NZ', 'LYS', 'CB', 'HIS', 9.9), ('NZ', 'LYS', 'CG', 'HIS', 8.97), ('NZ', 'LYS', 'ND1', 'HIS', 7.63), ('NZ', 'LYS', 'CD2', 'HIS', 9.44), ('NZ', 'LYS', 'CE1', 'HIS', 7.33), ('NZ', 'LYS', 'NE2', 'HIS', 8.56)]]}
LYS_GLU = { 
	'distances':
		[[11.12, 11.1, 9.99, 9.38, 10.21], [9.93, 9.85, 8.66, 7.99, 8.9], [10.58, 10.33, 8.98, 8.35, 9.07], [9.75, 9.35, 7.9, 7.33, 7.92], [10.9, 10.33, 8.84, 8.4, 8.66], [10.56, 10.31, 9.11, 8.04, 9.2], [9.17, 8.83, 7.62, 6.58, 7.73], [8.63, 8.26, 6.98, 5.97, 7.04], [7.58, 6.97, 5.59, 4.77, 5.52], [7.92, 7.26, 5.89, 5.34, 5.64]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'GLU', 11.12), ('CB', 'LYS', 'CG', 'GLU', 11.1), ('CB', 'LYS', 'CD', 'GLU', 9.99), ('CB', 'LYS', 'OE1', 'GLU', 9.38), ('CB', 'LYS', 'OE2', 'GLU', 10.21)], [('CG', 'LYS', 'CB', 'GLU', 9.93), ('CG', 'LYS', 'CG', 'GLU', 9.85), ('CG', 'LYS', 'CD', 'GLU', 8.66), ('CG', 'LYS', 'OE1', 'GLU', 7.99), ('CG', 'LYS', 'OE2', 'GLU', 8.9)], [('CD', 'LYS', 'CB', 'GLU', 10.58), ('CD', 'LYS', 'CG', 'GLU', 10.33), ('CD', 'LYS', 'CD', 'GLU', 8.98), ('CD', 'LYS', 'OE1', 'GLU', 8.35), ('CD', 'LYS', 'OE2', 'GLU', 9.07)], [('CE', 'LYS', 'CB', 'GLU', 9.75), ('CE', 'LYS', 'CG', 'GLU', 9.35), ('CE', 'LYS', 'CD', 'GLU', 7.9), ('CE', 'LYS', 'OE1', 'GLU', 7.33), ('CE', 'LYS', 'OE2', 'GLU', 7.92)], [('NZ', 'LYS', 'CB', 'GLU', 10.9), ('NZ', 'LYS', 'CG', 'GLU', 10.33), ('NZ', 'LYS', 'CD', 'GLU', 8.84), ('NZ', 'LYS', 'OE1', 'GLU', 8.4), ('NZ', 'LYS', 'OE2', 'GLU', 8.66)], [('CB', 'LYS', 'CB', 'GLU', 10.56), ('CB', 'LYS', 'CG', 'GLU', 10.31), ('CB', 'LYS', 'CD', 'GLU', 9.11), ('CB', 'LYS', 'OE1', 'GLU', 8.04), ('CB', 'LYS', 'OE2', 'GLU', 9.2)], [('CG', 'LYS', 'CB', 'GLU', 9.17), ('CG', 'LYS', 'CG', 'GLU', 8.83), ('CG', 'LYS', 'CD', 'GLU', 7.62), ('CG', 'LYS', 'OE1', 'GLU', 6.58), ('CG', 'LYS', 'OE2', 'GLU', 7.73)], [('CD', 'LYS', 'CB', 'GLU', 8.63), ('CD', 'LYS', 'CG', 'GLU', 8.26), ('CD', 'LYS', 'CD', 'GLU', 6.98), ('CD', 'LYS', 'OE1', 'GLU', 5.97), ('CD', 'LYS', 'OE2', 'GLU', 7.04)], [('CE', 'LYS', 'CB', 'GLU', 7.58), ('CE', 'LYS', 'CG', 'GLU', 6.97), ('CE', 'LYS', 'CD', 'GLU', 5.59), ('CE', 'LYS', 'OE1', 'GLU', 4.77), ('CE', 'LYS', 'OE2', 'GLU', 5.52)], [('NZ', 'LYS', 'CB', 'GLU', 7.92), ('NZ', 'LYS', 'CG', 'GLU', 7.26), ('NZ', 'LYS', 'CD', 'GLU', 5.89), ('NZ', 'LYS', 'OE1', 'GLU', 5.34), ('NZ', 'LYS', 'OE2', 'GLU', 5.64)]]}
GLU_GLU = { 
	'distances':
		[[9.66, 8.9, 8.66, 8.85, 8.63], [9.66, 8.64, 8.24, 8.61, 7.94], [8.51, 7.41, 6.83, 7.19, 6.48], [7.58, 6.66, 6.16, 6.34, 6.12], [9.05, 7.78, 7.03, 7.52, 6.37], [9.66, 9.66, 8.51, 7.58, 9.05], [8.9, 8.64, 7.41, 6.66, 7.78], [8.66, 8.24, 6.83, 6.16, 7.03], [8.85, 8.61, 7.19, 6.34, 7.52], [8.63, 7.94, 6.48, 6.12, 6.37]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 9.66), ('CB', 'GLU', 'CG', 'GLU', 8.9), ('CB', 'GLU', 'CD', 'GLU', 8.66), ('CB', 'GLU', 'OE1', 'GLU', 8.85), ('CB', 'GLU', 'OE2', 'GLU', 8.63)], [('CG', 'GLU', 'CB', 'GLU', 9.66), ('CG', 'GLU', 'CG', 'GLU', 8.64), ('CG', 'GLU', 'CD', 'GLU', 8.24), ('CG', 'GLU', 'OE1', 'GLU', 8.61), ('CG', 'GLU', 'OE2', 'GLU', 7.94)], [('CD', 'GLU', 'CB', 'GLU', 8.51), ('CD', 'GLU', 'CG', 'GLU', 7.41), ('CD', 'GLU', 'CD', 'GLU', 6.83), ('CD', 'GLU', 'OE1', 'GLU', 7.19), ('CD', 'GLU', 'OE2', 'GLU', 6.48)], [('OE1', 'GLU', 'CB', 'GLU', 7.58), ('OE1', 'GLU', 'CG', 'GLU', 6.66), ('OE1', 'GLU', 'CD', 'GLU', 6.16), ('OE1', 'GLU', 'OE1', 'GLU', 6.34), ('OE1', 'GLU', 'OE2', 'GLU', 6.12)], [('OE2', 'GLU', 'CB', 'GLU', 9.05), ('OE2', 'GLU', 'CG', 'GLU', 7.78), ('OE2', 'GLU', 'CD', 'GLU', 7.03), ('OE2', 'GLU', 'OE1', 'GLU', 7.52), ('OE2', 'GLU', 'OE2', 'GLU', 6.37)], [('CB', 'GLU', 'CB', 'GLU', 9.66), ('CB', 'GLU', 'CG', 'GLU', 9.66), ('CB', 'GLU', 'CD', 'GLU', 8.51), ('CB', 'GLU', 'OE1', 'GLU', 7.58), ('CB', 'GLU', 'OE2', 'GLU', 9.05)], [('CG', 'GLU', 'CB', 'GLU', 8.9), ('CG', 'GLU', 'CG', 'GLU', 8.64), ('CG', 'GLU', 'CD', 'GLU', 7.41), ('CG', 'GLU', 'OE1', 'GLU', 6.66), ('CG', 'GLU', 'OE2', 'GLU', 7.78)], [('CD', 'GLU', 'CB', 'GLU', 8.66), ('CD', 'GLU', 'CG', 'GLU', 8.24), ('CD', 'GLU', 'CD', 'GLU', 6.83), ('CD', 'GLU', 'OE1', 'GLU', 6.16), ('CD', 'GLU', 'OE2', 'GLU', 7.03)], [('OE1', 'GLU', 'CB', 'GLU', 8.85), ('OE1', 'GLU', 'CG', 'GLU', 8.61), ('OE1', 'GLU', 'CD', 'GLU', 7.19), ('OE1', 'GLU', 'OE1', 'GLU', 6.34), ('OE1', 'GLU', 'OE2', 'GLU', 7.52)], [('OE2', 'GLU', 'CB', 'GLU', 8.63), ('OE2', 'GLU', 'CG', 'GLU', 7.94), ('OE2', 'GLU', 'CD', 'GLU', 6.48), ('OE2', 'GLU', 'OE1', 'GLU', 6.12), ('OE2', 'GLU', 'OE2', 'GLU', 6.37)]]}
HIS_GLU = { 
	'distances':
		[[9.46, 8.93, 8.57, 8.96, 8.25], [8.17, 7.68, 7.21, 7.51, 7.02], [8.15, 7.59, 6.78, 6.94, 6.57], [7.02, 6.75, 6.51, 6.75, 6.59], [7.03, 6.6, 5.69, 5.66, 5.73], [6.19, 6.0, 5.49, 5.5, 5.8], [13.38, 12.42, 11.14, 10.81, 10.55], [11.98, 11.04, 9.82, 9.49, 9.29], [10.9, 9.96, 8.66, 8.3, 8.13], [11.61, 10.73, 9.66, 9.35, 9.27], [9.75, 8.85, 7.66, 7.3, 7.27], [10.24, 9.41, 8.39, 8.07, 8.11]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 9.46), ('CB', 'HIS', 'CG', 'GLU', 8.93), ('CB', 'HIS', 'CD', 'GLU', 8.57), ('CB', 'HIS', 'OE1', 'GLU', 8.96), ('CB', 'HIS', 'OE2', 'GLU', 8.25)], [('CG', 'HIS', 'CB', 'GLU', 8.17), ('CG', 'HIS', 'CG', 'GLU', 7.68), ('CG', 'HIS', 'CD', 'GLU', 7.21), ('CG', 'HIS', 'OE1', 'GLU', 7.51), ('CG', 'HIS', 'OE2', 'GLU', 7.02)], [('ND1', 'HIS', 'CB', 'GLU', 8.15), ('ND1', 'HIS', 'CG', 'GLU', 7.59), ('ND1', 'HIS', 'CD', 'GLU', 6.78), ('ND1', 'HIS', 'OE1', 'GLU', 6.94), ('ND1', 'HIS', 'OE2', 'GLU', 6.57)], [('CD2', 'HIS', 'CB', 'GLU', 7.02), ('CD2', 'HIS', 'CG', 'GLU', 6.75), ('CD2', 'HIS', 'CD', 'GLU', 6.51), ('CD2', 'HIS', 'OE1', 'GLU', 6.75), ('CD2', 'HIS', 'OE2', 'GLU', 6.59)], [('CE1', 'HIS', 'CB', 'GLU', 7.03), ('CE1', 'HIS', 'CG', 'GLU', 6.6), ('CE1', 'HIS', 'CD', 'GLU', 5.69), ('CE1', 'HIS', 'OE1', 'GLU', 5.66), ('CE1', 'HIS', 'OE2', 'GLU', 5.73)], [('NE2', 'HIS', 'CB', 'GLU', 6.19), ('NE2', 'HIS', 'CG', 'GLU', 6.0), ('NE2', 'HIS', 'CD', 'GLU', 5.49), ('NE2', 'HIS', 'OE1', 'GLU', 5.5), ('NE2', 'HIS', 'OE2', 'GLU', 5.8)], [('CB', 'HIS', 'CB', 'GLU', 13.38), ('CB', 'HIS', 'CG', 'GLU', 12.42), ('CB', 'HIS', 'CD', 'GLU', 11.14), ('CB', 'HIS', 'OE1', 'GLU', 10.81), ('CB', 'HIS', 'OE2', 'GLU', 10.55)], [('CG', 'HIS', 'CB', 'GLU', 11.98), ('CG', 'HIS', 'CG', 'GLU', 11.04), ('CG', 'HIS', 'CD', 'GLU', 9.82), ('CG', 'HIS', 'OE1', 'GLU', 9.49), ('CG', 'HIS', 'OE2', 'GLU', 9.29)], [('ND1', 'HIS', 'CB', 'GLU', 10.9), ('ND1', 'HIS', 'CG', 'GLU', 9.96), ('ND1', 'HIS', 'CD', 'GLU', 8.66), ('ND1', 'HIS', 'OE1', 'GLU', 8.3), ('ND1', 'HIS', 'OE2', 'GLU', 8.13)], [('CD2', 'HIS', 'CB', 'GLU', 11.61), ('CD2', 'HIS', 'CG', 'GLU', 10.73), ('CD2', 'HIS', 'CD', 'GLU', 9.66), ('CD2', 'HIS', 'OE1', 'GLU', 9.35), ('CD2', 'HIS', 'OE2', 'GLU', 9.27)], [('CE1', 'HIS', 'CB', 'GLU', 9.75), ('CE1', 'HIS', 'CG', 'GLU', 8.85), ('CE1', 'HIS', 'CD', 'GLU', 7.66), ('CE1', 'HIS', 'OE1', 'GLU', 7.3), ('CE1', 'HIS', 'OE2', 'GLU', 7.27)], [('NE2', 'HIS', 'CB', 'GLU', 10.24), ('NE2', 'HIS', 'CG', 'GLU', 9.41), ('NE2', 'HIS', 'CD', 'GLU', 8.39), ('NE2', 'HIS', 'OE1', 'GLU', 8.07), ('NE2', 'HIS', 'OE2', 'GLU', 8.11)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_HIS, d, 'A_1els_4_2_1_11')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_GLU, d, 'A_1els_4_2_1_11')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_GLU, d, 'A_1els_4_2_1_11')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_GLU, d, 'A_1els_4_2_1_11')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_HIS' :  match1,
		'LYS_GLU' :  match2,
		'GLU_GLU' :  match3,
		'HIS_GLU' :  match4}