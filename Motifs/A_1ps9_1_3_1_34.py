'''
FUNC:A_1ps9_1_3_1_34
PDB:1ps9
EC:1.3.1.34
RESI:tyr,his
LOCI:a-166,252;
'''
import motifFunctions as cmd
TYR_HIS = { 
	'distances':
		[[10.53, 9.9, 10.67, 8.82, 10.22, 9.08], [9.5, 8.71, 9.42, 7.54, 8.87, 7.69], [8.99, 8.24, 9.07, 7.01, 8.57, 7.29], [9.37, 8.39, 8.86, 7.24, 8.16, 7.1], [8.31, 7.4, 8.13, 6.08, 7.52, 6.21], [8.74, 7.57, 7.88, 6.37, 7.03, 5.96], [8.18, 7.03, 7.47, 5.7, 6.65, 5.41], [7.95, 6.64, 6.85, 5.36, 5.87, 4.72]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'HIS', 10.53), ('CB', 'TYR', 'CG', 'HIS', 9.9), ('CB', 'TYR', 'ND1', 'HIS', 10.67), ('CB', 'TYR', 'CD2', 'HIS', 8.82), ('CB', 'TYR', 'CE1', 'HIS', 10.22), ('CB', 'TYR', 'NE2', 'HIS', 9.08)], [('CG', 'TYR', 'CB', 'HIS', 9.5), ('CG', 'TYR', 'CG', 'HIS', 8.71), ('CG', 'TYR', 'ND1', 'HIS', 9.42), ('CG', 'TYR', 'CD2', 'HIS', 7.54), ('CG', 'TYR', 'CE1', 'HIS', 8.87), ('CG', 'TYR', 'NE2', 'HIS', 7.69)], [('CD1', 'TYR', 'CB', 'HIS', 8.99), ('CD1', 'TYR', 'CG', 'HIS', 8.24), ('CD1', 'TYR', 'ND1', 'HIS', 9.07), ('CD1', 'TYR', 'CD2', 'HIS', 7.01), ('CD1', 'TYR', 'CE1', 'HIS', 8.57), ('CD1', 'TYR', 'NE2', 'HIS', 7.29)], [('CD2', 'TYR', 'CB', 'HIS', 9.37), ('CD2', 'TYR', 'CG', 'HIS', 8.39), ('CD2', 'TYR', 'ND1', 'HIS', 8.86), ('CD2', 'TYR', 'CD2', 'HIS', 7.24), ('CD2', 'TYR', 'CE1', 'HIS', 8.16), ('CD2', 'TYR', 'NE2', 'HIS', 7.1)], [('CE1', 'TYR', 'CB', 'HIS', 8.31), ('CE1', 'TYR', 'CG', 'HIS', 7.4), ('CE1', 'TYR', 'ND1', 'HIS', 8.13), ('CE1', 'TYR', 'CD2', 'HIS', 6.08), ('CE1', 'TYR', 'CE1', 'HIS', 7.52), ('CE1', 'TYR', 'NE2', 'HIS', 6.21)], [('CE2', 'TYR', 'CB', 'HIS', 8.74), ('CE2', 'TYR', 'CG', 'HIS', 7.57), ('CE2', 'TYR', 'ND1', 'HIS', 7.88), ('CE2', 'TYR', 'CD2', 'HIS', 6.37), ('CE2', 'TYR', 'CE1', 'HIS', 7.03), ('CE2', 'TYR', 'NE2', 'HIS', 5.96)], [('CZ', 'TYR', 'CB', 'HIS', 8.18), ('CZ', 'TYR', 'CG', 'HIS', 7.03), ('CZ', 'TYR', 'ND1', 'HIS', 7.47), ('CZ', 'TYR', 'CD2', 'HIS', 5.7), ('CZ', 'TYR', 'CE1', 'HIS', 6.65), ('CZ', 'TYR', 'NE2', 'HIS', 5.41)], [('OH', 'TYR', 'CB', 'HIS', 7.95), ('OH', 'TYR', 'CG', 'HIS', 6.64), ('OH', 'TYR', 'ND1', 'HIS', 6.85), ('OH', 'TYR', 'CD2', 'HIS', 5.36), ('OH', 'TYR', 'CE1', 'HIS', 5.87), ('OH', 'TYR', 'NE2', 'HIS', 4.72)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TYR_HIS, d, 'A_1ps9_1_3_1_34')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TYR_HIS' :  match1}