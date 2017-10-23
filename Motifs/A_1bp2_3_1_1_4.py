'''
FUNC:A_1bp2_3_1_1_4
PDB:1bp2
EC:3.1.1.4
RESI:gly,his,asp
LOCI:a-30,48,99;
'''
import motifFunctions as cmd
ASP_GLY = { 
	'distances':
		[[15.69, 16.18, 15.98, 15.22], [14.74, 15.23, 15.15, 14.49], [15.16, 15.59, 15.52, 14.98], [13.75, 14.32, 14.31, 13.61]],
	'comparisons':
		[[('CB', 'ASP', 'O', 'GLY', 15.69), ('CB', 'ASP', 'C', 'GLY', 16.18), ('CB', 'ASP', 'CA', 'GLY', 15.98), ('CB', 'ASP', 'N', 'GLY', 15.22)], [('CG', 'ASP', 'O', 'GLY', 14.74), ('CG', 'ASP', 'C', 'GLY', 15.23), ('CG', 'ASP', 'CA', 'GLY', 15.15), ('CG', 'ASP', 'N', 'GLY', 14.49)], [('OD1', 'ASP', 'O', 'GLY', 15.16), ('OD1', 'ASP', 'C', 'GLY', 15.59), ('OD1', 'ASP', 'CA', 'GLY', 15.52), ('OD1', 'ASP', 'N', 'GLY', 14.98)], [('OD2', 'ASP', 'O', 'GLY', 13.75), ('OD2', 'ASP', 'C', 'GLY', 14.32), ('OD2', 'ASP', 'CA', 'GLY', 14.31), ('OD2', 'ASP', 'N', 'GLY', 13.61)]]}
HIS_GLY = { 
	'distances':
		[[10.84, 11.73, 11.69, 10.46], [10.8, 11.62, 11.6, 10.51], [9.73, 10.51, 10.55, 9.57], [11.95, 12.72, 12.69, 11.65], [10.4, 11.09, 11.13, 10.3], [11.7, 12.4, 12.4, 11.51]],
	'comparisons':
		[[('CB', 'HIS', 'O', 'GLY', 10.84), ('CB', 'HIS', 'C', 'GLY', 11.73), ('CB', 'HIS', 'CA', 'GLY', 11.69), ('CB', 'HIS', 'N', 'GLY', 10.46)], [('CG', 'HIS', 'O', 'GLY', 10.8), ('CG', 'HIS', 'C', 'GLY', 11.62), ('CG', 'HIS', 'CA', 'GLY', 11.6), ('CG', 'HIS', 'N', 'GLY', 10.51)], [('ND1', 'HIS', 'O', 'GLY', 9.73), ('ND1', 'HIS', 'C', 'GLY', 10.51), ('ND1', 'HIS', 'CA', 'GLY', 10.55), ('ND1', 'HIS', 'N', 'GLY', 9.57)], [('CD2', 'HIS', 'O', 'GLY', 11.95), ('CD2', 'HIS', 'C', 'GLY', 12.72), ('CD2', 'HIS', 'CA', 'GLY', 12.69), ('CD2', 'HIS', 'N', 'GLY', 11.65)], [('CE1', 'HIS', 'O', 'GLY', 10.4), ('CE1', 'HIS', 'C', 'GLY', 11.09), ('CE1', 'HIS', 'CA', 'GLY', 11.13), ('CE1', 'HIS', 'N', 'GLY', 10.3)], [('NE2', 'HIS', 'O', 'GLY', 11.7), ('NE2', 'HIS', 'C', 'GLY', 12.4), ('NE2', 'HIS', 'CA', 'GLY', 12.4), ('NE2', 'HIS', 'N', 'GLY', 11.51)]]}
HIS_ASP = { 
	'distances':
		[[9.67, 9.46, 10.57, 8.38], [8.43, 8.07, 9.13, 6.96], [8.64, 8.0, 8.9, 6.86], [7.17, 6.9, 8.04, 5.83], [7.58, 6.78, 7.61, 5.64], [6.53, 5.93, 6.95, 4.78]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 9.67), ('CB', 'HIS', 'CG', 'ASP', 9.46), ('CB', 'HIS', 'OD1', 'ASP', 10.57), ('CB', 'HIS', 'OD2', 'ASP', 8.38)], [('CG', 'HIS', 'CB', 'ASP', 8.43), ('CG', 'HIS', 'CG', 'ASP', 8.07), ('CG', 'HIS', 'OD1', 'ASP', 9.13), ('CG', 'HIS', 'OD2', 'ASP', 6.96)], [('ND1', 'HIS', 'CB', 'ASP', 8.64), ('ND1', 'HIS', 'CG', 'ASP', 8.0), ('ND1', 'HIS', 'OD1', 'ASP', 8.9), ('ND1', 'HIS', 'OD2', 'ASP', 6.86)], [('CD2', 'HIS', 'CB', 'ASP', 7.17), ('CD2', 'HIS', 'CG', 'ASP', 6.9), ('CD2', 'HIS', 'OD1', 'ASP', 8.04), ('CD2', 'HIS', 'OD2', 'ASP', 5.83)], [('CE1', 'HIS', 'CB', 'ASP', 7.58), ('CE1', 'HIS', 'CG', 'ASP', 6.78), ('CE1', 'HIS', 'OD1', 'ASP', 7.61), ('CE1', 'HIS', 'OD2', 'ASP', 5.64)], [('NE2', 'HIS', 'CB', 'ASP', 6.53), ('NE2', 'HIS', 'CG', 'ASP', 5.93), ('NE2', 'HIS', 'OD1', 'ASP', 6.95), ('NE2', 'HIS', 'OD2', 'ASP', 4.78)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_GLY, d, 'A_1bp2_3_1_1_4')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_GLY, d, 'A_1bp2_3_1_1_4')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASP, d, 'A_1bp2_3_1_1_4')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_GLY' :  match1,
		'HIS_GLY' :  match2,
		'HIS_ASP' :  match3}