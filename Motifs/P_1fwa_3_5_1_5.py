'''
FUNC:P_1fwa_3_5_1_5
PDB:1fwa
EC:3.5.1.5
RESI:his,asp,his,arg
LOCI:c-219,221,320,336;
'''
import motifFunctions as cmd
HIS_ARG = { 
	'distances':
		[[16.3, 15.18, 14.14, 13.57, 12.49, 11.84, 12.28], [15.12, 14.06, 12.96, 12.31, 11.18, 10.56, 10.91], [14.27, 13.17, 12.01, 11.44, 10.29, 9.54, 10.14], [14.8, 13.85, 12.76, 11.94, 10.79, 10.33, 10.34], [13.4, 12.4, 11.19, 10.5, 9.29, 8.61, 9.02], [13.73, 12.83, 11.67, 10.82, 9.61, 9.14, 9.13], [11.49, 10.93, 9.42, 8.97, 7.89, 7.04, 7.88], [10.77, 10.21, 8.72, 8.04, 6.84, 6.13, 6.63], [11.35, 10.69, 9.23, 8.46, 7.16, 6.46, 6.83], [9.74, 9.33, 7.89, 7.04, 5.86, 5.46, 5.48], [10.81, 10.2, 8.82, 7.86, 6.53, 6.1, 5.95], [9.8, 9.34, 7.97, 6.92, 5.64, 5.45, 4.95]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 16.3), ('CB', 'HIS', 'CG', 'ARG', 15.18), ('CB', 'HIS', 'CD', 'ARG', 14.14), ('CB', 'HIS', 'NE', 'ARG', 13.57), ('CB', 'HIS', 'CZ', 'ARG', 12.49), ('CB', 'HIS', 'NH1', 'ARG', 11.84), ('CB', 'HIS', 'NH2', 'ARG', 12.28)], [('CG', 'HIS', 'CB', 'ARG', 15.12), ('CG', 'HIS', 'CG', 'ARG', 14.06), ('CG', 'HIS', 'CD', 'ARG', 12.96), ('CG', 'HIS', 'NE', 'ARG', 12.31), ('CG', 'HIS', 'CZ', 'ARG', 11.18), ('CG', 'HIS', 'NH1', 'ARG', 10.56), ('CG', 'HIS', 'NH2', 'ARG', 10.91)], [('ND1', 'HIS', 'CB', 'ARG', 14.27), ('ND1', 'HIS', 'CG', 'ARG', 13.17), ('ND1', 'HIS', 'CD', 'ARG', 12.01), ('ND1', 'HIS', 'NE', 'ARG', 11.44), ('ND1', 'HIS', 'CZ', 'ARG', 10.29), ('ND1', 'HIS', 'NH1', 'ARG', 9.54), ('ND1', 'HIS', 'NH2', 'ARG', 10.14)], [('CD2', 'HIS', 'CB', 'ARG', 14.8), ('CD2', 'HIS', 'CG', 'ARG', 13.85), ('CD2', 'HIS', 'CD', 'ARG', 12.76), ('CD2', 'HIS', 'NE', 'ARG', 11.94), ('CD2', 'HIS', 'CZ', 'ARG', 10.79), ('CD2', 'HIS', 'NH1', 'ARG', 10.33), ('CD2', 'HIS', 'NH2', 'ARG', 10.34)], [('CE1', 'HIS', 'CB', 'ARG', 13.4), ('CE1', 'HIS', 'CG', 'ARG', 12.4), ('CE1', 'HIS', 'CD', 'ARG', 11.19), ('CE1', 'HIS', 'NE', 'ARG', 10.5), ('CE1', 'HIS', 'CZ', 'ARG', 9.29), ('CE1', 'HIS', 'NH1', 'ARG', 8.61), ('CE1', 'HIS', 'NH2', 'ARG', 9.02)], [('NE2', 'HIS', 'CB', 'ARG', 13.73), ('NE2', 'HIS', 'CG', 'ARG', 12.83), ('NE2', 'HIS', 'CD', 'ARG', 11.67), ('NE2', 'HIS', 'NE', 'ARG', 10.82), ('NE2', 'HIS', 'CZ', 'ARG', 9.61), ('NE2', 'HIS', 'NH1', 'ARG', 9.14), ('NE2', 'HIS', 'NH2', 'ARG', 9.13)], [('CB', 'HIS', 'CB', 'ARG', 11.49), ('CB', 'HIS', 'CG', 'ARG', 10.93), ('CB', 'HIS', 'CD', 'ARG', 9.42), ('CB', 'HIS', 'NE', 'ARG', 8.97), ('CB', 'HIS', 'CZ', 'ARG', 7.89), ('CB', 'HIS', 'NH1', 'ARG', 7.04), ('CB', 'HIS', 'NH2', 'ARG', 7.88)], [('CG', 'HIS', 'CB', 'ARG', 10.77), ('CG', 'HIS', 'CG', 'ARG', 10.21), ('CG', 'HIS', 'CD', 'ARG', 8.72), ('CG', 'HIS', 'NE', 'ARG', 8.04), ('CG', 'HIS', 'CZ', 'ARG', 6.84), ('CG', 'HIS', 'NH1', 'ARG', 6.13), ('CG', 'HIS', 'NH2', 'ARG', 6.63)], [('ND1', 'HIS', 'CB', 'ARG', 11.35), ('ND1', 'HIS', 'CG', 'ARG', 10.69), ('ND1', 'HIS', 'CD', 'ARG', 9.23), ('ND1', 'HIS', 'NE', 'ARG', 8.46), ('ND1', 'HIS', 'CZ', 'ARG', 7.16), ('ND1', 'HIS', 'NH1', 'ARG', 6.46), ('ND1', 'HIS', 'NH2', 'ARG', 6.83)], [('CD2', 'HIS', 'CB', 'ARG', 9.74), ('CD2', 'HIS', 'CG', 'ARG', 9.33), ('CD2', 'HIS', 'CD', 'ARG', 7.89), ('CD2', 'HIS', 'NE', 'ARG', 7.04), ('CD2', 'HIS', 'CZ', 'ARG', 5.86), ('CD2', 'HIS', 'NH1', 'ARG', 5.46), ('CD2', 'HIS', 'NH2', 'ARG', 5.48)], [('CE1', 'HIS', 'CB', 'ARG', 10.81), ('CE1', 'HIS', 'CG', 'ARG', 10.2), ('CE1', 'HIS', 'CD', 'ARG', 8.82), ('CE1', 'HIS', 'NE', 'ARG', 7.86), ('CE1', 'HIS', 'CZ', 'ARG', 6.53), ('CE1', 'HIS', 'NH1', 'ARG', 6.1), ('CE1', 'HIS', 'NH2', 'ARG', 5.95)], [('NE2', 'HIS', 'CB', 'ARG', 9.8), ('NE2', 'HIS', 'CG', 'ARG', 9.34), ('NE2', 'HIS', 'CD', 'ARG', 7.97), ('NE2', 'HIS', 'NE', 'ARG', 6.92), ('NE2', 'HIS', 'CZ', 'ARG', 5.64), ('NE2', 'HIS', 'NH1', 'ARG', 5.45), ('NE2', 'HIS', 'NH2', 'ARG', 4.95)]]}
HIS_ASP = { 
	'distances':
		[[7.07, 7.67, 7.94, 8.24], [6.53, 6.76, 7.02, 7.18], [5.44, 5.47, 5.65, 5.99], [7.35, 7.3, 7.59, 7.44], [5.83, 5.35, 5.5, 5.52], [6.97, 6.56, 6.79, 6.52], [8.41, 6.99, 6.94, 6.19], [8.4, 6.92, 6.78, 6.14], [7.49, 6.06, 6.05, 5.27], [9.51, 8.02, 7.74, 7.32], [8.21, 6.85, 6.74, 6.2], [9.39, 7.96, 7.69, 7.33]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.07), ('CB', 'HIS', 'CG', 'ASP', 7.67), ('CB', 'HIS', 'OD1', 'ASP', 7.94), ('CB', 'HIS', 'OD2', 'ASP', 8.24)], [('CG', 'HIS', 'CB', 'ASP', 6.53), ('CG', 'HIS', 'CG', 'ASP', 6.76), ('CG', 'HIS', 'OD1', 'ASP', 7.02), ('CG', 'HIS', 'OD2', 'ASP', 7.18)], [('ND1', 'HIS', 'CB', 'ASP', 5.44), ('ND1', 'HIS', 'CG', 'ASP', 5.47), ('ND1', 'HIS', 'OD1', 'ASP', 5.65), ('ND1', 'HIS', 'OD2', 'ASP', 5.99)], [('CD2', 'HIS', 'CB', 'ASP', 7.35), ('CD2', 'HIS', 'CG', 'ASP', 7.3), ('CD2', 'HIS', 'OD1', 'ASP', 7.59), ('CD2', 'HIS', 'OD2', 'ASP', 7.44)], [('CE1', 'HIS', 'CB', 'ASP', 5.83), ('CE1', 'HIS', 'CG', 'ASP', 5.35), ('CE1', 'HIS', 'OD1', 'ASP', 5.5), ('CE1', 'HIS', 'OD2', 'ASP', 5.52)], [('NE2', 'HIS', 'CB', 'ASP', 6.97), ('NE2', 'HIS', 'CG', 'ASP', 6.56), ('NE2', 'HIS', 'OD1', 'ASP', 6.79), ('NE2', 'HIS', 'OD2', 'ASP', 6.52)], [('CB', 'HIS', 'CB', 'ASP', 8.41), ('CB', 'HIS', 'CG', 'ASP', 6.99), ('CB', 'HIS', 'OD1', 'ASP', 6.94), ('CB', 'HIS', 'OD2', 'ASP', 6.19)], [('CG', 'HIS', 'CB', 'ASP', 8.4), ('CG', 'HIS', 'CG', 'ASP', 6.92), ('CG', 'HIS', 'OD1', 'ASP', 6.78), ('CG', 'HIS', 'OD2', 'ASP', 6.14)], [('ND1', 'HIS', 'CB', 'ASP', 7.49), ('ND1', 'HIS', 'CG', 'ASP', 6.06), ('ND1', 'HIS', 'OD1', 'ASP', 6.05), ('ND1', 'HIS', 'OD2', 'ASP', 5.27)], [('CD2', 'HIS', 'CB', 'ASP', 9.51), ('CD2', 'HIS', 'CG', 'ASP', 8.02), ('CD2', 'HIS', 'OD1', 'ASP', 7.74), ('CD2', 'HIS', 'OD2', 'ASP', 7.32)], [('CE1', 'HIS', 'CB', 'ASP', 8.21), ('CE1', 'HIS', 'CG', 'ASP', 6.85), ('CE1', 'HIS', 'OD1', 'ASP', 6.74), ('CE1', 'HIS', 'OD2', 'ASP', 6.2)], [('NE2', 'HIS', 'CB', 'ASP', 9.39), ('NE2', 'HIS', 'CG', 'ASP', 7.96), ('NE2', 'HIS', 'OD1', 'ASP', 7.69), ('NE2', 'HIS', 'OD2', 'ASP', 7.33)]]}
ASP_ARG = { 
	'distances':
		[[15.19, 14.07, 12.74, 12.44, 11.29, 10.2, 11.38], [13.82, 12.75, 11.38, 11.04, 9.87, 8.78, 9.97], [12.84, 11.7, 10.37, 10.15, 9.06, 7.9, 9.32], [13.81, 12.86, 11.43, 10.97, 9.73, 8.71, 9.68]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 15.19), ('CB', 'ASP', 'CG', 'ARG', 14.07), ('CB', 'ASP', 'CD', 'ARG', 12.74), ('CB', 'ASP', 'NE', 'ARG', 12.44), ('CB', 'ASP', 'CZ', 'ARG', 11.29), ('CB', 'ASP', 'NH1', 'ARG', 10.2), ('CB', 'ASP', 'NH2', 'ARG', 11.38)], [('CG', 'ASP', 'CB', 'ARG', 13.82), ('CG', 'ASP', 'CG', 'ARG', 12.75), ('CG', 'ASP', 'CD', 'ARG', 11.38), ('CG', 'ASP', 'NE', 'ARG', 11.04), ('CG', 'ASP', 'CZ', 'ARG', 9.87), ('CG', 'ASP', 'NH1', 'ARG', 8.78), ('CG', 'ASP', 'NH2', 'ARG', 9.97)], [('OD1', 'ASP', 'CB', 'ARG', 12.84), ('OD1', 'ASP', 'CG', 'ARG', 11.7), ('OD1', 'ASP', 'CD', 'ARG', 10.37), ('OD1', 'ASP', 'NE', 'ARG', 10.15), ('OD1', 'ASP', 'CZ', 'ARG', 9.06), ('OD1', 'ASP', 'NH1', 'ARG', 7.9), ('OD1', 'ASP', 'NH2', 'ARG', 9.32)], [('OD2', 'ASP', 'CB', 'ARG', 13.81), ('OD2', 'ASP', 'CG', 'ARG', 12.86), ('OD2', 'ASP', 'CD', 'ARG', 11.43), ('OD2', 'ASP', 'NE', 'ARG', 10.97), ('OD2', 'ASP', 'CZ', 'ARG', 9.73), ('OD2', 'ASP', 'NH1', 'ARG', 8.71), ('OD2', 'ASP', 'NH2', 'ARG', 9.68)]]}
HIS_HIS = { 
	'distances':
		[[11.93, 11.19, 9.88, 11.78, 9.73, 10.94], [10.62, 9.8, 8.47, 10.33, 8.26, 9.46], [9.45, 8.71, 7.44, 9.34, 7.4, 8.61], [10.46, 9.48, 8.12, 9.87, 7.71, 8.87], [8.49, 7.61, 6.29, 8.15, 6.13, 7.35], [9.17, 8.13, 6.78, 8.5, 6.33, 7.51], [11.93, 10.62, 9.45, 10.46, 8.49, 9.17], [11.19, 9.8, 8.71, 9.48, 7.61, 8.13], [9.88, 8.47, 7.44, 8.12, 6.29, 6.78], [11.78, 10.33, 9.34, 9.87, 8.15, 8.5], [9.73, 8.26, 7.4, 7.71, 6.13, 6.33], [10.94, 9.46, 8.61, 8.87, 7.35, 7.51]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 11.93), ('CB', 'HIS', 'CG', 'HIS', 11.19), ('CB', 'HIS', 'ND1', 'HIS', 9.88), ('CB', 'HIS', 'CD2', 'HIS', 11.78), ('CB', 'HIS', 'CE1', 'HIS', 9.73), ('CB', 'HIS', 'NE2', 'HIS', 10.94)], [('CG', 'HIS', 'CB', 'HIS', 10.62), ('CG', 'HIS', 'CG', 'HIS', 9.8), ('CG', 'HIS', 'ND1', 'HIS', 8.47), ('CG', 'HIS', 'CD2', 'HIS', 10.33), ('CG', 'HIS', 'CE1', 'HIS', 8.26), ('CG', 'HIS', 'NE2', 'HIS', 9.46)], [('ND1', 'HIS', 'CB', 'HIS', 9.45), ('ND1', 'HIS', 'CG', 'HIS', 8.71), ('ND1', 'HIS', 'ND1', 'HIS', 7.44), ('ND1', 'HIS', 'CD2', 'HIS', 9.34), ('ND1', 'HIS', 'CE1', 'HIS', 7.4), ('ND1', 'HIS', 'NE2', 'HIS', 8.61)], [('CD2', 'HIS', 'CB', 'HIS', 10.46), ('CD2', 'HIS', 'CG', 'HIS', 9.48), ('CD2', 'HIS', 'ND1', 'HIS', 8.12), ('CD2', 'HIS', 'CD2', 'HIS', 9.87), ('CD2', 'HIS', 'CE1', 'HIS', 7.71), ('CD2', 'HIS', 'NE2', 'HIS', 8.87)], [('CE1', 'HIS', 'CB', 'HIS', 8.49), ('CE1', 'HIS', 'CG', 'HIS', 7.61), ('CE1', 'HIS', 'ND1', 'HIS', 6.29), ('CE1', 'HIS', 'CD2', 'HIS', 8.15), ('CE1', 'HIS', 'CE1', 'HIS', 6.13), ('CE1', 'HIS', 'NE2', 'HIS', 7.35)], [('NE2', 'HIS', 'CB', 'HIS', 9.17), ('NE2', 'HIS', 'CG', 'HIS', 8.13), ('NE2', 'HIS', 'ND1', 'HIS', 6.78), ('NE2', 'HIS', 'CD2', 'HIS', 8.5), ('NE2', 'HIS', 'CE1', 'HIS', 6.33), ('NE2', 'HIS', 'NE2', 'HIS', 7.51)], [('CB', 'HIS', 'CB', 'HIS', 11.93), ('CB', 'HIS', 'CG', 'HIS', 10.62), ('CB', 'HIS', 'ND1', 'HIS', 9.45), ('CB', 'HIS', 'CD2', 'HIS', 10.46), ('CB', 'HIS', 'CE1', 'HIS', 8.49), ('CB', 'HIS', 'NE2', 'HIS', 9.17)], [('CG', 'HIS', 'CB', 'HIS', 11.19), ('CG', 'HIS', 'CG', 'HIS', 9.8), ('CG', 'HIS', 'ND1', 'HIS', 8.71), ('CG', 'HIS', 'CD2', 'HIS', 9.48), ('CG', 'HIS', 'CE1', 'HIS', 7.61), ('CG', 'HIS', 'NE2', 'HIS', 8.13)], [('ND1', 'HIS', 'CB', 'HIS', 9.88), ('ND1', 'HIS', 'CG', 'HIS', 8.47), ('ND1', 'HIS', 'ND1', 'HIS', 7.44), ('ND1', 'HIS', 'CD2', 'HIS', 8.12), ('ND1', 'HIS', 'CE1', 'HIS', 6.29), ('ND1', 'HIS', 'NE2', 'HIS', 6.78)], [('CD2', 'HIS', 'CB', 'HIS', 11.78), ('CD2', 'HIS', 'CG', 'HIS', 10.33), ('CD2', 'HIS', 'ND1', 'HIS', 9.34), ('CD2', 'HIS', 'CD2', 'HIS', 9.87), ('CD2', 'HIS', 'CE1', 'HIS', 8.15), ('CD2', 'HIS', 'NE2', 'HIS', 8.5)], [('CE1', 'HIS', 'CB', 'HIS', 9.73), ('CE1', 'HIS', 'CG', 'HIS', 8.26), ('CE1', 'HIS', 'ND1', 'HIS', 7.4), ('CE1', 'HIS', 'CD2', 'HIS', 7.71), ('CE1', 'HIS', 'CE1', 'HIS', 6.13), ('CE1', 'HIS', 'NE2', 'HIS', 6.33)], [('NE2', 'HIS', 'CB', 'HIS', 10.94), ('NE2', 'HIS', 'CG', 'HIS', 9.46), ('NE2', 'HIS', 'ND1', 'HIS', 8.61), ('NE2', 'HIS', 'CD2', 'HIS', 8.87), ('NE2', 'HIS', 'CE1', 'HIS', 7.35), ('NE2', 'HIS', 'NE2', 'HIS', 7.51)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ARG, d, 'P_1fwa_3_5_1_5')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'P_1fwa_3_5_1_5')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_ARG, d, 'P_1fwa_3_5_1_5')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_HIS, d, 'P_1fwa_3_5_1_5')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ARG' :  match1,
		'HIS_ASP' :  match2,
		'ASP_ARG' :  match3,
		'HIS_HIS' :  match4}