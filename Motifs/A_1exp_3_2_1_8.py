'''
FUNC:A_1exp_3_2_1_8
PDB:1exp
EC:3.2.1.8
RESI:glu,his,glu,asp
LOCI:a-127,205,233,235;
'''
import motifFunctions as cmd
GLU_ASP = { 
	'distances':
		[[9.06, 8.33, 8.32, 8.16], [10.58, 9.83, 9.8, 9.59], [11.22, 10.27, 10.19, 9.89], [10.64, 9.56, 9.5, 9.04], [12.45, 11.48, 11.36, 11.09], [18.38, 17.06, 16.48, 16.71], [16.87, 15.56, 14.99, 15.23], [16.15, 14.8, 14.27, 14.38], [16.87, 15.48, 14.96, 14.99], [14.94, 13.59, 13.09, 13.16]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 9.06), ('CB', 'GLU', 'CG', 'ASP', 8.33), ('CB', 'GLU', 'OD1', 'ASP', 8.32), ('CB', 'GLU', 'OD2', 'ASP', 8.16)], [('CG', 'GLU', 'CB', 'ASP', 10.58), ('CG', 'GLU', 'CG', 'ASP', 9.83), ('CG', 'GLU', 'OD1', 'ASP', 9.8), ('CG', 'GLU', 'OD2', 'ASP', 9.59)], [('CD', 'GLU', 'CB', 'ASP', 11.22), ('CD', 'GLU', 'CG', 'ASP', 10.27), ('CD', 'GLU', 'OD1', 'ASP', 10.19), ('CD', 'GLU', 'OD2', 'ASP', 9.89)], [('OE1', 'GLU', 'CB', 'ASP', 10.64), ('OE1', 'GLU', 'CG', 'ASP', 9.56), ('OE1', 'GLU', 'OD1', 'ASP', 9.5), ('OE1', 'GLU', 'OD2', 'ASP', 9.04)], [('OE2', 'GLU', 'CB', 'ASP', 12.45), ('OE2', 'GLU', 'CG', 'ASP', 11.48), ('OE2', 'GLU', 'OD1', 'ASP', 11.36), ('OE2', 'GLU', 'OD2', 'ASP', 11.09)], [('CB', 'GLU', 'CB', 'ASP', 18.38), ('CB', 'GLU', 'CG', 'ASP', 17.06), ('CB', 'GLU', 'OD1', 'ASP', 16.48), ('CB', 'GLU', 'OD2', 'ASP', 16.71)], [('CG', 'GLU', 'CB', 'ASP', 16.87), ('CG', 'GLU', 'CG', 'ASP', 15.56), ('CG', 'GLU', 'OD1', 'ASP', 14.99), ('CG', 'GLU', 'OD2', 'ASP', 15.23)], [('CD', 'GLU', 'CB', 'ASP', 16.15), ('CD', 'GLU', 'CG', 'ASP', 14.8), ('CD', 'GLU', 'OD1', 'ASP', 14.27), ('CD', 'GLU', 'OD2', 'ASP', 14.38)], [('OE1', 'GLU', 'CB', 'ASP', 16.87), ('OE1', 'GLU', 'CG', 'ASP', 15.48), ('OE1', 'GLU', 'OD1', 'ASP', 14.96), ('OE1', 'GLU', 'OD2', 'ASP', 14.99)], [('OE2', 'GLU', 'CB', 'ASP', 14.94), ('OE2', 'GLU', 'CG', 'ASP', 13.59), ('OE2', 'GLU', 'OD1', 'ASP', 13.09), ('OE2', 'GLU', 'OD2', 'ASP', 13.16)]]}
GLU_GLU = { 
	'distances':
		[[12.88, 11.38, 11.05, 12.07, 9.89], [12.0, 10.56, 10.37, 11.43, 9.28], [10.79, 9.36, 9.05, 10.06, 7.96], [10.79, 9.33, 8.75, 9.63, 7.58], [9.94, 8.58, 8.42, 9.46, 7.44], [12.88, 12.0, 10.79, 10.79, 9.94], [11.38, 10.56, 9.36, 9.33, 8.58], [11.05, 10.37, 9.05, 8.75, 8.42], [12.07, 11.43, 10.06, 9.63, 9.46], [9.89, 9.28, 7.96, 7.58, 7.44]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 12.88), ('CB', 'GLU', 'CG', 'GLU', 11.38), ('CB', 'GLU', 'CD', 'GLU', 11.05), ('CB', 'GLU', 'OE1', 'GLU', 12.07), ('CB', 'GLU', 'OE2', 'GLU', 9.89)], [('CG', 'GLU', 'CB', 'GLU', 12.0), ('CG', 'GLU', 'CG', 'GLU', 10.56), ('CG', 'GLU', 'CD', 'GLU', 10.37), ('CG', 'GLU', 'OE1', 'GLU', 11.43), ('CG', 'GLU', 'OE2', 'GLU', 9.28)], [('CD', 'GLU', 'CB', 'GLU', 10.79), ('CD', 'GLU', 'CG', 'GLU', 9.36), ('CD', 'GLU', 'CD', 'GLU', 9.05), ('CD', 'GLU', 'OE1', 'GLU', 10.06), ('CD', 'GLU', 'OE2', 'GLU', 7.96)], [('OE1', 'GLU', 'CB', 'GLU', 10.79), ('OE1', 'GLU', 'CG', 'GLU', 9.33), ('OE1', 'GLU', 'CD', 'GLU', 8.75), ('OE1', 'GLU', 'OE1', 'GLU', 9.63), ('OE1', 'GLU', 'OE2', 'GLU', 7.58)], [('OE2', 'GLU', 'CB', 'GLU', 9.94), ('OE2', 'GLU', 'CG', 'GLU', 8.58), ('OE2', 'GLU', 'CD', 'GLU', 8.42), ('OE2', 'GLU', 'OE1', 'GLU', 9.46), ('OE2', 'GLU', 'OE2', 'GLU', 7.44)], [('CB', 'GLU', 'CB', 'GLU', 12.88), ('CB', 'GLU', 'CG', 'GLU', 12.0), ('CB', 'GLU', 'CD', 'GLU', 10.79), ('CB', 'GLU', 'OE1', 'GLU', 10.79), ('CB', 'GLU', 'OE2', 'GLU', 9.94)], [('CG', 'GLU', 'CB', 'GLU', 11.38), ('CG', 'GLU', 'CG', 'GLU', 10.56), ('CG', 'GLU', 'CD', 'GLU', 9.36), ('CG', 'GLU', 'OE1', 'GLU', 9.33), ('CG', 'GLU', 'OE2', 'GLU', 8.58)], [('CD', 'GLU', 'CB', 'GLU', 11.05), ('CD', 'GLU', 'CG', 'GLU', 10.37), ('CD', 'GLU', 'CD', 'GLU', 9.05), ('CD', 'GLU', 'OE1', 'GLU', 8.75), ('CD', 'GLU', 'OE2', 'GLU', 8.42)], [('OE1', 'GLU', 'CB', 'GLU', 12.07), ('OE1', 'GLU', 'CG', 'GLU', 11.43), ('OE1', 'GLU', 'CD', 'GLU', 10.06), ('OE1', 'GLU', 'OE1', 'GLU', 9.63), ('OE1', 'GLU', 'OE2', 'GLU', 9.46)], [('OE2', 'GLU', 'CB', 'GLU', 9.89), ('OE2', 'GLU', 'CG', 'GLU', 9.28), ('OE2', 'GLU', 'CD', 'GLU', 7.96), ('OE2', 'GLU', 'OE1', 'GLU', 7.58), ('OE2', 'GLU', 'OE2', 'GLU', 7.44)]]}
HIS_ASP = { 
	'distances':
		[[8.08, 6.85, 5.77, 7.21], [7.87, 6.55, 5.74, 6.62], [6.77, 5.42, 4.9, 5.35], [8.93, 7.6, 6.95, 7.47], [7.39, 6.1, 5.91, 5.7], [8.66, 7.36, 7.01, 6.99]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 8.08), ('CB', 'HIS', 'CG', 'ASP', 6.85), ('CB', 'HIS', 'OD1', 'ASP', 5.77), ('CB', 'HIS', 'OD2', 'ASP', 7.21)], [('CG', 'HIS', 'CB', 'ASP', 7.87), ('CG', 'HIS', 'CG', 'ASP', 6.55), ('CG', 'HIS', 'OD1', 'ASP', 5.74), ('CG', 'HIS', 'OD2', 'ASP', 6.62)], [('ND1', 'HIS', 'CB', 'ASP', 6.77), ('ND1', 'HIS', 'CG', 'ASP', 5.42), ('ND1', 'HIS', 'OD1', 'ASP', 4.9), ('ND1', 'HIS', 'OD2', 'ASP', 5.35)], [('CD2', 'HIS', 'CB', 'ASP', 8.93), ('CD2', 'HIS', 'CG', 'ASP', 7.6), ('CD2', 'HIS', 'OD1', 'ASP', 6.95), ('CD2', 'HIS', 'OD2', 'ASP', 7.47)], [('CE1', 'HIS', 'CB', 'ASP', 7.39), ('CE1', 'HIS', 'CG', 'ASP', 6.1), ('CE1', 'HIS', 'OD1', 'ASP', 5.91), ('CE1', 'HIS', 'OD2', 'ASP', 5.7)], [('NE2', 'HIS', 'CB', 'ASP', 8.66), ('NE2', 'HIS', 'CG', 'ASP', 7.36), ('NE2', 'HIS', 'OD1', 'ASP', 7.01), ('NE2', 'HIS', 'OD2', 'ASP', 6.99)]]}
HIS_GLU = { 
	'distances':
		[[8.05, 9.13, 9.11, 8.44, 10.0], [6.8, 7.86, 7.77, 7.02, 8.71], [6.35, 7.61, 7.67, 6.85, 8.76], [6.34, 7.12, 6.77, 5.96, 7.6], [5.55, 6.7, 6.62, 5.69, 7.73], [5.52, 6.32, 5.92, 4.94, 6.89], [13.38, 11.96, 11.35, 12.06, 10.29], [12.77, 11.3, 10.63, 11.37, 9.48], [13.65, 12.16, 11.43, 12.16, 10.23], [11.52, 10.03, 9.35, 10.13, 8.19], [13.09, 11.59, 10.82, 11.56, 9.6], [11.78, 10.27, 9.52, 10.29, 8.3]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 8.05), ('CB', 'HIS', 'CG', 'GLU', 9.13), ('CB', 'HIS', 'CD', 'GLU', 9.11), ('CB', 'HIS', 'OE1', 'GLU', 8.44), ('CB', 'HIS', 'OE2', 'GLU', 10.0)], [('CG', 'HIS', 'CB', 'GLU', 6.8), ('CG', 'HIS', 'CG', 'GLU', 7.86), ('CG', 'HIS', 'CD', 'GLU', 7.77), ('CG', 'HIS', 'OE1', 'GLU', 7.02), ('CG', 'HIS', 'OE2', 'GLU', 8.71)], [('ND1', 'HIS', 'CB', 'GLU', 6.35), ('ND1', 'HIS', 'CG', 'GLU', 7.61), ('ND1', 'HIS', 'CD', 'GLU', 7.67), ('ND1', 'HIS', 'OE1', 'GLU', 6.85), ('ND1', 'HIS', 'OE2', 'GLU', 8.76)], [('CD2', 'HIS', 'CB', 'GLU', 6.34), ('CD2', 'HIS', 'CG', 'GLU', 7.12), ('CD2', 'HIS', 'CD', 'GLU', 6.77), ('CD2', 'HIS', 'OE1', 'GLU', 5.96), ('CD2', 'HIS', 'OE2', 'GLU', 7.6)], [('CE1', 'HIS', 'CB', 'GLU', 5.55), ('CE1', 'HIS', 'CG', 'GLU', 6.7), ('CE1', 'HIS', 'CD', 'GLU', 6.62), ('CE1', 'HIS', 'OE1', 'GLU', 5.69), ('CE1', 'HIS', 'OE2', 'GLU', 7.73)], [('NE2', 'HIS', 'CB', 'GLU', 5.52), ('NE2', 'HIS', 'CG', 'GLU', 6.32), ('NE2', 'HIS', 'CD', 'GLU', 5.92), ('NE2', 'HIS', 'OE1', 'GLU', 4.94), ('NE2', 'HIS', 'OE2', 'GLU', 6.89)], [('CB', 'HIS', 'CB', 'GLU', 13.38), ('CB', 'HIS', 'CG', 'GLU', 11.96), ('CB', 'HIS', 'CD', 'GLU', 11.35), ('CB', 'HIS', 'OE1', 'GLU', 12.06), ('CB', 'HIS', 'OE2', 'GLU', 10.29)], [('CG', 'HIS', 'CB', 'GLU', 12.77), ('CG', 'HIS', 'CG', 'GLU', 11.3), ('CG', 'HIS', 'CD', 'GLU', 10.63), ('CG', 'HIS', 'OE1', 'GLU', 11.37), ('CG', 'HIS', 'OE2', 'GLU', 9.48)], [('ND1', 'HIS', 'CB', 'GLU', 13.65), ('ND1', 'HIS', 'CG', 'GLU', 12.16), ('ND1', 'HIS', 'CD', 'GLU', 11.43), ('ND1', 'HIS', 'OE1', 'GLU', 12.16), ('ND1', 'HIS', 'OE2', 'GLU', 10.23)], [('CD2', 'HIS', 'CB', 'GLU', 11.52), ('CD2', 'HIS', 'CG', 'GLU', 10.03), ('CD2', 'HIS', 'CD', 'GLU', 9.35), ('CD2', 'HIS', 'OE1', 'GLU', 10.13), ('CD2', 'HIS', 'OE2', 'GLU', 8.19)], [('CE1', 'HIS', 'CB', 'GLU', 13.09), ('CE1', 'HIS', 'CG', 'GLU', 11.59), ('CE1', 'HIS', 'CD', 'GLU', 10.82), ('CE1', 'HIS', 'OE1', 'GLU', 11.56), ('CE1', 'HIS', 'OE2', 'GLU', 9.6)], [('NE2', 'HIS', 'CB', 'GLU', 11.78), ('NE2', 'HIS', 'CG', 'GLU', 10.27), ('NE2', 'HIS', 'CD', 'GLU', 9.52), ('NE2', 'HIS', 'OE1', 'GLU', 10.29), ('NE2', 'HIS', 'OE2', 'GLU', 8.3)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_ASP, d, 'A_1exp_3_2_1_8')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_GLU, d, 'A_1exp_3_2_1_8')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASP, d, 'A_1exp_3_2_1_8')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_GLU, d, 'A_1exp_3_2_1_8')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_ASP' :  match1,
		'GLU_GLU' :  match2,
		'HIS_ASP' :  match3,
		'HIS_GLU' :  match4}