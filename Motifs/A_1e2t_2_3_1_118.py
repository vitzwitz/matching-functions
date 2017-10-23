'''
FUNC:A_1e2t_2_3_1_118
PDB:1e2t
EC:2.3.1.118
RESI:cys,his,asp
LOCI:a-69,107,122;
'''
import motifFunctions as cmd
HIS_CYS = { 
	'distances':
		[[7.15, 6.61], [6.83, 6.44], [5.89, 5.43], [7.76, 7.55], [6.46, 6.23], [7.56, 7.43]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYS', 7.15), ('CB', 'HIS', 'SG', 'CYS', 6.61)], [('CG', 'HIS', 'CB', 'CYS', 6.83), ('CG', 'HIS', 'SG', 'CYS', 6.44)], [('ND1', 'HIS', 'CB', 'CYS', 5.89), ('ND1', 'HIS', 'SG', 'CYS', 5.43)], [('CD2', 'HIS', 'CB', 'CYS', 7.76), ('CD2', 'HIS', 'SG', 'CYS', 7.55)], [('CE1', 'HIS', 'CB', 'CYS', 6.46), ('CE1', 'HIS', 'SG', 'CYS', 6.23)], [('NE2', 'HIS', 'CB', 'CYS', 7.56), ('NE2', 'HIS', 'SG', 'CYS', 7.43)]]}
CYS_ASP = { 
	'distances':
		[[10.67, 9.57, 8.61, 9.85], [11.11, 9.83, 8.96, 9.85]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASP', 10.67), ('CB', 'CYS', 'CG', 'ASP', 9.57), ('CB', 'CYS', 'OD1', 'ASP', 8.61), ('CB', 'CYS', 'OD2', 'ASP', 9.85)], [('SG', 'CYS', 'CB', 'ASP', 11.11), ('SG', 'CYS', 'CG', 'ASP', 9.83), ('SG', 'CYS', 'OD1', 'ASP', 8.96), ('SG', 'CYS', 'OD2', 'ASP', 9.85)]]}
HIS_ASP = { 
	'distances':
		[[10.17, 9.14, 8.96, 8.74], [8.76, 7.67, 7.5, 7.3], [8.53, 7.28, 6.85, 7.03], [7.68, 6.72, 6.79, 6.28], [7.32, 6.0, 5.57, 5.79], [6.65, 5.5, 5.48, 5.13]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 10.17), ('CB', 'HIS', 'CG', 'ASP', 9.14), ('CB', 'HIS', 'OD1', 'ASP', 8.96), ('CB', 'HIS', 'OD2', 'ASP', 8.74)], [('CG', 'HIS', 'CB', 'ASP', 8.76), ('CG', 'HIS', 'CG', 'ASP', 7.67), ('CG', 'HIS', 'OD1', 'ASP', 7.5), ('CG', 'HIS', 'OD2', 'ASP', 7.3)], [('ND1', 'HIS', 'CB', 'ASP', 8.53), ('ND1', 'HIS', 'CG', 'ASP', 7.28), ('ND1', 'HIS', 'OD1', 'ASP', 6.85), ('ND1', 'HIS', 'OD2', 'ASP', 7.03)], [('CD2', 'HIS', 'CB', 'ASP', 7.68), ('CD2', 'HIS', 'CG', 'ASP', 6.72), ('CD2', 'HIS', 'OD1', 'ASP', 6.79), ('CD2', 'HIS', 'OD2', 'ASP', 6.28)], [('CE1', 'HIS', 'CB', 'ASP', 7.32), ('CE1', 'HIS', 'CG', 'ASP', 6.0), ('CE1', 'HIS', 'OD1', 'ASP', 5.57), ('CE1', 'HIS', 'OD2', 'ASP', 5.79)], [('NE2', 'HIS', 'CB', 'ASP', 6.65), ('NE2', 'HIS', 'CG', 'ASP', 5.5), ('NE2', 'HIS', 'OD1', 'ASP', 5.48), ('NE2', 'HIS', 'OD2', 'ASP', 5.13)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_CYS, d, 'A_1e2t_2_3_1_118')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_ASP, d, 'A_1e2t_2_3_1_118')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASP, d, 'A_1e2t_2_3_1_118')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_CYS' :  match1,
		'CYS_ASP' :  match2,
		'HIS_ASP' :  match3}