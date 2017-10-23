'''
FUNC:A_1de6_5_3_1_14
PDB:1de6
EC:5.3.1.14
RESI:lys,his,asp
LOCI:a-236,270,302;
'''
import motifFunctions as cmd
HIS_LYS = { 
	'distances':
		[[6.43, 6.23, 7.19, 7.53, 8.78], [6.11, 5.77, 6.33, 6.62, 7.69], [5.63, 5.68, 6.05, 6.67, 7.62], [6.78, 6.08, 6.26, 6.12, 6.99], [6.13, 5.98, 5.84, 6.29, 6.94], [6.8, 6.22, 5.97, 5.93, 6.49]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'LYS', 6.43), ('CB', 'HIS', 'CG', 'LYS', 6.23), ('CB', 'HIS', 'CD', 'LYS', 7.19), ('CB', 'HIS', 'CE', 'LYS', 7.53), ('CB', 'HIS', 'NZ', 'LYS', 8.78)], [('CG', 'HIS', 'CB', 'LYS', 6.11), ('CG', 'HIS', 'CG', 'LYS', 5.77), ('CG', 'HIS', 'CD', 'LYS', 6.33), ('CG', 'HIS', 'CE', 'LYS', 6.62), ('CG', 'HIS', 'NZ', 'LYS', 7.69)], [('ND1', 'HIS', 'CB', 'LYS', 5.63), ('ND1', 'HIS', 'CG', 'LYS', 5.68), ('ND1', 'HIS', 'CD', 'LYS', 6.05), ('ND1', 'HIS', 'CE', 'LYS', 6.67), ('ND1', 'HIS', 'NZ', 'LYS', 7.62)], [('CD2', 'HIS', 'CB', 'LYS', 6.78), ('CD2', 'HIS', 'CG', 'LYS', 6.08), ('CD2', 'HIS', 'CD', 'LYS', 6.26), ('CD2', 'HIS', 'CE', 'LYS', 6.12), ('CD2', 'HIS', 'NZ', 'LYS', 6.99)], [('CE1', 'HIS', 'CB', 'LYS', 6.13), ('CE1', 'HIS', 'CG', 'LYS', 5.98), ('CE1', 'HIS', 'CD', 'LYS', 5.84), ('CE1', 'HIS', 'CE', 'LYS', 6.29), ('CE1', 'HIS', 'NZ', 'LYS', 6.94)], [('NE2', 'HIS', 'CB', 'LYS', 6.8), ('NE2', 'HIS', 'CG', 'LYS', 6.22), ('NE2', 'HIS', 'CD', 'LYS', 5.97), ('NE2', 'HIS', 'CE', 'LYS', 5.93), ('NE2', 'HIS', 'NZ', 'LYS', 6.49)]]}
HIS_ASP = { 
	'distances':
		[[7.87, 7.61, 7.39, 8.18], [7.28, 6.71, 6.49, 7.08], [8.2, 7.46, 7.3, 7.53], [6.24, 5.46, 5.18, 5.84], [7.94, 6.97, 6.81, 6.81], [6.81, 5.72, 5.5, 5.66]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.87), ('CB', 'HIS', 'CG', 'ASP', 7.61), ('CB', 'HIS', 'OD1', 'ASP', 7.39), ('CB', 'HIS', 'OD2', 'ASP', 8.18)], [('CG', 'HIS', 'CB', 'ASP', 7.28), ('CG', 'HIS', 'CG', 'ASP', 6.71), ('CG', 'HIS', 'OD1', 'ASP', 6.49), ('CG', 'HIS', 'OD2', 'ASP', 7.08)], [('ND1', 'HIS', 'CB', 'ASP', 8.2), ('ND1', 'HIS', 'CG', 'ASP', 7.46), ('ND1', 'HIS', 'OD1', 'ASP', 7.3), ('ND1', 'HIS', 'OD2', 'ASP', 7.53)], [('CD2', 'HIS', 'CB', 'ASP', 6.24), ('CD2', 'HIS', 'CG', 'ASP', 5.46), ('CD2', 'HIS', 'OD1', 'ASP', 5.18), ('CD2', 'HIS', 'OD2', 'ASP', 5.84)], [('CE1', 'HIS', 'CB', 'ASP', 7.94), ('CE1', 'HIS', 'CG', 'ASP', 6.97), ('CE1', 'HIS', 'OD1', 'ASP', 6.81), ('CE1', 'HIS', 'OD2', 'ASP', 6.81)], [('NE2', 'HIS', 'CB', 'ASP', 6.81), ('NE2', 'HIS', 'CG', 'ASP', 5.72), ('NE2', 'HIS', 'OD1', 'ASP', 5.5), ('NE2', 'HIS', 'OD2', 'ASP', 5.66)]]}
LYS_ASP = { 
	'distances':
		[[9.0, 8.83, 9.29, 8.59], [7.57, 7.53, 8.13, 7.31], [7.39, 7.13, 7.83, 6.57], [6.11, 5.94, 6.84, 5.3], [6.51, 6.14, 7.09, 5.11]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASP', 9.0), ('CB', 'LYS', 'CG', 'ASP', 8.83), ('CB', 'LYS', 'OD1', 'ASP', 9.29), ('CB', 'LYS', 'OD2', 'ASP', 8.59)], [('CG', 'LYS', 'CB', 'ASP', 7.57), ('CG', 'LYS', 'CG', 'ASP', 7.53), ('CG', 'LYS', 'OD1', 'ASP', 8.13), ('CG', 'LYS', 'OD2', 'ASP', 7.31)], [('CD', 'LYS', 'CB', 'ASP', 7.39), ('CD', 'LYS', 'CG', 'ASP', 7.13), ('CD', 'LYS', 'OD1', 'ASP', 7.83), ('CD', 'LYS', 'OD2', 'ASP', 6.57)], [('CE', 'LYS', 'CB', 'ASP', 6.11), ('CE', 'LYS', 'CG', 'ASP', 5.94), ('CE', 'LYS', 'OD1', 'ASP', 6.84), ('CE', 'LYS', 'OD2', 'ASP', 5.3)], [('NZ', 'LYS', 'CB', 'ASP', 6.51), ('NZ', 'LYS', 'CG', 'ASP', 6.14), ('NZ', 'LYS', 'OD1', 'ASP', 7.09), ('NZ', 'LYS', 'OD2', 'ASP', 5.11)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_LYS, d, 'A_1de6_5_3_1_14')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'A_1de6_5_3_1_14')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LYS_ASP, d, 'A_1de6_5_3_1_14')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_LYS' :  match1,
		'HIS_ASP' :  match2,
		'LYS_ASP' :  match3}