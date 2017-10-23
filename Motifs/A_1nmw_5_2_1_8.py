'''
FUNC:A_1nmw_5_2_1_8
PDB:1nmw
EC:5.2.1.8
RESI:his,cys,his
LOCI:a-59,113,157;
'''
import motifFunctions as cmd
HIS_CYS = { 
	'distances':
		[[9.81, 10.25], [8.39, 8.75], [7.64, 7.99], [7.83, 8.08], [6.47, 6.69], [6.58, 6.73], [10.08, 10.33], [9.07, 9.19], [7.95, 7.93], [9.26, 9.34], [7.45, 7.27], [8.32, 8.23]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYS', 9.81), ('CB', 'HIS', 'SG', 'CYS', 10.25)], [('CG', 'HIS', 'CB', 'CYS', 8.39), ('CG', 'HIS', 'SG', 'CYS', 8.75)], [('ND1', 'HIS', 'CB', 'CYS', 7.64), ('ND1', 'HIS', 'SG', 'CYS', 7.99)], [('CD2', 'HIS', 'CB', 'CYS', 7.83), ('CD2', 'HIS', 'SG', 'CYS', 8.08)], [('CE1', 'HIS', 'CB', 'CYS', 6.47), ('CE1', 'HIS', 'SG', 'CYS', 6.69)], [('NE2', 'HIS', 'CB', 'CYS', 6.58), ('NE2', 'HIS', 'SG', 'CYS', 6.73)], [('CB', 'HIS', 'CB', 'CYS', 10.08), ('CB', 'HIS', 'SG', 'CYS', 10.33)], [('CG', 'HIS', 'CB', 'CYS', 9.07), ('CG', 'HIS', 'SG', 'CYS', 9.19)], [('ND1', 'HIS', 'CB', 'CYS', 7.95), ('ND1', 'HIS', 'SG', 'CYS', 7.93)], [('CD2', 'HIS', 'CB', 'CYS', 9.26), ('CD2', 'HIS', 'SG', 'CYS', 9.34)], [('CE1', 'HIS', 'CB', 'CYS', 7.45), ('CE1', 'HIS', 'SG', 'CYS', 7.27)], [('NE2', 'HIS', 'CB', 'CYS', 8.32), ('NE2', 'HIS', 'SG', 'CYS', 8.23)]]}
CYS_HISI = { 
	'distances':
		[[10.08, 9.07, 7.95, 9.26, 7.45, 8.32], [10.33, 9.19, 7.93, 9.34, 7.27, 8.23]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HISI', 10.08), ('CB', 'CYS', 'CG', 'HISI', 9.07), ('CB', 'CYS', 'ND1', 'HISI', 7.95), ('CB', 'CYS', 'CD2', 'HISI', 9.26), ('CB', 'CYS', 'CE1', 'HISI', 7.45), ('CB', 'CYS', 'NE2', 'HISI', 8.32)], [('SG', 'CYS', 'CB', 'HISI', 10.33), ('SG', 'CYS', 'CG', 'HISI', 9.19), ('SG', 'CYS', 'ND1', 'HISI', 7.93), ('SG', 'CYS', 'CD2', 'HISI', 9.34), ('SG', 'CYS', 'CE1', 'HISI', 7.27), ('SG', 'CYS', 'NE2', 'HISI', 8.23)]]}
HIS_HIS = { 
	'distances':
		[[7.1, 7.74, 7.34, 9.06, 8.5, 9.43], [6.98, 7.22, 6.51, 8.46, 7.5, 8.58], [5.99, 5.98, 5.2, 7.16, 6.16, 7.22], [8.1, 8.1, 7.16, 9.25, 7.93, 9.13], [6.78, 6.36, 5.25, 7.33, 5.83, 7.04], [7.97, 7.64, 6.51, 8.63, 7.03, 8.28], [7.1, 6.98, 5.99, 8.1, 6.78, 7.97], [7.74, 7.22, 5.98, 8.1, 6.36, 7.64], [7.34, 6.51, 5.2, 7.16, 5.25, 6.51], [9.06, 8.46, 7.16, 9.25, 7.33, 8.63], [8.5, 7.5, 6.16, 7.93, 5.83, 7.03], [9.43, 8.58, 7.22, 9.13, 7.04, 8.28]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 7.1), ('CB', 'HIS', 'CG', 'HIS', 7.74), ('CB', 'HIS', 'ND1', 'HIS', 7.34), ('CB', 'HIS', 'CD2', 'HIS', 9.06), ('CB', 'HIS', 'CE1', 'HIS', 8.5), ('CB', 'HIS', 'NE2', 'HIS', 9.43)], [('CG', 'HIS', 'CB', 'HIS', 6.98), ('CG', 'HIS', 'CG', 'HIS', 7.22), ('CG', 'HIS', 'ND1', 'HIS', 6.51), ('CG', 'HIS', 'CD2', 'HIS', 8.46), ('CG', 'HIS', 'CE1', 'HIS', 7.5), ('CG', 'HIS', 'NE2', 'HIS', 8.58)], [('ND1', 'HIS', 'CB', 'HIS', 5.99), ('ND1', 'HIS', 'CG', 'HIS', 5.98), ('ND1', 'HIS', 'ND1', 'HIS', 5.2), ('ND1', 'HIS', 'CD2', 'HIS', 7.16), ('ND1', 'HIS', 'CE1', 'HIS', 6.16), ('ND1', 'HIS', 'NE2', 'HIS', 7.22)], [('CD2', 'HIS', 'CB', 'HIS', 8.1), ('CD2', 'HIS', 'CG', 'HIS', 8.1), ('CD2', 'HIS', 'ND1', 'HIS', 7.16), ('CD2', 'HIS', 'CD2', 'HIS', 9.25), ('CD2', 'HIS', 'CE1', 'HIS', 7.93), ('CD2', 'HIS', 'NE2', 'HIS', 9.13)], [('CE1', 'HIS', 'CB', 'HIS', 6.78), ('CE1', 'HIS', 'CG', 'HIS', 6.36), ('CE1', 'HIS', 'ND1', 'HIS', 5.25), ('CE1', 'HIS', 'CD2', 'HIS', 7.33), ('CE1', 'HIS', 'CE1', 'HIS', 5.83), ('CE1', 'HIS', 'NE2', 'HIS', 7.04)], [('NE2', 'HIS', 'CB', 'HIS', 7.97), ('NE2', 'HIS', 'CG', 'HIS', 7.64), ('NE2', 'HIS', 'ND1', 'HIS', 6.51), ('NE2', 'HIS', 'CD2', 'HIS', 8.63), ('NE2', 'HIS', 'CE1', 'HIS', 7.03), ('NE2', 'HIS', 'NE2', 'HIS', 8.28)], [('CB', 'HIS', 'CB', 'HIS', 7.1), ('CB', 'HIS', 'CG', 'HIS', 6.98), ('CB', 'HIS', 'ND1', 'HIS', 5.99), ('CB', 'HIS', 'CD2', 'HIS', 8.1), ('CB', 'HIS', 'CE1', 'HIS', 6.78), ('CB', 'HIS', 'NE2', 'HIS', 7.97)], [('CG', 'HIS', 'CB', 'HIS', 7.74), ('CG', 'HIS', 'CG', 'HIS', 7.22), ('CG', 'HIS', 'ND1', 'HIS', 5.98), ('CG', 'HIS', 'CD2', 'HIS', 8.1), ('CG', 'HIS', 'CE1', 'HIS', 6.36), ('CG', 'HIS', 'NE2', 'HIS', 7.64)], [('ND1', 'HIS', 'CB', 'HIS', 7.34), ('ND1', 'HIS', 'CG', 'HIS', 6.51), ('ND1', 'HIS', 'ND1', 'HIS', 5.2), ('ND1', 'HIS', 'CD2', 'HIS', 7.16), ('ND1', 'HIS', 'CE1', 'HIS', 5.25), ('ND1', 'HIS', 'NE2', 'HIS', 6.51)], [('CD2', 'HIS', 'CB', 'HIS', 9.06), ('CD2', 'HIS', 'CG', 'HIS', 8.46), ('CD2', 'HIS', 'ND1', 'HIS', 7.16), ('CD2', 'HIS', 'CD2', 'HIS', 9.25), ('CD2', 'HIS', 'CE1', 'HIS', 7.33), ('CD2', 'HIS', 'NE2', 'HIS', 8.63)], [('CE1', 'HIS', 'CB', 'HIS', 8.5), ('CE1', 'HIS', 'CG', 'HIS', 7.5), ('CE1', 'HIS', 'ND1', 'HIS', 6.16), ('CE1', 'HIS', 'CD2', 'HIS', 7.93), ('CE1', 'HIS', 'CE1', 'HIS', 5.83), ('CE1', 'HIS', 'NE2', 'HIS', 7.03)], [('NE2', 'HIS', 'CB', 'HIS', 9.43), ('NE2', 'HIS', 'CG', 'HIS', 8.58), ('NE2', 'HIS', 'ND1', 'HIS', 7.22), ('NE2', 'HIS', 'CD2', 'HIS', 9.13), ('NE2', 'HIS', 'CE1', 'HIS', 7.04), ('NE2', 'HIS', 'NE2', 'HIS', 8.28)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_CYS, d, 'A_1nmw_5_2_1_8')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_HISI, d, 'A_1nmw_5_2_1_8')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_HIS, d, 'A_1nmw_5_2_1_8')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_CYS' :  match1,
		'CYS_HISI' :  match2,
		'HIS_HIS' :  match3}