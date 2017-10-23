'''
FUNC:A_1b6t_2_7_7_3
PDB:1b6t
EC:2.7.7.3
RESI:his,arg,ser
LOCI:a-18,91,129;
'''
import motifFunctions as cmd
HIS_ARG = { 
	'distances':
		[[12.72, 11.21, 10.92, 11.71, 11.61, 12.59, 10.71], [12.07, 10.57, 10.14, 10.75, 10.55, 11.44, 9.68], [12.65, 11.16, 10.52, 11.0, 10.8, 11.57, 10.07], [11.13, 9.65, 9.27, 9.77, 9.45, 10.3, 8.5], [12.14, 10.71, 9.97, 10.26, 9.94, 10.58, 9.25], [11.19, 9.76, 9.17, 9.45, 9.03, 9.72, 8.21]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 12.72), ('CB', 'HIS', 'CG', 'ARG', 11.21), ('CB', 'HIS', 'CD', 'ARG', 10.92), ('CB', 'HIS', 'NE', 'ARG', 11.71), ('CB', 'HIS', 'CZ', 'ARG', 11.61), ('CB', 'HIS', 'NH1', 'ARG', 12.59), ('CB', 'HIS', 'NH2', 'ARG', 10.71)], [('CG', 'HIS', 'CB', 'ARG', 12.07), ('CG', 'HIS', 'CG', 'ARG', 10.57), ('CG', 'HIS', 'CD', 'ARG', 10.14), ('CG', 'HIS', 'NE', 'ARG', 10.75), ('CG', 'HIS', 'CZ', 'ARG', 10.55), ('CG', 'HIS', 'NH1', 'ARG', 11.44), ('CG', 'HIS', 'NH2', 'ARG', 9.68)], [('ND1', 'HIS', 'CB', 'ARG', 12.65), ('ND1', 'HIS', 'CG', 'ARG', 11.16), ('ND1', 'HIS', 'CD', 'ARG', 10.52), ('ND1', 'HIS', 'NE', 'ARG', 11.0), ('ND1', 'HIS', 'CZ', 'ARG', 10.8), ('ND1', 'HIS', 'NH1', 'ARG', 11.57), ('ND1', 'HIS', 'NH2', 'ARG', 10.07)], [('CD2', 'HIS', 'CB', 'ARG', 11.13), ('CD2', 'HIS', 'CG', 'ARG', 9.65), ('CD2', 'HIS', 'CD', 'ARG', 9.27), ('CD2', 'HIS', 'NE', 'ARG', 9.77), ('CD2', 'HIS', 'CZ', 'ARG', 9.45), ('CD2', 'HIS', 'NH1', 'ARG', 10.3), ('CD2', 'HIS', 'NH2', 'ARG', 8.5)], [('CE1', 'HIS', 'CB', 'ARG', 12.14), ('CE1', 'HIS', 'CG', 'ARG', 10.71), ('CE1', 'HIS', 'CD', 'ARG', 9.97), ('CE1', 'HIS', 'NE', 'ARG', 10.26), ('CE1', 'HIS', 'CZ', 'ARG', 9.94), ('CE1', 'HIS', 'NH1', 'ARG', 10.58), ('CE1', 'HIS', 'NH2', 'ARG', 9.25)], [('NE2', 'HIS', 'CB', 'ARG', 11.19), ('NE2', 'HIS', 'CG', 'ARG', 9.76), ('NE2', 'HIS', 'CD', 'ARG', 9.17), ('NE2', 'HIS', 'NE', 'ARG', 9.45), ('NE2', 'HIS', 'CZ', 'ARG', 9.03), ('NE2', 'HIS', 'NH1', 'ARG', 9.72), ('NE2', 'HIS', 'NH2', 'ARG', 8.21)]]}
SER_ARG = { 
	'distances':
		[[12.45, 11.35, 10.09, 9.76, 9.48, 9.55, 9.47], [11.82, 10.6, 9.44, 9.31, 9.06, 9.36, 8.86], [14.12, 13.24, 11.79, 11.33, 11.3, 11.16, 11.69], [13.06, 12.19, 10.77, 10.24, 10.14, 9.97, 10.52], [12.05, 11.06, 9.67, 9.31, 9.24, 9.28, 9.48], [10.68, 9.76, 8.34, 7.89, 7.86, 7.91, 8.22]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ARG', 12.45), ('CB', 'SER', 'CG', 'ARG', 11.35), ('CB', 'SER', 'CD', 'ARG', 10.09), ('CB', 'SER', 'NE', 'ARG', 9.76), ('CB', 'SER', 'CZ', 'ARG', 9.48), ('CB', 'SER', 'NH1', 'ARG', 9.55), ('CB', 'SER', 'NH2', 'ARG', 9.47)], [('OG', 'SER', 'CB', 'ARG', 11.82), ('OG', 'SER', 'CG', 'ARG', 10.6), ('OG', 'SER', 'CD', 'ARG', 9.44), ('OG', 'SER', 'NE', 'ARG', 9.31), ('OG', 'SER', 'CZ', 'ARG', 9.06), ('OG', 'SER', 'NH1', 'ARG', 9.36), ('OG', 'SER', 'NH2', 'ARG', 8.86)], [('O', 'SER', 'CB', 'ARG', 14.12), ('O', 'SER', 'CG', 'ARG', 13.24), ('O', 'SER', 'CD', 'ARG', 11.79), ('O', 'SER', 'NE', 'ARG', 11.33), ('O', 'SER', 'CZ', 'ARG', 11.3), ('O', 'SER', 'NH1', 'ARG', 11.16), ('O', 'SER', 'NH2', 'ARG', 11.69)], [('C', 'SER', 'CB', 'ARG', 13.06), ('C', 'SER', 'CG', 'ARG', 12.19), ('C', 'SER', 'CD', 'ARG', 10.77), ('C', 'SER', 'NE', 'ARG', 10.24), ('C', 'SER', 'CZ', 'ARG', 10.14), ('C', 'SER', 'NH1', 'ARG', 9.97), ('C', 'SER', 'NH2', 'ARG', 10.52)], [('CA', 'SER', 'CB', 'ARG', 12.05), ('CA', 'SER', 'CG', 'ARG', 11.06), ('CA', 'SER', 'CD', 'ARG', 9.67), ('CA', 'SER', 'NE', 'ARG', 9.31), ('CA', 'SER', 'CZ', 'ARG', 9.24), ('CA', 'SER', 'NH1', 'ARG', 9.28), ('CA', 'SER', 'NH2', 'ARG', 9.48)], [('N', 'SER', 'CB', 'ARG', 10.68), ('N', 'SER', 'CG', 'ARG', 9.76), ('N', 'SER', 'CD', 'ARG', 8.34), ('N', 'SER', 'NE', 'ARG', 7.89), ('N', 'SER', 'CZ', 'ARG', 7.86), ('N', 'SER', 'NH1', 'ARG', 7.91), ('N', 'SER', 'NH2', 'ARG', 8.22)]]}
SER_HIS = { 
	'distances':
		[[9.94, 8.57, 7.56, 8.26, 6.48, 6.98], [8.55, 7.17, 6.22, 6.88, 5.15, 5.65], [12.73, 11.49, 10.39, 11.34, 9.52, 10.14], [12.18, 10.87, 9.87, 10.58, 8.89, 9.35], [10.72, 9.43, 8.49, 9.14, 7.53, 7.96], [10.76, 9.46, 8.75, 8.97, 7.75, 7.88]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 9.94), ('CB', 'SER', 'CG', 'HIS', 8.57), ('CB', 'SER', 'ND1', 'HIS', 7.56), ('CB', 'SER', 'CD2', 'HIS', 8.26), ('CB', 'SER', 'CE1', 'HIS', 6.48), ('CB', 'SER', 'NE2', 'HIS', 6.98)], [('OG', 'SER', 'CB', 'HIS', 8.55), ('OG', 'SER', 'CG', 'HIS', 7.17), ('OG', 'SER', 'ND1', 'HIS', 6.22), ('OG', 'SER', 'CD2', 'HIS', 6.88), ('OG', 'SER', 'CE1', 'HIS', 5.15), ('OG', 'SER', 'NE2', 'HIS', 5.65)], [('O', 'SER', 'CB', 'HIS', 12.73), ('O', 'SER', 'CG', 'HIS', 11.49), ('O', 'SER', 'ND1', 'HIS', 10.39), ('O', 'SER', 'CD2', 'HIS', 11.34), ('O', 'SER', 'CE1', 'HIS', 9.52), ('O', 'SER', 'NE2', 'HIS', 10.14)], [('C', 'SER', 'CB', 'HIS', 12.18), ('C', 'SER', 'CG', 'HIS', 10.87), ('C', 'SER', 'ND1', 'HIS', 9.87), ('C', 'SER', 'CD2', 'HIS', 10.58), ('C', 'SER', 'CE1', 'HIS', 8.89), ('C', 'SER', 'NE2', 'HIS', 9.35)], [('CA', 'SER', 'CB', 'HIS', 10.72), ('CA', 'SER', 'CG', 'HIS', 9.43), ('CA', 'SER', 'ND1', 'HIS', 8.49), ('CA', 'SER', 'CD2', 'HIS', 9.14), ('CA', 'SER', 'CE1', 'HIS', 7.53), ('CA', 'SER', 'NE2', 'HIS', 7.96)], [('N', 'SER', 'CB', 'HIS', 10.76), ('N', 'SER', 'CG', 'HIS', 9.46), ('N', 'SER', 'ND1', 'HIS', 8.75), ('N', 'SER', 'CD2', 'HIS', 8.97), ('N', 'SER', 'CE1', 'HIS', 7.75), ('N', 'SER', 'NE2', 'HIS', 7.88)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ARG, d, 'A_1b6t_2_7_7_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_ARG, d, 'A_1b6t_2_7_7_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_HIS, d, 'A_1b6t_2_7_7_3')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ARG' :  match1,
		'SER_ARG' :  match2,
		'SER_HIS' :  match3}