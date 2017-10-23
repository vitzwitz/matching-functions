'''
FUNC:P_1pjb_1_4_1_1
PDB:1pjb
EC:1.4.1.1
RESI:lys,his,glu,asp
LOCI:a-74,95,117,269;
'''
import motifFunctions as cmd
LYS_HIS = { 
	'distances':
		[[11.19, 10.97, 9.9, 11.89, 10.31, 11.5], [11.27, 10.87, 9.78, 11.63, 10.0, 11.13], [10.52, 9.93, 8.74, 10.59, 8.81, 9.95], [9.53, 8.88, 7.79, 9.45, 7.81, 8.84], [8.93, 8.03, 6.85, 8.44, 6.61, 7.64]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'HIS', 11.19), ('CB', 'LYS', 'CG', 'HIS', 10.97), ('CB', 'LYS', 'ND1', 'HIS', 9.9), ('CB', 'LYS', 'CD2', 'HIS', 11.89), ('CB', 'LYS', 'CE1', 'HIS', 10.31), ('CB', 'LYS', 'NE2', 'HIS', 11.5)], [('CG', 'LYS', 'CB', 'HIS', 11.27), ('CG', 'LYS', 'CG', 'HIS', 10.87), ('CG', 'LYS', 'ND1', 'HIS', 9.78), ('CG', 'LYS', 'CD2', 'HIS', 11.63), ('CG', 'LYS', 'CE1', 'HIS', 10.0), ('CG', 'LYS', 'NE2', 'HIS', 11.13)], [('CD', 'LYS', 'CB', 'HIS', 10.52), ('CD', 'LYS', 'CG', 'HIS', 9.93), ('CD', 'LYS', 'ND1', 'HIS', 8.74), ('CD', 'LYS', 'CD2', 'HIS', 10.59), ('CD', 'LYS', 'CE1', 'HIS', 8.81), ('CD', 'LYS', 'NE2', 'HIS', 9.95)], [('CE', 'LYS', 'CB', 'HIS', 9.53), ('CE', 'LYS', 'CG', 'HIS', 8.88), ('CE', 'LYS', 'ND1', 'HIS', 7.79), ('CE', 'LYS', 'CD2', 'HIS', 9.45), ('CE', 'LYS', 'CE1', 'HIS', 7.81), ('CE', 'LYS', 'NE2', 'HIS', 8.84)], [('NZ', 'LYS', 'CB', 'HIS', 8.93), ('NZ', 'LYS', 'CG', 'HIS', 8.03), ('NZ', 'LYS', 'ND1', 'HIS', 6.85), ('NZ', 'LYS', 'CD2', 'HIS', 8.44), ('NZ', 'LYS', 'CE1', 'HIS', 6.61), ('NZ', 'LYS', 'NE2', 'HIS', 7.64)]]}
HIS_ASP = { 
	'distances':
		[[11.63, 11.04, 11.85, 9.93], [10.94, 10.17, 10.89, 9.01], [11.29, 10.45, 11.16, 9.23], [10.16, 9.25, 9.85, 8.14], [10.82, 9.82, 10.41, 8.6], [10.1, 9.03, 9.54, 7.87]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 11.63), ('CB', 'HIS', 'CG', 'ASP', 11.04), ('CB', 'HIS', 'OD1', 'ASP', 11.85), ('CB', 'HIS', 'OD2', 'ASP', 9.93)], [('CG', 'HIS', 'CB', 'ASP', 10.94), ('CG', 'HIS', 'CG', 'ASP', 10.17), ('CG', 'HIS', 'OD1', 'ASP', 10.89), ('CG', 'HIS', 'OD2', 'ASP', 9.01)], [('ND1', 'HIS', 'CB', 'ASP', 11.29), ('ND1', 'HIS', 'CG', 'ASP', 10.45), ('ND1', 'HIS', 'OD1', 'ASP', 11.16), ('ND1', 'HIS', 'OD2', 'ASP', 9.23)], [('CD2', 'HIS', 'CB', 'ASP', 10.16), ('CD2', 'HIS', 'CG', 'ASP', 9.25), ('CD2', 'HIS', 'OD1', 'ASP', 9.85), ('CD2', 'HIS', 'OD2', 'ASP', 8.14)], [('CE1', 'HIS', 'CB', 'ASP', 10.82), ('CE1', 'HIS', 'CG', 'ASP', 9.82), ('CE1', 'HIS', 'OD1', 'ASP', 10.41), ('CE1', 'HIS', 'OD2', 'ASP', 8.6)], [('NE2', 'HIS', 'CB', 'ASP', 10.1), ('NE2', 'HIS', 'CG', 'ASP', 9.03), ('NE2', 'HIS', 'OD1', 'ASP', 9.54), ('NE2', 'HIS', 'OD2', 'ASP', 7.87)]]}
LYS_ASP = { 
	'distances':
		[[15.24, 14.91, 15.86, 13.8], [14.24, 13.91, 14.83, 12.84], [13.57, 13.08, 13.93, 11.97], [12.09, 11.62, 12.5, 10.51], [11.6, 10.93, 11.69, 9.76]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASP', 15.24), ('CB', 'LYS', 'CG', 'ASP', 14.91), ('CB', 'LYS', 'OD1', 'ASP', 15.86), ('CB', 'LYS', 'OD2', 'ASP', 13.8)], [('CG', 'LYS', 'CB', 'ASP', 14.24), ('CG', 'LYS', 'CG', 'ASP', 13.91), ('CG', 'LYS', 'OD1', 'ASP', 14.83), ('CG', 'LYS', 'OD2', 'ASP', 12.84)], [('CD', 'LYS', 'CB', 'ASP', 13.57), ('CD', 'LYS', 'CG', 'ASP', 13.08), ('CD', 'LYS', 'OD1', 'ASP', 13.93), ('CD', 'LYS', 'OD2', 'ASP', 11.97)], [('CE', 'LYS', 'CB', 'ASP', 12.09), ('CE', 'LYS', 'CG', 'ASP', 11.62), ('CE', 'LYS', 'OD1', 'ASP', 12.5), ('CE', 'LYS', 'OD2', 'ASP', 10.51)], [('NZ', 'LYS', 'CB', 'ASP', 11.6), ('NZ', 'LYS', 'CG', 'ASP', 10.93), ('NZ', 'LYS', 'OD1', 'ASP', 11.69), ('NZ', 'LYS', 'OD2', 'ASP', 9.76)]]}
HIS_GLU = { 
	'distances':
		[[8.67, 7.56, 6.91, 7.49, 6.22], [7.7, 6.86, 6.43, 6.92, 6.14], [7.33, 6.77, 6.18, 6.32, 6.16], [7.48, 6.82, 6.82, 7.41, 6.74], [6.85, 6.65, 6.41, 6.48, 6.73], [6.94, 6.68, 6.79, 7.15, 7.05]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 8.67), ('CB', 'HIS', 'CG', 'GLU', 7.56), ('CB', 'HIS', 'CD', 'GLU', 6.91), ('CB', 'HIS', 'OE1', 'GLU', 7.49), ('CB', 'HIS', 'OE2', 'GLU', 6.22)], [('CG', 'HIS', 'CB', 'GLU', 7.7), ('CG', 'HIS', 'CG', 'GLU', 6.86), ('CG', 'HIS', 'CD', 'GLU', 6.43), ('CG', 'HIS', 'OE1', 'GLU', 6.92), ('CG', 'HIS', 'OE2', 'GLU', 6.14)], [('ND1', 'HIS', 'CB', 'GLU', 7.33), ('ND1', 'HIS', 'CG', 'GLU', 6.77), ('ND1', 'HIS', 'CD', 'GLU', 6.18), ('ND1', 'HIS', 'OE1', 'GLU', 6.32), ('ND1', 'HIS', 'OE2', 'GLU', 6.16)], [('CD2', 'HIS', 'CB', 'GLU', 7.48), ('CD2', 'HIS', 'CG', 'GLU', 6.82), ('CD2', 'HIS', 'CD', 'GLU', 6.82), ('CD2', 'HIS', 'OE1', 'GLU', 7.41), ('CD2', 'HIS', 'OE2', 'GLU', 6.74)], [('CE1', 'HIS', 'CB', 'GLU', 6.85), ('CE1', 'HIS', 'CG', 'GLU', 6.65), ('CE1', 'HIS', 'CD', 'GLU', 6.41), ('CE1', 'HIS', 'OE1', 'GLU', 6.48), ('CE1', 'HIS', 'OE2', 'GLU', 6.73)], [('NE2', 'HIS', 'CB', 'GLU', 6.94), ('NE2', 'HIS', 'CG', 'GLU', 6.68), ('NE2', 'HIS', 'CD', 'GLU', 6.79), ('NE2', 'HIS', 'OE1', 'GLU', 7.15), ('NE2', 'HIS', 'OE2', 'GLU', 7.05)]]}
GLU_ASP = { 
	'distances':
		[[14.7, 13.44, 13.61, 12.39], [14.59, 13.43, 13.71, 12.37], [14.85, 13.8, 14.23, 12.66], [15.22, 14.16, 14.61, 12.98], [14.89, 13.95, 14.46, 12.81]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 14.7), ('CB', 'GLU', 'CG', 'ASP', 13.44), ('CB', 'GLU', 'OD1', 'ASP', 13.61), ('CB', 'GLU', 'OD2', 'ASP', 12.39)], [('CG', 'GLU', 'CB', 'ASP', 14.59), ('CG', 'GLU', 'CG', 'ASP', 13.43), ('CG', 'GLU', 'OD1', 'ASP', 13.71), ('CG', 'GLU', 'OD2', 'ASP', 12.37)], [('CD', 'GLU', 'CB', 'ASP', 14.85), ('CD', 'GLU', 'CG', 'ASP', 13.8), ('CD', 'GLU', 'OD1', 'ASP', 14.23), ('CD', 'GLU', 'OD2', 'ASP', 12.66)], [('OE1', 'GLU', 'CB', 'ASP', 15.22), ('OE1', 'GLU', 'CG', 'ASP', 14.16), ('OE1', 'GLU', 'OD1', 'ASP', 14.61), ('OE1', 'GLU', 'OD2', 'ASP', 12.98)], [('OE2', 'GLU', 'CB', 'ASP', 14.89), ('OE2', 'GLU', 'CG', 'ASP', 13.95), ('OE2', 'GLU', 'OD1', 'ASP', 14.46), ('OE2', 'GLU', 'OD2', 'ASP', 12.81)]]}
LYS_GLU = { 
	'distances':
		[[13.59, 13.5, 12.34, 11.57, 12.4], [13.56, 13.59, 12.57, 11.84, 12.72], [12.25, 12.38, 11.47, 10.71, 11.74], [11.75, 11.82, 11.01, 10.41, 11.23], [10.43, 10.61, 9.96, 9.38, 10.32]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'GLU', 13.59), ('CB', 'LYS', 'CG', 'GLU', 13.5), ('CB', 'LYS', 'CD', 'GLU', 12.34), ('CB', 'LYS', 'OE1', 'GLU', 11.57), ('CB', 'LYS', 'OE2', 'GLU', 12.4)], [('CG', 'LYS', 'CB', 'GLU', 13.56), ('CG', 'LYS', 'CG', 'GLU', 13.59), ('CG', 'LYS', 'CD', 'GLU', 12.57), ('CG', 'LYS', 'OE1', 'GLU', 11.84), ('CG', 'LYS', 'OE2', 'GLU', 12.72)], [('CD', 'LYS', 'CB', 'GLU', 12.25), ('CD', 'LYS', 'CG', 'GLU', 12.38), ('CD', 'LYS', 'CD', 'GLU', 11.47), ('CD', 'LYS', 'OE1', 'GLU', 10.71), ('CD', 'LYS', 'OE2', 'GLU', 11.74)], [('CE', 'LYS', 'CB', 'GLU', 11.75), ('CE', 'LYS', 'CG', 'GLU', 11.82), ('CE', 'LYS', 'CD', 'GLU', 11.01), ('CE', 'LYS', 'OE1', 'GLU', 10.41), ('CE', 'LYS', 'OE2', 'GLU', 11.23)], [('NZ', 'LYS', 'CB', 'GLU', 10.43), ('NZ', 'LYS', 'CG', 'GLU', 10.61), ('NZ', 'LYS', 'CD', 'GLU', 9.96), ('NZ', 'LYS', 'OE1', 'GLU', 9.38), ('NZ', 'LYS', 'OE2', 'GLU', 10.32)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_HIS, d, 'P_1pjb_1_4_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'P_1pjb_1_4_1_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LYS_ASP, d, 'P_1pjb_1_4_1_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_GLU, d, 'P_1pjb_1_4_1_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLU_ASP, d, 'P_1pjb_1_4_1_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(LYS_GLU, d, 'P_1pjb_1_4_1_1')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_HIS' :  match1,
		'HIS_ASP' :  match2,
		'LYS_ASP' :  match3,
		'HIS_GLU' :  match4,
		'GLU_ASP' :  match5,
		'LYS_GLU' :  match6}