'''
FUNC:A_1szj_1_2_1_12
PDB:1szj
EC:1.2.1.12
RESI:cys,his
LOCI:r-149,176;
'''
import motifFunctions as cmd
CYS_HIS = { 
	'distances':
		[[10.83, 9.57, 9.59, 8.37, 8.48, 7.64], [9.39, 8.05, 8.03, 6.84, 6.88, 6.01]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 10.83), ('CB', 'CYS', 'CG', 'HIS', 9.57), ('CB', 'CYS', 'ND1', 'HIS', 9.59), ('CB', 'CYS', 'CD2', 'HIS', 8.37), ('CB', 'CYS', 'CE1', 'HIS', 8.48), ('CB', 'CYS', 'NE2', 'HIS', 7.64)], [('SG', 'CYS', 'CB', 'HIS', 9.39), ('SG', 'CYS', 'CG', 'HIS', 8.05), ('SG', 'CYS', 'ND1', 'HIS', 8.03), ('SG', 'CYS', 'CD2', 'HIS', 6.84), ('SG', 'CYS', 'CE1', 'HIS', 6.88), ('SG', 'CYS', 'NE2', 'HIS', 6.01)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_HIS, d, 'A_1szj_1_2_1_12')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_HIS' :  match1}