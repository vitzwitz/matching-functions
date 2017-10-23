'''
FUNC:A_1pjb_1_4_1_1
PDB:1pjb
EC:1.4.1.1
RESI:lys,his,glu,asp
LOCI:a-74,95,117,269;
'''
import motifFunctions as cmd
GLU_LYS = { 
	'distances':
		[[13.59, 13.56, 12.25, 11.75, 10.43], [13.5, 13.59, 12.38, 11.82, 10.61], [12.34, 12.57, 11.47, 11.01, 9.96], [11.57, 11.84, 10.71, 10.41, 9.38], [12.4, 12.72, 11.74, 11.23, 10.32]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LYS', 13.59), ('CB', 'GLU', 'CG', 'LYS', 13.56), ('CB', 'GLU', 'CD', 'LYS', 12.25), ('CB', 'GLU', 'CE', 'LYS', 11.75), ('CB', 'GLU', 'NZ', 'LYS', 10.43)], [('CG', 'GLU', 'CB', 'LYS', 13.5), ('CG', 'GLU', 'CG', 'LYS', 13.59), ('CG', 'GLU', 'CD', 'LYS', 12.38), ('CG', 'GLU', 'CE', 'LYS', 11.82), ('CG', 'GLU', 'NZ', 'LYS', 10.61)], [('CD', 'GLU', 'CB', 'LYS', 12.34), ('CD', 'GLU', 'CG', 'LYS', 12.57), ('CD', 'GLU', 'CD', 'LYS', 11.47), ('CD', 'GLU', 'CE', 'LYS', 11.01), ('CD', 'GLU', 'NZ', 'LYS', 9.96)], [('OE1', 'GLU', 'CB', 'LYS', 11.57), ('OE1', 'GLU', 'CG', 'LYS', 11.84), ('OE1', 'GLU', 'CD', 'LYS', 10.71), ('OE1', 'GLU', 'CE', 'LYS', 10.41), ('OE1', 'GLU', 'NZ', 'LYS', 9.38)], [('OE2', 'GLU', 'CB', 'LYS', 12.4), ('OE2', 'GLU', 'CG', 'LYS', 12.72), ('OE2', 'GLU', 'CD', 'LYS', 11.74), ('OE2', 'GLU', 'CE', 'LYS', 11.23), ('OE2', 'GLU', 'NZ', 'LYS', 10.32)]]}
HIS_ASP = { 
	'distances':
		[[11.63, 11.04, 11.85, 9.93], [10.94, 10.17, 10.89, 9.01], [11.29, 10.45, 11.16, 9.23], [10.16, 9.25, 9.85, 8.14], [10.82, 9.82, 10.41, 8.6], [10.1, 9.03, 9.54, 7.87]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 11.63), ('CB', 'HIS', 'CG', 'ASP', 11.04), ('CB', 'HIS', 'OD1', 'ASP', 11.85), ('CB', 'HIS', 'OD2', 'ASP', 9.93)], [('CG', 'HIS', 'CB', 'ASP', 10.94), ('CG', 'HIS', 'CG', 'ASP', 10.17), ('CG', 'HIS', 'OD1', 'ASP', 10.89), ('CG', 'HIS', 'OD2', 'ASP', 9.01)], [('ND1', 'HIS', 'CB', 'ASP', 11.29), ('ND1', 'HIS', 'CG', 'ASP', 10.45), ('ND1', 'HIS', 'OD1', 'ASP', 11.16), ('ND1', 'HIS', 'OD2', 'ASP', 9.23)], [('CD2', 'HIS', 'CB', 'ASP', 10.16), ('CD2', 'HIS', 'CG', 'ASP', 9.25), ('CD2', 'HIS', 'OD1', 'ASP', 9.85), ('CD2', 'HIS', 'OD2', 'ASP', 8.14)], [('CE1', 'HIS', 'CB', 'ASP', 10.82), ('CE1', 'HIS', 'CG', 'ASP', 9.82), ('CE1', 'HIS', 'OD1', 'ASP', 10.41), ('CE1', 'HIS', 'OD2', 'ASP', 8.6)], [('NE2', 'HIS', 'CB', 'ASP', 10.1), ('NE2', 'HIS', 'CG', 'ASP', 9.03), ('NE2', 'HIS', 'OD1', 'ASP', 9.54), ('NE2', 'HIS', 'OD2', 'ASP', 7.87)]]}
GLU_HIS = { 
	'distances':
		[[8.67, 7.7, 7.33, 7.48, 6.85, 6.94], [7.56, 6.86, 6.77, 6.82, 6.65, 6.68], [6.91, 6.43, 6.18, 6.82, 6.41, 6.79], [7.49, 6.92, 6.32, 7.41, 6.48, 7.15], [6.22, 6.14, 6.16, 6.74, 6.73, 7.05]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 8.67), ('CB', 'GLU', 'CG', 'HIS', 7.7), ('CB', 'GLU', 'ND1', 'HIS', 7.33), ('CB', 'GLU', 'CD2', 'HIS', 7.48), ('CB', 'GLU', 'CE1', 'HIS', 6.85), ('CB', 'GLU', 'NE2', 'HIS', 6.94)], [('CG', 'GLU', 'CB', 'HIS', 7.56), ('CG', 'GLU', 'CG', 'HIS', 6.86), ('CG', 'GLU', 'ND1', 'HIS', 6.77), ('CG', 'GLU', 'CD2', 'HIS', 6.82), ('CG', 'GLU', 'CE1', 'HIS', 6.65), ('CG', 'GLU', 'NE2', 'HIS', 6.68)], [('CD', 'GLU', 'CB', 'HIS', 6.91), ('CD', 'GLU', 'CG', 'HIS', 6.43), ('CD', 'GLU', 'ND1', 'HIS', 6.18), ('CD', 'GLU', 'CD2', 'HIS', 6.82), ('CD', 'GLU', 'CE1', 'HIS', 6.41), ('CD', 'GLU', 'NE2', 'HIS', 6.79)], [('OE1', 'GLU', 'CB', 'HIS', 7.49), ('OE1', 'GLU', 'CG', 'HIS', 6.92), ('OE1', 'GLU', 'ND1', 'HIS', 6.32), ('OE1', 'GLU', 'CD2', 'HIS', 7.41), ('OE1', 'GLU', 'CE1', 'HIS', 6.48), ('OE1', 'GLU', 'NE2', 'HIS', 7.15)], [('OE2', 'GLU', 'CB', 'HIS', 6.22), ('OE2', 'GLU', 'CG', 'HIS', 6.14), ('OE2', 'GLU', 'ND1', 'HIS', 6.16), ('OE2', 'GLU', 'CD2', 'HIS', 6.74), ('OE2', 'GLU', 'CE1', 'HIS', 6.73), ('OE2', 'GLU', 'NE2', 'HIS', 7.05)]]}
HIS_LYS = { 
	'distances':
		[[11.19, 11.27, 10.52, 9.53, 8.93], [10.97, 10.87, 9.93, 8.88, 8.03], [9.9, 9.78, 8.74, 7.79, 6.85], [11.89, 11.63, 10.59, 9.45, 8.44], [10.31, 10.0, 8.81, 7.81, 6.61], [11.5, 11.13, 9.95, 8.84, 7.64]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'LYS', 11.19), ('CB', 'HIS', 'CG', 'LYS', 11.27), ('CB', 'HIS', 'CD', 'LYS', 10.52), ('CB', 'HIS', 'CE', 'LYS', 9.53), ('CB', 'HIS', 'NZ', 'LYS', 8.93)], [('CG', 'HIS', 'CB', 'LYS', 10.97), ('CG', 'HIS', 'CG', 'LYS', 10.87), ('CG', 'HIS', 'CD', 'LYS', 9.93), ('CG', 'HIS', 'CE', 'LYS', 8.88), ('CG', 'HIS', 'NZ', 'LYS', 8.03)], [('ND1', 'HIS', 'CB', 'LYS', 9.9), ('ND1', 'HIS', 'CG', 'LYS', 9.78), ('ND1', 'HIS', 'CD', 'LYS', 8.74), ('ND1', 'HIS', 'CE', 'LYS', 7.79), ('ND1', 'HIS', 'NZ', 'LYS', 6.85)], [('CD2', 'HIS', 'CB', 'LYS', 11.89), ('CD2', 'HIS', 'CG', 'LYS', 11.63), ('CD2', 'HIS', 'CD', 'LYS', 10.59), ('CD2', 'HIS', 'CE', 'LYS', 9.45), ('CD2', 'HIS', 'NZ', 'LYS', 8.44)], [('CE1', 'HIS', 'CB', 'LYS', 10.31), ('CE1', 'HIS', 'CG', 'LYS', 10.0), ('CE1', 'HIS', 'CD', 'LYS', 8.81), ('CE1', 'HIS', 'CE', 'LYS', 7.81), ('CE1', 'HIS', 'NZ', 'LYS', 6.61)], [('NE2', 'HIS', 'CB', 'LYS', 11.5), ('NE2', 'HIS', 'CG', 'LYS', 11.13), ('NE2', 'HIS', 'CD', 'LYS', 9.95), ('NE2', 'HIS', 'CE', 'LYS', 8.84), ('NE2', 'HIS', 'NZ', 'LYS', 7.64)]]}
GLU_ASP = { 
	'distances':
		[[14.7, 13.44, 13.61, 12.39], [14.59, 13.43, 13.71, 12.37], [14.85, 13.8, 14.23, 12.66], [15.22, 14.16, 14.61, 12.98], [14.89, 13.95, 14.46, 12.81]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 14.7), ('CB', 'GLU', 'CG', 'ASP', 13.44), ('CB', 'GLU', 'OD1', 'ASP', 13.61), ('CB', 'GLU', 'OD2', 'ASP', 12.39)], [('CG', 'GLU', 'CB', 'ASP', 14.59), ('CG', 'GLU', 'CG', 'ASP', 13.43), ('CG', 'GLU', 'OD1', 'ASP', 13.71), ('CG', 'GLU', 'OD2', 'ASP', 12.37)], [('CD', 'GLU', 'CB', 'ASP', 14.85), ('CD', 'GLU', 'CG', 'ASP', 13.8), ('CD', 'GLU', 'OD1', 'ASP', 14.23), ('CD', 'GLU', 'OD2', 'ASP', 12.66)], [('OE1', 'GLU', 'CB', 'ASP', 15.22), ('OE1', 'GLU', 'CG', 'ASP', 14.16), ('OE1', 'GLU', 'OD1', 'ASP', 14.61), ('OE1', 'GLU', 'OD2', 'ASP', 12.98)], [('OE2', 'GLU', 'CB', 'ASP', 14.89), ('OE2', 'GLU', 'CG', 'ASP', 13.95), ('OE2', 'GLU', 'OD1', 'ASP', 14.46), ('OE2', 'GLU', 'OD2', 'ASP', 12.81)]]}
ASP_LYS = { 
	'distances':
		[[15.24, 14.24, 13.57, 12.09, 11.6], [14.91, 13.91, 13.08, 11.62, 10.93], [15.86, 14.83, 13.93, 12.5, 11.69], [13.8, 12.84, 11.97, 10.51, 9.76]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 15.24), ('CB', 'ASP', 'CG', 'LYS', 14.24), ('CB', 'ASP', 'CD', 'LYS', 13.57), ('CB', 'ASP', 'CE', 'LYS', 12.09), ('CB', 'ASP', 'NZ', 'LYS', 11.6)], [('CG', 'ASP', 'CB', 'LYS', 14.91), ('CG', 'ASP', 'CG', 'LYS', 13.91), ('CG', 'ASP', 'CD', 'LYS', 13.08), ('CG', 'ASP', 'CE', 'LYS', 11.62), ('CG', 'ASP', 'NZ', 'LYS', 10.93)], [('OD1', 'ASP', 'CB', 'LYS', 15.86), ('OD1', 'ASP', 'CG', 'LYS', 14.83), ('OD1', 'ASP', 'CD', 'LYS', 13.93), ('OD1', 'ASP', 'CE', 'LYS', 12.5), ('OD1', 'ASP', 'NZ', 'LYS', 11.69)], [('OD2', 'ASP', 'CB', 'LYS', 13.8), ('OD2', 'ASP', 'CG', 'LYS', 12.84), ('OD2', 'ASP', 'CD', 'LYS', 11.97), ('OD2', 'ASP', 'CE', 'LYS', 10.51), ('OD2', 'ASP', 'NZ', 'LYS', 9.76)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_LYS, d, 'A_1pjb_1_4_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'A_1pjb_1_4_1_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_HIS, d, 'A_1pjb_1_4_1_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_LYS, d, 'A_1pjb_1_4_1_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLU_ASP, d, 'A_1pjb_1_4_1_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ASP_LYS, d, 'A_1pjb_1_4_1_1')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_LYS' :  match1,
		'HIS_ASP' :  match2,
		'GLU_HIS' :  match3,
		'HIS_LYS' :  match4,
		'GLU_ASP' :  match5,
		'ASP_LYS' :  match6}