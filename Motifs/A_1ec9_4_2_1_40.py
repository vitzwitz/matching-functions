'''
FUNC:A_1ec9_4_2_1_40
PDB:1ec9
EC:4.2.1.40
RESI:lys,lys,asp,his,asp
LOCI:a-205,207,313,339,366;
'''
import motifFunctions as cmd
HIS_ASP = { 
	'distances':
		[[5.86, 6.56, 6.5, 7.66], [6.09, 6.42, 5.97, 7.66], [5.45, 5.39, 4.71, 6.65], [7.35, 7.59, 6.95, 8.86], [6.54, 6.25, 5.29, 7.48], [7.54, 7.47, 6.6, 8.73], [7.52, 7.52, 8.23, 7.07], [8.14, 8.25, 9.12, 7.61], [8.77, 9.16, 10.09, 8.63], [8.61, 8.57, 9.48, 7.69], [9.49, 9.86, 10.86, 9.18], [9.42, 9.57, 10.56, 8.71]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 5.86), ('CB', 'HIS', 'CG', 'ASP', 6.56), ('CB', 'HIS', 'OD1', 'ASP', 6.5), ('CB', 'HIS', 'OD2', 'ASP', 7.66)], [('CG', 'HIS', 'CB', 'ASP', 6.09), ('CG', 'HIS', 'CG', 'ASP', 6.42), ('CG', 'HIS', 'OD1', 'ASP', 5.97), ('CG', 'HIS', 'OD2', 'ASP', 7.66)], [('ND1', 'HIS', 'CB', 'ASP', 5.45), ('ND1', 'HIS', 'CG', 'ASP', 5.39), ('ND1', 'HIS', 'OD1', 'ASP', 4.71), ('ND1', 'HIS', 'OD2', 'ASP', 6.65)], [('CD2', 'HIS', 'CB', 'ASP', 7.35), ('CD2', 'HIS', 'CG', 'ASP', 7.59), ('CD2', 'HIS', 'OD1', 'ASP', 6.95), ('CD2', 'HIS', 'OD2', 'ASP', 8.86)], [('CE1', 'HIS', 'CB', 'ASP', 6.54), ('CE1', 'HIS', 'CG', 'ASP', 6.25), ('CE1', 'HIS', 'OD1', 'ASP', 5.29), ('CE1', 'HIS', 'OD2', 'ASP', 7.48)], [('NE2', 'HIS', 'CB', 'ASP', 7.54), ('NE2', 'HIS', 'CG', 'ASP', 7.47), ('NE2', 'HIS', 'OD1', 'ASP', 6.6), ('NE2', 'HIS', 'OD2', 'ASP', 8.73)], [('CB', 'HIS', 'CB', 'ASP', 7.52), ('CB', 'HIS', 'CG', 'ASP', 7.52), ('CB', 'HIS', 'OD1', 'ASP', 8.23), ('CB', 'HIS', 'OD2', 'ASP', 7.07)], [('CG', 'HIS', 'CB', 'ASP', 8.14), ('CG', 'HIS', 'CG', 'ASP', 8.25), ('CG', 'HIS', 'OD1', 'ASP', 9.12), ('CG', 'HIS', 'OD2', 'ASP', 7.61)], [('ND1', 'HIS', 'CB', 'ASP', 8.77), ('ND1', 'HIS', 'CG', 'ASP', 9.16), ('ND1', 'HIS', 'OD1', 'ASP', 10.09), ('ND1', 'HIS', 'OD2', 'ASP', 8.63)], [('CD2', 'HIS', 'CB', 'ASP', 8.61), ('CD2', 'HIS', 'CG', 'ASP', 8.57), ('CD2', 'HIS', 'OD1', 'ASP', 9.48), ('CD2', 'HIS', 'OD2', 'ASP', 7.69)], [('CE1', 'HIS', 'CB', 'ASP', 9.49), ('CE1', 'HIS', 'CG', 'ASP', 9.86), ('CE1', 'HIS', 'OD1', 'ASP', 10.86), ('CE1', 'HIS', 'OD2', 'ASP', 9.18)], [('NE2', 'HIS', 'CB', 'ASP', 9.42), ('NE2', 'HIS', 'CG', 'ASP', 9.57), ('NE2', 'HIS', 'OD1', 'ASP', 10.56), ('NE2', 'HIS', 'OD2', 'ASP', 8.71)]]}
LYS_ASPI = { 
	'distances':
		[[8.5, 7.67, 7.56, 7.54], [8.43, 7.47, 7.53, 7.0], [7.11, 6.11, 6.32, 5.51], [7.56, 6.53, 6.93, 5.55], [6.68, 5.69, 6.3, 4.49], [12.13, 11.68, 12.33, 10.74], [12.88, 12.45, 13.16, 11.4], [12.05, 11.64, 12.44, 10.52], [11.42, 10.82, 11.52, 9.64], [10.7, 10.13, 10.91, 8.89]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASPI', 8.5), ('CB', 'LYS', 'CG', 'ASPI', 7.67), ('CB', 'LYS', 'OD1', 'ASPI', 7.56), ('CB', 'LYS', 'OD2', 'ASPI', 7.54)], [('CG', 'LYS', 'CB', 'ASPI', 8.43), ('CG', 'LYS', 'CG', 'ASPI', 7.47), ('CG', 'LYS', 'OD1', 'ASPI', 7.53), ('CG', 'LYS', 'OD2', 'ASPI', 7.0)], [('CD', 'LYS', 'CB', 'ASPI', 7.11), ('CD', 'LYS', 'CG', 'ASPI', 6.11), ('CD', 'LYS', 'OD1', 'ASPI', 6.32), ('CD', 'LYS', 'OD2', 'ASPI', 5.51)], [('CE', 'LYS', 'CB', 'ASPI', 7.56), ('CE', 'LYS', 'CG', 'ASPI', 6.53), ('CE', 'LYS', 'OD1', 'ASPI', 6.93), ('CE', 'LYS', 'OD2', 'ASPI', 5.55)], [('NZ', 'LYS', 'CB', 'ASPI', 6.68), ('NZ', 'LYS', 'CG', 'ASPI', 5.69), ('NZ', 'LYS', 'OD1', 'ASPI', 6.3), ('NZ', 'LYS', 'OD2', 'ASPI', 4.49)], [('CB', 'LYS', 'CB', 'ASPI', 12.13), ('CB', 'LYS', 'CG', 'ASPI', 11.68), ('CB', 'LYS', 'OD1', 'ASPI', 12.33), ('CB', 'LYS', 'OD2', 'ASPI', 10.74)], [('CG', 'LYS', 'CB', 'ASPI', 12.88), ('CG', 'LYS', 'CG', 'ASPI', 12.45), ('CG', 'LYS', 'OD1', 'ASPI', 13.16), ('CG', 'LYS', 'OD2', 'ASPI', 11.4)], [('CD', 'LYS', 'CB', 'ASPI', 12.05), ('CD', 'LYS', 'CG', 'ASPI', 11.64), ('CD', 'LYS', 'OD1', 'ASPI', 12.44), ('CD', 'LYS', 'OD2', 'ASPI', 10.52)], [('CE', 'LYS', 'CB', 'ASPI', 11.42), ('CE', 'LYS', 'CG', 'ASPI', 10.82), ('CE', 'LYS', 'OD1', 'ASPI', 11.52), ('CE', 'LYS', 'OD2', 'ASPI', 9.64)], [('NZ', 'LYS', 'CB', 'ASPI', 10.7), ('NZ', 'LYS', 'CG', 'ASPI', 10.13), ('NZ', 'LYS', 'OD1', 'ASPI', 10.91), ('NZ', 'LYS', 'OD2', 'ASPI', 8.89)]]}
LYS_LYS = { 
	'distances':
		[[9.0, 10.32, 10.37, 9.68, 9.99], [7.99, 9.19, 9.12, 8.3, 8.58], [8.34, 9.36, 8.98, 8.09, 8.03], [7.76, 8.53, 7.94, 6.88, 6.67], [8.65, 9.21, 8.35, 7.3, 6.66], [9.0, 7.99, 8.34, 7.76, 8.65], [10.32, 9.19, 9.36, 8.53, 9.21], [10.37, 9.12, 8.98, 7.94, 8.35], [9.68, 8.3, 8.09, 6.88, 7.3], [9.99, 8.58, 8.03, 6.67, 6.66]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'LYS', 9.0), ('CB', 'LYS', 'CG', 'LYS', 10.32), ('CB', 'LYS', 'CD', 'LYS', 10.37), ('CB', 'LYS', 'CE', 'LYS', 9.68), ('CB', 'LYS', 'NZ', 'LYS', 9.99)], [('CG', 'LYS', 'CB', 'LYS', 7.99), ('CG', 'LYS', 'CG', 'LYS', 9.19), ('CG', 'LYS', 'CD', 'LYS', 9.12), ('CG', 'LYS', 'CE', 'LYS', 8.3), ('CG', 'LYS', 'NZ', 'LYS', 8.58)], [('CD', 'LYS', 'CB', 'LYS', 8.34), ('CD', 'LYS', 'CG', 'LYS', 9.36), ('CD', 'LYS', 'CD', 'LYS', 8.98), ('CD', 'LYS', 'CE', 'LYS', 8.09), ('CD', 'LYS', 'NZ', 'LYS', 8.03)], [('CE', 'LYS', 'CB', 'LYS', 7.76), ('CE', 'LYS', 'CG', 'LYS', 8.53), ('CE', 'LYS', 'CD', 'LYS', 7.94), ('CE', 'LYS', 'CE', 'LYS', 6.88), ('CE', 'LYS', 'NZ', 'LYS', 6.67)], [('NZ', 'LYS', 'CB', 'LYS', 8.65), ('NZ', 'LYS', 'CG', 'LYS', 9.21), ('NZ', 'LYS', 'CD', 'LYS', 8.35), ('NZ', 'LYS', 'CE', 'LYS', 7.3), ('NZ', 'LYS', 'NZ', 'LYS', 6.66)], [('CB', 'LYS', 'CB', 'LYS', 9.0), ('CB', 'LYS', 'CG', 'LYS', 7.99), ('CB', 'LYS', 'CD', 'LYS', 8.34), ('CB', 'LYS', 'CE', 'LYS', 7.76), ('CB', 'LYS', 'NZ', 'LYS', 8.65)], [('CG', 'LYS', 'CB', 'LYS', 10.32), ('CG', 'LYS', 'CG', 'LYS', 9.19), ('CG', 'LYS', 'CD', 'LYS', 9.36), ('CG', 'LYS', 'CE', 'LYS', 8.53), ('CG', 'LYS', 'NZ', 'LYS', 9.21)], [('CD', 'LYS', 'CB', 'LYS', 10.37), ('CD', 'LYS', 'CG', 'LYS', 9.12), ('CD', 'LYS', 'CD', 'LYS', 8.98), ('CD', 'LYS', 'CE', 'LYS', 7.94), ('CD', 'LYS', 'NZ', 'LYS', 8.35)], [('CE', 'LYS', 'CB', 'LYS', 9.68), ('CE', 'LYS', 'CG', 'LYS', 8.3), ('CE', 'LYS', 'CD', 'LYS', 8.09), ('CE', 'LYS', 'CE', 'LYS', 6.88), ('CE', 'LYS', 'NZ', 'LYS', 7.3)], [('NZ', 'LYS', 'CB', 'LYS', 9.99), ('NZ', 'LYS', 'CG', 'LYS', 8.58), ('NZ', 'LYS', 'CD', 'LYS', 8.03), ('NZ', 'LYS', 'CE', 'LYS', 6.67), ('NZ', 'LYS', 'NZ', 'LYS', 6.66)]]}
ASP_LYS = { 
	'distances':
		[[15.96, 15.34, 13.83, 13.31, 11.84], [16.16, 15.57, 14.08, 13.59, 12.15], [15.87, 15.22, 13.74, 13.17, 11.75], [16.86, 16.38, 14.9, 14.53, 13.11], [17.13, 17.11, 15.73, 15.14, 13.77], [17.01, 16.97, 15.6, 15.17, 13.83], [16.2, 16.1, 14.71, 14.37, 13.03], [17.98, 18.0, 16.67, 16.29, 14.98], [8.5, 8.43, 7.11, 7.56, 6.68], [7.67, 7.47, 6.11, 6.53, 5.69], [7.56, 7.53, 6.32, 6.93, 6.3], [7.54, 7.0, 5.51, 5.55, 4.49], [12.13, 12.88, 12.05, 11.42, 10.7], [11.68, 12.45, 11.64, 10.82, 10.13], [12.33, 13.16, 12.44, 11.52, 10.91], [10.74, 11.4, 10.52, 9.64, 8.89]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 15.96), ('CB', 'ASP', 'CG', 'LYS', 15.34), ('CB', 'ASP', 'CD', 'LYS', 13.83), ('CB', 'ASP', 'CE', 'LYS', 13.31), ('CB', 'ASP', 'NZ', 'LYS', 11.84)], [('CG', 'ASP', 'CB', 'LYS', 16.16), ('CG', 'ASP', 'CG', 'LYS', 15.57), ('CG', 'ASP', 'CD', 'LYS', 14.08), ('CG', 'ASP', 'CE', 'LYS', 13.59), ('CG', 'ASP', 'NZ', 'LYS', 12.15)], [('OD1', 'ASP', 'CB', 'LYS', 15.87), ('OD1', 'ASP', 'CG', 'LYS', 15.22), ('OD1', 'ASP', 'CD', 'LYS', 13.74), ('OD1', 'ASP', 'CE', 'LYS', 13.17), ('OD1', 'ASP', 'NZ', 'LYS', 11.75)], [('OD2', 'ASP', 'CB', 'LYS', 16.86), ('OD2', 'ASP', 'CG', 'LYS', 16.38), ('OD2', 'ASP', 'CD', 'LYS', 14.9), ('OD2', 'ASP', 'CE', 'LYS', 14.53), ('OD2', 'ASP', 'NZ', 'LYS', 13.11)], [('CB', 'ASP', 'CB', 'LYS', 17.13), ('CB', 'ASP', 'CG', 'LYS', 17.11), ('CB', 'ASP', 'CD', 'LYS', 15.73), ('CB', 'ASP', 'CE', 'LYS', 15.14), ('CB', 'ASP', 'NZ', 'LYS', 13.77)], [('CG', 'ASP', 'CB', 'LYS', 17.01), ('CG', 'ASP', 'CG', 'LYS', 16.97), ('CG', 'ASP', 'CD', 'LYS', 15.6), ('CG', 'ASP', 'CE', 'LYS', 15.17), ('CG', 'ASP', 'NZ', 'LYS', 13.83)], [('OD1', 'ASP', 'CB', 'LYS', 16.2), ('OD1', 'ASP', 'CG', 'LYS', 16.1), ('OD1', 'ASP', 'CD', 'LYS', 14.71), ('OD1', 'ASP', 'CE', 'LYS', 14.37), ('OD1', 'ASP', 'NZ', 'LYS', 13.03)], [('OD2', 'ASP', 'CB', 'LYS', 17.98), ('OD2', 'ASP', 'CG', 'LYS', 18.0), ('OD2', 'ASP', 'CD', 'LYS', 16.67), ('OD2', 'ASP', 'CE', 'LYS', 16.29), ('OD2', 'ASP', 'NZ', 'LYS', 14.98)], [('CB', 'ASP', 'CB', 'LYS', 8.5), ('CB', 'ASP', 'CG', 'LYS', 8.43), ('CB', 'ASP', 'CD', 'LYS', 7.11), ('CB', 'ASP', 'CE', 'LYS', 7.56), ('CB', 'ASP', 'NZ', 'LYS', 6.68)], [('CG', 'ASP', 'CB', 'LYS', 7.67), ('CG', 'ASP', 'CG', 'LYS', 7.47), ('CG', 'ASP', 'CD', 'LYS', 6.11), ('CG', 'ASP', 'CE', 'LYS', 6.53), ('CG', 'ASP', 'NZ', 'LYS', 5.69)], [('OD1', 'ASP', 'CB', 'LYS', 7.56), ('OD1', 'ASP', 'CG', 'LYS', 7.53), ('OD1', 'ASP', 'CD', 'LYS', 6.32), ('OD1', 'ASP', 'CE', 'LYS', 6.93), ('OD1', 'ASP', 'NZ', 'LYS', 6.3)], [('OD2', 'ASP', 'CB', 'LYS', 7.54), ('OD2', 'ASP', 'CG', 'LYS', 7.0), ('OD2', 'ASP', 'CD', 'LYS', 5.51), ('OD2', 'ASP', 'CE', 'LYS', 5.55), ('OD2', 'ASP', 'NZ', 'LYS', 4.49)], [('CB', 'ASP', 'CB', 'LYS', 12.13), ('CB', 'ASP', 'CG', 'LYS', 12.88), ('CB', 'ASP', 'CD', 'LYS', 12.05), ('CB', 'ASP', 'CE', 'LYS', 11.42), ('CB', 'ASP', 'NZ', 'LYS', 10.7)], [('CG', 'ASP', 'CB', 'LYS', 11.68), ('CG', 'ASP', 'CG', 'LYS', 12.45), ('CG', 'ASP', 'CD', 'LYS', 11.64), ('CG', 'ASP', 'CE', 'LYS', 10.82), ('CG', 'ASP', 'NZ', 'LYS', 10.13)], [('OD1', 'ASP', 'CB', 'LYS', 12.33), ('OD1', 'ASP', 'CG', 'LYS', 13.16), ('OD1', 'ASP', 'CD', 'LYS', 12.44), ('OD1', 'ASP', 'CE', 'LYS', 11.52), ('OD1', 'ASP', 'NZ', 'LYS', 10.91)], [('OD2', 'ASP', 'CB', 'LYS', 10.74), ('OD2', 'ASP', 'CG', 'LYS', 11.4), ('OD2', 'ASP', 'CD', 'LYS', 10.52), ('OD2', 'ASP', 'CE', 'LYS', 9.64), ('OD2', 'ASP', 'NZ', 'LYS', 8.89)]]}
HIS_LYS = { 
	'distances':
		[[12.54, 11.76, 10.25, 9.6, 8.12], [12.86, 11.98, 10.51, 9.7, 8.24], [13.84, 13.01, 11.54, 10.79, 9.35], [12.57, 11.55, 10.14, 9.14, 7.75], [14.09, 13.17, 11.76, 10.89, 9.53], [13.39, 12.35, 10.99, 9.98, 8.66], [13.8, 13.87, 12.54, 11.73, 10.41], [13.23, 13.15, 11.75, 11.09, 9.7], [13.92, 13.78, 12.37, 11.88, 10.5], [12.23, 12.03, 10.59, 9.93, 8.51], [13.4, 13.13, 11.68, 11.31, 9.93], [12.37, 12.04, 10.57, 10.12, 8.7]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'LYS', 12.54), ('CB', 'HIS', 'CG', 'LYS', 11.76), ('CB', 'HIS', 'CD', 'LYS', 10.25), ('CB', 'HIS', 'CE', 'LYS', 9.6), ('CB', 'HIS', 'NZ', 'LYS', 8.12)], [('CG', 'HIS', 'CB', 'LYS', 12.86), ('CG', 'HIS', 'CG', 'LYS', 11.98), ('CG', 'HIS', 'CD', 'LYS', 10.51), ('CG', 'HIS', 'CE', 'LYS', 9.7), ('CG', 'HIS', 'NZ', 'LYS', 8.24)], [('ND1', 'HIS', 'CB', 'LYS', 13.84), ('ND1', 'HIS', 'CG', 'LYS', 13.01), ('ND1', 'HIS', 'CD', 'LYS', 11.54), ('ND1', 'HIS', 'CE', 'LYS', 10.79), ('ND1', 'HIS', 'NZ', 'LYS', 9.35)], [('CD2', 'HIS', 'CB', 'LYS', 12.57), ('CD2', 'HIS', 'CG', 'LYS', 11.55), ('CD2', 'HIS', 'CD', 'LYS', 10.14), ('CD2', 'HIS', 'CE', 'LYS', 9.14), ('CD2', 'HIS', 'NZ', 'LYS', 7.75)], [('CE1', 'HIS', 'CB', 'LYS', 14.09), ('CE1', 'HIS', 'CG', 'LYS', 13.17), ('CE1', 'HIS', 'CD', 'LYS', 11.76), ('CE1', 'HIS', 'CE', 'LYS', 10.89), ('CE1', 'HIS', 'NZ', 'LYS', 9.53)], [('NE2', 'HIS', 'CB', 'LYS', 13.39), ('NE2', 'HIS', 'CG', 'LYS', 12.35), ('NE2', 'HIS', 'CD', 'LYS', 10.99), ('NE2', 'HIS', 'CE', 'LYS', 9.98), ('NE2', 'HIS', 'NZ', 'LYS', 8.66)], [('CB', 'HIS', 'CB', 'LYS', 13.8), ('CB', 'HIS', 'CG', 'LYS', 13.87), ('CB', 'HIS', 'CD', 'LYS', 12.54), ('CB', 'HIS', 'CE', 'LYS', 11.73), ('CB', 'HIS', 'NZ', 'LYS', 10.41)], [('CG', 'HIS', 'CB', 'LYS', 13.23), ('CG', 'HIS', 'CG', 'LYS', 13.15), ('CG', 'HIS', 'CD', 'LYS', 11.75), ('CG', 'HIS', 'CE', 'LYS', 11.09), ('CG', 'HIS', 'NZ', 'LYS', 9.7)], [('ND1', 'HIS', 'CB', 'LYS', 13.92), ('ND1', 'HIS', 'CG', 'LYS', 13.78), ('ND1', 'HIS', 'CD', 'LYS', 12.37), ('ND1', 'HIS', 'CE', 'LYS', 11.88), ('ND1', 'HIS', 'NZ', 'LYS', 10.5)], [('CD2', 'HIS', 'CB', 'LYS', 12.23), ('CD2', 'HIS', 'CG', 'LYS', 12.03), ('CD2', 'HIS', 'CD', 'LYS', 10.59), ('CD2', 'HIS', 'CE', 'LYS', 9.93), ('CD2', 'HIS', 'NZ', 'LYS', 8.51)], [('CE1', 'HIS', 'CB', 'LYS', 13.4), ('CE1', 'HIS', 'CG', 'LYS', 13.13), ('CE1', 'HIS', 'CD', 'LYS', 11.68), ('CE1', 'HIS', 'CE', 'LYS', 11.31), ('CE1', 'HIS', 'NZ', 'LYS', 9.93)], [('NE2', 'HIS', 'CB', 'LYS', 12.37), ('NE2', 'HIS', 'CG', 'LYS', 12.04), ('NE2', 'HIS', 'CD', 'LYS', 10.57), ('NE2', 'HIS', 'CE', 'LYS', 10.12), ('NE2', 'HIS', 'NZ', 'LYS', 8.7)]]}
ASP_ASP = { 
	'distances':
		[[10.03, 10.55, 11.2, 10.45], [10.14, 10.87, 11.64, 10.79], [10.1, 10.84, 11.71, 10.62], [10.62, 11.49, 12.21, 11.56], [10.03, 10.14, 10.1, 10.62], [10.55, 10.87, 10.84, 11.49], [11.2, 11.64, 11.71, 12.21], [10.45, 10.79, 10.62, 11.56]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 10.03), ('CB', 'ASP', 'CG', 'ASP', 10.55), ('CB', 'ASP', 'OD1', 'ASP', 11.2), ('CB', 'ASP', 'OD2', 'ASP', 10.45)], [('CG', 'ASP', 'CB', 'ASP', 10.14), ('CG', 'ASP', 'CG', 'ASP', 10.87), ('CG', 'ASP', 'OD1', 'ASP', 11.64), ('CG', 'ASP', 'OD2', 'ASP', 10.79)], [('OD1', 'ASP', 'CB', 'ASP', 10.1), ('OD1', 'ASP', 'CG', 'ASP', 10.84), ('OD1', 'ASP', 'OD1', 'ASP', 11.71), ('OD1', 'ASP', 'OD2', 'ASP', 10.62)], [('OD2', 'ASP', 'CB', 'ASP', 10.62), ('OD2', 'ASP', 'CG', 'ASP', 11.49), ('OD2', 'ASP', 'OD1', 'ASP', 12.21), ('OD2', 'ASP', 'OD2', 'ASP', 11.56)], [('CB', 'ASP', 'CB', 'ASP', 10.03), ('CB', 'ASP', 'CG', 'ASP', 10.14), ('CB', 'ASP', 'OD1', 'ASP', 10.1), ('CB', 'ASP', 'OD2', 'ASP', 10.62)], [('CG', 'ASP', 'CB', 'ASP', 10.55), ('CG', 'ASP', 'CG', 'ASP', 10.87), ('CG', 'ASP', 'OD1', 'ASP', 10.84), ('CG', 'ASP', 'OD2', 'ASP', 11.49)], [('OD1', 'ASP', 'CB', 'ASP', 11.2), ('OD1', 'ASP', 'CG', 'ASP', 11.64), ('OD1', 'ASP', 'OD1', 'ASP', 11.71), ('OD1', 'ASP', 'OD2', 'ASP', 12.21)], [('OD2', 'ASP', 'CB', 'ASP', 10.45), ('OD2', 'ASP', 'CG', 'ASP', 10.79), ('OD2', 'ASP', 'OD1', 'ASP', 10.62), ('OD2', 'ASP', 'OD2', 'ASP', 11.56)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASP, d, 'A_1ec9_4_2_1_40')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_ASPI, d, 'A_1ec9_4_2_1_40')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LYS_LYS, d, 'A_1ec9_4_2_1_40')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_LYS, d, 'A_1ec9_4_2_1_40')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_LYS, d, 'A_1ec9_4_2_1_40')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ASP_ASP, d, 'A_1ec9_4_2_1_40')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASP' :  match1,
		'LYS_ASPI' :  match2,
		'LYS_LYS' :  match3,
		'ASP_LYS' :  match4,
		'HIS_LYS' :  match5,
		'ASP_ASP' :  match6}