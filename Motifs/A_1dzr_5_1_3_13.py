'''
FUNC:A_1dzr_5_1_3_13
PDB:1dzr
EC:5.1.3.13
RESI:his,asp
LOCI:a-63,170;
'''
import motifFunctions as cmd
ASP_HIS = { 
	'distances':
		[[9.47, 8.11, 8.0, 6.98, 6.85, 6.07, 11.83, 11.17, 9.66, 9.19], [8.28, 6.84, 6.6, 5.82, 5.38, 4.72, 10.88, 10.2, 8.69, 8.36], [7.49, 6.07, 5.99, 4.94, 4.83, 3.92, 10.2, 9.41, 7.91, 7.79], [8.33, 6.88, 6.35, 6.1, 5.1, 4.86, 10.96, 10.38, 8.9, 8.53], [11.09, 9.98, 10.31, 8.7, 9.37, 8.27, 12.89, 12.2, 10.8, 10.24], [11.13, 9.9, 10.08, 8.62, 9.01, 8.0, 13.22, 12.49, 11.03, 10.57], [9.96, 8.65, 8.75, 7.39, 7.63, 6.65, 12.29, 11.51, 10.03, 9.7], [10.53, 9.16, 9.14, 7.94, 7.95, 7.07, 13.1, 12.24, 10.76, 10.62]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 9.47), ('CB', 'ASP', 'CG', 'HIS', 8.11), ('CB', 'ASP', 'ND1', 'HIS', 8.0), ('CB', 'ASP', 'CD2', 'HIS', 6.98), ('CB', 'ASP', 'CE1', 'HIS', 6.85), ('CB', 'ASP', 'NE2', 'HIS', 6.07), ('CB', 'ASP', 'O', 'HIS', 11.83), ('CB', 'ASP', 'C', 'HIS', 11.17), ('CB', 'ASP', 'CA', 'HIS', 9.66), ('CB', 'ASP', 'N', 'HIS', 9.19)], [('CG', 'ASP', 'CB', 'HIS', 8.28), ('CG', 'ASP', 'CG', 'HIS', 6.84), ('CG', 'ASP', 'ND1', 'HIS', 6.6), ('CG', 'ASP', 'CD2', 'HIS', 5.82), ('CG', 'ASP', 'CE1', 'HIS', 5.38), ('CG', 'ASP', 'NE2', 'HIS', 4.72), ('CG', 'ASP', 'O', 'HIS', 10.88), ('CG', 'ASP', 'C', 'HIS', 10.2), ('CG', 'ASP', 'CA', 'HIS', 8.69), ('CG', 'ASP', 'N', 'HIS', 8.36)], [('OD1', 'ASP', 'CB', 'HIS', 7.49), ('OD1', 'ASP', 'CG', 'HIS', 6.07), ('OD1', 'ASP', 'ND1', 'HIS', 5.99), ('OD1', 'ASP', 'CD2', 'HIS', 4.94), ('OD1', 'ASP', 'CE1', 'HIS', 4.83), ('OD1', 'ASP', 'NE2', 'HIS', 3.92), ('OD1', 'ASP', 'O', 'HIS', 10.2), ('OD1', 'ASP', 'C', 'HIS', 9.41), ('OD1', 'ASP', 'CA', 'HIS', 7.91), ('OD1', 'ASP', 'N', 'HIS', 7.79)], [('OD2', 'ASP', 'CB', 'HIS', 8.33), ('OD2', 'ASP', 'CG', 'HIS', 6.88), ('OD2', 'ASP', 'ND1', 'HIS', 6.35), ('OD2', 'ASP', 'CD2', 'HIS', 6.1), ('OD2', 'ASP', 'CE1', 'HIS', 5.1), ('OD2', 'ASP', 'NE2', 'HIS', 4.86), ('OD2', 'ASP', 'O', 'HIS', 10.96), ('OD2', 'ASP', 'C', 'HIS', 10.38), ('OD2', 'ASP', 'CA', 'HIS', 8.9), ('OD2', 'ASP', 'N', 'HIS', 8.53)], [('O', 'ASP', 'CB', 'HIS', 11.09), ('O', 'ASP', 'CG', 'HIS', 9.98), ('O', 'ASP', 'ND1', 'HIS', 10.31), ('O', 'ASP', 'CD2', 'HIS', 8.7), ('O', 'ASP', 'CE1', 'HIS', 9.37), ('O', 'ASP', 'NE2', 'HIS', 8.27), ('O', 'ASP', 'O', 'HIS', 12.89), ('O', 'ASP', 'C', 'HIS', 12.2), ('O', 'ASP', 'CA', 'HIS', 10.8), ('O', 'ASP', 'N', 'HIS', 10.24)], [('C', 'ASP', 'CB', 'HIS', 11.13), ('C', 'ASP', 'CG', 'HIS', 9.9), ('C', 'ASP', 'ND1', 'HIS', 10.08), ('C', 'ASP', 'CD2', 'HIS', 8.62), ('C', 'ASP', 'CE1', 'HIS', 9.01), ('C', 'ASP', 'NE2', 'HIS', 8.0), ('C', 'ASP', 'O', 'HIS', 13.22), ('C', 'ASP', 'C', 'HIS', 12.49), ('C', 'ASP', 'CA', 'HIS', 11.03), ('C', 'ASP', 'N', 'HIS', 10.57)], [('CA', 'ASP', 'CB', 'HIS', 9.96), ('CA', 'ASP', 'CG', 'HIS', 8.65), ('CA', 'ASP', 'ND1', 'HIS', 8.75), ('CA', 'ASP', 'CD2', 'HIS', 7.39), ('CA', 'ASP', 'CE1', 'HIS', 7.63), ('CA', 'ASP', 'NE2', 'HIS', 6.65), ('CA', 'ASP', 'O', 'HIS', 12.29), ('CA', 'ASP', 'C', 'HIS', 11.51), ('CA', 'ASP', 'CA', 'HIS', 10.03), ('CA', 'ASP', 'N', 'HIS', 9.7)], [('N', 'ASP', 'CB', 'HIS', 10.53), ('N', 'ASP', 'CG', 'HIS', 9.16), ('N', 'ASP', 'ND1', 'HIS', 9.14), ('N', 'ASP', 'CD2', 'HIS', 7.94), ('N', 'ASP', 'CE1', 'HIS', 7.95), ('N', 'ASP', 'NE2', 'HIS', 7.07), ('N', 'ASP', 'O', 'HIS', 13.1), ('N', 'ASP', 'C', 'HIS', 12.24), ('N', 'ASP', 'CA', 'HIS', 10.76), ('N', 'ASP', 'N', 'HIS', 10.62)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HIS, d, 'A_1dzr_5_1_3_13')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HIS' :  match1}