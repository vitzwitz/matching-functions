'''
FUNC:M_1kcz_4_3_1_2
PDB:1kcz
EC:4.3.1.2
RESI:his,lys,mg
LOCI:a-194,331,901;
'''
import motifFunctions as cmd
LYS_HIS = { 
	'distances':
		[[16.52, 15.49, 15.85, 14.24, 14.91, 13.86], [15.7, 14.62, 14.96, 13.32, 13.97, 12.9], [16.19, 15.02, 15.23, 13.72, 14.14, 13.14], [15.5, 14.3, 14.49, 12.98, 13.37, 12.36], [16.1, 14.82, 14.88, 13.53, 13.68, 12.77]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'HIS', 16.52), ('CB', 'LYS', 'CG', 'HIS', 15.49), ('CB', 'LYS', 'ND1', 'HIS', 15.85), ('CB', 'LYS', 'CD2', 'HIS', 14.24), ('CB', 'LYS', 'CE1', 'HIS', 14.91), ('CB', 'LYS', 'NE2', 'HIS', 13.86)], [('CG', 'LYS', 'CB', 'HIS', 15.7), ('CG', 'LYS', 'CG', 'HIS', 14.62), ('CG', 'LYS', 'ND1', 'HIS', 14.96), ('CG', 'LYS', 'CD2', 'HIS', 13.32), ('CG', 'LYS', 'CE1', 'HIS', 13.97), ('CG', 'LYS', 'NE2', 'HIS', 12.9)], [('CD', 'LYS', 'CB', 'HIS', 16.19), ('CD', 'LYS', 'CG', 'HIS', 15.02), ('CD', 'LYS', 'ND1', 'HIS', 15.23), ('CD', 'LYS', 'CD2', 'HIS', 13.72), ('CD', 'LYS', 'CE1', 'HIS', 14.14), ('CD', 'LYS', 'NE2', 'HIS', 13.14)], [('CE', 'LYS', 'CB', 'HIS', 15.5), ('CE', 'LYS', 'CG', 'HIS', 14.3), ('CE', 'LYS', 'ND1', 'HIS', 14.49), ('CE', 'LYS', 'CD2', 'HIS', 12.98), ('CE', 'LYS', 'CE1', 'HIS', 13.37), ('CE', 'LYS', 'NE2', 'HIS', 12.36)], [('NZ', 'LYS', 'CB', 'HIS', 16.1), ('NZ', 'LYS', 'CG', 'HIS', 14.82), ('NZ', 'LYS', 'ND1', 'HIS', 14.88), ('NZ', 'LYS', 'CD2', 'HIS', 13.53), ('NZ', 'LYS', 'CE1', 'HIS', 13.68), ('NZ', 'LYS', 'NE2', 'HIS', 12.77)]]}
HIS_MG = { 
	'distances':
		[[9.96], [8.6], [8.5], [7.46], [7.32], [6.52]],
	'comparisons':
		[[('CB', 'HIS', 'MG', 'MG', 9.96)], [('CG', 'HIS', 'MG', 'MG', 8.6)], [('ND1', 'HIS', 'MG', 'MG', 8.5)], [('CD2', 'HIS', 'MG', 'MG', 7.46)], [('CE1', 'HIS', 'MG', 'MG', 7.32)], [('NE2', 'HIS', 'MG', 'MG', 6.52)]]}
LYS_MG = { 
	'distances':
		[[11.49], [10.2], [9.98], [8.84], [8.89]],
	'comparisons':
		[[('CB', 'LYS', 'MG', 'MG', 11.49)], [('CG', 'LYS', 'MG', 'MG', 10.2)], [('CD', 'LYS', 'MG', 'MG', 9.98)], [('CE', 'LYS', 'MG', 'MG', 8.84)], [('NZ', 'LYS', 'MG', 'MG', 8.89)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_HIS, d, 'M_1kcz_4_3_1_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_MG, d, 'M_1kcz_4_3_1_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LYS_MG, d, 'M_1kcz_4_3_1_2')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_HIS' :  match1,
		'HIS_MG' :  match2,
		'LYS_MG' :  match3}