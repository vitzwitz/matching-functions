'''
FUNC:M_2b3i_1_10_99_1
PDB:2b3i
EC:1.10.99.1
RESI:his,cu1
LOCI:a-85,110;
'''
import motifFunctions as cmd
HIS_CU1 = { 
	'distances':
		[[5.55], [5.12], [4.03], [6.19], [4.92], [6.1]],
	'comparisons':
		[[('CB', 'HIS', 'CU', 'CU1', 5.55)], [('CG', 'HIS', 'CU', 'CU1', 5.12)], [('ND1', 'HIS', 'CU', 'CU1', 4.03)], [('CD2', 'HIS', 'CU', 'CU1', 6.19)], [('CE1', 'HIS', 'CU', 'CU1', 4.92)], [('NE2', 'HIS', 'CU', 'CU1', 6.1)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_CU1, d, 'M_2b3i_1_10_99_1')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_CU1' :  match1}