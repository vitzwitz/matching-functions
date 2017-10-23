'''
FUNC:A_1c9u_1_1_5_2
PDB:1c9u
EC:1.1.5.2
RESI:his,asp
LOCI:a-144,163;
'''
import motifFunctions as cmd
HIS_ASP = { 
	'distances':
		[[7.58, 6.8, 5.56, 7.65, 7.69, 6.92, 7.15, 6.37], [8.08, 6.97, 5.76, 7.54, 8.23, 7.69, 7.97, 7.39], [7.49, 6.19, 5.1, 6.52, 7.72, 7.39, 7.68, 7.38], [9.36, 8.18, 7.01, 8.61, 9.51, 9.02, 9.31, 8.7], [8.55, 7.14, 6.2, 7.2, 8.79, 8.59, 8.89, 8.66], [9.59, 8.25, 7.21, 8.42, 9.78, 9.48, 9.79, 9.36], [7.62, 7.55, 6.58, 8.72, 7.38, 6.31, 6.54, 5.54], [8.64, 8.37, 7.28, 9.47, 8.38, 7.39, 7.67, 6.67], [8.8, 8.19, 6.98, 9.12, 8.61, 7.77, 8.11, 7.21], [9.56, 8.87, 7.66, 9.73, 8.88, 8.23, 8.87, 8.19]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.58), ('CB', 'HIS', 'CG', 'ASP', 6.8), ('CB', 'HIS', 'OD1', 'ASP', 5.56), ('CB', 'HIS', 'OD2', 'ASP', 7.65), ('CB', 'HIS', 'O', 'ASP', 7.69), ('CB', 'HIS', 'C', 'ASP', 6.92), ('CB', 'HIS', 'CA', 'ASP', 7.15), ('CB', 'HIS', 'N', 'ASP', 6.37)], [('CG', 'HIS', 'CB', 'ASP', 8.08), ('CG', 'HIS', 'CG', 'ASP', 6.97), ('CG', 'HIS', 'OD1', 'ASP', 5.76), ('CG', 'HIS', 'OD2', 'ASP', 7.54), ('CG', 'HIS', 'O', 'ASP', 8.23), ('CG', 'HIS', 'C', 'ASP', 7.69), ('CG', 'HIS', 'CA', 'ASP', 7.97), ('CG', 'HIS', 'N', 'ASP', 7.39)], [('ND1', 'HIS', 'CB', 'ASP', 7.49), ('ND1', 'HIS', 'CG', 'ASP', 6.19), ('ND1', 'HIS', 'OD1', 'ASP', 5.1), ('ND1', 'HIS', 'OD2', 'ASP', 6.52), ('ND1', 'HIS', 'O', 'ASP', 7.72), ('ND1', 'HIS', 'C', 'ASP', 7.39), ('ND1', 'HIS', 'CA', 'ASP', 7.68), ('ND1', 'HIS', 'N', 'ASP', 7.38)], [('CD2', 'HIS', 'CB', 'ASP', 9.36), ('CD2', 'HIS', 'CG', 'ASP', 8.18), ('CD2', 'HIS', 'OD1', 'ASP', 7.01), ('CD2', 'HIS', 'OD2', 'ASP', 8.61), ('CD2', 'HIS', 'O', 'ASP', 9.51), ('CD2', 'HIS', 'C', 'ASP', 9.02), ('CD2', 'HIS', 'CA', 'ASP', 9.31), ('CD2', 'HIS', 'N', 'ASP', 8.7)], [('CE1', 'HIS', 'CB', 'ASP', 8.55), ('CE1', 'HIS', 'CG', 'ASP', 7.14), ('CE1', 'HIS', 'OD1', 'ASP', 6.2), ('CE1', 'HIS', 'OD2', 'ASP', 7.2), ('CE1', 'HIS', 'O', 'ASP', 8.79), ('CE1', 'HIS', 'C', 'ASP', 8.59), ('CE1', 'HIS', 'CA', 'ASP', 8.89), ('CE1', 'HIS', 'N', 'ASP', 8.66)], [('NE2', 'HIS', 'CB', 'ASP', 9.59), ('NE2', 'HIS', 'CG', 'ASP', 8.25), ('NE2', 'HIS', 'OD1', 'ASP', 7.21), ('NE2', 'HIS', 'OD2', 'ASP', 8.42), ('NE2', 'HIS', 'O', 'ASP', 9.78), ('NE2', 'HIS', 'C', 'ASP', 9.48), ('NE2', 'HIS', 'CA', 'ASP', 9.79), ('NE2', 'HIS', 'N', 'ASP', 9.36)], [('O', 'HIS', 'CB', 'ASP', 7.62), ('O', 'HIS', 'CG', 'ASP', 7.55), ('O', 'HIS', 'OD1', 'ASP', 6.58), ('O', 'HIS', 'OD2', 'ASP', 8.72), ('O', 'HIS', 'O', 'ASP', 7.38), ('O', 'HIS', 'C', 'ASP', 6.31), ('O', 'HIS', 'CA', 'ASP', 6.54), ('O', 'HIS', 'N', 'ASP', 5.54)], [('C', 'HIS', 'CB', 'ASP', 8.64), ('C', 'HIS', 'CG', 'ASP', 8.37), ('C', 'HIS', 'OD1', 'ASP', 7.28), ('C', 'HIS', 'OD2', 'ASP', 9.47), ('C', 'HIS', 'O', 'ASP', 8.38), ('C', 'HIS', 'C', 'ASP', 7.39), ('C', 'HIS', 'CA', 'ASP', 7.67), ('C', 'HIS', 'N', 'ASP', 6.67)], [('CA', 'HIS', 'CB', 'ASP', 8.8), ('CA', 'HIS', 'CG', 'ASP', 8.19), ('CA', 'HIS', 'OD1', 'ASP', 6.98), ('CA', 'HIS', 'OD2', 'ASP', 9.12), ('CA', 'HIS', 'O', 'ASP', 8.61), ('CA', 'HIS', 'C', 'ASP', 7.77), ('CA', 'HIS', 'CA', 'ASP', 8.11), ('CA', 'HIS', 'N', 'ASP', 7.21)], [('N', 'HIS', 'CB', 'ASP', 9.56), ('N', 'HIS', 'CG', 'ASP', 8.87), ('N', 'HIS', 'OD1', 'ASP', 7.66), ('N', 'HIS', 'OD2', 'ASP', 9.73), ('N', 'HIS', 'O', 'ASP', 8.88), ('N', 'HIS', 'C', 'ASP', 8.23), ('N', 'HIS', 'CA', 'ASP', 8.87), ('N', 'HIS', 'N', 'ASP', 8.19)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASP, d, 'A_1c9u_1_1_5_2')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASP' :  match1}