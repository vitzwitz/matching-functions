'''
FUNC:A_2f9z_3_1_1_61
PDB:2f9z
EC:3.1.1.61
RESI:thr,cys,his
LOCI:c-21,27,44;
'''
import motifFunctions as cmd
HIS_CYS = { 
	'distances':
		[[6.99, 7.26, 8.58, 8.1, 8.17, 9.4], [5.92, 6.19, 7.74, 7.34, 7.24, 8.34], [6.43, 6.77, 8.08, 7.9, 7.81, 8.72], [4.68, 4.84, 6.93, 6.41, 6.08, 7.13], [5.74, 6.05, 7.56, 7.44, 7.18, 7.88], [4.56, 4.75, 6.81, 6.5, 6.05, 6.81], [6.45, 6.21, 8.55, 7.66, 7.4, 8.72], [6.37, 6.55, 7.96, 7.14, 7.17, 8.57], [6.86, 7.31, 8.09, 7.51, 7.76, 9.13], [8.27, 8.68, 9.32, 8.74, 9.09, 10.48]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYS', 6.99), ('CB', 'HIS', 'SG', 'CYS', 7.26), ('CB', 'HIS', 'O', 'CYS', 8.58), ('CB', 'HIS', 'C', 'CYS', 8.1), ('CB', 'HIS', 'CA', 'CYS', 8.17), ('CB', 'HIS', 'N', 'CYS', 9.4)], [('CG', 'HIS', 'CB', 'CYS', 5.92), ('CG', 'HIS', 'SG', 'CYS', 6.19), ('CG', 'HIS', 'O', 'CYS', 7.74), ('CG', 'HIS', 'C', 'CYS', 7.34), ('CG', 'HIS', 'CA', 'CYS', 7.24), ('CG', 'HIS', 'N', 'CYS', 8.34)], [('ND1', 'HIS', 'CB', 'CYS', 6.43), ('ND1', 'HIS', 'SG', 'CYS', 6.77), ('ND1', 'HIS', 'O', 'CYS', 8.08), ('ND1', 'HIS', 'C', 'CYS', 7.9), ('ND1', 'HIS', 'CA', 'CYS', 7.81), ('ND1', 'HIS', 'N', 'CYS', 8.72)], [('CD2', 'HIS', 'CB', 'CYS', 4.68), ('CD2', 'HIS', 'SG', 'CYS', 4.84), ('CD2', 'HIS', 'O', 'CYS', 6.93), ('CD2', 'HIS', 'C', 'CYS', 6.41), ('CD2', 'HIS', 'CA', 'CYS', 6.08), ('CD2', 'HIS', 'N', 'CYS', 7.13)], [('CE1', 'HIS', 'CB', 'CYS', 5.74), ('CE1', 'HIS', 'SG', 'CYS', 6.05), ('CE1', 'HIS', 'O', 'CYS', 7.56), ('CE1', 'HIS', 'C', 'CYS', 7.44), ('CE1', 'HIS', 'CA', 'CYS', 7.18), ('CE1', 'HIS', 'N', 'CYS', 7.88)], [('NE2', 'HIS', 'CB', 'CYS', 4.56), ('NE2', 'HIS', 'SG', 'CYS', 4.75), ('NE2', 'HIS', 'O', 'CYS', 6.81), ('NE2', 'HIS', 'C', 'CYS', 6.5), ('NE2', 'HIS', 'CA', 'CYS', 6.05), ('NE2', 'HIS', 'N', 'CYS', 6.81)], [('O', 'HIS', 'CB', 'CYS', 6.45), ('O', 'HIS', 'SG', 'CYS', 6.21), ('O', 'HIS', 'O', 'CYS', 8.55), ('O', 'HIS', 'C', 'CYS', 7.66), ('O', 'HIS', 'CA', 'CYS', 7.4), ('O', 'HIS', 'N', 'CYS', 8.72)], [('C', 'HIS', 'CB', 'CYS', 6.37), ('C', 'HIS', 'SG', 'CYS', 6.55), ('C', 'HIS', 'O', 'CYS', 7.96), ('C', 'HIS', 'C', 'CYS', 7.14), ('C', 'HIS', 'CA', 'CYS', 7.17), ('C', 'HIS', 'N', 'CYS', 8.57)], [('CA', 'HIS', 'CB', 'CYS', 6.86), ('CA', 'HIS', 'SG', 'CYS', 7.31), ('CA', 'HIS', 'O', 'CYS', 8.09), ('CA', 'HIS', 'C', 'CYS', 7.51), ('CA', 'HIS', 'CA', 'CYS', 7.76), ('CA', 'HIS', 'N', 'CYS', 9.13)], [('N', 'HIS', 'CB', 'CYS', 8.27), ('N', 'HIS', 'SG', 'CYS', 8.68), ('N', 'HIS', 'O', 'CYS', 9.32), ('N', 'HIS', 'C', 'CYS', 8.74), ('N', 'HIS', 'CA', 'CYS', 9.09), ('N', 'HIS', 'N', 'CYS', 10.48)]]}
THR_CYS = { 
	'distances':
		[[9.76, 10.55, 10.2, 10.44, 10.87, 11.71], [8.74, 9.37, 9.59, 9.74, 9.97, 10.77], [9.34, 10.39, 9.3, 9.63, 10.27, 11.13], [9.62, 10.65, 9.51, 10.1, 10.56, 11.05], [10.34, 11.2, 10.53, 11.03, 11.4, 11.93], [10.8, 11.59, 11.13, 11.5, 11.9, 12.6], [11.96, 12.86, 11.99, 12.43, 12.97, 13.69]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'CYS', 9.76), ('CB', 'THR', 'SG', 'CYS', 10.55), ('CB', 'THR', 'O', 'CYS', 10.2), ('CB', 'THR', 'C', 'CYS', 10.44), ('CB', 'THR', 'CA', 'CYS', 10.87), ('CB', 'THR', 'N', 'CYS', 11.71)], [('OG1', 'THR', 'CB', 'CYS', 8.74), ('OG1', 'THR', 'SG', 'CYS', 9.37), ('OG1', 'THR', 'O', 'CYS', 9.59), ('OG1', 'THR', 'C', 'CYS', 9.74), ('OG1', 'THR', 'CA', 'CYS', 9.97), ('OG1', 'THR', 'N', 'CYS', 10.77)], [('CG2', 'THR', 'CB', 'CYS', 9.34), ('CG2', 'THR', 'SG', 'CYS', 10.39), ('CG2', 'THR', 'O', 'CYS', 9.3), ('CG2', 'THR', 'C', 'CYS', 9.63), ('CG2', 'THR', 'CA', 'CYS', 10.27), ('CG2', 'THR', 'N', 'CYS', 11.13)], [('O', 'THR', 'CB', 'CYS', 9.62), ('O', 'THR', 'SG', 'CYS', 10.65), ('O', 'THR', 'O', 'CYS', 9.51), ('O', 'THR', 'C', 'CYS', 10.1), ('O', 'THR', 'CA', 'CYS', 10.56), ('O', 'THR', 'N', 'CYS', 11.05)], [('C', 'THR', 'CB', 'CYS', 10.34), ('C', 'THR', 'SG', 'CYS', 11.2), ('C', 'THR', 'O', 'CYS', 10.53), ('C', 'THR', 'C', 'CYS', 11.03), ('C', 'THR', 'CA', 'CYS', 11.4), ('C', 'THR', 'N', 'CYS', 11.93)], [('CA', 'THR', 'CB', 'CYS', 10.8), ('CA', 'THR', 'SG', 'CYS', 11.59), ('CA', 'THR', 'O', 'CYS', 11.13), ('CA', 'THR', 'C', 'CYS', 11.5), ('CA', 'THR', 'CA', 'CYS', 11.9), ('CA', 'THR', 'N', 'CYS', 12.6)], [('N', 'THR', 'CB', 'CYS', 11.96), ('N', 'THR', 'SG', 'CYS', 12.86), ('N', 'THR', 'O', 'CYS', 11.99), ('N', 'THR', 'C', 'CYS', 12.43), ('N', 'THR', 'CA', 'CYS', 12.97), ('N', 'THR', 'N', 'CYS', 13.69)]]}
THR_HIS = { 
	'distances':
		[[6.37, 6.26, 5.34, 7.33, 6.09, 7.22, 9.17, 8.71, 7.3, 7.72], [5.58, 5.18, 4.07, 6.19, 4.76, 5.96, 8.28, 7.98, 6.72, 7.38], [6.44, 6.36, 5.67, 7.32, 6.35, 7.3, 9.11, 8.44, 7.01, 7.45], [8.21, 7.56, 6.44, 8.17, 6.48, 7.56, 10.71, 10.23, 9.01, 9.78], [8.33, 7.77, 6.56, 8.52, 6.72, 7.93, 10.96, 10.57, 9.3, 9.97], [7.82, 7.56, 6.47, 8.54, 6.98, 8.21, 10.6, 10.19, 8.81, 9.25], [8.86, 8.76, 7.77, 9.78, 8.34, 9.53, 11.67, 11.16, 9.7, 9.98]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'HIS', 6.37), ('CB', 'THR', 'CG', 'HIS', 6.26), ('CB', 'THR', 'ND1', 'HIS', 5.34), ('CB', 'THR', 'CD2', 'HIS', 7.33), ('CB', 'THR', 'CE1', 'HIS', 6.09), ('CB', 'THR', 'NE2', 'HIS', 7.22), ('CB', 'THR', 'O', 'HIS', 9.17), ('CB', 'THR', 'C', 'HIS', 8.71), ('CB', 'THR', 'CA', 'HIS', 7.3), ('CB', 'THR', 'N', 'HIS', 7.72)], [('OG1', 'THR', 'CB', 'HIS', 5.58), ('OG1', 'THR', 'CG', 'HIS', 5.18), ('OG1', 'THR', 'ND1', 'HIS', 4.07), ('OG1', 'THR', 'CD2', 'HIS', 6.19), ('OG1', 'THR', 'CE1', 'HIS', 4.76), ('OG1', 'THR', 'NE2', 'HIS', 5.96), ('OG1', 'THR', 'O', 'HIS', 8.28), ('OG1', 'THR', 'C', 'HIS', 7.98), ('OG1', 'THR', 'CA', 'HIS', 6.72), ('OG1', 'THR', 'N', 'HIS', 7.38)], [('CG2', 'THR', 'CB', 'HIS', 6.44), ('CG2', 'THR', 'CG', 'HIS', 6.36), ('CG2', 'THR', 'ND1', 'HIS', 5.67), ('CG2', 'THR', 'CD2', 'HIS', 7.32), ('CG2', 'THR', 'CE1', 'HIS', 6.35), ('CG2', 'THR', 'NE2', 'HIS', 7.3), ('CG2', 'THR', 'O', 'HIS', 9.11), ('CG2', 'THR', 'C', 'HIS', 8.44), ('CG2', 'THR', 'CA', 'HIS', 7.01), ('CG2', 'THR', 'N', 'HIS', 7.45)], [('O', 'THR', 'CB', 'HIS', 8.21), ('O', 'THR', 'CG', 'HIS', 7.56), ('O', 'THR', 'ND1', 'HIS', 6.44), ('O', 'THR', 'CD2', 'HIS', 8.17), ('O', 'THR', 'CE1', 'HIS', 6.48), ('O', 'THR', 'NE2', 'HIS', 7.56), ('O', 'THR', 'O', 'HIS', 10.71), ('O', 'THR', 'C', 'HIS', 10.23), ('O', 'THR', 'CA', 'HIS', 9.01), ('O', 'THR', 'N', 'HIS', 9.78)], [('C', 'THR', 'CB', 'HIS', 8.33), ('C', 'THR', 'CG', 'HIS', 7.77), ('C', 'THR', 'ND1', 'HIS', 6.56), ('C', 'THR', 'CD2', 'HIS', 8.52), ('C', 'THR', 'CE1', 'HIS', 6.72), ('C', 'THR', 'NE2', 'HIS', 7.93), ('C', 'THR', 'O', 'HIS', 10.96), ('C', 'THR', 'C', 'HIS', 10.57), ('C', 'THR', 'CA', 'HIS', 9.3), ('C', 'THR', 'N', 'HIS', 9.97)], [('CA', 'THR', 'CB', 'HIS', 7.82), ('CA', 'THR', 'CG', 'HIS', 7.56), ('CA', 'THR', 'ND1', 'HIS', 6.47), ('CA', 'THR', 'CD2', 'HIS', 8.54), ('CA', 'THR', 'CE1', 'HIS', 6.98), ('CA', 'THR', 'NE2', 'HIS', 8.21), ('CA', 'THR', 'O', 'HIS', 10.6), ('CA', 'THR', 'C', 'HIS', 10.19), ('CA', 'THR', 'CA', 'HIS', 8.81), ('CA', 'THR', 'N', 'HIS', 9.25)], [('N', 'THR', 'CB', 'HIS', 8.86), ('N', 'THR', 'CG', 'HIS', 8.76), ('N', 'THR', 'ND1', 'HIS', 7.77), ('N', 'THR', 'CD2', 'HIS', 9.78), ('N', 'THR', 'CE1', 'HIS', 8.34), ('N', 'THR', 'NE2', 'HIS', 9.53), ('N', 'THR', 'O', 'HIS', 11.67), ('N', 'THR', 'C', 'HIS', 11.16), ('N', 'THR', 'CA', 'HIS', 9.7), ('N', 'THR', 'N', 'HIS', 9.98)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_CYS, d, 'A_2f9z_3_1_1_61')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(THR_CYS, d, 'A_2f9z_3_1_1_61')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(THR_HIS, d, 'A_2f9z_3_1_1_61')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_CYS' :  match1,
		'THR_CYS' :  match2,
		'THR_HIS' :  match3}