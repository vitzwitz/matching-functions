'''
FUNC:P_1bcs_3_4_16_6
PDB:1bcs
EC:3.4.16.6
RESI:gly,ser,tyr,asp,his
LOCI:a-53,146,147;b-338,397;
'''
import motifFunctions as cmd
SER_TYR = { 
	'distances':
		[[6.85, 8.24, 8.68, 9.31, 10.04, 10.57, 10.89, 12.2, 8.23, 7.02, 6.17, 4.71], [6.8, 8.1, 8.31, 9.32, 9.65, 10.51, 10.65, 11.94, 8.66, 7.52, 6.34, 5.04]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'TYR', 6.85), ('CB', 'SER', 'CG', 'TYR', 8.24), ('CB', 'SER', 'CD1', 'TYR', 8.68), ('CB', 'SER', 'CD2', 'TYR', 9.31), ('CB', 'SER', 'CE1', 'TYR', 10.04), ('CB', 'SER', 'CE2', 'TYR', 10.57), ('CB', 'SER', 'CZ', 'TYR', 10.89), ('CB', 'SER', 'OH', 'TYR', 12.2), ('CB', 'SER', 'O', 'TYR', 8.23), ('CB', 'SER', 'C', 'TYR', 7.02), ('CB', 'SER', 'CA', 'TYR', 6.17), ('CB', 'SER', 'N', 'TYR', 4.71)], [('OG', 'SER', 'CB', 'TYR', 6.8), ('OG', 'SER', 'CG', 'TYR', 8.1), ('OG', 'SER', 'CD1', 'TYR', 8.31), ('OG', 'SER', 'CD2', 'TYR', 9.32), ('OG', 'SER', 'CE1', 'TYR', 9.65), ('OG', 'SER', 'CE2', 'TYR', 10.51), ('OG', 'SER', 'CZ', 'TYR', 10.65), ('OG', 'SER', 'OH', 'TYR', 11.94), ('OG', 'SER', 'O', 'TYR', 8.66), ('OG', 'SER', 'C', 'TYR', 7.52), ('OG', 'SER', 'CA', 'TYR', 6.34), ('OG', 'SER', 'N', 'TYR', 5.04)]]}
GLY_SER = { 
	'distances':
		[[8.2, 7.42], [8.45, 7.92], [8.09, 7.77], [7.01, 6.95]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'SER', 8.2), ('O', 'GLY', 'OG', 'SER', 7.42)], [('C', 'GLY', 'CB', 'SER', 8.45), ('C', 'GLY', 'OG', 'SER', 7.92)], [('CA', 'GLY', 'CB', 'SER', 8.09), ('CA', 'GLY', 'OG', 'SER', 7.77)], [('N', 'GLY', 'CB', 'SER', 7.01), ('N', 'GLY', 'OG', 'SER', 6.95)]]}
ASP_HIS = { 
	'distances':
		[[6.03, 6.79, 6.53, 8.15, 7.79, 8.65], [5.4, 5.82, 5.33, 7.15, 6.55, 7.48], [5.32, 5.78, 5.44, 7.01, 6.59, 7.4], [5.75, 5.71, 4.83, 6.94, 5.86, 6.98]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 6.03), ('CB', 'ASP', 'CG', 'HIS', 6.79), ('CB', 'ASP', 'ND1', 'HIS', 6.53), ('CB', 'ASP', 'CD2', 'HIS', 8.15), ('CB', 'ASP', 'CE1', 'HIS', 7.79), ('CB', 'ASP', 'NE2', 'HIS', 8.65)], [('CG', 'ASP', 'CB', 'HIS', 5.4), ('CG', 'ASP', 'CG', 'HIS', 5.82), ('CG', 'ASP', 'ND1', 'HIS', 5.33), ('CG', 'ASP', 'CD2', 'HIS', 7.15), ('CG', 'ASP', 'CE1', 'HIS', 6.55), ('CG', 'ASP', 'NE2', 'HIS', 7.48)], [('OD1', 'ASP', 'CB', 'HIS', 5.32), ('OD1', 'ASP', 'CG', 'HIS', 5.78), ('OD1', 'ASP', 'ND1', 'HIS', 5.44), ('OD1', 'ASP', 'CD2', 'HIS', 7.01), ('OD1', 'ASP', 'CE1', 'HIS', 6.59), ('OD1', 'ASP', 'NE2', 'HIS', 7.4)], [('OD2', 'ASP', 'CB', 'HIS', 5.75), ('OD2', 'ASP', 'CG', 'HIS', 5.71), ('OD2', 'ASP', 'ND1', 'HIS', 4.83), ('OD2', 'ASP', 'CD2', 'HIS', 6.94), ('OD2', 'ASP', 'CE1', 'HIS', 5.86), ('OD2', 'ASP', 'NE2', 'HIS', 6.98)]]}
TYR_ASP = { 
	'distances':
		[[15.56, 14.28, 14.32, 13.29], [16.74, 15.45, 15.5, 14.42], [16.64, 15.33, 15.37, 14.27], [18.01, 16.75, 16.81, 15.71], [17.8, 16.49, 16.54, 15.41], [19.08, 17.82, 17.89, 16.75], [18.98, 17.7, 17.76, 16.61], [20.11, 18.83, 18.91, 17.73], [16.66, 15.59, 15.9, 14.44], [15.65, 14.57, 14.84, 13.46], [14.78, 13.59, 13.77, 12.51], [13.44, 12.27, 12.46, 11.23]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASP', 15.56), ('CB', 'TYR', 'CG', 'ASP', 14.28), ('CB', 'TYR', 'OD1', 'ASP', 14.32), ('CB', 'TYR', 'OD2', 'ASP', 13.29)], [('CG', 'TYR', 'CB', 'ASP', 16.74), ('CG', 'TYR', 'CG', 'ASP', 15.45), ('CG', 'TYR', 'OD1', 'ASP', 15.5), ('CG', 'TYR', 'OD2', 'ASP', 14.42)], [('CD1', 'TYR', 'CB', 'ASP', 16.64), ('CD1', 'TYR', 'CG', 'ASP', 15.33), ('CD1', 'TYR', 'OD1', 'ASP', 15.37), ('CD1', 'TYR', 'OD2', 'ASP', 14.27)], [('CD2', 'TYR', 'CB', 'ASP', 18.01), ('CD2', 'TYR', 'CG', 'ASP', 16.75), ('CD2', 'TYR', 'OD1', 'ASP', 16.81), ('CD2', 'TYR', 'OD2', 'ASP', 15.71)], [('CE1', 'TYR', 'CB', 'ASP', 17.8), ('CE1', 'TYR', 'CG', 'ASP', 16.49), ('CE1', 'TYR', 'OD1', 'ASP', 16.54), ('CE1', 'TYR', 'OD2', 'ASP', 15.41)], [('CE2', 'TYR', 'CB', 'ASP', 19.08), ('CE2', 'TYR', 'CG', 'ASP', 17.82), ('CE2', 'TYR', 'OD1', 'ASP', 17.89), ('CE2', 'TYR', 'OD2', 'ASP', 16.75)], [('CZ', 'TYR', 'CB', 'ASP', 18.98), ('CZ', 'TYR', 'CG', 'ASP', 17.7), ('CZ', 'TYR', 'OD1', 'ASP', 17.76), ('CZ', 'TYR', 'OD2', 'ASP', 16.61)], [('OH', 'TYR', 'CB', 'ASP', 20.11), ('OH', 'TYR', 'CG', 'ASP', 18.83), ('OH', 'TYR', 'OD1', 'ASP', 18.91), ('OH', 'TYR', 'OD2', 'ASP', 17.73)], [('O', 'TYR', 'CB', 'ASP', 16.66), ('O', 'TYR', 'CG', 'ASP', 15.59), ('O', 'TYR', 'OD1', 'ASP', 15.9), ('O', 'TYR', 'OD2', 'ASP', 14.44)], [('C', 'TYR', 'CB', 'ASP', 15.65), ('C', 'TYR', 'CG', 'ASP', 14.57), ('C', 'TYR', 'OD1', 'ASP', 14.84), ('C', 'TYR', 'OD2', 'ASP', 13.46)], [('CA', 'TYR', 'CB', 'ASP', 14.78), ('CA', 'TYR', 'CG', 'ASP', 13.59), ('CA', 'TYR', 'OD1', 'ASP', 13.77), ('CA', 'TYR', 'OD2', 'ASP', 12.51)], [('N', 'TYR', 'CB', 'ASP', 13.44), ('N', 'TYR', 'CG', 'ASP', 12.27), ('N', 'TYR', 'OD1', 'ASP', 12.46), ('N', 'TYR', 'OD2', 'ASP', 11.23)]]}
GLY_TYR = { 
	'distances':
		[[5.99, 6.49, 6.65, 7.4, 7.63, 8.27, 8.38, 9.55, 9.26, 8.53, 7.22, 7.32], [5.74, 6.22, 6.69, 6.87, 7.66, 7.8, 8.16, 9.36, 8.95, 8.24, 7.14, 7.37], [6.16, 6.97, 7.72, 7.51, 8.8, 8.62, 9.21, 10.46, 9.24, 8.38, 7.42, 7.39], [5.28, 6.37, 7.31, 6.94, 8.52, 8.22, 8.92, 10.25, 8.15, 7.19, 6.34, 6.21]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'TYR', 5.99), ('O', 'GLY', 'CG', 'TYR', 6.49), ('O', 'GLY', 'CD1', 'TYR', 6.65), ('O', 'GLY', 'CD2', 'TYR', 7.4), ('O', 'GLY', 'CE1', 'TYR', 7.63), ('O', 'GLY', 'CE2', 'TYR', 8.27), ('O', 'GLY', 'CZ', 'TYR', 8.38), ('O', 'GLY', 'OH', 'TYR', 9.55), ('O', 'GLY', 'O', 'TYR', 9.26), ('O', 'GLY', 'C', 'TYR', 8.53), ('O', 'GLY', 'CA', 'TYR', 7.22), ('O', 'GLY', 'N', 'TYR', 7.32)], [('C', 'GLY', 'CB', 'TYR', 5.74), ('C', 'GLY', 'CG', 'TYR', 6.22), ('C', 'GLY', 'CD1', 'TYR', 6.69), ('C', 'GLY', 'CD2', 'TYR', 6.87), ('C', 'GLY', 'CE1', 'TYR', 7.66), ('C', 'GLY', 'CE2', 'TYR', 7.8), ('C', 'GLY', 'CZ', 'TYR', 8.16), ('C', 'GLY', 'OH', 'TYR', 9.36), ('C', 'GLY', 'O', 'TYR', 8.95), ('C', 'GLY', 'C', 'TYR', 8.24), ('C', 'GLY', 'CA', 'TYR', 7.14), ('C', 'GLY', 'N', 'TYR', 7.37)], [('CA', 'GLY', 'CB', 'TYR', 6.16), ('CA', 'GLY', 'CG', 'TYR', 6.97), ('CA', 'GLY', 'CD1', 'TYR', 7.72), ('CA', 'GLY', 'CD2', 'TYR', 7.51), ('CA', 'GLY', 'CE1', 'TYR', 8.8), ('CA', 'GLY', 'CE2', 'TYR', 8.62), ('CA', 'GLY', 'CZ', 'TYR', 9.21), ('CA', 'GLY', 'OH', 'TYR', 10.46), ('CA', 'GLY', 'O', 'TYR', 9.24), ('CA', 'GLY', 'C', 'TYR', 8.38), ('CA', 'GLY', 'CA', 'TYR', 7.42), ('CA', 'GLY', 'N', 'TYR', 7.39)], [('N', 'GLY', 'CB', 'TYR', 5.28), ('N', 'GLY', 'CG', 'TYR', 6.37), ('N', 'GLY', 'CD1', 'TYR', 7.31), ('N', 'GLY', 'CD2', 'TYR', 6.94), ('N', 'GLY', 'CE1', 'TYR', 8.52), ('N', 'GLY', 'CE2', 'TYR', 8.22), ('N', 'GLY', 'CZ', 'TYR', 8.92), ('N', 'GLY', 'OH', 'TYR', 10.25), ('N', 'GLY', 'O', 'TYR', 8.15), ('N', 'GLY', 'C', 'TYR', 7.19), ('N', 'GLY', 'CA', 'TYR', 6.34), ('N', 'GLY', 'N', 'TYR', 6.21)]]}
TYR_HIS = { 
	'distances':
		[[13.36, 11.9, 11.32, 11.04, 10.0, 9.77], [14.73, 13.26, 12.6, 12.46, 11.3, 11.16], [14.95, 13.49, 12.7, 12.81, 11.43, 11.46], [15.89, 14.43, 13.83, 13.56, 12.52, 12.3], [16.26, 14.81, 13.97, 14.17, 12.72, 12.81], [17.13, 15.66, 15.0, 14.85, 13.7, 13.56], [17.31, 15.84, 15.07, 15.13, 13.8, 13.79], [18.58, 17.12, 16.3, 16.44, 15.05, 15.1], [14.86, 13.44, 12.79, 12.73, 11.58, 11.51], [13.68, 12.26, 11.67, 11.51, 10.44, 10.3], [12.82, 11.36, 10.7, 10.62, 9.43, 9.34], [11.38, 9.93, 9.31, 9.19, 8.04, 7.92]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'HIS', 13.36), ('CB', 'TYR', 'CG', 'HIS', 11.9), ('CB', 'TYR', 'ND1', 'HIS', 11.32), ('CB', 'TYR', 'CD2', 'HIS', 11.04), ('CB', 'TYR', 'CE1', 'HIS', 10.0), ('CB', 'TYR', 'NE2', 'HIS', 9.77)], [('CG', 'TYR', 'CB', 'HIS', 14.73), ('CG', 'TYR', 'CG', 'HIS', 13.26), ('CG', 'TYR', 'ND1', 'HIS', 12.6), ('CG', 'TYR', 'CD2', 'HIS', 12.46), ('CG', 'TYR', 'CE1', 'HIS', 11.3), ('CG', 'TYR', 'NE2', 'HIS', 11.16)], [('CD1', 'TYR', 'CB', 'HIS', 14.95), ('CD1', 'TYR', 'CG', 'HIS', 13.49), ('CD1', 'TYR', 'ND1', 'HIS', 12.7), ('CD1', 'TYR', 'CD2', 'HIS', 12.81), ('CD1', 'TYR', 'CE1', 'HIS', 11.43), ('CD1', 'TYR', 'NE2', 'HIS', 11.46)], [('CD2', 'TYR', 'CB', 'HIS', 15.89), ('CD2', 'TYR', 'CG', 'HIS', 14.43), ('CD2', 'TYR', 'ND1', 'HIS', 13.83), ('CD2', 'TYR', 'CD2', 'HIS', 13.56), ('CD2', 'TYR', 'CE1', 'HIS', 12.52), ('CD2', 'TYR', 'NE2', 'HIS', 12.3)], [('CE1', 'TYR', 'CB', 'HIS', 16.26), ('CE1', 'TYR', 'CG', 'HIS', 14.81), ('CE1', 'TYR', 'ND1', 'HIS', 13.97), ('CE1', 'TYR', 'CD2', 'HIS', 14.17), ('CE1', 'TYR', 'CE1', 'HIS', 12.72), ('CE1', 'TYR', 'NE2', 'HIS', 12.81)], [('CE2', 'TYR', 'CB', 'HIS', 17.13), ('CE2', 'TYR', 'CG', 'HIS', 15.66), ('CE2', 'TYR', 'ND1', 'HIS', 15.0), ('CE2', 'TYR', 'CD2', 'HIS', 14.85), ('CE2', 'TYR', 'CE1', 'HIS', 13.7), ('CE2', 'TYR', 'NE2', 'HIS', 13.56)], [('CZ', 'TYR', 'CB', 'HIS', 17.31), ('CZ', 'TYR', 'CG', 'HIS', 15.84), ('CZ', 'TYR', 'ND1', 'HIS', 15.07), ('CZ', 'TYR', 'CD2', 'HIS', 15.13), ('CZ', 'TYR', 'CE1', 'HIS', 13.8), ('CZ', 'TYR', 'NE2', 'HIS', 13.79)], [('OH', 'TYR', 'CB', 'HIS', 18.58), ('OH', 'TYR', 'CG', 'HIS', 17.12), ('OH', 'TYR', 'ND1', 'HIS', 16.3), ('OH', 'TYR', 'CD2', 'HIS', 16.44), ('OH', 'TYR', 'CE1', 'HIS', 15.05), ('OH', 'TYR', 'NE2', 'HIS', 15.1)], [('O', 'TYR', 'CB', 'HIS', 14.86), ('O', 'TYR', 'CG', 'HIS', 13.44), ('O', 'TYR', 'ND1', 'HIS', 12.79), ('O', 'TYR', 'CD2', 'HIS', 12.73), ('O', 'TYR', 'CE1', 'HIS', 11.58), ('O', 'TYR', 'NE2', 'HIS', 11.51)], [('C', 'TYR', 'CB', 'HIS', 13.68), ('C', 'TYR', 'CG', 'HIS', 12.26), ('C', 'TYR', 'ND1', 'HIS', 11.67), ('C', 'TYR', 'CD2', 'HIS', 11.51), ('C', 'TYR', 'CE1', 'HIS', 10.44), ('C', 'TYR', 'NE2', 'HIS', 10.3)], [('CA', 'TYR', 'CB', 'HIS', 12.82), ('CA', 'TYR', 'CG', 'HIS', 11.36), ('CA', 'TYR', 'ND1', 'HIS', 10.7), ('CA', 'TYR', 'CD2', 'HIS', 10.62), ('CA', 'TYR', 'CE1', 'HIS', 9.43), ('CA', 'TYR', 'NE2', 'HIS', 9.34)], [('N', 'TYR', 'CB', 'HIS', 11.38), ('N', 'TYR', 'CG', 'HIS', 9.93), ('N', 'TYR', 'ND1', 'HIS', 9.31), ('N', 'TYR', 'CD2', 'HIS', 9.19), ('N', 'TYR', 'CE1', 'HIS', 8.04), ('N', 'TYR', 'NE2', 'HIS', 7.92)]]}
GLY_HIS = { 
	'distances':
		[[13.11, 11.74, 11.29, 10.85, 10.06, 9.7], [13.66, 12.28, 11.93, 11.28, 10.66, 10.17], [13.08, 11.73, 11.57, 10.61, 10.33, 9.63], [12.5, 11.11, 10.94, 9.97, 9.66, 8.95]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'HIS', 13.11), ('O', 'GLY', 'CG', 'HIS', 11.74), ('O', 'GLY', 'ND1', 'HIS', 11.29), ('O', 'GLY', 'CD2', 'HIS', 10.85), ('O', 'GLY', 'CE1', 'HIS', 10.06), ('O', 'GLY', 'NE2', 'HIS', 9.7)], [('C', 'GLY', 'CB', 'HIS', 13.66), ('C', 'GLY', 'CG', 'HIS', 12.28), ('C', 'GLY', 'ND1', 'HIS', 11.93), ('C', 'GLY', 'CD2', 'HIS', 11.28), ('C', 'GLY', 'CE1', 'HIS', 10.66), ('C', 'GLY', 'NE2', 'HIS', 10.17)], [('CA', 'GLY', 'CB', 'HIS', 13.08), ('CA', 'GLY', 'CG', 'HIS', 11.73), ('CA', 'GLY', 'ND1', 'HIS', 11.57), ('CA', 'GLY', 'CD2', 'HIS', 10.61), ('CA', 'GLY', 'CE1', 'HIS', 10.33), ('CA', 'GLY', 'NE2', 'HIS', 9.63)], [('N', 'GLY', 'CB', 'HIS', 12.5), ('N', 'GLY', 'CG', 'HIS', 11.11), ('N', 'GLY', 'ND1', 'HIS', 10.94), ('N', 'GLY', 'CD2', 'HIS', 9.97), ('N', 'GLY', 'CE1', 'HIS', 9.66), ('N', 'GLY', 'NE2', 'HIS', 8.95)]]}
SER_ASP = { 
	'distances':
		[[11.09, 9.95, 10.12, 9.03], [10.83, 9.55, 9.58, 8.65]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 11.09), ('CB', 'SER', 'CG', 'ASP', 9.95), ('CB', 'SER', 'OD1', 'ASP', 10.12), ('CB', 'SER', 'OD2', 'ASP', 9.03)], [('OG', 'SER', 'CB', 'ASP', 10.83), ('OG', 'SER', 'CG', 'ASP', 9.55), ('OG', 'SER', 'OD1', 'ASP', 9.58), ('OG', 'SER', 'OD2', 'ASP', 8.65)]]}
SER_HIS = { 
	'distances':
		[[8.7, 7.27, 6.79, 6.51, 5.55, 5.29], [8.66, 7.19, 6.52, 6.55, 5.2, 5.18]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 8.7), ('CB', 'SER', 'CG', 'HIS', 7.27), ('CB', 'SER', 'ND1', 'HIS', 6.79), ('CB', 'SER', 'CD2', 'HIS', 6.51), ('CB', 'SER', 'CE1', 'HIS', 5.55), ('CB', 'SER', 'NE2', 'HIS', 5.29)], [('OG', 'SER', 'CB', 'HIS', 8.66), ('OG', 'SER', 'CG', 'HIS', 7.19), ('OG', 'SER', 'ND1', 'HIS', 6.52), ('OG', 'SER', 'CD2', 'HIS', 6.55), ('OG', 'SER', 'CE1', 'HIS', 5.2), ('OG', 'SER', 'NE2', 'HIS', 5.18)]]}
GLY_ASP = { 
	'distances':
		[[15.53, 14.07, 13.72, 13.37], [16.29, 14.86, 14.55, 14.15], [16.03, 14.66, 14.33, 14.01], [15.45, 14.13, 13.93, 13.41]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ASP', 15.53), ('O', 'GLY', 'CG', 'ASP', 14.07), ('O', 'GLY', 'OD1', 'ASP', 13.72), ('O', 'GLY', 'OD2', 'ASP', 13.37)], [('C', 'GLY', 'CB', 'ASP', 16.29), ('C', 'GLY', 'CG', 'ASP', 14.86), ('C', 'GLY', 'OD1', 'ASP', 14.55), ('C', 'GLY', 'OD2', 'ASP', 14.15)], [('CA', 'GLY', 'CB', 'ASP', 16.03), ('CA', 'GLY', 'CG', 'ASP', 14.66), ('CA', 'GLY', 'OD1', 'ASP', 14.33), ('CA', 'GLY', 'OD2', 'ASP', 14.01)], [('N', 'GLY', 'CB', 'ASP', 15.45), ('N', 'GLY', 'CG', 'ASP', 14.13), ('N', 'GLY', 'OD1', 'ASP', 13.93), ('N', 'GLY', 'OD2', 'ASP', 13.41)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_TYR, d, 'P_1bcs_3_4_16_6')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLY_SER, d, 'P_1bcs_3_4_16_6')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_HIS, d, 'P_1bcs_3_4_16_6')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(TYR_ASP, d, 'P_1bcs_3_4_16_6')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLY_TYR, d, 'P_1bcs_3_4_16_6')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(TYR_HIS, d, 'P_1bcs_3_4_16_6')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(GLY_HIS, d, 'P_1bcs_3_4_16_6')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(SER_ASP, d, 'P_1bcs_3_4_16_6')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(SER_HIS, d, 'P_1bcs_3_4_16_6')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(GLY_ASP, d, 'P_1bcs_3_4_16_6')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_TYR' :  match1,
		'GLY_SER' :  match2,
		'ASP_HIS' :  match3,
		'TYR_ASP' :  match4,
		'GLY_TYR' :  match5,
		'TYR_HIS' :  match6,
		'GLY_HIS' :  match7,
		'SER_ASP' :  match8,
		'SER_HIS' :  match9,
		'GLY_ASP' :  match10}