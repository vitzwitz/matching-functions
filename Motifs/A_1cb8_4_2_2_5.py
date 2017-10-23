'''
FUNC:A_1cb8_4_2_2_5
PDB:1cb8
EC:4.2.2.5
RESI:his,tyr,arg
LOCI:a-225,234,288;
'''
import motifFunctions as cmd
TYR_HIS = { 
	'distances':
		[[9.48, 8.94, 9.1, 8.62, 8.9, 8.61], [8.65, 7.89, 7.88, 7.54, 7.55, 7.31], [9.2, 8.21, 8.12, 7.61, 7.49, 7.13], [7.67, 6.96, 6.81, 6.88, 6.65, 6.68], [8.91, 7.71, 7.42, 7.07, 6.58, 6.3], [7.29, 6.32, 5.87, 6.25, 5.52, 5.76], [7.98, 6.76, 6.25, 6.36, 5.47, 5.52], [8.09, 6.73, 5.95, 6.35, 4.91, 5.2]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'HIS', 9.48), ('CB', 'TYR', 'CG', 'HIS', 8.94), ('CB', 'TYR', 'ND1', 'HIS', 9.1), ('CB', 'TYR', 'CD2', 'HIS', 8.62), ('CB', 'TYR', 'CE1', 'HIS', 8.9), ('CB', 'TYR', 'NE2', 'HIS', 8.61)], [('CG', 'TYR', 'CB', 'HIS', 8.65), ('CG', 'TYR', 'CG', 'HIS', 7.89), ('CG', 'TYR', 'ND1', 'HIS', 7.88), ('CG', 'TYR', 'CD2', 'HIS', 7.54), ('CG', 'TYR', 'CE1', 'HIS', 7.55), ('CG', 'TYR', 'NE2', 'HIS', 7.31)], [('CD1', 'TYR', 'CB', 'HIS', 9.2), ('CD1', 'TYR', 'CG', 'HIS', 8.21), ('CD1', 'TYR', 'ND1', 'HIS', 8.12), ('CD1', 'TYR', 'CD2', 'HIS', 7.61), ('CD1', 'TYR', 'CE1', 'HIS', 7.49), ('CD1', 'TYR', 'NE2', 'HIS', 7.13)], [('CD2', 'TYR', 'CB', 'HIS', 7.67), ('CD2', 'TYR', 'CG', 'HIS', 6.96), ('CD2', 'TYR', 'ND1', 'HIS', 6.81), ('CD2', 'TYR', 'CD2', 'HIS', 6.88), ('CD2', 'TYR', 'CE1', 'HIS', 6.65), ('CD2', 'TYR', 'NE2', 'HIS', 6.68)], [('CE1', 'TYR', 'CB', 'HIS', 8.91), ('CE1', 'TYR', 'CG', 'HIS', 7.71), ('CE1', 'TYR', 'ND1', 'HIS', 7.42), ('CE1', 'TYR', 'CD2', 'HIS', 7.07), ('CE1', 'TYR', 'CE1', 'HIS', 6.58), ('CE1', 'TYR', 'NE2', 'HIS', 6.3)], [('CE2', 'TYR', 'CB', 'HIS', 7.29), ('CE2', 'TYR', 'CG', 'HIS', 6.32), ('CE2', 'TYR', 'ND1', 'HIS', 5.87), ('CE2', 'TYR', 'CD2', 'HIS', 6.25), ('CE2', 'TYR', 'CE1', 'HIS', 5.52), ('CE2', 'TYR', 'NE2', 'HIS', 5.76)], [('CZ', 'TYR', 'CB', 'HIS', 7.98), ('CZ', 'TYR', 'CG', 'HIS', 6.76), ('CZ', 'TYR', 'ND1', 'HIS', 6.25), ('CZ', 'TYR', 'CD2', 'HIS', 6.36), ('CZ', 'TYR', 'CE1', 'HIS', 5.47), ('CZ', 'TYR', 'NE2', 'HIS', 5.52)], [('OH', 'TYR', 'CB', 'HIS', 8.09), ('OH', 'TYR', 'CG', 'HIS', 6.73), ('OH', 'TYR', 'ND1', 'HIS', 5.95), ('OH', 'TYR', 'CD2', 'HIS', 6.35), ('OH', 'TYR', 'CE1', 'HIS', 4.91), ('OH', 'TYR', 'NE2', 'HIS', 5.2)]]}
HIS_ARG = { 
	'distances':
		[[10.92, 10.7, 10.24, 10.55, 9.84, 8.61, 10.57], [10.49, 10.03, 9.47, 9.55, 8.71, 7.51, 9.3], [9.27, 8.74, 8.12, 8.19, 7.4, 6.22, 8.07], [11.33, 10.68, 10.08, 9.93, 8.92, 7.8, 9.28], [9.49, 8.71, 7.99, 7.76, 6.77, 5.7, 7.2], [10.75, 9.93, 9.25, 8.9, 7.81, 6.79, 8.03]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 10.92), ('CB', 'HIS', 'CG', 'ARG', 10.7), ('CB', 'HIS', 'CD', 'ARG', 10.24), ('CB', 'HIS', 'NE', 'ARG', 10.55), ('CB', 'HIS', 'CZ', 'ARG', 9.84), ('CB', 'HIS', 'NH1', 'ARG', 8.61), ('CB', 'HIS', 'NH2', 'ARG', 10.57)], [('CG', 'HIS', 'CB', 'ARG', 10.49), ('CG', 'HIS', 'CG', 'ARG', 10.03), ('CG', 'HIS', 'CD', 'ARG', 9.47), ('CG', 'HIS', 'NE', 'ARG', 9.55), ('CG', 'HIS', 'CZ', 'ARG', 8.71), ('CG', 'HIS', 'NH1', 'ARG', 7.51), ('CG', 'HIS', 'NH2', 'ARG', 9.3)], [('ND1', 'HIS', 'CB', 'ARG', 9.27), ('ND1', 'HIS', 'CG', 'ARG', 8.74), ('ND1', 'HIS', 'CD', 'ARG', 8.12), ('ND1', 'HIS', 'NE', 'ARG', 8.19), ('ND1', 'HIS', 'CZ', 'ARG', 7.4), ('ND1', 'HIS', 'NH1', 'ARG', 6.22), ('ND1', 'HIS', 'NH2', 'ARG', 8.07)], [('CD2', 'HIS', 'CB', 'ARG', 11.33), ('CD2', 'HIS', 'CG', 'ARG', 10.68), ('CD2', 'HIS', 'CD', 'ARG', 10.08), ('CD2', 'HIS', 'NE', 'ARG', 9.93), ('CD2', 'HIS', 'CZ', 'ARG', 8.92), ('CD2', 'HIS', 'NH1', 'ARG', 7.8), ('CD2', 'HIS', 'NH2', 'ARG', 9.28)], [('CE1', 'HIS', 'CB', 'ARG', 9.49), ('CE1', 'HIS', 'CG', 'ARG', 8.71), ('CE1', 'HIS', 'CD', 'ARG', 7.99), ('CE1', 'HIS', 'NE', 'ARG', 7.76), ('CE1', 'HIS', 'CZ', 'ARG', 6.77), ('CE1', 'HIS', 'NH1', 'ARG', 5.7), ('CE1', 'HIS', 'NH2', 'ARG', 7.2)], [('NE2', 'HIS', 'CB', 'ARG', 10.75), ('NE2', 'HIS', 'CG', 'ARG', 9.93), ('NE2', 'HIS', 'CD', 'ARG', 9.25), ('NE2', 'HIS', 'NE', 'ARG', 8.9), ('NE2', 'HIS', 'CZ', 'ARG', 7.81), ('NE2', 'HIS', 'NH1', 'ARG', 6.79), ('NE2', 'HIS', 'NH2', 'ARG', 8.03)]]}
TYR_ARG = { 
	'distances':
		[[12.22, 11.51, 11.9, 11.66, 10.63, 9.62, 10.77], [11.21, 10.39, 10.63, 10.31, 9.23, 8.22, 9.34], [11.62, 10.62, 10.72, 10.17, 8.98, 8.13, 8.86], [10.02, 9.29, 9.53, 9.37, 8.37, 7.24, 8.7], [10.97, 9.85, 9.78, 9.1, 7.85, 7.07, 7.63], [9.2, 8.35, 8.39, 8.14, 7.08, 5.94, 7.43], [9.75, 8.68, 8.55, 7.99, 6.77, 5.83, 6.78], [9.32, 8.14, 7.74, 7.02, 5.74, 4.94, 5.65]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ARG', 12.22), ('CB', 'TYR', 'CG', 'ARG', 11.51), ('CB', 'TYR', 'CD', 'ARG', 11.9), ('CB', 'TYR', 'NE', 'ARG', 11.66), ('CB', 'TYR', 'CZ', 'ARG', 10.63), ('CB', 'TYR', 'NH1', 'ARG', 9.62), ('CB', 'TYR', 'NH2', 'ARG', 10.77)], [('CG', 'TYR', 'CB', 'ARG', 11.21), ('CG', 'TYR', 'CG', 'ARG', 10.39), ('CG', 'TYR', 'CD', 'ARG', 10.63), ('CG', 'TYR', 'NE', 'ARG', 10.31), ('CG', 'TYR', 'CZ', 'ARG', 9.23), ('CG', 'TYR', 'NH1', 'ARG', 8.22), ('CG', 'TYR', 'NH2', 'ARG', 9.34)], [('CD1', 'TYR', 'CB', 'ARG', 11.62), ('CD1', 'TYR', 'CG', 'ARG', 10.62), ('CD1', 'TYR', 'CD', 'ARG', 10.72), ('CD1', 'TYR', 'NE', 'ARG', 10.17), ('CD1', 'TYR', 'CZ', 'ARG', 8.98), ('CD1', 'TYR', 'NH1', 'ARG', 8.13), ('CD1', 'TYR', 'NH2', 'ARG', 8.86)], [('CD2', 'TYR', 'CB', 'ARG', 10.02), ('CD2', 'TYR', 'CG', 'ARG', 9.29), ('CD2', 'TYR', 'CD', 'ARG', 9.53), ('CD2', 'TYR', 'NE', 'ARG', 9.37), ('CD2', 'TYR', 'CZ', 'ARG', 8.37), ('CD2', 'TYR', 'NH1', 'ARG', 7.24), ('CD2', 'TYR', 'NH2', 'ARG', 8.7)], [('CE1', 'TYR', 'CB', 'ARG', 10.97), ('CE1', 'TYR', 'CG', 'ARG', 9.85), ('CE1', 'TYR', 'CD', 'ARG', 9.78), ('CE1', 'TYR', 'NE', 'ARG', 9.1), ('CE1', 'TYR', 'CZ', 'ARG', 7.85), ('CE1', 'TYR', 'NH1', 'ARG', 7.07), ('CE1', 'TYR', 'NH2', 'ARG', 7.63)], [('CE2', 'TYR', 'CB', 'ARG', 9.2), ('CE2', 'TYR', 'CG', 'ARG', 8.35), ('CE2', 'TYR', 'CD', 'ARG', 8.39), ('CE2', 'TYR', 'NE', 'ARG', 8.14), ('CE2', 'TYR', 'CZ', 'ARG', 7.08), ('CE2', 'TYR', 'NH1', 'ARG', 5.94), ('CE2', 'TYR', 'NH2', 'ARG', 7.43)], [('CZ', 'TYR', 'CB', 'ARG', 9.75), ('CZ', 'TYR', 'CG', 'ARG', 8.68), ('CZ', 'TYR', 'CD', 'ARG', 8.55), ('CZ', 'TYR', 'NE', 'ARG', 7.99), ('CZ', 'TYR', 'CZ', 'ARG', 6.77), ('CZ', 'TYR', 'NH1', 'ARG', 5.83), ('CZ', 'TYR', 'NH2', 'ARG', 6.78)], [('OH', 'TYR', 'CB', 'ARG', 9.32), ('OH', 'TYR', 'CG', 'ARG', 8.14), ('OH', 'TYR', 'CD', 'ARG', 7.74), ('OH', 'TYR', 'NE', 'ARG', 7.02), ('OH', 'TYR', 'CZ', 'ARG', 5.74), ('OH', 'TYR', 'NH1', 'ARG', 4.94), ('OH', 'TYR', 'NH2', 'ARG', 5.65)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TYR_HIS, d, 'A_1cb8_4_2_2_5')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ARG, d, 'A_1cb8_4_2_2_5')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_ARG, d, 'A_1cb8_4_2_2_5')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TYR_HIS' :  match1,
		'HIS_ARG' :  match2,
		'TYR_ARG' :  match3}