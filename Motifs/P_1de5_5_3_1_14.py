'''
FUNC:P_1de5_5_3_1_14
PDB:1de5
EC:5.3.1.14
RESI:lys,his,asp
LOCI:a-236,270,302;
'''
import motifFunctions as cmd
LYS_HIS = { 
	'distances':
		[[6.84, 6.38, 5.43, 7.15, 5.82, 6.85], [6.45, 5.81, 5.17, 6.29, 5.34, 6.03], [7.66, 6.74, 6.04, 6.85, 5.69, 6.24], [7.97, 7.01, 6.66, 6.78, 6.18, 6.25], [9.09, 7.95, 7.56, 7.45, 6.77, 6.68]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'HIS', 6.84), ('CB', 'LYS', 'CG', 'HIS', 6.38), ('CB', 'LYS', 'ND1', 'HIS', 5.43), ('CB', 'LYS', 'CD2', 'HIS', 7.15), ('CB', 'LYS', 'CE1', 'HIS', 5.82), ('CB', 'LYS', 'NE2', 'HIS', 6.85)], [('CG', 'LYS', 'CB', 'HIS', 6.45), ('CG', 'LYS', 'CG', 'HIS', 5.81), ('CG', 'LYS', 'ND1', 'HIS', 5.17), ('CG', 'LYS', 'CD2', 'HIS', 6.29), ('CG', 'LYS', 'CE1', 'HIS', 5.34), ('CG', 'LYS', 'NE2', 'HIS', 6.03)], [('CD', 'LYS', 'CB', 'HIS', 7.66), ('CD', 'LYS', 'CG', 'HIS', 6.74), ('CD', 'LYS', 'ND1', 'HIS', 6.04), ('CD', 'LYS', 'CD2', 'HIS', 6.85), ('CD', 'LYS', 'CE1', 'HIS', 5.69), ('CD', 'LYS', 'NE2', 'HIS', 6.24)], [('CE', 'LYS', 'CB', 'HIS', 7.97), ('CE', 'LYS', 'CG', 'HIS', 7.01), ('CE', 'LYS', 'ND1', 'HIS', 6.66), ('CE', 'LYS', 'CD2', 'HIS', 6.78), ('CE', 'LYS', 'CE1', 'HIS', 6.18), ('CE', 'LYS', 'NE2', 'HIS', 6.25)], [('NZ', 'LYS', 'CB', 'HIS', 9.09), ('NZ', 'LYS', 'CG', 'HIS', 7.95), ('NZ', 'LYS', 'ND1', 'HIS', 7.56), ('NZ', 'LYS', 'CD2', 'HIS', 7.45), ('NZ', 'LYS', 'CE1', 'HIS', 6.77), ('NZ', 'LYS', 'NE2', 'HIS', 6.68)]]}
HIS_ASP = { 
	'distances':
		[[7.96, 7.51, 7.52, 7.68], [7.35, 6.63, 6.69, 6.56], [8.03, 7.27, 7.52, 6.85], [6.54, 5.56, 5.49, 5.54], [7.75, 6.78, 7.07, 6.13], [6.87, 5.73, 5.84, 5.22]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.96), ('CB', 'HIS', 'CG', 'ASP', 7.51), ('CB', 'HIS', 'OD1', 'ASP', 7.52), ('CB', 'HIS', 'OD2', 'ASP', 7.68)], [('CG', 'HIS', 'CB', 'ASP', 7.35), ('CG', 'HIS', 'CG', 'ASP', 6.63), ('CG', 'HIS', 'OD1', 'ASP', 6.69), ('CG', 'HIS', 'OD2', 'ASP', 6.56)], [('ND1', 'HIS', 'CB', 'ASP', 8.03), ('ND1', 'HIS', 'CG', 'ASP', 7.27), ('ND1', 'HIS', 'OD1', 'ASP', 7.52), ('ND1', 'HIS', 'OD2', 'ASP', 6.85)], [('CD2', 'HIS', 'CB', 'ASP', 6.54), ('CD2', 'HIS', 'CG', 'ASP', 5.56), ('CD2', 'HIS', 'OD1', 'ASP', 5.49), ('CD2', 'HIS', 'OD2', 'ASP', 5.54)], [('CE1', 'HIS', 'CB', 'ASP', 7.75), ('CE1', 'HIS', 'CG', 'ASP', 6.78), ('CE1', 'HIS', 'OD1', 'ASP', 7.07), ('CE1', 'HIS', 'OD2', 'ASP', 6.13)], [('NE2', 'HIS', 'CB', 'ASP', 6.87), ('NE2', 'HIS', 'CG', 'ASP', 5.73), ('NE2', 'HIS', 'OD1', 'ASP', 5.84), ('NE2', 'HIS', 'OD2', 'ASP', 5.22)]]}
LYS_ASP = { 
	'distances':
		[[9.0, 8.78, 9.54, 8.09], [7.5, 7.35, 8.2, 6.69], [7.39, 7.19, 8.16, 6.25], [6.15, 6.08, 7.18, 5.15], [6.49, 6.23, 7.31, 5.08]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASP', 9.0), ('CB', 'LYS', 'CG', 'ASP', 8.78), ('CB', 'LYS', 'OD1', 'ASP', 9.54), ('CB', 'LYS', 'OD2', 'ASP', 8.09)], [('CG', 'LYS', 'CB', 'ASP', 7.5), ('CG', 'LYS', 'CG', 'ASP', 7.35), ('CG', 'LYS', 'OD1', 'ASP', 8.2), ('CG', 'LYS', 'OD2', 'ASP', 6.69)], [('CD', 'LYS', 'CB', 'ASP', 7.39), ('CD', 'LYS', 'CG', 'ASP', 7.19), ('CD', 'LYS', 'OD1', 'ASP', 8.16), ('CD', 'LYS', 'OD2', 'ASP', 6.25)], [('CE', 'LYS', 'CB', 'ASP', 6.15), ('CE', 'LYS', 'CG', 'ASP', 6.08), ('CE', 'LYS', 'OD1', 'ASP', 7.18), ('CE', 'LYS', 'OD2', 'ASP', 5.15)], [('NZ', 'LYS', 'CB', 'ASP', 6.49), ('NZ', 'LYS', 'CG', 'ASP', 6.23), ('NZ', 'LYS', 'OD1', 'ASP', 7.31), ('NZ', 'LYS', 'OD2', 'ASP', 5.08)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_HIS, d, 'P_1de5_5_3_1_14')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'P_1de5_5_3_1_14')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LYS_ASP, d, 'P_1de5_5_3_1_14')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_HIS' :  match1,
		'HIS_ASP' :  match2,
		'LYS_ASP' :  match3}