'''
FUNC:A_1gdh_1_1_1_29
PDB:1gdh
EC:1.1.1.29
RESI:arg,asp,asp,glu,his
LOCI:a-240,242,264,269,287;
'''
import motifFunctions as cmd
ASP_HIS = { 
	'distances':
		[[15.31, 14.42, 13.31, 14.62, 12.81, 13.64], [15.59, 14.56, 13.43, 14.62, 12.78, 13.53], [15.11, 14.02, 12.95, 13.96, 12.2, 12.84], [16.45, 15.4, 14.22, 15.47, 13.54, 14.33], [7.99, 7.97, 8.78, 7.63, 8.94, 8.29], [7.14, 7.23, 8.27, 6.84, 8.51, 7.73], [7.07, 7.5, 8.65, 7.33, 9.1, 8.4], [6.87, 6.69, 7.74, 6.02, 7.81, 6.86]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 15.31), ('CB', 'ASP', 'CG', 'HIS', 14.42), ('CB', 'ASP', 'ND1', 'HIS', 13.31), ('CB', 'ASP', 'CD2', 'HIS', 14.62), ('CB', 'ASP', 'CE1', 'HIS', 12.81), ('CB', 'ASP', 'NE2', 'HIS', 13.64)], [('CG', 'ASP', 'CB', 'HIS', 15.59), ('CG', 'ASP', 'CG', 'HIS', 14.56), ('CG', 'ASP', 'ND1', 'HIS', 13.43), ('CG', 'ASP', 'CD2', 'HIS', 14.62), ('CG', 'ASP', 'CE1', 'HIS', 12.78), ('CG', 'ASP', 'NE2', 'HIS', 13.53)], [('OD1', 'ASP', 'CB', 'HIS', 15.11), ('OD1', 'ASP', 'CG', 'HIS', 14.02), ('OD1', 'ASP', 'ND1', 'HIS', 12.95), ('OD1', 'ASP', 'CD2', 'HIS', 13.96), ('OD1', 'ASP', 'CE1', 'HIS', 12.2), ('OD1', 'ASP', 'NE2', 'HIS', 12.84)], [('OD2', 'ASP', 'CB', 'HIS', 16.45), ('OD2', 'ASP', 'CG', 'HIS', 15.4), ('OD2', 'ASP', 'ND1', 'HIS', 14.22), ('OD2', 'ASP', 'CD2', 'HIS', 15.47), ('OD2', 'ASP', 'CE1', 'HIS', 13.54), ('OD2', 'ASP', 'NE2', 'HIS', 14.33)], [('CB', 'ASP', 'CB', 'HIS', 7.99), ('CB', 'ASP', 'CG', 'HIS', 7.97), ('CB', 'ASP', 'ND1', 'HIS', 8.78), ('CB', 'ASP', 'CD2', 'HIS', 7.63), ('CB', 'ASP', 'CE1', 'HIS', 8.94), ('CB', 'ASP', 'NE2', 'HIS', 8.29)], [('CG', 'ASP', 'CB', 'HIS', 7.14), ('CG', 'ASP', 'CG', 'HIS', 7.23), ('CG', 'ASP', 'ND1', 'HIS', 8.27), ('CG', 'ASP', 'CD2', 'HIS', 6.84), ('CG', 'ASP', 'CE1', 'HIS', 8.51), ('CG', 'ASP', 'NE2', 'HIS', 7.73)], [('OD1', 'ASP', 'CB', 'HIS', 7.07), ('OD1', 'ASP', 'CG', 'HIS', 7.5), ('OD1', 'ASP', 'ND1', 'HIS', 8.65), ('OD1', 'ASP', 'CD2', 'HIS', 7.33), ('OD1', 'ASP', 'CE1', 'HIS', 9.1), ('OD1', 'ASP', 'NE2', 'HIS', 8.4)], [('OD2', 'ASP', 'CB', 'HIS', 6.87), ('OD2', 'ASP', 'CG', 'HIS', 6.69), ('OD2', 'ASP', 'ND1', 'HIS', 7.74), ('OD2', 'ASP', 'CD2', 'HIS', 6.02), ('OD2', 'ASP', 'CE1', 'HIS', 7.81), ('OD2', 'ASP', 'NE2', 'HIS', 6.86)]]}
ARG_HIS = { 
	'distances':
		[[12.92, 11.69, 10.87, 11.31, 9.91, 10.19], [12.93, 11.61, 10.69, 11.19, 9.63, 9.96], [13.24, 11.97, 10.91, 11.74, 9.95, 10.49], [13.29, 11.97, 10.84, 11.74, 9.84, 10.44], [13.76, 12.5, 11.28, 12.41, 10.38, 11.12], [14.59, 13.4, 12.15, 13.39, 11.34, 12.14], [13.78, 12.51, 11.26, 12.43, 10.36, 11.12]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'HIS', 12.92), ('CB', 'ARG', 'CG', 'HIS', 11.69), ('CB', 'ARG', 'ND1', 'HIS', 10.87), ('CB', 'ARG', 'CD2', 'HIS', 11.31), ('CB', 'ARG', 'CE1', 'HIS', 9.91), ('CB', 'ARG', 'NE2', 'HIS', 10.19)], [('CG', 'ARG', 'CB', 'HIS', 12.93), ('CG', 'ARG', 'CG', 'HIS', 11.61), ('CG', 'ARG', 'ND1', 'HIS', 10.69), ('CG', 'ARG', 'CD2', 'HIS', 11.19), ('CG', 'ARG', 'CE1', 'HIS', 9.63), ('CG', 'ARG', 'NE2', 'HIS', 9.96)], [('CD', 'ARG', 'CB', 'HIS', 13.24), ('CD', 'ARG', 'CG', 'HIS', 11.97), ('CD', 'ARG', 'ND1', 'HIS', 10.91), ('CD', 'ARG', 'CD2', 'HIS', 11.74), ('CD', 'ARG', 'CE1', 'HIS', 9.95), ('CD', 'ARG', 'NE2', 'HIS', 10.49)], [('NE', 'ARG', 'CB', 'HIS', 13.29), ('NE', 'ARG', 'CG', 'HIS', 11.97), ('NE', 'ARG', 'ND1', 'HIS', 10.84), ('NE', 'ARG', 'CD2', 'HIS', 11.74), ('NE', 'ARG', 'CE1', 'HIS', 9.84), ('NE', 'ARG', 'NE2', 'HIS', 10.44)], [('CZ', 'ARG', 'CB', 'HIS', 13.76), ('CZ', 'ARG', 'CG', 'HIS', 12.5), ('CZ', 'ARG', 'ND1', 'HIS', 11.28), ('CZ', 'ARG', 'CD2', 'HIS', 12.41), ('CZ', 'ARG', 'CE1', 'HIS', 10.38), ('CZ', 'ARG', 'NE2', 'HIS', 11.12)], [('NH1', 'ARG', 'CB', 'HIS', 14.59), ('NH1', 'ARG', 'CG', 'HIS', 13.4), ('NH1', 'ARG', 'ND1', 'HIS', 12.15), ('NH1', 'ARG', 'CD2', 'HIS', 13.39), ('NH1', 'ARG', 'CE1', 'HIS', 11.34), ('NH1', 'ARG', 'NE2', 'HIS', 12.14)], [('NH2', 'ARG', 'CB', 'HIS', 13.78), ('NH2', 'ARG', 'CG', 'HIS', 12.51), ('NH2', 'ARG', 'ND1', 'HIS', 11.26), ('NH2', 'ARG', 'CD2', 'HIS', 12.43), ('NH2', 'ARG', 'CE1', 'HIS', 10.36), ('NH2', 'ARG', 'NE2', 'HIS', 11.12)]]}
GLU_HIS = { 
	'distances':
		[[8.16, 8.37, 7.57, 9.56, 8.44, 9.57], [8.02, 7.86, 6.83, 8.92, 7.46, 8.68], [6.77, 6.48, 5.46, 7.47, 6.1, 7.25], [5.71, 5.5, 4.57, 6.63, 5.48, 6.6], [7.14, 6.63, 5.64, 7.4, 5.98, 7.04]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 8.16), ('CB', 'GLU', 'CG', 'HIS', 8.37), ('CB', 'GLU', 'ND1', 'HIS', 7.57), ('CB', 'GLU', 'CD2', 'HIS', 9.56), ('CB', 'GLU', 'CE1', 'HIS', 8.44), ('CB', 'GLU', 'NE2', 'HIS', 9.57)], [('CG', 'GLU', 'CB', 'HIS', 8.02), ('CG', 'GLU', 'CG', 'HIS', 7.86), ('CG', 'GLU', 'ND1', 'HIS', 6.83), ('CG', 'GLU', 'CD2', 'HIS', 8.92), ('CG', 'GLU', 'CE1', 'HIS', 7.46), ('CG', 'GLU', 'NE2', 'HIS', 8.68)], [('CD', 'GLU', 'CB', 'HIS', 6.77), ('CD', 'GLU', 'CG', 'HIS', 6.48), ('CD', 'GLU', 'ND1', 'HIS', 5.46), ('CD', 'GLU', 'CD2', 'HIS', 7.47), ('CD', 'GLU', 'CE1', 'HIS', 6.1), ('CD', 'GLU', 'NE2', 'HIS', 7.25)], [('OE1', 'GLU', 'CB', 'HIS', 5.71), ('OE1', 'GLU', 'CG', 'HIS', 5.5), ('OE1', 'GLU', 'ND1', 'HIS', 4.57), ('OE1', 'GLU', 'CD2', 'HIS', 6.63), ('OE1', 'GLU', 'CE1', 'HIS', 5.48), ('OE1', 'GLU', 'NE2', 'HIS', 6.6)], [('OE2', 'GLU', 'CB', 'HIS', 7.14), ('OE2', 'GLU', 'CG', 'HIS', 6.63), ('OE2', 'GLU', 'ND1', 'HIS', 5.64), ('OE2', 'GLU', 'CD2', 'HIS', 7.4), ('OE2', 'GLU', 'CE1', 'HIS', 5.98), ('OE2', 'GLU', 'NE2', 'HIS', 7.04)]]}
ARG_GLU = { 
	'distances':
		[[12.6, 11.28, 10.57, 11.25, 9.46], [12.66, 11.25, 10.58, 11.17, 9.59], [12.19, 10.76, 10.32, 11.03, 9.43], [12.3, 10.82, 10.44, 11.03, 9.7], [12.2, 10.74, 10.57, 11.21, 9.97], [12.44, 11.04, 11.03, 11.81, 10.41], [12.34, 10.88, 10.75, 11.26, 10.3]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'GLU', 12.6), ('CB', 'ARG', 'CG', 'GLU', 11.28), ('CB', 'ARG', 'CD', 'GLU', 10.57), ('CB', 'ARG', 'OE1', 'GLU', 11.25), ('CB', 'ARG', 'OE2', 'GLU', 9.46)], [('CG', 'ARG', 'CB', 'GLU', 12.66), ('CG', 'ARG', 'CG', 'GLU', 11.25), ('CG', 'ARG', 'CD', 'GLU', 10.58), ('CG', 'ARG', 'OE1', 'GLU', 11.17), ('CG', 'ARG', 'OE2', 'GLU', 9.59)], [('CD', 'ARG', 'CB', 'GLU', 12.19), ('CD', 'ARG', 'CG', 'GLU', 10.76), ('CD', 'ARG', 'CD', 'GLU', 10.32), ('CD', 'ARG', 'OE1', 'GLU', 11.03), ('CD', 'ARG', 'OE2', 'GLU', 9.43)], [('NE', 'ARG', 'CB', 'GLU', 12.3), ('NE', 'ARG', 'CG', 'GLU', 10.82), ('NE', 'ARG', 'CD', 'GLU', 10.44), ('NE', 'ARG', 'OE1', 'GLU', 11.03), ('NE', 'ARG', 'OE2', 'GLU', 9.7)], [('CZ', 'ARG', 'CB', 'GLU', 12.2), ('CZ', 'ARG', 'CG', 'GLU', 10.74), ('CZ', 'ARG', 'CD', 'GLU', 10.57), ('CZ', 'ARG', 'OE1', 'GLU', 11.21), ('CZ', 'ARG', 'OE2', 'GLU', 9.97)], [('NH1', 'ARG', 'CB', 'GLU', 12.44), ('NH1', 'ARG', 'CG', 'GLU', 11.04), ('NH1', 'ARG', 'CD', 'GLU', 11.03), ('NH1', 'ARG', 'OE1', 'GLU', 11.81), ('NH1', 'ARG', 'OE2', 'GLU', 10.41)], [('NH2', 'ARG', 'CB', 'GLU', 12.34), ('NH2', 'ARG', 'CG', 'GLU', 10.88), ('NH2', 'ARG', 'CD', 'GLU', 10.75), ('NH2', 'ARG', 'OE1', 'GLU', 11.26), ('NH2', 'ARG', 'OE2', 'GLU', 10.3)]]}
ARG_ASP = { 
	'distances':
		[[7.61, 6.9, 5.72, 7.8], [7.95, 7.01, 5.91, 7.67], [6.89, 5.89, 4.99, 6.43], [7.76, 6.71, 6.05, 6.94], [7.6, 6.59, 6.27, 6.56], [6.63, 5.59, 5.55, 5.36], [8.76, 7.81, 7.58, 7.65], [12.13, 12.83, 13.92, 12.41], [12.81, 13.34, 14.41, 12.78], [13.67, 14.17, 15.18, 13.67], [14.34, 14.69, 15.67, 14.09], [15.28, 15.59, 16.5, 15.0], [15.96, 16.36, 17.26, 15.87], [15.8, 15.98, 16.86, 15.32]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 7.61), ('CB', 'ARG', 'CG', 'ASP', 6.9), ('CB', 'ARG', 'OD1', 'ASP', 5.72), ('CB', 'ARG', 'OD2', 'ASP', 7.8)], [('CG', 'ARG', 'CB', 'ASP', 7.95), ('CG', 'ARG', 'CG', 'ASP', 7.01), ('CG', 'ARG', 'OD1', 'ASP', 5.91), ('CG', 'ARG', 'OD2', 'ASP', 7.67)], [('CD', 'ARG', 'CB', 'ASP', 6.89), ('CD', 'ARG', 'CG', 'ASP', 5.89), ('CD', 'ARG', 'OD1', 'ASP', 4.99), ('CD', 'ARG', 'OD2', 'ASP', 6.43)], [('NE', 'ARG', 'CB', 'ASP', 7.76), ('NE', 'ARG', 'CG', 'ASP', 6.71), ('NE', 'ARG', 'OD1', 'ASP', 6.05), ('NE', 'ARG', 'OD2', 'ASP', 6.94)], [('CZ', 'ARG', 'CB', 'ASP', 7.6), ('CZ', 'ARG', 'CG', 'ASP', 6.59), ('CZ', 'ARG', 'OD1', 'ASP', 6.27), ('CZ', 'ARG', 'OD2', 'ASP', 6.56)], [('NH1', 'ARG', 'CB', 'ASP', 6.63), ('NH1', 'ARG', 'CG', 'ASP', 5.59), ('NH1', 'ARG', 'OD1', 'ASP', 5.55), ('NH1', 'ARG', 'OD2', 'ASP', 5.36)], [('NH2', 'ARG', 'CB', 'ASP', 8.76), ('NH2', 'ARG', 'CG', 'ASP', 7.81), ('NH2', 'ARG', 'OD1', 'ASP', 7.58), ('NH2', 'ARG', 'OD2', 'ASP', 7.65)], [('CB', 'ARG', 'CB', 'ASP', 12.13), ('CB', 'ARG', 'CG', 'ASP', 12.83), ('CB', 'ARG', 'OD1', 'ASP', 13.92), ('CB', 'ARG', 'OD2', 'ASP', 12.41)], [('CG', 'ARG', 'CB', 'ASP', 12.81), ('CG', 'ARG', 'CG', 'ASP', 13.34), ('CG', 'ARG', 'OD1', 'ASP', 14.41), ('CG', 'ARG', 'OD2', 'ASP', 12.78)], [('CD', 'ARG', 'CB', 'ASP', 13.67), ('CD', 'ARG', 'CG', 'ASP', 14.17), ('CD', 'ARG', 'OD1', 'ASP', 15.18), ('CD', 'ARG', 'OD2', 'ASP', 13.67)], [('NE', 'ARG', 'CB', 'ASP', 14.34), ('NE', 'ARG', 'CG', 'ASP', 14.69), ('NE', 'ARG', 'OD1', 'ASP', 15.67), ('NE', 'ARG', 'OD2', 'ASP', 14.09)], [('CZ', 'ARG', 'CB', 'ASP', 15.28), ('CZ', 'ARG', 'CG', 'ASP', 15.59), ('CZ', 'ARG', 'OD1', 'ASP', 16.5), ('CZ', 'ARG', 'OD2', 'ASP', 15.0)], [('NH1', 'ARG', 'CB', 'ASP', 15.96), ('NH1', 'ARG', 'CG', 'ASP', 16.36), ('NH1', 'ARG', 'OD1', 'ASP', 17.26), ('NH1', 'ARG', 'OD2', 'ASP', 15.87)], [('NH2', 'ARG', 'CB', 'ASP', 15.8), ('NH2', 'ARG', 'CG', 'ASP', 15.98), ('NH2', 'ARG', 'OD1', 'ASP', 16.86), ('NH2', 'ARG', 'OD2', 'ASP', 15.32)]]}
ASP_GLU = { 
	'distances':
		[[12.09, 11.02, 11.21, 12.33, 10.36], [12.86, 11.66, 11.72, 12.75, 10.85], [12.96, 11.7, 11.56, 12.53, 10.61], [13.57, 12.35, 12.51, 13.52, 11.72], [11.79, 11.53, 10.16, 9.9, 9.57], [11.78, 11.56, 10.15, 9.67, 9.74], [11.83, 11.79, 10.44, 9.88, 10.18], [11.9, 11.53, 10.06, 9.5, 9.65]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 12.09), ('CB', 'ASP', 'CG', 'GLU', 11.02), ('CB', 'ASP', 'CD', 'GLU', 11.21), ('CB', 'ASP', 'OE1', 'GLU', 12.33), ('CB', 'ASP', 'OE2', 'GLU', 10.36)], [('CG', 'ASP', 'CB', 'GLU', 12.86), ('CG', 'ASP', 'CG', 'GLU', 11.66), ('CG', 'ASP', 'CD', 'GLU', 11.72), ('CG', 'ASP', 'OE1', 'GLU', 12.75), ('CG', 'ASP', 'OE2', 'GLU', 10.85)], [('OD1', 'ASP', 'CB', 'GLU', 12.96), ('OD1', 'ASP', 'CG', 'GLU', 11.7), ('OD1', 'ASP', 'CD', 'GLU', 11.56), ('OD1', 'ASP', 'OE1', 'GLU', 12.53), ('OD1', 'ASP', 'OE2', 'GLU', 10.61)], [('OD2', 'ASP', 'CB', 'GLU', 13.57), ('OD2', 'ASP', 'CG', 'GLU', 12.35), ('OD2', 'ASP', 'CD', 'GLU', 12.51), ('OD2', 'ASP', 'OE1', 'GLU', 13.52), ('OD2', 'ASP', 'OE2', 'GLU', 11.72)], [('CB', 'ASP', 'CB', 'GLU', 11.79), ('CB', 'ASP', 'CG', 'GLU', 11.53), ('CB', 'ASP', 'CD', 'GLU', 10.16), ('CB', 'ASP', 'OE1', 'GLU', 9.9), ('CB', 'ASP', 'OE2', 'GLU', 9.57)], [('CG', 'ASP', 'CB', 'GLU', 11.78), ('CG', 'ASP', 'CG', 'GLU', 11.56), ('CG', 'ASP', 'CD', 'GLU', 10.15), ('CG', 'ASP', 'OE1', 'GLU', 9.67), ('CG', 'ASP', 'OE2', 'GLU', 9.74)], [('OD1', 'ASP', 'CB', 'GLU', 11.83), ('OD1', 'ASP', 'CG', 'GLU', 11.79), ('OD1', 'ASP', 'CD', 'GLU', 10.44), ('OD1', 'ASP', 'OE1', 'GLU', 9.88), ('OD1', 'ASP', 'OE2', 'GLU', 10.18)], [('OD2', 'ASP', 'CB', 'GLU', 11.9), ('OD2', 'ASP', 'CG', 'GLU', 11.53), ('OD2', 'ASP', 'CD', 'GLU', 10.06), ('OD2', 'ASP', 'OE1', 'GLU', 9.5), ('OD2', 'ASP', 'OE2', 'GLU', 9.65)]]}
HIS_ASPI = { 
	'distances':
		[[7.99, 7.14, 7.07, 6.87], [7.97, 7.23, 7.5, 6.69], [8.78, 8.27, 8.65, 7.74], [7.63, 6.84, 7.33, 6.02], [8.94, 8.51, 9.1, 7.81], [8.29, 7.73, 8.4, 6.86]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASPI', 7.99), ('CB', 'HIS', 'CG', 'ASPI', 7.14), ('CB', 'HIS', 'OD1', 'ASPI', 7.07), ('CB', 'HIS', 'OD2', 'ASPI', 6.87)], [('CG', 'HIS', 'CB', 'ASPI', 7.97), ('CG', 'HIS', 'CG', 'ASPI', 7.23), ('CG', 'HIS', 'OD1', 'ASPI', 7.5), ('CG', 'HIS', 'OD2', 'ASPI', 6.69)], [('ND1', 'HIS', 'CB', 'ASPI', 8.78), ('ND1', 'HIS', 'CG', 'ASPI', 8.27), ('ND1', 'HIS', 'OD1', 'ASPI', 8.65), ('ND1', 'HIS', 'OD2', 'ASPI', 7.74)], [('CD2', 'HIS', 'CB', 'ASPI', 7.63), ('CD2', 'HIS', 'CG', 'ASPI', 6.84), ('CD2', 'HIS', 'OD1', 'ASPI', 7.33), ('CD2', 'HIS', 'OD2', 'ASPI', 6.02)], [('CE1', 'HIS', 'CB', 'ASPI', 8.94), ('CE1', 'HIS', 'CG', 'ASPI', 8.51), ('CE1', 'HIS', 'OD1', 'ASPI', 9.1), ('CE1', 'HIS', 'OD2', 'ASPI', 7.81)], [('NE2', 'HIS', 'CB', 'ASPI', 8.29), ('NE2', 'HIS', 'CG', 'ASPI', 7.73), ('NE2', 'HIS', 'OD1', 'ASPI', 8.4), ('NE2', 'HIS', 'OD2', 'ASPI', 6.86)]]}
ASP_ASP = { 
	'distances':
		[[15.5, 16.3, 17.13, 16.19], [15.78, 16.53, 17.44, 16.3], [15.02, 15.77, 16.74, 15.49], [16.92, 17.61, 18.52, 17.33], [15.5, 15.78, 15.02, 16.92], [16.3, 16.53, 15.77, 17.61], [17.13, 17.44, 16.74, 18.52], [16.19, 16.3, 15.49, 17.33]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 15.5), ('CB', 'ASP', 'CG', 'ASP', 16.3), ('CB', 'ASP', 'OD1', 'ASP', 17.13), ('CB', 'ASP', 'OD2', 'ASP', 16.19)], [('CG', 'ASP', 'CB', 'ASP', 15.78), ('CG', 'ASP', 'CG', 'ASP', 16.53), ('CG', 'ASP', 'OD1', 'ASP', 17.44), ('CG', 'ASP', 'OD2', 'ASP', 16.3)], [('OD1', 'ASP', 'CB', 'ASP', 15.02), ('OD1', 'ASP', 'CG', 'ASP', 15.77), ('OD1', 'ASP', 'OD1', 'ASP', 16.74), ('OD1', 'ASP', 'OD2', 'ASP', 15.49)], [('OD2', 'ASP', 'CB', 'ASP', 16.92), ('OD2', 'ASP', 'CG', 'ASP', 17.61), ('OD2', 'ASP', 'OD1', 'ASP', 18.52), ('OD2', 'ASP', 'OD2', 'ASP', 17.33)], [('CB', 'ASP', 'CB', 'ASP', 15.5), ('CB', 'ASP', 'CG', 'ASP', 15.78), ('CB', 'ASP', 'OD1', 'ASP', 15.02), ('CB', 'ASP', 'OD2', 'ASP', 16.92)], [('CG', 'ASP', 'CB', 'ASP', 16.3), ('CG', 'ASP', 'CG', 'ASP', 16.53), ('CG', 'ASP', 'OD1', 'ASP', 15.77), ('CG', 'ASP', 'OD2', 'ASP', 17.61)], [('OD1', 'ASP', 'CB', 'ASP', 17.13), ('OD1', 'ASP', 'CG', 'ASP', 17.44), ('OD1', 'ASP', 'OD1', 'ASP', 16.74), ('OD1', 'ASP', 'OD2', 'ASP', 18.52)], [('OD2', 'ASP', 'CB', 'ASP', 16.19), ('OD2', 'ASP', 'CG', 'ASP', 16.3), ('OD2', 'ASP', 'OD1', 'ASP', 15.49), ('OD2', 'ASP', 'OD2', 'ASP', 17.33)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HIS, d, 'A_1gdh_1_1_1_29')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_HIS, d, 'A_1gdh_1_1_1_29')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_HIS, d, 'A_1gdh_1_1_1_29')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ARG_GLU, d, 'A_1gdh_1_1_1_29')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ARG_ASP, d, 'A_1gdh_1_1_1_29')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ASP_GLU, d, 'A_1gdh_1_1_1_29')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(HIS_ASPI, d, 'A_1gdh_1_1_1_29')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ASP_ASP, d, 'A_1gdh_1_1_1_29')
	if match8 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HIS' :  match1,
		'ARG_HIS' :  match2,
		'GLU_HIS' :  match3,
		'ARG_GLU' :  match4,
		'ARG_ASP' :  match5,
		'ASP_GLU' :  match6,
		'HIS_ASPI' :  match7,
		'ASP_ASP' :  match8}