'''
FUNC:A_1aui_3_1_3_16
PDB:1aui
EC:3.1.3.16
RESI:asp,his
LOCI:a-121,151;
'''
import motifFunctions as cmd
ASP_HIS = { 
	'distances':
		[[6.25, 5.97, 5.05, 6.91, 5.67, 6.74, 7.49, 7.91, 7.49, 8.64], [6.12, 6.07, 5.16, 7.22, 6.03, 7.18, 6.63, 7.28, 7.08, 8.4], [7.16, 7.25, 6.37, 8.44, 7.23, 8.4, 7.17, 7.99, 8.02, 9.39], [5.3, 5.25, 4.4, 6.46, 5.43, 6.53, 5.72, 6.34, 6.07, 7.4], [8.07, 7.78, 7.25, 8.3, 7.48, 8.11, 9.88, 10.03, 9.54, 10.38], [8.08, 7.76, 7.0, 8.41, 7.28, 8.13, 9.61, 9.92, 9.49, 10.47], [7.33, 7.24, 6.49, 8.15, 7.08, 8.05, 8.41, 8.86, 8.62, 9.76], [7.11, 7.37, 6.94, 8.37, 7.74, 8.55, 7.96, 8.39, 8.37, 9.49]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 6.25), ('CB', 'ASP', 'CG', 'HIS', 5.97), ('CB', 'ASP', 'ND1', 'HIS', 5.05), ('CB', 'ASP', 'CD2', 'HIS', 6.91), ('CB', 'ASP', 'CE1', 'HIS', 5.67), ('CB', 'ASP', 'NE2', 'HIS', 6.74), ('CB', 'ASP', 'O', 'HIS', 7.49), ('CB', 'ASP', 'C', 'HIS', 7.91), ('CB', 'ASP', 'CA', 'HIS', 7.49), ('CB', 'ASP', 'N', 'HIS', 8.64)], [('CG', 'ASP', 'CB', 'HIS', 6.12), ('CG', 'ASP', 'CG', 'HIS', 6.07), ('CG', 'ASP', 'ND1', 'HIS', 5.16), ('CG', 'ASP', 'CD2', 'HIS', 7.22), ('CG', 'ASP', 'CE1', 'HIS', 6.03), ('CG', 'ASP', 'NE2', 'HIS', 7.18), ('CG', 'ASP', 'O', 'HIS', 6.63), ('CG', 'ASP', 'C', 'HIS', 7.28), ('CG', 'ASP', 'CA', 'HIS', 7.08), ('CG', 'ASP', 'N', 'HIS', 8.4)], [('OD1', 'ASP', 'CB', 'HIS', 7.16), ('OD1', 'ASP', 'CG', 'HIS', 7.25), ('OD1', 'ASP', 'ND1', 'HIS', 6.37), ('OD1', 'ASP', 'CD2', 'HIS', 8.44), ('OD1', 'ASP', 'CE1', 'HIS', 7.23), ('OD1', 'ASP', 'NE2', 'HIS', 8.4), ('OD1', 'ASP', 'O', 'HIS', 7.17), ('OD1', 'ASP', 'C', 'HIS', 7.99), ('OD1', 'ASP', 'CA', 'HIS', 8.02), ('OD1', 'ASP', 'N', 'HIS', 9.39)], [('OD2', 'ASP', 'CB', 'HIS', 5.3), ('OD2', 'ASP', 'CG', 'HIS', 5.25), ('OD2', 'ASP', 'ND1', 'HIS', 4.4), ('OD2', 'ASP', 'CD2', 'HIS', 6.46), ('OD2', 'ASP', 'CE1', 'HIS', 5.43), ('OD2', 'ASP', 'NE2', 'HIS', 6.53), ('OD2', 'ASP', 'O', 'HIS', 5.72), ('OD2', 'ASP', 'C', 'HIS', 6.34), ('OD2', 'ASP', 'CA', 'HIS', 6.07), ('OD2', 'ASP', 'N', 'HIS', 7.4)], [('O', 'ASP', 'CB', 'HIS', 8.07), ('O', 'ASP', 'CG', 'HIS', 7.78), ('O', 'ASP', 'ND1', 'HIS', 7.25), ('O', 'ASP', 'CD2', 'HIS', 8.3), ('O', 'ASP', 'CE1', 'HIS', 7.48), ('O', 'ASP', 'NE2', 'HIS', 8.11), ('O', 'ASP', 'O', 'HIS', 9.88), ('O', 'ASP', 'C', 'HIS', 10.03), ('O', 'ASP', 'CA', 'HIS', 9.54), ('O', 'ASP', 'N', 'HIS', 10.38)], [('C', 'ASP', 'CB', 'HIS', 8.08), ('C', 'ASP', 'CG', 'HIS', 7.76), ('C', 'ASP', 'ND1', 'HIS', 7.0), ('C', 'ASP', 'CD2', 'HIS', 8.41), ('C', 'ASP', 'CE1', 'HIS', 7.28), ('C', 'ASP', 'NE2', 'HIS', 8.13), ('C', 'ASP', 'O', 'HIS', 9.61), ('C', 'ASP', 'C', 'HIS', 9.92), ('C', 'ASP', 'CA', 'HIS', 9.49), ('C', 'ASP', 'N', 'HIS', 10.47)], [('CA', 'ASP', 'CB', 'HIS', 7.33), ('CA', 'ASP', 'CG', 'HIS', 7.24), ('CA', 'ASP', 'ND1', 'HIS', 6.49), ('CA', 'ASP', 'CD2', 'HIS', 8.15), ('CA', 'ASP', 'CE1', 'HIS', 7.08), ('CA', 'ASP', 'NE2', 'HIS', 8.05), ('CA', 'ASP', 'O', 'HIS', 8.41), ('CA', 'ASP', 'C', 'HIS', 8.86), ('CA', 'ASP', 'CA', 'HIS', 8.62), ('CA', 'ASP', 'N', 'HIS', 9.76)], [('N', 'ASP', 'CB', 'HIS', 7.11), ('N', 'ASP', 'CG', 'HIS', 7.37), ('N', 'ASP', 'ND1', 'HIS', 6.94), ('N', 'ASP', 'CD2', 'HIS', 8.37), ('N', 'ASP', 'CE1', 'HIS', 7.74), ('N', 'ASP', 'NE2', 'HIS', 8.55), ('N', 'ASP', 'O', 'HIS', 7.96), ('N', 'ASP', 'C', 'HIS', 8.39), ('N', 'ASP', 'CA', 'HIS', 8.37), ('N', 'ASP', 'N', 'HIS', 9.49)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HIS, d, 'A_1aui_3_1_3_16')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HIS' :  match1}