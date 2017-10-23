'''
FUNC:A_1a65_1_10_3_2
PDB:1a65
EC:1.10.3.2
RESI:his,cys,his
LOCI:a-451,452,453;
'''
import motifFunctions as cmd
HIS_CYS = { 
	'distances':
		[[7.27, 8.86, 6.02, 6.41, 6.29, 5.02], [7.81, 9.15, 5.79, 6.3, 6.65, 5.68], [7.42, 8.5, 4.84, 5.51, 6.28, 5.72], [9.1, 10.36, 6.95, 7.4, 7.84, 6.92], [8.53, 9.41, 5.73, 6.36, 7.33, 6.91], [9.44, 10.47, 6.88, 7.4, 8.16, 7.52], [7.77, 7.4, 6.04, 5.58, 6.78, 7.61], [9.03, 8.77, 6.84, 6.67, 7.99, 8.63], [9.76, 9.36, 7.41, 7.46, 8.89, 9.57], [9.9, 9.84, 7.6, 7.47, 8.68, 9.11], [10.91, 10.64, 8.37, 8.52, 9.94, 10.48], [11.0, 10.9, 8.49, 8.54, 9.85, 10.24], [8.19, 7.48, 6.3, 6.4, 7.81, 8.78], [7.0, 6.31, 5.38, 5.29, 6.63, 7.69], [6.6, 6.32, 4.7, 4.4, 5.79, 6.69], [5.33, 5.23, 4.25, 3.34, 4.44, 5.51]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYS', 7.27), ('CB', 'HIS', 'SG', 'CYS', 8.86), ('CB', 'HIS', 'O', 'CYS', 6.02), ('CB', 'HIS', 'C', 'CYS', 6.41), ('CB', 'HIS', 'CA', 'CYS', 6.29), ('CB', 'HIS', 'N', 'CYS', 5.02)], [('CG', 'HIS', 'CB', 'CYS', 7.81), ('CG', 'HIS', 'SG', 'CYS', 9.15), ('CG', 'HIS', 'O', 'CYS', 5.79), ('CG', 'HIS', 'C', 'CYS', 6.3), ('CG', 'HIS', 'CA', 'CYS', 6.65), ('CG', 'HIS', 'N', 'CYS', 5.68)], [('ND1', 'HIS', 'CB', 'CYS', 7.42), ('ND1', 'HIS', 'SG', 'CYS', 8.5), ('ND1', 'HIS', 'O', 'CYS', 4.84), ('ND1', 'HIS', 'C', 'CYS', 5.51), ('ND1', 'HIS', 'CA', 'CYS', 6.28), ('ND1', 'HIS', 'N', 'CYS', 5.72)], [('CD2', 'HIS', 'CB', 'CYS', 9.1), ('CD2', 'HIS', 'SG', 'CYS', 10.36), ('CD2', 'HIS', 'O', 'CYS', 6.95), ('CD2', 'HIS', 'C', 'CYS', 7.4), ('CD2', 'HIS', 'CA', 'CYS', 7.84), ('CD2', 'HIS', 'N', 'CYS', 6.92)], [('CE1', 'HIS', 'CB', 'CYS', 8.53), ('CE1', 'HIS', 'SG', 'CYS', 9.41), ('CE1', 'HIS', 'O', 'CYS', 5.73), ('CE1', 'HIS', 'C', 'CYS', 6.36), ('CE1', 'HIS', 'CA', 'CYS', 7.33), ('CE1', 'HIS', 'N', 'CYS', 6.91)], [('NE2', 'HIS', 'CB', 'CYS', 9.44), ('NE2', 'HIS', 'SG', 'CYS', 10.47), ('NE2', 'HIS', 'O', 'CYS', 6.88), ('NE2', 'HIS', 'C', 'CYS', 7.4), ('NE2', 'HIS', 'CA', 'CYS', 8.16), ('NE2', 'HIS', 'N', 'CYS', 7.52)], [('CB', 'HIS', 'CB', 'CYS', 7.77), ('CB', 'HIS', 'SG', 'CYS', 7.4), ('CB', 'HIS', 'O', 'CYS', 6.04), ('CB', 'HIS', 'C', 'CYS', 5.58), ('CB', 'HIS', 'CA', 'CYS', 6.78), ('CB', 'HIS', 'N', 'CYS', 7.61)], [('CG', 'HIS', 'CB', 'CYS', 9.03), ('CG', 'HIS', 'SG', 'CYS', 8.77), ('CG', 'HIS', 'O', 'CYS', 6.84), ('CG', 'HIS', 'C', 'CYS', 6.67), ('CG', 'HIS', 'CA', 'CYS', 7.99), ('CG', 'HIS', 'N', 'CYS', 8.63)], [('ND1', 'HIS', 'CB', 'CYS', 9.76), ('ND1', 'HIS', 'SG', 'CYS', 9.36), ('ND1', 'HIS', 'O', 'CYS', 7.41), ('ND1', 'HIS', 'C', 'CYS', 7.46), ('ND1', 'HIS', 'CA', 'CYS', 8.89), ('ND1', 'HIS', 'N', 'CYS', 9.57)], [('CD2', 'HIS', 'CB', 'CYS', 9.9), ('CD2', 'HIS', 'SG', 'CYS', 9.84), ('CD2', 'HIS', 'O', 'CYS', 7.6), ('CD2', 'HIS', 'C', 'CYS', 7.47), ('CD2', 'HIS', 'CA', 'CYS', 8.68), ('CD2', 'HIS', 'N', 'CYS', 9.11)], [('CE1', 'HIS', 'CB', 'CYS', 10.91), ('CE1', 'HIS', 'SG', 'CYS', 10.64), ('CE1', 'HIS', 'O', 'CYS', 8.37), ('CE1', 'HIS', 'C', 'CYS', 8.52), ('CE1', 'HIS', 'CA', 'CYS', 9.94), ('CE1', 'HIS', 'N', 'CYS', 10.48)], [('NE2', 'HIS', 'CB', 'CYS', 11.0), ('NE2', 'HIS', 'SG', 'CYS', 10.9), ('NE2', 'HIS', 'O', 'CYS', 8.49), ('NE2', 'HIS', 'C', 'CYS', 8.54), ('NE2', 'HIS', 'CA', 'CYS', 9.85), ('NE2', 'HIS', 'N', 'CYS', 10.24)], [('O', 'HIS', 'CB', 'CYS', 8.19), ('O', 'HIS', 'SG', 'CYS', 7.48), ('O', 'HIS', 'O', 'CYS', 6.3), ('O', 'HIS', 'C', 'CYS', 6.4), ('O', 'HIS', 'CA', 'CYS', 7.81), ('O', 'HIS', 'N', 'CYS', 8.78)], [('C', 'HIS', 'CB', 'CYS', 7.0), ('C', 'HIS', 'SG', 'CYS', 6.31), ('C', 'HIS', 'O', 'CYS', 5.38), ('C', 'HIS', 'C', 'CYS', 5.29), ('C', 'HIS', 'CA', 'CYS', 6.63), ('C', 'HIS', 'N', 'CYS', 7.69)], [('CA', 'HIS', 'CB', 'CYS', 6.6), ('CA', 'HIS', 'SG', 'CYS', 6.32), ('CA', 'HIS', 'O', 'CYS', 4.7), ('CA', 'HIS', 'C', 'CYS', 4.4), ('CA', 'HIS', 'CA', 'CYS', 5.79), ('CA', 'HIS', 'N', 'CYS', 6.69)], [('N', 'HIS', 'CB', 'CYS', 5.33), ('N', 'HIS', 'SG', 'CYS', 5.23), ('N', 'HIS', 'O', 'CYS', 4.25), ('N', 'HIS', 'C', 'CYS', 3.34), ('N', 'HIS', 'CA', 'CYS', 4.44), ('N', 'HIS', 'N', 'CYS', 5.51)]]}
HIS_HIS = { 
	'distances':
		[[8.86, 9.33, 10.17, 9.38, 10.68, 10.26, 10.0, 9.21, 8.1, 7.48], [8.05, 8.27, 9.06, 8.19, 9.43, 8.95, 9.23, 8.6, 7.44, 7.15], [6.98, 7.14, 7.81, 7.22, 8.24, 7.92, 7.9, 7.35, 6.27, 6.23], [8.51, 8.47, 9.24, 8.1, 9.37, 8.72, 9.87, 9.39, 8.16, 8.06], [6.85, 6.63, 7.2, 6.46, 7.38, 6.97, 7.82, 7.52, 6.44, 6.77], [7.82, 7.52, 8.17, 7.06, 8.16, 7.51, 9.08, 8.78, 7.61, 7.83], [8.86, 8.05, 6.98, 8.51, 6.85, 7.82], [9.33, 8.27, 7.14, 8.47, 6.63, 7.52], [10.17, 9.06, 7.81, 9.24, 7.2, 8.17], [9.38, 8.19, 7.22, 8.1, 6.46, 7.06], [10.68, 9.43, 8.24, 9.37, 7.38, 8.16], [10.26, 8.95, 7.92, 8.72, 6.97, 7.51], [10.0, 9.23, 7.9, 9.87, 7.82, 9.08], [9.21, 8.6, 7.35, 9.39, 7.52, 8.78], [8.1, 7.44, 6.27, 8.16, 6.44, 7.61], [7.48, 7.15, 6.23, 8.06, 6.77, 7.83]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 8.86), ('CB', 'HIS', 'CG', 'HIS', 9.33), ('CB', 'HIS', 'ND1', 'HIS', 10.17), ('CB', 'HIS', 'CD2', 'HIS', 9.38), ('CB', 'HIS', 'CE1', 'HIS', 10.68), ('CB', 'HIS', 'NE2', 'HIS', 10.26), ('CB', 'HIS', 'O', 'HIS', 10.0), ('CB', 'HIS', 'C', 'HIS', 9.21), ('CB', 'HIS', 'CA', 'HIS', 8.1), ('CB', 'HIS', 'N', 'HIS', 7.48)], [('CG', 'HIS', 'CB', 'HIS', 8.05), ('CG', 'HIS', 'CG', 'HIS', 8.27), ('CG', 'HIS', 'ND1', 'HIS', 9.06), ('CG', 'HIS', 'CD2', 'HIS', 8.19), ('CG', 'HIS', 'CE1', 'HIS', 9.43), ('CG', 'HIS', 'NE2', 'HIS', 8.95), ('CG', 'HIS', 'O', 'HIS', 9.23), ('CG', 'HIS', 'C', 'HIS', 8.6), ('CG', 'HIS', 'CA', 'HIS', 7.44), ('CG', 'HIS', 'N', 'HIS', 7.15)], [('ND1', 'HIS', 'CB', 'HIS', 6.98), ('ND1', 'HIS', 'CG', 'HIS', 7.14), ('ND1', 'HIS', 'ND1', 'HIS', 7.81), ('ND1', 'HIS', 'CD2', 'HIS', 7.22), ('ND1', 'HIS', 'CE1', 'HIS', 8.24), ('ND1', 'HIS', 'NE2', 'HIS', 7.92), ('ND1', 'HIS', 'O', 'HIS', 7.9), ('ND1', 'HIS', 'C', 'HIS', 7.35), ('ND1', 'HIS', 'CA', 'HIS', 6.27), ('ND1', 'HIS', 'N', 'HIS', 6.23)], [('CD2', 'HIS', 'CB', 'HIS', 8.51), ('CD2', 'HIS', 'CG', 'HIS', 8.47), ('CD2', 'HIS', 'ND1', 'HIS', 9.24), ('CD2', 'HIS', 'CD2', 'HIS', 8.1), ('CD2', 'HIS', 'CE1', 'HIS', 9.37), ('CD2', 'HIS', 'NE2', 'HIS', 8.72), ('CD2', 'HIS', 'O', 'HIS', 9.87), ('CD2', 'HIS', 'C', 'HIS', 9.39), ('CD2', 'HIS', 'CA', 'HIS', 8.16), ('CD2', 'HIS', 'N', 'HIS', 8.06)], [('CE1', 'HIS', 'CB', 'HIS', 6.85), ('CE1', 'HIS', 'CG', 'HIS', 6.63), ('CE1', 'HIS', 'ND1', 'HIS', 7.2), ('CE1', 'HIS', 'CD2', 'HIS', 6.46), ('CE1', 'HIS', 'CE1', 'HIS', 7.38), ('CE1', 'HIS', 'NE2', 'HIS', 6.97), ('CE1', 'HIS', 'O', 'HIS', 7.82), ('CE1', 'HIS', 'C', 'HIS', 7.52), ('CE1', 'HIS', 'CA', 'HIS', 6.44), ('CE1', 'HIS', 'N', 'HIS', 6.77)], [('NE2', 'HIS', 'CB', 'HIS', 7.82), ('NE2', 'HIS', 'CG', 'HIS', 7.52), ('NE2', 'HIS', 'ND1', 'HIS', 8.17), ('NE2', 'HIS', 'CD2', 'HIS', 7.06), ('NE2', 'HIS', 'CE1', 'HIS', 8.16), ('NE2', 'HIS', 'NE2', 'HIS', 7.51), ('NE2', 'HIS', 'O', 'HIS', 9.08), ('NE2', 'HIS', 'C', 'HIS', 8.78), ('NE2', 'HIS', 'CA', 'HIS', 7.61), ('NE2', 'HIS', 'N', 'HIS', 7.83)], [('CB', 'HIS', 'CB', 'HIS', 8.86), ('CB', 'HIS', 'CG', 'HIS', 8.05), ('CB', 'HIS', 'ND1', 'HIS', 6.98), ('CB', 'HIS', 'CD2', 'HIS', 8.51), ('CB', 'HIS', 'CE1', 'HIS', 6.85), ('CB', 'HIS', 'NE2', 'HIS', 7.82)], [('CG', 'HIS', 'CB', 'HIS', 9.33), ('CG', 'HIS', 'CG', 'HIS', 8.27), ('CG', 'HIS', 'ND1', 'HIS', 7.14), ('CG', 'HIS', 'CD2', 'HIS', 8.47), ('CG', 'HIS', 'CE1', 'HIS', 6.63), ('CG', 'HIS', 'NE2', 'HIS', 7.52)], [('ND1', 'HIS', 'CB', 'HIS', 10.17), ('ND1', 'HIS', 'CG', 'HIS', 9.06), ('ND1', 'HIS', 'ND1', 'HIS', 7.81), ('ND1', 'HIS', 'CD2', 'HIS', 9.24), ('ND1', 'HIS', 'CE1', 'HIS', 7.2), ('ND1', 'HIS', 'NE2', 'HIS', 8.17)], [('CD2', 'HIS', 'CB', 'HIS', 9.38), ('CD2', 'HIS', 'CG', 'HIS', 8.19), ('CD2', 'HIS', 'ND1', 'HIS', 7.22), ('CD2', 'HIS', 'CD2', 'HIS', 8.1), ('CD2', 'HIS', 'CE1', 'HIS', 6.46), ('CD2', 'HIS', 'NE2', 'HIS', 7.06)], [('CE1', 'HIS', 'CB', 'HIS', 10.68), ('CE1', 'HIS', 'CG', 'HIS', 9.43), ('CE1', 'HIS', 'ND1', 'HIS', 8.24), ('CE1', 'HIS', 'CD2', 'HIS', 9.37), ('CE1', 'HIS', 'CE1', 'HIS', 7.38), ('CE1', 'HIS', 'NE2', 'HIS', 8.16)], [('NE2', 'HIS', 'CB', 'HIS', 10.26), ('NE2', 'HIS', 'CG', 'HIS', 8.95), ('NE2', 'HIS', 'ND1', 'HIS', 7.92), ('NE2', 'HIS', 'CD2', 'HIS', 8.72), ('NE2', 'HIS', 'CE1', 'HIS', 6.97), ('NE2', 'HIS', 'NE2', 'HIS', 7.51)], [('O', 'HIS', 'CB', 'HIS', 10.0), ('O', 'HIS', 'CG', 'HIS', 9.23), ('O', 'HIS', 'ND1', 'HIS', 7.9), ('O', 'HIS', 'CD2', 'HIS', 9.87), ('O', 'HIS', 'CE1', 'HIS', 7.82), ('O', 'HIS', 'NE2', 'HIS', 9.08)], [('C', 'HIS', 'CB', 'HIS', 9.21), ('C', 'HIS', 'CG', 'HIS', 8.6), ('C', 'HIS', 'ND1', 'HIS', 7.35), ('C', 'HIS', 'CD2', 'HIS', 9.39), ('C', 'HIS', 'CE1', 'HIS', 7.52), ('C', 'HIS', 'NE2', 'HIS', 8.78)], [('CA', 'HIS', 'CB', 'HIS', 8.1), ('CA', 'HIS', 'CG', 'HIS', 7.44), ('CA', 'HIS', 'ND1', 'HIS', 6.27), ('CA', 'HIS', 'CD2', 'HIS', 8.16), ('CA', 'HIS', 'CE1', 'HIS', 6.44), ('CA', 'HIS', 'NE2', 'HIS', 7.61)], [('N', 'HIS', 'CB', 'HIS', 7.48), ('N', 'HIS', 'CG', 'HIS', 7.15), ('N', 'HIS', 'ND1', 'HIS', 6.23), ('N', 'HIS', 'CD2', 'HIS', 8.06), ('N', 'HIS', 'CE1', 'HIS', 6.77), ('N', 'HIS', 'NE2', 'HIS', 7.83)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_CYS, d, 'A_1a65_1_10_3_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_HIS, d, 'A_1a65_1_10_3_2')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_CYS' :  match1,
		'HIS_HIS' :  match2}