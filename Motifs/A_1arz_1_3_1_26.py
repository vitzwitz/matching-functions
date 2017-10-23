'''
FUNC:A_1arz_1_3_1_26
PDB:1arz
EC:1.3.1.26
RESI:his,lys
LOCI:a-159,163;
'''
import motifFunctions as cmd
HIS_LYS = { 
	'distances':
		[[6.17, 6.62, 5.79, 6.95, 8.07], [6.86, 6.86, 5.63, 6.41, 7.49], [7.41, 7.11, 5.75, 6.14, 7.38], [7.55, 7.41, 6.1, 6.67, 7.45], [8.28, 7.76, 6.26, 6.27, 7.29], [8.37, 7.93, 6.45, 6.58, 7.32]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'LYS', 6.17), ('CB', 'HIS', 'CG', 'LYS', 6.62), ('CB', 'HIS', 'CD', 'LYS', 5.79), ('CB', 'HIS', 'CE', 'LYS', 6.95), ('CB', 'HIS', 'NZ', 'LYS', 8.07)], [('CG', 'HIS', 'CB', 'LYS', 6.86), ('CG', 'HIS', 'CG', 'LYS', 6.86), ('CG', 'HIS', 'CD', 'LYS', 5.63), ('CG', 'HIS', 'CE', 'LYS', 6.41), ('CG', 'HIS', 'NZ', 'LYS', 7.49)], [('ND1', 'HIS', 'CB', 'LYS', 7.41), ('ND1', 'HIS', 'CG', 'LYS', 7.11), ('ND1', 'HIS', 'CD', 'LYS', 5.75), ('ND1', 'HIS', 'CE', 'LYS', 6.14), ('ND1', 'HIS', 'NZ', 'LYS', 7.38)], [('CD2', 'HIS', 'CB', 'LYS', 7.55), ('CD2', 'HIS', 'CG', 'LYS', 7.41), ('CD2', 'HIS', 'CD', 'LYS', 6.1), ('CD2', 'HIS', 'CE', 'LYS', 6.67), ('CD2', 'HIS', 'NZ', 'LYS', 7.45)], [('CE1', 'HIS', 'CB', 'LYS', 8.28), ('CE1', 'HIS', 'CG', 'LYS', 7.76), ('CE1', 'HIS', 'CD', 'LYS', 6.26), ('CE1', 'HIS', 'CE', 'LYS', 6.27), ('CE1', 'HIS', 'NZ', 'LYS', 7.29)], [('NE2', 'HIS', 'CB', 'LYS', 8.37), ('NE2', 'HIS', 'CG', 'LYS', 7.93), ('NE2', 'HIS', 'CD', 'LYS', 6.45), ('NE2', 'HIS', 'CE', 'LYS', 6.58), ('NE2', 'HIS', 'NZ', 'LYS', 7.32)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_LYS, d, 'A_1arz_1_3_1_26')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_LYS' :  match1}