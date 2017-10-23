'''
FUNC:A_1cf2_1_2_1_59
PDB:1cf2
EC:1.2.1.59
RESI:cys,his
LOCI:o-140,219;
'''
import motifFunctions as cmd
CYS_HIS = { 
	'distances':
		[[8.96, 8.02, 8.64, 6.67, 7.93, 6.64], [8.44, 7.25, 7.55, 5.96, 6.64, 5.49]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 8.96), ('CB', 'CYS', 'CG', 'HIS', 8.02), ('CB', 'CYS', 'ND1', 'HIS', 8.64), ('CB', 'CYS', 'CD2', 'HIS', 6.67), ('CB', 'CYS', 'CE1', 'HIS', 7.93), ('CB', 'CYS', 'NE2', 'HIS', 6.64)], [('SG', 'CYS', 'CB', 'HIS', 8.44), ('SG', 'CYS', 'CG', 'HIS', 7.25), ('SG', 'CYS', 'ND1', 'HIS', 7.55), ('SG', 'CYS', 'CD2', 'HIS', 5.96), ('SG', 'CYS', 'CE1', 'HIS', 6.64), ('SG', 'CYS', 'NE2', 'HIS', 5.49)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_HIS, d, 'A_1cf2_1_2_1_59')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_HIS' :  match1}