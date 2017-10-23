'''
FUNC:P_1xic_5_3_1_5
PDB:1xic
EC:5.3.1.5
RESI:lys,his,asp
LOCI:a-183,220,255;
'''
import motifFunctions as cmd
LYS_HIS = { 
	'distances':
		[[6.39, 5.94, 5.5, 6.49, 5.91, 6.4], [6.16, 5.62, 5.63, 5.77, 5.83, 5.82], [7.23, 6.32, 6.16, 6.05, 5.83, 5.67], [7.49, 6.56, 6.75, 5.87, 6.28, 5.62], [8.75, 7.64, 7.65, 6.78, 6.85, 6.18]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'HIS', 6.39), ('CB', 'LYS', 'CG', 'HIS', 5.94), ('CB', 'LYS', 'ND1', 'HIS', 5.5), ('CB', 'LYS', 'CD2', 'HIS', 6.49), ('CB', 'LYS', 'CE1', 'HIS', 5.91), ('CB', 'LYS', 'NE2', 'HIS', 6.4)], [('CG', 'LYS', 'CB', 'HIS', 6.16), ('CG', 'LYS', 'CG', 'HIS', 5.62), ('CG', 'LYS', 'ND1', 'HIS', 5.63), ('CG', 'LYS', 'CD2', 'HIS', 5.77), ('CG', 'LYS', 'CE1', 'HIS', 5.83), ('CG', 'LYS', 'NE2', 'HIS', 5.82)], [('CD', 'LYS', 'CB', 'HIS', 7.23), ('CD', 'LYS', 'CG', 'HIS', 6.32), ('CD', 'LYS', 'ND1', 'HIS', 6.16), ('CD', 'LYS', 'CD2', 'HIS', 6.05), ('CD', 'LYS', 'CE1', 'HIS', 5.83), ('CD', 'LYS', 'NE2', 'HIS', 5.67)], [('CE', 'LYS', 'CB', 'HIS', 7.49), ('CE', 'LYS', 'CG', 'HIS', 6.56), ('CE', 'LYS', 'ND1', 'HIS', 6.75), ('CE', 'LYS', 'CD2', 'HIS', 5.87), ('CE', 'LYS', 'CE1', 'HIS', 6.28), ('CE', 'LYS', 'NE2', 'HIS', 5.62)], [('NZ', 'LYS', 'CB', 'HIS', 8.75), ('NZ', 'LYS', 'CG', 'HIS', 7.64), ('NZ', 'LYS', 'ND1', 'HIS', 7.65), ('NZ', 'LYS', 'CD2', 'HIS', 6.78), ('NZ', 'LYS', 'CE1', 'HIS', 6.85), ('NZ', 'LYS', 'NE2', 'HIS', 6.18)]]}
HIS_ASP = { 
	'distances':
		[[9.14, 8.46, 7.85, 8.7], [8.34, 7.49, 6.99, 7.52], [9.04, 8.1, 7.77, 7.84], [7.11, 6.15, 5.66, 6.2], [8.44, 7.38, 7.19, 6.89], [7.18, 6.08, 5.86, 5.71]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 9.14), ('CB', 'HIS', 'CG', 'ASP', 8.46), ('CB', 'HIS', 'OD1', 'ASP', 7.85), ('CB', 'HIS', 'OD2', 'ASP', 8.7)], [('CG', 'HIS', 'CB', 'ASP', 8.34), ('CG', 'HIS', 'CG', 'ASP', 7.49), ('CG', 'HIS', 'OD1', 'ASP', 6.99), ('CG', 'HIS', 'OD2', 'ASP', 7.52)], [('ND1', 'HIS', 'CB', 'ASP', 9.04), ('ND1', 'HIS', 'CG', 'ASP', 8.1), ('ND1', 'HIS', 'OD1', 'ASP', 7.77), ('ND1', 'HIS', 'OD2', 'ASP', 7.84)], [('CD2', 'HIS', 'CB', 'ASP', 7.11), ('CD2', 'HIS', 'CG', 'ASP', 6.15), ('CD2', 'HIS', 'OD1', 'ASP', 5.66), ('CD2', 'HIS', 'OD2', 'ASP', 6.2)], [('CE1', 'HIS', 'CB', 'ASP', 8.44), ('CE1', 'HIS', 'CG', 'ASP', 7.38), ('CE1', 'HIS', 'OD1', 'ASP', 7.19), ('CE1', 'HIS', 'OD2', 'ASP', 6.89)], [('NE2', 'HIS', 'CB', 'ASP', 7.18), ('NE2', 'HIS', 'CG', 'ASP', 6.08), ('NE2', 'HIS', 'OD1', 'ASP', 5.86), ('NE2', 'HIS', 'OD2', 'ASP', 5.71)]]}
LYS_ASP = { 
	'distances':
		[[9.49, 9.13, 9.29, 8.83], [8.02, 7.81, 8.04, 7.64], [7.36, 7.14, 7.64, 6.72], [5.85, 5.8, 6.44, 5.54], [5.78, 5.7, 6.64, 5.05]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASP', 9.49), ('CB', 'LYS', 'CG', 'ASP', 9.13), ('CB', 'LYS', 'OD1', 'ASP', 9.29), ('CB', 'LYS', 'OD2', 'ASP', 8.83)], [('CG', 'LYS', 'CB', 'ASP', 8.02), ('CG', 'LYS', 'CG', 'ASP', 7.81), ('CG', 'LYS', 'OD1', 'ASP', 8.04), ('CG', 'LYS', 'OD2', 'ASP', 7.64)], [('CD', 'LYS', 'CB', 'ASP', 7.36), ('CD', 'LYS', 'CG', 'ASP', 7.14), ('CD', 'LYS', 'OD1', 'ASP', 7.64), ('CD', 'LYS', 'OD2', 'ASP', 6.72)], [('CE', 'LYS', 'CB', 'ASP', 5.85), ('CE', 'LYS', 'CG', 'ASP', 5.8), ('CE', 'LYS', 'OD1', 'ASP', 6.44), ('CE', 'LYS', 'OD2', 'ASP', 5.54)], [('NZ', 'LYS', 'CB', 'ASP', 5.78), ('NZ', 'LYS', 'CG', 'ASP', 5.7), ('NZ', 'LYS', 'OD1', 'ASP', 6.64), ('NZ', 'LYS', 'OD2', 'ASP', 5.05)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_HIS, d, 'P_1xic_5_3_1_5')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'P_1xic_5_3_1_5')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LYS_ASP, d, 'P_1xic_5_3_1_5')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_HIS' :  match1,
		'HIS_ASP' :  match2,
		'LYS_ASP' :  match3}