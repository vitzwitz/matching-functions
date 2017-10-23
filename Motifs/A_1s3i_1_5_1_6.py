'''
FUNC:A_1s3i_1_5_1_6
PDB:1s3i
EC:1.5.1.6
RESI:his,asp
LOCI:a-106,142;
'''
import motifFunctions as cmd
ASP_HIS = { 
	'distances':
		[[7.9, 7.16, 6.5, 7.47, 6.43, 7.04], [7.33, 6.55, 5.59, 7.08, 5.63, 6.57], [7.12, 6.66, 5.72, 7.47, 6.15, 7.19], [7.47, 6.45, 5.28, 6.82, 4.98, 6.03]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 7.9), ('CB', 'ASP', 'CG', 'HIS', 7.16), ('CB', 'ASP', 'ND1', 'HIS', 6.5), ('CB', 'ASP', 'CD2', 'HIS', 7.47), ('CB', 'ASP', 'CE1', 'HIS', 6.43), ('CB', 'ASP', 'NE2', 'HIS', 7.04)], [('CG', 'ASP', 'CB', 'HIS', 7.33), ('CG', 'ASP', 'CG', 'HIS', 6.55), ('CG', 'ASP', 'ND1', 'HIS', 5.59), ('CG', 'ASP', 'CD2', 'HIS', 7.08), ('CG', 'ASP', 'CE1', 'HIS', 5.63), ('CG', 'ASP', 'NE2', 'HIS', 6.57)], [('OD1', 'ASP', 'CB', 'HIS', 7.12), ('OD1', 'ASP', 'CG', 'HIS', 6.66), ('OD1', 'ASP', 'ND1', 'HIS', 5.72), ('OD1', 'ASP', 'CD2', 'HIS', 7.47), ('OD1', 'ASP', 'CE1', 'HIS', 6.15), ('OD1', 'ASP', 'NE2', 'HIS', 7.19)], [('OD2', 'ASP', 'CB', 'HIS', 7.47), ('OD2', 'ASP', 'CG', 'HIS', 6.45), ('OD2', 'ASP', 'ND1', 'HIS', 5.28), ('OD2', 'ASP', 'CD2', 'HIS', 6.82), ('OD2', 'ASP', 'CE1', 'HIS', 4.98), ('OD2', 'ASP', 'NE2', 'HIS', 6.03)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HIS, d, 'A_1s3i_1_5_1_6')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HIS' :  match1}