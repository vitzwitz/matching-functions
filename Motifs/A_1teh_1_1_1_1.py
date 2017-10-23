'''
FUNC:A_1teh_1_1_1_1
PDB:1teh
EC:1.1.1.1
RESI:his,thr
LOCI:a-47,48;
'''
import motifFunctions as cmd
THR_HIS = { 
	'distances':
		[[7.44, 7.78, 7.42, 8.82, 8.3, 9.08, 6.28, 5.72, 6.84, 6.72], [7.34, 7.63, 7.04, 8.78, 7.96, 8.93, 6.89, 6.21, 7.14, 7.04], [8.85, 9.05, 8.58, 9.98, 9.28, 10.08, 7.23, 6.93, 8.2, 8.13], [8.1, 7.95, 7.78, 8.38, 8.12, 8.46, 5.19, 5.7, 7.18, 7.69], [7.4, 7.52, 7.47, 8.16, 8.06, 8.45, 4.86, 4.97, 6.38, 6.67], [6.49, 6.65, 6.42, 7.54, 7.19, 7.81, 4.77, 4.43, 5.79, 6.05], [5.18, 5.65, 5.74, 6.66, 6.74, 7.22, 4.24, 3.33, 4.41, 4.65]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'HIS', 7.44), ('CB', 'THR', 'CG', 'HIS', 7.78), ('CB', 'THR', 'ND1', 'HIS', 7.42), ('CB', 'THR', 'CD2', 'HIS', 8.82), ('CB', 'THR', 'CE1', 'HIS', 8.3), ('CB', 'THR', 'NE2', 'HIS', 9.08), ('CB', 'THR', 'O', 'HIS', 6.28), ('CB', 'THR', 'C', 'HIS', 5.72), ('CB', 'THR', 'CA', 'HIS', 6.84), ('CB', 'THR', 'N', 'HIS', 6.72)], [('OG1', 'THR', 'CB', 'HIS', 7.34), ('OG1', 'THR', 'CG', 'HIS', 7.63), ('OG1', 'THR', 'ND1', 'HIS', 7.04), ('OG1', 'THR', 'CD2', 'HIS', 8.78), ('OG1', 'THR', 'CE1', 'HIS', 7.96), ('OG1', 'THR', 'NE2', 'HIS', 8.93), ('OG1', 'THR', 'O', 'HIS', 6.89), ('OG1', 'THR', 'C', 'HIS', 6.21), ('OG1', 'THR', 'CA', 'HIS', 7.14), ('OG1', 'THR', 'N', 'HIS', 7.04)], [('CG2', 'THR', 'CB', 'HIS', 8.85), ('CG2', 'THR', 'CG', 'HIS', 9.05), ('CG2', 'THR', 'ND1', 'HIS', 8.58), ('CG2', 'THR', 'CD2', 'HIS', 9.98), ('CG2', 'THR', 'CE1', 'HIS', 9.28), ('CG2', 'THR', 'NE2', 'HIS', 10.08), ('CG2', 'THR', 'O', 'HIS', 7.23), ('CG2', 'THR', 'C', 'HIS', 6.93), ('CG2', 'THR', 'CA', 'HIS', 8.2), ('CG2', 'THR', 'N', 'HIS', 8.13)], [('O', 'THR', 'CB', 'HIS', 8.1), ('O', 'THR', 'CG', 'HIS', 7.95), ('O', 'THR', 'ND1', 'HIS', 7.78), ('O', 'THR', 'CD2', 'HIS', 8.38), ('O', 'THR', 'CE1', 'HIS', 8.12), ('O', 'THR', 'NE2', 'HIS', 8.46), ('O', 'THR', 'O', 'HIS', 5.19), ('O', 'THR', 'C', 'HIS', 5.7), ('O', 'THR', 'CA', 'HIS', 7.18), ('O', 'THR', 'N', 'HIS', 7.69)], [('C', 'THR', 'CB', 'HIS', 7.4), ('C', 'THR', 'CG', 'HIS', 7.52), ('C', 'THR', 'ND1', 'HIS', 7.47), ('C', 'THR', 'CD2', 'HIS', 8.16), ('C', 'THR', 'CE1', 'HIS', 8.06), ('C', 'THR', 'NE2', 'HIS', 8.45), ('C', 'THR', 'O', 'HIS', 4.86), ('C', 'THR', 'C', 'HIS', 4.97), ('C', 'THR', 'CA', 'HIS', 6.38), ('C', 'THR', 'N', 'HIS', 6.67)], [('CA', 'THR', 'CB', 'HIS', 6.49), ('CA', 'THR', 'CG', 'HIS', 6.65), ('CA', 'THR', 'ND1', 'HIS', 6.42), ('CA', 'THR', 'CD2', 'HIS', 7.54), ('CA', 'THR', 'CE1', 'HIS', 7.19), ('CA', 'THR', 'NE2', 'HIS', 7.81), ('CA', 'THR', 'O', 'HIS', 4.77), ('CA', 'THR', 'C', 'HIS', 4.43), ('CA', 'THR', 'CA', 'HIS', 5.79), ('CA', 'THR', 'N', 'HIS', 6.05)], [('N', 'THR', 'CB', 'HIS', 5.18), ('N', 'THR', 'CG', 'HIS', 5.65), ('N', 'THR', 'ND1', 'HIS', 5.74), ('N', 'THR', 'CD2', 'HIS', 6.66), ('N', 'THR', 'CE1', 'HIS', 6.74), ('N', 'THR', 'NE2', 'HIS', 7.22), ('N', 'THR', 'O', 'HIS', 4.24), ('N', 'THR', 'C', 'HIS', 3.33), ('N', 'THR', 'CA', 'HIS', 4.41), ('N', 'THR', 'N', 'HIS', 4.65)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(THR_HIS, d, 'A_1teh_1_1_1_1')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'THR_HIS' :  match1}