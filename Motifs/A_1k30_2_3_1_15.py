'''
FUNC:A_1k30_2_3_1_15
PDB:1k30
EC:2.3.1.15
RESI:his,asp
LOCI:a-139,144;
'''
import motifFunctions as cmd
HIS_ASP = { 
	'distances':
		[[7.41, 6.62, 7.44, 5.37, 10.47, 9.84, 8.88, 9.29], [6.91, 6.21, 7.03, 5.11, 10.08, 9.28, 8.27, 8.46], [5.68, 5.06, 5.9, 4.15, 8.9, 8.03, 6.97, 7.09], [7.84, 7.24, 8.0, 6.27, 11.01, 10.1, 9.1, 9.09], [6.13, 5.71, 6.42, 5.1, 9.25, 8.23, 7.19, 7.0], [7.42, 6.96, 7.65, 6.23, 10.52, 9.49, 8.5, 8.28], [8.53, 7.21, 7.46, 6.13, 11.53, 11.02, 9.77, 10.04], [7.32, 6.02, 6.37, 4.91, 10.31, 9.8, 8.58, 8.94], [7.02, 6.01, 6.71, 4.76, 9.95, 9.47, 8.45, 9.01], [8.17, 7.22, 7.88, 6.01, 10.88, 10.54, 9.62, 10.3]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.41), ('CB', 'HIS', 'CG', 'ASP', 6.62), ('CB', 'HIS', 'OD1', 'ASP', 7.44), ('CB', 'HIS', 'OD2', 'ASP', 5.37), ('CB', 'HIS', 'O', 'ASP', 10.47), ('CB', 'HIS', 'C', 'ASP', 9.84), ('CB', 'HIS', 'CA', 'ASP', 8.88), ('CB', 'HIS', 'N', 'ASP', 9.29)], [('CG', 'HIS', 'CB', 'ASP', 6.91), ('CG', 'HIS', 'CG', 'ASP', 6.21), ('CG', 'HIS', 'OD1', 'ASP', 7.03), ('CG', 'HIS', 'OD2', 'ASP', 5.11), ('CG', 'HIS', 'O', 'ASP', 10.08), ('CG', 'HIS', 'C', 'ASP', 9.28), ('CG', 'HIS', 'CA', 'ASP', 8.27), ('CG', 'HIS', 'N', 'ASP', 8.46)], [('ND1', 'HIS', 'CB', 'ASP', 5.68), ('ND1', 'HIS', 'CG', 'ASP', 5.06), ('ND1', 'HIS', 'OD1', 'ASP', 5.9), ('ND1', 'HIS', 'OD2', 'ASP', 4.15), ('ND1', 'HIS', 'O', 'ASP', 8.9), ('ND1', 'HIS', 'C', 'ASP', 8.03), ('ND1', 'HIS', 'CA', 'ASP', 6.97), ('ND1', 'HIS', 'N', 'ASP', 7.09)], [('CD2', 'HIS', 'CB', 'ASP', 7.84), ('CD2', 'HIS', 'CG', 'ASP', 7.24), ('CD2', 'HIS', 'OD1', 'ASP', 8.0), ('CD2', 'HIS', 'OD2', 'ASP', 6.27), ('CD2', 'HIS', 'O', 'ASP', 11.01), ('CD2', 'HIS', 'C', 'ASP', 10.1), ('CD2', 'HIS', 'CA', 'ASP', 9.1), ('CD2', 'HIS', 'N', 'ASP', 9.09)], [('CE1', 'HIS', 'CB', 'ASP', 6.13), ('CE1', 'HIS', 'CG', 'ASP', 5.71), ('CE1', 'HIS', 'OD1', 'ASP', 6.42), ('CE1', 'HIS', 'OD2', 'ASP', 5.1), ('CE1', 'HIS', 'O', 'ASP', 9.25), ('CE1', 'HIS', 'C', 'ASP', 8.23), ('CE1', 'HIS', 'CA', 'ASP', 7.19), ('CE1', 'HIS', 'N', 'ASP', 7.0)], [('NE2', 'HIS', 'CB', 'ASP', 7.42), ('NE2', 'HIS', 'CG', 'ASP', 6.96), ('NE2', 'HIS', 'OD1', 'ASP', 7.65), ('NE2', 'HIS', 'OD2', 'ASP', 6.23), ('NE2', 'HIS', 'O', 'ASP', 10.52), ('NE2', 'HIS', 'C', 'ASP', 9.49), ('NE2', 'HIS', 'CA', 'ASP', 8.5), ('NE2', 'HIS', 'N', 'ASP', 8.28)], [('O', 'HIS', 'CB', 'ASP', 8.53), ('O', 'HIS', 'CG', 'ASP', 7.21), ('O', 'HIS', 'OD1', 'ASP', 7.46), ('O', 'HIS', 'OD2', 'ASP', 6.13), ('O', 'HIS', 'O', 'ASP', 11.53), ('O', 'HIS', 'C', 'ASP', 11.02), ('O', 'HIS', 'CA', 'ASP', 9.77), ('O', 'HIS', 'N', 'ASP', 10.04)], [('C', 'HIS', 'CB', 'ASP', 7.32), ('C', 'HIS', 'CG', 'ASP', 6.02), ('C', 'HIS', 'OD1', 'ASP', 6.37), ('C', 'HIS', 'OD2', 'ASP', 4.91), ('C', 'HIS', 'O', 'ASP', 10.31), ('C', 'HIS', 'C', 'ASP', 9.8), ('C', 'HIS', 'CA', 'ASP', 8.58), ('C', 'HIS', 'N', 'ASP', 8.94)], [('CA', 'HIS', 'CB', 'ASP', 7.02), ('CA', 'HIS', 'CG', 'ASP', 6.01), ('CA', 'HIS', 'OD1', 'ASP', 6.71), ('CA', 'HIS', 'OD2', 'ASP', 4.76), ('CA', 'HIS', 'O', 'ASP', 9.95), ('CA', 'HIS', 'C', 'ASP', 9.47), ('CA', 'HIS', 'CA', 'ASP', 8.45), ('CA', 'HIS', 'N', 'ASP', 9.01)], [('N', 'HIS', 'CB', 'ASP', 8.17), ('N', 'HIS', 'CG', 'ASP', 7.22), ('N', 'HIS', 'OD1', 'ASP', 7.88), ('N', 'HIS', 'OD2', 'ASP', 6.01), ('N', 'HIS', 'O', 'ASP', 10.88), ('N', 'HIS', 'C', 'ASP', 10.54), ('N', 'HIS', 'CA', 'ASP', 9.62), ('N', 'HIS', 'N', 'ASP', 10.3)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASP, d, 'A_1k30_2_3_1_15')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASP' :  match1}