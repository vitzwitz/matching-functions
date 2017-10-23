'''
FUNC:A_1bs0_2_3_1_47
PDB:1bs0
EC:2.3.1.47
RESI:his,glu,asp,lys
LOCI:a-133,175,204,236;
'''
import motifFunctions as cmd
GLU_LYS = { 
	'distances':
		[[13.96, 13.47, 12.01, 12.0, 12.22], [13.91, 13.24, 11.76, 11.52, 11.61], [13.39, 12.62, 11.12, 10.76, 10.98], [12.23, 11.47, 9.97, 9.69, 10.02], [14.25, 13.38, 11.89, 11.39, 11.62]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LYS', 13.96), ('CB', 'GLU', 'CG', 'LYS', 13.47), ('CB', 'GLU', 'CD', 'LYS', 12.01), ('CB', 'GLU', 'CE', 'LYS', 12.0), ('CB', 'GLU', 'NZ', 'LYS', 12.22)], [('CG', 'GLU', 'CB', 'LYS', 13.91), ('CG', 'GLU', 'CG', 'LYS', 13.24), ('CG', 'GLU', 'CD', 'LYS', 11.76), ('CG', 'GLU', 'CE', 'LYS', 11.52), ('CG', 'GLU', 'NZ', 'LYS', 11.61)], [('CD', 'GLU', 'CB', 'LYS', 13.39), ('CD', 'GLU', 'CG', 'LYS', 12.62), ('CD', 'GLU', 'CD', 'LYS', 11.12), ('CD', 'GLU', 'CE', 'LYS', 10.76), ('CD', 'GLU', 'NZ', 'LYS', 10.98)], [('OE1', 'GLU', 'CB', 'LYS', 12.23), ('OE1', 'GLU', 'CG', 'LYS', 11.47), ('OE1', 'GLU', 'CD', 'LYS', 9.97), ('OE1', 'GLU', 'CE', 'LYS', 9.69), ('OE1', 'GLU', 'NZ', 'LYS', 10.02)], [('OE2', 'GLU', 'CB', 'LYS', 14.25), ('OE2', 'GLU', 'CG', 'LYS', 13.38), ('OE2', 'GLU', 'CD', 'LYS', 11.89), ('OE2', 'GLU', 'CE', 'LYS', 11.39), ('OE2', 'GLU', 'NZ', 'LYS', 11.62)]]}
ASP_HIS = { 
	'distances':
		[[9.56, 8.24, 8.22, 7.13, 7.15, 6.33], [8.89, 7.46, 7.17, 6.48, 5.97, 5.39], [8.99, 7.57, 7.02, 6.85, 5.84, 5.67], [8.51, 7.05, 6.8, 6.01, 5.56, 4.86]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 9.56), ('CB', 'ASP', 'CG', 'HIS', 8.24), ('CB', 'ASP', 'ND1', 'HIS', 8.22), ('CB', 'ASP', 'CD2', 'HIS', 7.13), ('CB', 'ASP', 'CE1', 'HIS', 7.15), ('CB', 'ASP', 'NE2', 'HIS', 6.33)], [('CG', 'ASP', 'CB', 'HIS', 8.89), ('CG', 'ASP', 'CG', 'HIS', 7.46), ('CG', 'ASP', 'ND1', 'HIS', 7.17), ('CG', 'ASP', 'CD2', 'HIS', 6.48), ('CG', 'ASP', 'CE1', 'HIS', 5.97), ('CG', 'ASP', 'NE2', 'HIS', 5.39)], [('OD1', 'ASP', 'CB', 'HIS', 8.99), ('OD1', 'ASP', 'CG', 'HIS', 7.57), ('OD1', 'ASP', 'ND1', 'HIS', 7.02), ('OD1', 'ASP', 'CD2', 'HIS', 6.85), ('OD1', 'ASP', 'CE1', 'HIS', 5.84), ('OD1', 'ASP', 'NE2', 'HIS', 5.67)], [('OD2', 'ASP', 'CB', 'HIS', 8.51), ('OD2', 'ASP', 'CG', 'HIS', 7.05), ('OD2', 'ASP', 'ND1', 'HIS', 6.8), ('OD2', 'ASP', 'CD2', 'HIS', 6.01), ('OD2', 'ASP', 'CE1', 'HIS', 5.56), ('OD2', 'ASP', 'NE2', 'HIS', 4.86)]]}
GLU_HIS = { 
	'distances':
		[[8.36, 7.81, 8.12, 7.42, 7.96, 7.54], [7.07, 6.47, 6.97, 5.99, 6.85, 6.27], [5.92, 5.6, 6.12, 5.59, 6.39, 6.1], [6.01, 5.59, 5.7, 5.84, 6.0, 6.08], [5.41, 5.54, 6.38, 5.68, 6.91, 6.55]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 8.36), ('CB', 'GLU', 'CG', 'HIS', 7.81), ('CB', 'GLU', 'ND1', 'HIS', 8.12), ('CB', 'GLU', 'CD2', 'HIS', 7.42), ('CB', 'GLU', 'CE1', 'HIS', 7.96), ('CB', 'GLU', 'NE2', 'HIS', 7.54)], [('CG', 'GLU', 'CB', 'HIS', 7.07), ('CG', 'GLU', 'CG', 'HIS', 6.47), ('CG', 'GLU', 'ND1', 'HIS', 6.97), ('CG', 'GLU', 'CD2', 'HIS', 5.99), ('CG', 'GLU', 'CE1', 'HIS', 6.85), ('CG', 'GLU', 'NE2', 'HIS', 6.27)], [('CD', 'GLU', 'CB', 'HIS', 5.92), ('CD', 'GLU', 'CG', 'HIS', 5.6), ('CD', 'GLU', 'ND1', 'HIS', 6.12), ('CD', 'GLU', 'CD2', 'HIS', 5.59), ('CD', 'GLU', 'CE1', 'HIS', 6.39), ('CD', 'GLU', 'NE2', 'HIS', 6.1)], [('OE1', 'GLU', 'CB', 'HIS', 6.01), ('OE1', 'GLU', 'CG', 'HIS', 5.59), ('OE1', 'GLU', 'ND1', 'HIS', 5.7), ('OE1', 'GLU', 'CD2', 'HIS', 5.84), ('OE1', 'GLU', 'CE1', 'HIS', 6.0), ('OE1', 'GLU', 'NE2', 'HIS', 6.08)], [('OE2', 'GLU', 'CB', 'HIS', 5.41), ('OE2', 'GLU', 'CG', 'HIS', 5.54), ('OE2', 'GLU', 'ND1', 'HIS', 6.38), ('OE2', 'GLU', 'CD2', 'HIS', 5.68), ('OE2', 'GLU', 'CE1', 'HIS', 6.91), ('OE2', 'GLU', 'NE2', 'HIS', 6.55)]]}
ASP_GLU = { 
	'distances':
		[[7.0, 6.54, 7.64, 7.85, 8.53], [7.39, 6.77, 7.51, 7.47, 8.44], [7.34, 6.91, 7.49, 7.18, 8.54], [8.19, 7.31, 7.87, 7.88, 8.63]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 7.0), ('CB', 'ASP', 'CG', 'GLU', 6.54), ('CB', 'ASP', 'CD', 'GLU', 7.64), ('CB', 'ASP', 'OE1', 'GLU', 7.85), ('CB', 'ASP', 'OE2', 'GLU', 8.53)], [('CG', 'ASP', 'CB', 'GLU', 7.39), ('CG', 'ASP', 'CG', 'GLU', 6.77), ('CG', 'ASP', 'CD', 'GLU', 7.51), ('CG', 'ASP', 'OE1', 'GLU', 7.47), ('CG', 'ASP', 'OE2', 'GLU', 8.44)], [('OD1', 'ASP', 'CB', 'GLU', 7.34), ('OD1', 'ASP', 'CG', 'GLU', 6.91), ('OD1', 'ASP', 'CD', 'GLU', 7.49), ('OD1', 'ASP', 'OE1', 'GLU', 7.18), ('OD1', 'ASP', 'OE2', 'GLU', 8.54)], [('OD2', 'ASP', 'CB', 'GLU', 8.19), ('OD2', 'ASP', 'CG', 'GLU', 7.31), ('OD2', 'ASP', 'CD', 'GLU', 7.87), ('OD2', 'ASP', 'OE1', 'GLU', 7.88), ('OD2', 'ASP', 'OE2', 'GLU', 8.63)]]}
ASP_LYS = { 
	'distances':
		[[13.5, 13.01, 11.73, 11.64, 11.15], [12.22, 11.64, 10.38, 10.23, 9.67], [11.09, 10.59, 9.33, 9.32, 8.87], [12.43, 11.72, 10.48, 10.13, 9.41]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 13.5), ('CB', 'ASP', 'CG', 'LYS', 13.01), ('CB', 'ASP', 'CD', 'LYS', 11.73), ('CB', 'ASP', 'CE', 'LYS', 11.64), ('CB', 'ASP', 'NZ', 'LYS', 11.15)], [('CG', 'ASP', 'CB', 'LYS', 12.22), ('CG', 'ASP', 'CG', 'LYS', 11.64), ('CG', 'ASP', 'CD', 'LYS', 10.38), ('CG', 'ASP', 'CE', 'LYS', 10.23), ('CG', 'ASP', 'NZ', 'LYS', 9.67)], [('OD1', 'ASP', 'CB', 'LYS', 11.09), ('OD1', 'ASP', 'CG', 'LYS', 10.59), ('OD1', 'ASP', 'CD', 'LYS', 9.33), ('OD1', 'ASP', 'CE', 'LYS', 9.32), ('OD1', 'ASP', 'NZ', 'LYS', 8.87)], [('OD2', 'ASP', 'CB', 'LYS', 12.43), ('OD2', 'ASP', 'CG', 'LYS', 11.72), ('OD2', 'ASP', 'CD', 'LYS', 10.48), ('OD2', 'ASP', 'CE', 'LYS', 10.13), ('OD2', 'ASP', 'NZ', 'LYS', 9.41)]]}
HIS_LYS = { 
	'distances':
		[[13.42, 12.23, 10.84, 9.87, 9.89], [12.63, 11.5, 10.09, 9.19, 9.04], [11.27, 10.12, 8.72, 7.83, 7.67], [13.13, 12.07, 10.66, 9.87, 9.55], [10.99, 9.94, 8.56, 7.8, 7.43], [12.18, 11.18, 9.8, 9.1, 8.65]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'LYS', 13.42), ('CB', 'HIS', 'CG', 'LYS', 12.23), ('CB', 'HIS', 'CD', 'LYS', 10.84), ('CB', 'HIS', 'CE', 'LYS', 9.87), ('CB', 'HIS', 'NZ', 'LYS', 9.89)], [('CG', 'HIS', 'CB', 'LYS', 12.63), ('CG', 'HIS', 'CG', 'LYS', 11.5), ('CG', 'HIS', 'CD', 'LYS', 10.09), ('CG', 'HIS', 'CE', 'LYS', 9.19), ('CG', 'HIS', 'NZ', 'LYS', 9.04)], [('ND1', 'HIS', 'CB', 'LYS', 11.27), ('ND1', 'HIS', 'CG', 'LYS', 10.12), ('ND1', 'HIS', 'CD', 'LYS', 8.72), ('ND1', 'HIS', 'CE', 'LYS', 7.83), ('ND1', 'HIS', 'NZ', 'LYS', 7.67)], [('CD2', 'HIS', 'CB', 'LYS', 13.13), ('CD2', 'HIS', 'CG', 'LYS', 12.07), ('CD2', 'HIS', 'CD', 'LYS', 10.66), ('CD2', 'HIS', 'CE', 'LYS', 9.87), ('CD2', 'HIS', 'NZ', 'LYS', 9.55)], [('CE1', 'HIS', 'CB', 'LYS', 10.99), ('CE1', 'HIS', 'CG', 'LYS', 9.94), ('CE1', 'HIS', 'CD', 'LYS', 8.56), ('CE1', 'HIS', 'CE', 'LYS', 7.8), ('CE1', 'HIS', 'NZ', 'LYS', 7.43)], [('NE2', 'HIS', 'CB', 'LYS', 12.18), ('NE2', 'HIS', 'CG', 'LYS', 11.18), ('NE2', 'HIS', 'CD', 'LYS', 9.8), ('NE2', 'HIS', 'CE', 'LYS', 9.1), ('NE2', 'HIS', 'NZ', 'LYS', 8.65)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_LYS, d, 'A_1bs0_2_3_1_47')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'A_1bs0_2_3_1_47')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_HIS, d, 'A_1bs0_2_3_1_47')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_GLU, d, 'A_1bs0_2_3_1_47')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_LYS, d, 'A_1bs0_2_3_1_47')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(HIS_LYS, d, 'A_1bs0_2_3_1_47')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_LYS' :  match1,
		'ASP_HIS' :  match2,
		'GLU_HIS' :  match3,
		'ASP_GLU' :  match4,
		'ASP_LYS' :  match5,
		'HIS_LYS' :  match6}