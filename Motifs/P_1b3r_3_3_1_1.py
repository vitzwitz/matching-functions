'''
FUNC:P_1b3r_3_3_1_1
PDB:1b3r
EC:3.3.1.1
RESI:his,asp,lys,asp,asn,cys,his
LOCI:a-54,130,185,189,190,194,300;
'''
import motifFunctions as cmd
LYS_HIS = { 
	'distances':
		[[16.74, 16.21, 14.88, 16.94, 14.87, 16.14, 16.98, 17.8, 17.43, 16.66], [15.28, 14.72, 13.39, 15.44, 13.37, 14.64, 15.59, 16.37, 15.96, 15.18], [15.05, 14.35, 12.99, 14.96, 12.82, 14.05, 15.66, 16.36, 15.82, 15.06], [13.65, 12.91, 11.54, 13.48, 11.34, 12.56, 14.4, 15.04, 14.43, 13.68], [13.71, 12.82, 11.44, 13.25, 11.07, 12.22, 14.79, 15.31, 14.58, 13.89], [19.75, 20.04, 19.73, 20.75, 20.26, 20.87, 21.48, 20.37, 19.26, 19.1], [18.95, 19.16, 18.88, 19.8, 19.35, 19.9, 20.6, 19.47, 18.41, 18.34], [17.49, 17.73, 17.45, 18.39, 17.95, 18.51, 19.18, 18.05, 16.97, 16.89], [16.72, 16.88, 16.63, 17.45, 17.06, 17.55, 18.31, 17.15, 16.15, 16.17], [15.24, 15.43, 15.21, 16.04, 15.68, 16.18, 16.86, 15.71, 14.68, 14.68]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'HIS', 16.74), ('CB', 'LYS', 'CG', 'HIS', 16.21), ('CB', 'LYS', 'ND1', 'HIS', 14.88), ('CB', 'LYS', 'CD2', 'HIS', 16.94), ('CB', 'LYS', 'CE1', 'HIS', 14.87), ('CB', 'LYS', 'NE2', 'HIS', 16.14), ('CB', 'LYS', 'O', 'HIS', 16.98), ('CB', 'LYS', 'C', 'HIS', 17.8), ('CB', 'LYS', 'CA', 'HIS', 17.43), ('CB', 'LYS', 'N', 'HIS', 16.66)], [('CG', 'LYS', 'CB', 'HIS', 15.28), ('CG', 'LYS', 'CG', 'HIS', 14.72), ('CG', 'LYS', 'ND1', 'HIS', 13.39), ('CG', 'LYS', 'CD2', 'HIS', 15.44), ('CG', 'LYS', 'CE1', 'HIS', 13.37), ('CG', 'LYS', 'NE2', 'HIS', 14.64), ('CG', 'LYS', 'O', 'HIS', 15.59), ('CG', 'LYS', 'C', 'HIS', 16.37), ('CG', 'LYS', 'CA', 'HIS', 15.96), ('CG', 'LYS', 'N', 'HIS', 15.18)], [('CD', 'LYS', 'CB', 'HIS', 15.05), ('CD', 'LYS', 'CG', 'HIS', 14.35), ('CD', 'LYS', 'ND1', 'HIS', 12.99), ('CD', 'LYS', 'CD2', 'HIS', 14.96), ('CD', 'LYS', 'CE1', 'HIS', 12.82), ('CD', 'LYS', 'NE2', 'HIS', 14.05), ('CD', 'LYS', 'O', 'HIS', 15.66), ('CD', 'LYS', 'C', 'HIS', 16.36), ('CD', 'LYS', 'CA', 'HIS', 15.82), ('CD', 'LYS', 'N', 'HIS', 15.06)], [('CE', 'LYS', 'CB', 'HIS', 13.65), ('CE', 'LYS', 'CG', 'HIS', 12.91), ('CE', 'LYS', 'ND1', 'HIS', 11.54), ('CE', 'LYS', 'CD2', 'HIS', 13.48), ('CE', 'LYS', 'CE1', 'HIS', 11.34), ('CE', 'LYS', 'NE2', 'HIS', 12.56), ('CE', 'LYS', 'O', 'HIS', 14.4), ('CE', 'LYS', 'C', 'HIS', 15.04), ('CE', 'LYS', 'CA', 'HIS', 14.43), ('CE', 'LYS', 'N', 'HIS', 13.68)], [('NZ', 'LYS', 'CB', 'HIS', 13.71), ('NZ', 'LYS', 'CG', 'HIS', 12.82), ('NZ', 'LYS', 'ND1', 'HIS', 11.44), ('NZ', 'LYS', 'CD2', 'HIS', 13.25), ('NZ', 'LYS', 'CE1', 'HIS', 11.07), ('NZ', 'LYS', 'NE2', 'HIS', 12.22), ('NZ', 'LYS', 'O', 'HIS', 14.79), ('NZ', 'LYS', 'C', 'HIS', 15.31), ('NZ', 'LYS', 'CA', 'HIS', 14.58), ('NZ', 'LYS', 'N', 'HIS', 13.89)], [('CB', 'LYS', 'CB', 'HIS', 19.75), ('CB', 'LYS', 'CG', 'HIS', 20.04), ('CB', 'LYS', 'ND1', 'HIS', 19.73), ('CB', 'LYS', 'CD2', 'HIS', 20.75), ('CB', 'LYS', 'CE1', 'HIS', 20.26), ('CB', 'LYS', 'NE2', 'HIS', 20.87), ('CB', 'LYS', 'O', 'HIS', 21.48), ('CB', 'LYS', 'C', 'HIS', 20.37), ('CB', 'LYS', 'CA', 'HIS', 19.26), ('CB', 'LYS', 'N', 'HIS', 19.1)], [('CG', 'LYS', 'CB', 'HIS', 18.95), ('CG', 'LYS', 'CG', 'HIS', 19.16), ('CG', 'LYS', 'ND1', 'HIS', 18.88), ('CG', 'LYS', 'CD2', 'HIS', 19.8), ('CG', 'LYS', 'CE1', 'HIS', 19.35), ('CG', 'LYS', 'NE2', 'HIS', 19.9), ('CG', 'LYS', 'O', 'HIS', 20.6), ('CG', 'LYS', 'C', 'HIS', 19.47), ('CG', 'LYS', 'CA', 'HIS', 18.41), ('CG', 'LYS', 'N', 'HIS', 18.34)], [('CD', 'LYS', 'CB', 'HIS', 17.49), ('CD', 'LYS', 'CG', 'HIS', 17.73), ('CD', 'LYS', 'ND1', 'HIS', 17.45), ('CD', 'LYS', 'CD2', 'HIS', 18.39), ('CD', 'LYS', 'CE1', 'HIS', 17.95), ('CD', 'LYS', 'NE2', 'HIS', 18.51), ('CD', 'LYS', 'O', 'HIS', 19.18), ('CD', 'LYS', 'C', 'HIS', 18.05), ('CD', 'LYS', 'CA', 'HIS', 16.97), ('CD', 'LYS', 'N', 'HIS', 16.89)], [('CE', 'LYS', 'CB', 'HIS', 16.72), ('CE', 'LYS', 'CG', 'HIS', 16.88), ('CE', 'LYS', 'ND1', 'HIS', 16.63), ('CE', 'LYS', 'CD2', 'HIS', 17.45), ('CE', 'LYS', 'CE1', 'HIS', 17.06), ('CE', 'LYS', 'NE2', 'HIS', 17.55), ('CE', 'LYS', 'O', 'HIS', 18.31), ('CE', 'LYS', 'C', 'HIS', 17.15), ('CE', 'LYS', 'CA', 'HIS', 16.15), ('CE', 'LYS', 'N', 'HIS', 16.17)], [('NZ', 'LYS', 'CB', 'HIS', 15.24), ('NZ', 'LYS', 'CG', 'HIS', 15.43), ('NZ', 'LYS', 'ND1', 'HIS', 15.21), ('NZ', 'LYS', 'CD2', 'HIS', 16.04), ('NZ', 'LYS', 'CE1', 'HIS', 15.68), ('NZ', 'LYS', 'NE2', 'HIS', 16.18), ('NZ', 'LYS', 'O', 'HIS', 16.86), ('NZ', 'LYS', 'C', 'HIS', 15.71), ('NZ', 'LYS', 'CA', 'HIS', 14.68), ('NZ', 'LYS', 'N', 'HIS', 14.68)]]}
LYS_CYS = { 
	'distances':
		[[15.61, 14.54], [15.35, 14.16], [14.34, 13.06], [14.2, 12.79], [13.25, 11.75]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'CYS', 15.61), ('CB', 'LYS', 'SG', 'CYS', 14.54)], [('CG', 'LYS', 'CB', 'CYS', 15.35), ('CG', 'LYS', 'SG', 'CYS', 14.16)], [('CD', 'LYS', 'CB', 'CYS', 14.34), ('CD', 'LYS', 'SG', 'CYS', 13.06)], [('CE', 'LYS', 'CB', 'CYS', 14.2), ('CE', 'LYS', 'SG', 'CYS', 12.79)], [('NZ', 'LYS', 'CB', 'CYS', 13.25), ('NZ', 'LYS', 'SG', 'CYS', 11.75)]]}
ASP_HIS = { 
	'distances':
		[[8.47, 7.76, 6.98, 8.08, 6.87, 7.55, 9.07, 9.23, 8.33, 7.01], [7.99, 7.09, 6.07, 7.4, 5.8, 6.66, 9.04, 9.2, 8.2, 7.07], [8.15, 7.01, 6.03, 7.04, 5.39, 6.1, 9.62, 9.62, 8.45, 7.44], [7.81, 7.03, 5.86, 7.57, 5.8, 6.9, 8.72, 9.05, 8.19, 7.18], [18.23, 17.72, 17.45, 17.6, 17.19, 17.28, 19.3, 18.09, 17.68, 18.38], [17.01, 16.58, 16.38, 16.5, 16.2, 16.27, 18.02, 16.81, 16.39, 17.04], [15.94, 15.45, 15.26, 15.33, 15.04, 15.08, 16.92, 15.72, 15.34, 16.05], [17.21, 16.89, 16.76, 16.89, 16.68, 16.75, 18.18, 16.97, 16.52, 17.06], [14.43, 13.73, 12.44, 14.29, 12.26, 13.43, 15.51, 16.12, 15.58, 15.25], [13.2, 12.43, 11.15, 12.92, 10.9, 12.03, 14.5, 15.02, 14.4, 14.1], [12.6, 11.9, 10.68, 12.41, 10.51, 11.6, 13.95, 14.45, 13.88, 13.71], [12.98, 12.09, 10.77, 12.49, 10.39, 11.49, 14.39, 14.85, 14.12, 13.73], [15.77, 16.32, 16.41, 17.0, 17.11, 17.46, 16.91, 15.88, 14.93, 14.57], [14.82, 15.31, 15.44, 15.9, 16.08, 16.36, 15.84, 14.79, 13.92, 13.65], [14.95, 15.46, 15.71, 15.98, 16.34, 16.51, 15.71, 14.68, 13.93, 13.64], [14.09, 14.48, 14.53, 15.06, 15.12, 15.44, 15.27, 14.17, 13.27, 13.11]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 8.47), ('CB', 'ASP', 'CG', 'HIS', 7.76), ('CB', 'ASP', 'ND1', 'HIS', 6.98), ('CB', 'ASP', 'CD2', 'HIS', 8.08), ('CB', 'ASP', 'CE1', 'HIS', 6.87), ('CB', 'ASP', 'NE2', 'HIS', 7.55), ('CB', 'ASP', 'O', 'HIS', 9.07), ('CB', 'ASP', 'C', 'HIS', 9.23), ('CB', 'ASP', 'CA', 'HIS', 8.33), ('CB', 'ASP', 'N', 'HIS', 7.01)], [('CG', 'ASP', 'CB', 'HIS', 7.99), ('CG', 'ASP', 'CG', 'HIS', 7.09), ('CG', 'ASP', 'ND1', 'HIS', 6.07), ('CG', 'ASP', 'CD2', 'HIS', 7.4), ('CG', 'ASP', 'CE1', 'HIS', 5.8), ('CG', 'ASP', 'NE2', 'HIS', 6.66), ('CG', 'ASP', 'O', 'HIS', 9.04), ('CG', 'ASP', 'C', 'HIS', 9.2), ('CG', 'ASP', 'CA', 'HIS', 8.2), ('CG', 'ASP', 'N', 'HIS', 7.07)], [('OD1', 'ASP', 'CB', 'HIS', 8.15), ('OD1', 'ASP', 'CG', 'HIS', 7.01), ('OD1', 'ASP', 'ND1', 'HIS', 6.03), ('OD1', 'ASP', 'CD2', 'HIS', 7.04), ('OD1', 'ASP', 'CE1', 'HIS', 5.39), ('OD1', 'ASP', 'NE2', 'HIS', 6.1), ('OD1', 'ASP', 'O', 'HIS', 9.62), ('OD1', 'ASP', 'C', 'HIS', 9.62), ('OD1', 'ASP', 'CA', 'HIS', 8.45), ('OD1', 'ASP', 'N', 'HIS', 7.44)], [('OD2', 'ASP', 'CB', 'HIS', 7.81), ('OD2', 'ASP', 'CG', 'HIS', 7.03), ('OD2', 'ASP', 'ND1', 'HIS', 5.86), ('OD2', 'ASP', 'CD2', 'HIS', 7.57), ('OD2', 'ASP', 'CE1', 'HIS', 5.8), ('OD2', 'ASP', 'NE2', 'HIS', 6.9), ('OD2', 'ASP', 'O', 'HIS', 8.72), ('OD2', 'ASP', 'C', 'HIS', 9.05), ('OD2', 'ASP', 'CA', 'HIS', 8.19), ('OD2', 'ASP', 'N', 'HIS', 7.18)], [('CB', 'ASP', 'CB', 'HIS', 18.23), ('CB', 'ASP', 'CG', 'HIS', 17.72), ('CB', 'ASP', 'ND1', 'HIS', 17.45), ('CB', 'ASP', 'CD2', 'HIS', 17.6), ('CB', 'ASP', 'CE1', 'HIS', 17.19), ('CB', 'ASP', 'NE2', 'HIS', 17.28), ('CB', 'ASP', 'O', 'HIS', 19.3), ('CB', 'ASP', 'C', 'HIS', 18.09), ('CB', 'ASP', 'CA', 'HIS', 17.68), ('CB', 'ASP', 'N', 'HIS', 18.38)], [('CG', 'ASP', 'CB', 'HIS', 17.01), ('CG', 'ASP', 'CG', 'HIS', 16.58), ('CG', 'ASP', 'ND1', 'HIS', 16.38), ('CG', 'ASP', 'CD2', 'HIS', 16.5), ('CG', 'ASP', 'CE1', 'HIS', 16.2), ('CG', 'ASP', 'NE2', 'HIS', 16.27), ('CG', 'ASP', 'O', 'HIS', 18.02), ('CG', 'ASP', 'C', 'HIS', 16.81), ('CG', 'ASP', 'CA', 'HIS', 16.39), ('CG', 'ASP', 'N', 'HIS', 17.04)], [('OD1', 'ASP', 'CB', 'HIS', 15.94), ('OD1', 'ASP', 'CG', 'HIS', 15.45), ('OD1', 'ASP', 'ND1', 'HIS', 15.26), ('OD1', 'ASP', 'CD2', 'HIS', 15.33), ('OD1', 'ASP', 'CE1', 'HIS', 15.04), ('OD1', 'ASP', 'NE2', 'HIS', 15.08), ('OD1', 'ASP', 'O', 'HIS', 16.92), ('OD1', 'ASP', 'C', 'HIS', 15.72), ('OD1', 'ASP', 'CA', 'HIS', 15.34), ('OD1', 'ASP', 'N', 'HIS', 16.05)], [('OD2', 'ASP', 'CB', 'HIS', 17.21), ('OD2', 'ASP', 'CG', 'HIS', 16.89), ('OD2', 'ASP', 'ND1', 'HIS', 16.76), ('OD2', 'ASP', 'CD2', 'HIS', 16.89), ('OD2', 'ASP', 'CE1', 'HIS', 16.68), ('OD2', 'ASP', 'NE2', 'HIS', 16.75), ('OD2', 'ASP', 'O', 'HIS', 18.18), ('OD2', 'ASP', 'C', 'HIS', 16.97), ('OD2', 'ASP', 'CA', 'HIS', 16.52), ('OD2', 'ASP', 'N', 'HIS', 17.06)], [('CB', 'ASP', 'CB', 'HIS', 14.43), ('CB', 'ASP', 'CG', 'HIS', 13.73), ('CB', 'ASP', 'ND1', 'HIS', 12.44), ('CB', 'ASP', 'CD2', 'HIS', 14.29), ('CB', 'ASP', 'CE1', 'HIS', 12.26), ('CB', 'ASP', 'NE2', 'HIS', 13.43), ('CB', 'ASP', 'O', 'HIS', 15.51), ('CB', 'ASP', 'C', 'HIS', 16.12), ('CB', 'ASP', 'CA', 'HIS', 15.58), ('CB', 'ASP', 'N', 'HIS', 15.25)], [('CG', 'ASP', 'CB', 'HIS', 13.2), ('CG', 'ASP', 'CG', 'HIS', 12.43), ('CG', 'ASP', 'ND1', 'HIS', 11.15), ('CG', 'ASP', 'CD2', 'HIS', 12.92), ('CG', 'ASP', 'CE1', 'HIS', 10.9), ('CG', 'ASP', 'NE2', 'HIS', 12.03), ('CG', 'ASP', 'O', 'HIS', 14.5), ('CG', 'ASP', 'C', 'HIS', 15.02), ('CG', 'ASP', 'CA', 'HIS', 14.4), ('CG', 'ASP', 'N', 'HIS', 14.1)], [('OD1', 'ASP', 'CB', 'HIS', 12.6), ('OD1', 'ASP', 'CG', 'HIS', 11.9), ('OD1', 'ASP', 'ND1', 'HIS', 10.68), ('OD1', 'ASP', 'CD2', 'HIS', 12.41), ('OD1', 'ASP', 'CE1', 'HIS', 10.51), ('OD1', 'ASP', 'NE2', 'HIS', 11.6), ('OD1', 'ASP', 'O', 'HIS', 13.95), ('OD1', 'ASP', 'C', 'HIS', 14.45), ('OD1', 'ASP', 'CA', 'HIS', 13.88), ('OD1', 'ASP', 'N', 'HIS', 13.71)], [('OD2', 'ASP', 'CB', 'HIS', 12.98), ('OD2', 'ASP', 'CG', 'HIS', 12.09), ('OD2', 'ASP', 'ND1', 'HIS', 10.77), ('OD2', 'ASP', 'CD2', 'HIS', 12.49), ('OD2', 'ASP', 'CE1', 'HIS', 10.39), ('OD2', 'ASP', 'NE2', 'HIS', 11.49), ('OD2', 'ASP', 'O', 'HIS', 14.39), ('OD2', 'ASP', 'C', 'HIS', 14.85), ('OD2', 'ASP', 'CA', 'HIS', 14.12), ('OD2', 'ASP', 'N', 'HIS', 13.73)], [('CB', 'ASP', 'CB', 'HIS', 15.77), ('CB', 'ASP', 'CG', 'HIS', 16.32), ('CB', 'ASP', 'ND1', 'HIS', 16.41), ('CB', 'ASP', 'CD2', 'HIS', 17.0), ('CB', 'ASP', 'CE1', 'HIS', 17.11), ('CB', 'ASP', 'NE2', 'HIS', 17.46), ('CB', 'ASP', 'O', 'HIS', 16.91), ('CB', 'ASP', 'C', 'HIS', 15.88), ('CB', 'ASP', 'CA', 'HIS', 14.93), ('CB', 'ASP', 'N', 'HIS', 14.57)], [('CG', 'ASP', 'CB', 'HIS', 14.82), ('CG', 'ASP', 'CG', 'HIS', 15.31), ('CG', 'ASP', 'ND1', 'HIS', 15.44), ('CG', 'ASP', 'CD2', 'HIS', 15.9), ('CG', 'ASP', 'CE1', 'HIS', 16.08), ('CG', 'ASP', 'NE2', 'HIS', 16.36), ('CG', 'ASP', 'O', 'HIS', 15.84), ('CG', 'ASP', 'C', 'HIS', 14.79), ('CG', 'ASP', 'CA', 'HIS', 13.92), ('CG', 'ASP', 'N', 'HIS', 13.65)], [('OD1', 'ASP', 'CB', 'HIS', 14.95), ('OD1', 'ASP', 'CG', 'HIS', 15.46), ('OD1', 'ASP', 'ND1', 'HIS', 15.71), ('OD1', 'ASP', 'CD2', 'HIS', 15.98), ('OD1', 'ASP', 'CE1', 'HIS', 16.34), ('OD1', 'ASP', 'NE2', 'HIS', 16.51), ('OD1', 'ASP', 'O', 'HIS', 15.71), ('OD1', 'ASP', 'C', 'HIS', 14.68), ('OD1', 'ASP', 'CA', 'HIS', 13.93), ('OD1', 'ASP', 'N', 'HIS', 13.64)], [('OD2', 'ASP', 'CB', 'HIS', 14.09), ('OD2', 'ASP', 'CG', 'HIS', 14.48), ('OD2', 'ASP', 'ND1', 'HIS', 14.53), ('OD2', 'ASP', 'CD2', 'HIS', 15.06), ('OD2', 'ASP', 'CE1', 'HIS', 15.12), ('OD2', 'ASP', 'NE2', 'HIS', 15.44), ('OD2', 'ASP', 'O', 'HIS', 15.27), ('OD2', 'ASP', 'C', 'HIS', 14.17), ('OD2', 'ASP', 'CA', 'HIS', 13.27), ('OD2', 'ASP', 'N', 'HIS', 13.11)]]}
HIS_ASPI = { 
	'distances':
		[[14.43, 13.2, 12.6, 12.98], [13.73, 12.43, 11.9, 12.09], [12.44, 11.15, 10.68, 10.77], [14.29, 12.92, 12.41, 12.49], [12.26, 10.9, 10.51, 10.39], [13.43, 12.03, 11.6, 11.49], [15.51, 14.5, 13.95, 14.39], [16.12, 15.02, 14.45, 14.85], [15.58, 14.4, 13.88, 14.12], [15.25, 14.1, 13.71, 13.73], [15.77, 14.82, 14.95, 14.09], [16.32, 15.31, 15.46, 14.48], [16.41, 15.44, 15.71, 14.53], [17.0, 15.9, 15.98, 15.06], [17.11, 16.08, 16.34, 15.12], [17.46, 16.36, 16.51, 15.44], [16.91, 15.84, 15.71, 15.27], [15.88, 14.79, 14.68, 14.17], [14.93, 13.92, 13.93, 13.27], [14.57, 13.65, 13.64, 13.11]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASPI', 14.43), ('CB', 'HIS', 'CG', 'ASPI', 13.2), ('CB', 'HIS', 'OD1', 'ASPI', 12.6), ('CB', 'HIS', 'OD2', 'ASPI', 12.98)], [('CG', 'HIS', 'CB', 'ASPI', 13.73), ('CG', 'HIS', 'CG', 'ASPI', 12.43), ('CG', 'HIS', 'OD1', 'ASPI', 11.9), ('CG', 'HIS', 'OD2', 'ASPI', 12.09)], [('ND1', 'HIS', 'CB', 'ASPI', 12.44), ('ND1', 'HIS', 'CG', 'ASPI', 11.15), ('ND1', 'HIS', 'OD1', 'ASPI', 10.68), ('ND1', 'HIS', 'OD2', 'ASPI', 10.77)], [('CD2', 'HIS', 'CB', 'ASPI', 14.29), ('CD2', 'HIS', 'CG', 'ASPI', 12.92), ('CD2', 'HIS', 'OD1', 'ASPI', 12.41), ('CD2', 'HIS', 'OD2', 'ASPI', 12.49)], [('CE1', 'HIS', 'CB', 'ASPI', 12.26), ('CE1', 'HIS', 'CG', 'ASPI', 10.9), ('CE1', 'HIS', 'OD1', 'ASPI', 10.51), ('CE1', 'HIS', 'OD2', 'ASPI', 10.39)], [('NE2', 'HIS', 'CB', 'ASPI', 13.43), ('NE2', 'HIS', 'CG', 'ASPI', 12.03), ('NE2', 'HIS', 'OD1', 'ASPI', 11.6), ('NE2', 'HIS', 'OD2', 'ASPI', 11.49)], [('O', 'HIS', 'CB', 'ASPI', 15.51), ('O', 'HIS', 'CG', 'ASPI', 14.5), ('O', 'HIS', 'OD1', 'ASPI', 13.95), ('O', 'HIS', 'OD2', 'ASPI', 14.39)], [('C', 'HIS', 'CB', 'ASPI', 16.12), ('C', 'HIS', 'CG', 'ASPI', 15.02), ('C', 'HIS', 'OD1', 'ASPI', 14.45), ('C', 'HIS', 'OD2', 'ASPI', 14.85)], [('CA', 'HIS', 'CB', 'ASPI', 15.58), ('CA', 'HIS', 'CG', 'ASPI', 14.4), ('CA', 'HIS', 'OD1', 'ASPI', 13.88), ('CA', 'HIS', 'OD2', 'ASPI', 14.12)], [('N', 'HIS', 'CB', 'ASPI', 15.25), ('N', 'HIS', 'CG', 'ASPI', 14.1), ('N', 'HIS', 'OD1', 'ASPI', 13.71), ('N', 'HIS', 'OD2', 'ASPI', 13.73)], [('CB', 'HIS', 'CB', 'ASPI', 15.77), ('CB', 'HIS', 'CG', 'ASPI', 14.82), ('CB', 'HIS', 'OD1', 'ASPI', 14.95), ('CB', 'HIS', 'OD2', 'ASPI', 14.09)], [('CG', 'HIS', 'CB', 'ASPI', 16.32), ('CG', 'HIS', 'CG', 'ASPI', 15.31), ('CG', 'HIS', 'OD1', 'ASPI', 15.46), ('CG', 'HIS', 'OD2', 'ASPI', 14.48)], [('ND1', 'HIS', 'CB', 'ASPI', 16.41), ('ND1', 'HIS', 'CG', 'ASPI', 15.44), ('ND1', 'HIS', 'OD1', 'ASPI', 15.71), ('ND1', 'HIS', 'OD2', 'ASPI', 14.53)], [('CD2', 'HIS', 'CB', 'ASPI', 17.0), ('CD2', 'HIS', 'CG', 'ASPI', 15.9), ('CD2', 'HIS', 'OD1', 'ASPI', 15.98), ('CD2', 'HIS', 'OD2', 'ASPI', 15.06)], [('CE1', 'HIS', 'CB', 'ASPI', 17.11), ('CE1', 'HIS', 'CG', 'ASPI', 16.08), ('CE1', 'HIS', 'OD1', 'ASPI', 16.34), ('CE1', 'HIS', 'OD2', 'ASPI', 15.12)], [('NE2', 'HIS', 'CB', 'ASPI', 17.46), ('NE2', 'HIS', 'CG', 'ASPI', 16.36), ('NE2', 'HIS', 'OD1', 'ASPI', 16.51), ('NE2', 'HIS', 'OD2', 'ASPI', 15.44)], [('O', 'HIS', 'CB', 'ASPI', 16.91), ('O', 'HIS', 'CG', 'ASPI', 15.84), ('O', 'HIS', 'OD1', 'ASPI', 15.71), ('O', 'HIS', 'OD2', 'ASPI', 15.27)], [('C', 'HIS', 'CB', 'ASPI', 15.88), ('C', 'HIS', 'CG', 'ASPI', 14.79), ('C', 'HIS', 'OD1', 'ASPI', 14.68), ('C', 'HIS', 'OD2', 'ASPI', 14.17)], [('CA', 'HIS', 'CB', 'ASPI', 14.93), ('CA', 'HIS', 'CG', 'ASPI', 13.92), ('CA', 'HIS', 'OD1', 'ASPI', 13.93), ('CA', 'HIS', 'OD2', 'ASPI', 13.27)], [('N', 'HIS', 'CB', 'ASPI', 14.57), ('N', 'HIS', 'CG', 'ASPI', 13.65), ('N', 'HIS', 'OD1', 'ASPI', 13.64), ('N', 'HIS', 'OD2', 'ASPI', 13.11)]]}
ASP_CYS = { 
	'distances':
		[[19.73, 18.08], [18.25, 16.59], [17.93, 16.23], [17.48, 15.87], [10.11, 8.9], [10.05, 8.64], [9.59, 8.22], [10.73, 9.19]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'CYS', 19.73), ('CB', 'ASP', 'SG', 'CYS', 18.08)], [('CG', 'ASP', 'CB', 'CYS', 18.25), ('CG', 'ASP', 'SG', 'CYS', 16.59)], [('OD1', 'ASP', 'CB', 'CYS', 17.93), ('OD1', 'ASP', 'SG', 'CYS', 16.23)], [('OD2', 'ASP', 'CB', 'CYS', 17.48), ('OD2', 'ASP', 'SG', 'CYS', 15.87)], [('CB', 'ASP', 'CB', 'CYS', 10.11), ('CB', 'ASP', 'SG', 'CYS', 8.9)], [('CG', 'ASP', 'CB', 'CYS', 10.05), ('CG', 'ASP', 'SG', 'CYS', 8.64)], [('OD1', 'ASP', 'CB', 'CYS', 9.59), ('OD1', 'ASP', 'SG', 'CYS', 8.22)], [('OD2', 'ASP', 'CB', 'CYS', 10.73), ('OD2', 'ASP', 'SG', 'CYS', 9.19)]]}
ASN_HIS = { 
	'distances':
		[[18.76, 17.83, 16.57, 18.09, 16.07, 17.03, 20.27, 20.72, 19.99, 19.68], [18.09, 17.12, 15.82, 17.36, 15.28, 16.25, 19.59, 20.03, 19.26, 18.85], [16.95, 15.95, 14.65, 16.16, 14.08, 15.04, 18.51, 18.92, 18.11, 17.7], [18.92, 17.94, 16.61, 18.19, 16.06, 17.05, 20.32, 20.79, 20.02, 19.52], [13.96, 14.87, 14.95, 15.9, 15.97, 16.53, 15.41, 14.61, 13.38, 12.61], [13.62, 14.39, 14.34, 15.39, 15.29, 15.91, 15.28, 14.4, 13.13, 12.52], [12.98, 13.67, 13.64, 14.61, 14.52, 15.09, 14.6, 13.65, 12.42, 11.92], [14.22, 14.93, 14.76, 15.98, 15.69, 16.41, 16.08, 15.19, 13.86, 13.29]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'HIS', 18.76), ('CB', 'ASN', 'CG', 'HIS', 17.83), ('CB', 'ASN', 'ND1', 'HIS', 16.57), ('CB', 'ASN', 'CD2', 'HIS', 18.09), ('CB', 'ASN', 'CE1', 'HIS', 16.07), ('CB', 'ASN', 'NE2', 'HIS', 17.03), ('CB', 'ASN', 'O', 'HIS', 20.27), ('CB', 'ASN', 'C', 'HIS', 20.72), ('CB', 'ASN', 'CA', 'HIS', 19.99), ('CB', 'ASN', 'N', 'HIS', 19.68)], [('CG', 'ASN', 'CB', 'HIS', 18.09), ('CG', 'ASN', 'CG', 'HIS', 17.12), ('CG', 'ASN', 'ND1', 'HIS', 15.82), ('CG', 'ASN', 'CD2', 'HIS', 17.36), ('CG', 'ASN', 'CE1', 'HIS', 15.28), ('CG', 'ASN', 'NE2', 'HIS', 16.25), ('CG', 'ASN', 'O', 'HIS', 19.59), ('CG', 'ASN', 'C', 'HIS', 20.03), ('CG', 'ASN', 'CA', 'HIS', 19.26), ('CG', 'ASN', 'N', 'HIS', 18.85)], [('OD1', 'ASN', 'CB', 'HIS', 16.95), ('OD1', 'ASN', 'CG', 'HIS', 15.95), ('OD1', 'ASN', 'ND1', 'HIS', 14.65), ('OD1', 'ASN', 'CD2', 'HIS', 16.16), ('OD1', 'ASN', 'CE1', 'HIS', 14.08), ('OD1', 'ASN', 'NE2', 'HIS', 15.04), ('OD1', 'ASN', 'O', 'HIS', 18.51), ('OD1', 'ASN', 'C', 'HIS', 18.92), ('OD1', 'ASN', 'CA', 'HIS', 18.11), ('OD1', 'ASN', 'N', 'HIS', 17.7)], [('ND2', 'ASN', 'CB', 'HIS', 18.92), ('ND2', 'ASN', 'CG', 'HIS', 17.94), ('ND2', 'ASN', 'ND1', 'HIS', 16.61), ('ND2', 'ASN', 'CD2', 'HIS', 18.19), ('ND2', 'ASN', 'CE1', 'HIS', 16.06), ('ND2', 'ASN', 'NE2', 'HIS', 17.05), ('ND2', 'ASN', 'O', 'HIS', 20.32), ('ND2', 'ASN', 'C', 'HIS', 20.79), ('ND2', 'ASN', 'CA', 'HIS', 20.02), ('ND2', 'ASN', 'N', 'HIS', 19.52)], [('CB', 'ASN', 'CB', 'HIS', 13.96), ('CB', 'ASN', 'CG', 'HIS', 14.87), ('CB', 'ASN', 'ND1', 'HIS', 14.95), ('CB', 'ASN', 'CD2', 'HIS', 15.9), ('CB', 'ASN', 'CE1', 'HIS', 15.97), ('CB', 'ASN', 'NE2', 'HIS', 16.53), ('CB', 'ASN', 'O', 'HIS', 15.41), ('CB', 'ASN', 'C', 'HIS', 14.61), ('CB', 'ASN', 'CA', 'HIS', 13.38), ('CB', 'ASN', 'N', 'HIS', 12.61)], [('CG', 'ASN', 'CB', 'HIS', 13.62), ('CG', 'ASN', 'CG', 'HIS', 14.39), ('CG', 'ASN', 'ND1', 'HIS', 14.34), ('CG', 'ASN', 'CD2', 'HIS', 15.39), ('CG', 'ASN', 'CE1', 'HIS', 15.29), ('CG', 'ASN', 'NE2', 'HIS', 15.91), ('CG', 'ASN', 'O', 'HIS', 15.28), ('CG', 'ASN', 'C', 'HIS', 14.4), ('CG', 'ASN', 'CA', 'HIS', 13.13), ('CG', 'ASN', 'N', 'HIS', 12.52)], [('OD1', 'ASN', 'CB', 'HIS', 12.98), ('OD1', 'ASN', 'CG', 'HIS', 13.67), ('OD1', 'ASN', 'ND1', 'HIS', 13.64), ('OD1', 'ASN', 'CD2', 'HIS', 14.61), ('OD1', 'ASN', 'CE1', 'HIS', 14.52), ('OD1', 'ASN', 'NE2', 'HIS', 15.09), ('OD1', 'ASN', 'O', 'HIS', 14.6), ('OD1', 'ASN', 'C', 'HIS', 13.65), ('OD1', 'ASN', 'CA', 'HIS', 12.42), ('OD1', 'ASN', 'N', 'HIS', 11.92)], [('ND2', 'ASN', 'CB', 'HIS', 14.22), ('ND2', 'ASN', 'CG', 'HIS', 14.93), ('ND2', 'ASN', 'ND1', 'HIS', 14.76), ('ND2', 'ASN', 'CD2', 'HIS', 15.98), ('ND2', 'ASN', 'CE1', 'HIS', 15.69), ('ND2', 'ASN', 'NE2', 'HIS', 16.41), ('ND2', 'ASN', 'O', 'HIS', 16.08), ('ND2', 'ASN', 'C', 'HIS', 15.19), ('ND2', 'ASN', 'CA', 'HIS', 13.86), ('ND2', 'ASN', 'N', 'HIS', 13.29)]]}
CYS_ASPI = { 
	'distances':
		[[10.11, 10.05, 9.59, 10.73], [8.9, 8.64, 8.22, 9.19]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASPI', 10.11), ('CB', 'CYS', 'CG', 'ASPI', 10.05), ('CB', 'CYS', 'OD1', 'ASPI', 9.59), ('CB', 'CYS', 'OD2', 'ASPI', 10.73)], [('SG', 'CYS', 'CB', 'ASPI', 8.9), ('SG', 'CYS', 'CG', 'ASPI', 8.64), ('SG', 'CYS', 'OD1', 'ASPI', 8.22), ('SG', 'CYS', 'OD2', 'ASPI', 9.19)]]}
ASN_CYS = { 
	'distances':
		[[8.32, 7.42], [9.5, 8.37], [9.52, 8.17], [10.67, 9.62]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'CYS', 8.32), ('CB', 'ASN', 'SG', 'CYS', 7.42)], [('CG', 'ASN', 'CB', 'CYS', 9.5), ('CG', 'ASN', 'SG', 'CYS', 8.37)], [('OD1', 'ASN', 'CB', 'CYS', 9.52), ('OD1', 'ASN', 'SG', 'CYS', 8.17)], [('ND2', 'ASN', 'CB', 'CYS', 10.67), ('ND2', 'ASN', 'SG', 'CYS', 9.62)]]}
HIS_HIS = { 
	'distances':
		[[19.24, 18.93, 19.21, 18.56, 19.02, 18.62, 19.15, 18.11, 18.21, 18.77], [17.82, 17.48, 17.73, 17.11, 17.54, 17.15, 17.81, 16.76, 16.83, 17.44], [17.11, 16.82, 17.03, 16.55, 16.9, 16.61, 17.3, 16.19, 16.14, 16.7], [17.06, 16.65, 16.91, 16.19, 16.64, 16.19, 16.99, 15.95, 16.1, 16.8], [15.91, 15.57, 15.76, 15.29, 15.6, 15.31, 16.16, 15.04, 14.98, 15.61], [15.85, 15.43, 15.65, 15.02, 15.4, 15.01, 15.93, 14.86, 14.93, 15.65], [21.94, 21.65, 21.86, 21.33, 21.68, 21.35, 21.98, 20.92, 20.93, 21.45], [21.64, 21.29, 21.51, 20.89, 21.28, 20.89, 21.58, 20.54, 20.63, 21.22], [20.3, 19.9, 20.11, 19.48, 19.84, 19.45, 20.28, 19.23, 19.34, 19.97], [20.15, 19.71, 19.81, 19.33, 19.51, 19.21, 20.36, 19.27, 19.28, 19.95], [19.24, 17.82, 17.11, 17.06, 15.91, 15.85, 21.94, 21.64, 20.3, 20.15], [18.93, 17.48, 16.82, 16.65, 15.57, 15.43, 21.65, 21.29, 19.9, 19.71], [19.21, 17.73, 17.03, 16.91, 15.76, 15.65, 21.86, 21.51, 20.11, 19.81], [18.56, 17.11, 16.55, 16.19, 15.29, 15.02, 21.33, 20.89, 19.48, 19.33], [19.02, 17.54, 16.9, 16.64, 15.6, 15.4, 21.68, 21.28, 19.84, 19.51], [18.62, 17.15, 16.61, 16.19, 15.31, 15.01, 21.35, 20.89, 19.45, 19.21], [19.15, 17.81, 17.3, 16.99, 16.16, 15.93, 21.98, 21.58, 20.28, 20.36], [18.11, 16.76, 16.19, 15.95, 15.04, 14.86, 20.92, 20.54, 19.23, 19.27], [18.21, 16.83, 16.14, 16.1, 14.98, 14.93, 20.93, 20.63, 19.34, 19.28], [18.77, 17.44, 16.7, 16.8, 15.61, 15.65, 21.45, 21.22, 19.97, 19.95]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 19.24), ('CB', 'HIS', 'CG', 'HIS', 18.93), ('CB', 'HIS', 'ND1', 'HIS', 19.21), ('CB', 'HIS', 'CD2', 'HIS', 18.56), ('CB', 'HIS', 'CE1', 'HIS', 19.02), ('CB', 'HIS', 'NE2', 'HIS', 18.62), ('CB', 'HIS', 'O', 'HIS', 19.15), ('CB', 'HIS', 'C', 'HIS', 18.11), ('CB', 'HIS', 'CA', 'HIS', 18.21), ('CB', 'HIS', 'N', 'HIS', 18.77)], [('CG', 'HIS', 'CB', 'HIS', 17.82), ('CG', 'HIS', 'CG', 'HIS', 17.48), ('CG', 'HIS', 'ND1', 'HIS', 17.73), ('CG', 'HIS', 'CD2', 'HIS', 17.11), ('CG', 'HIS', 'CE1', 'HIS', 17.54), ('CG', 'HIS', 'NE2', 'HIS', 17.15), ('CG', 'HIS', 'O', 'HIS', 17.81), ('CG', 'HIS', 'C', 'HIS', 16.76), ('CG', 'HIS', 'CA', 'HIS', 16.83), ('CG', 'HIS', 'N', 'HIS', 17.44)], [('ND1', 'HIS', 'CB', 'HIS', 17.11), ('ND1', 'HIS', 'CG', 'HIS', 16.82), ('ND1', 'HIS', 'ND1', 'HIS', 17.03), ('ND1', 'HIS', 'CD2', 'HIS', 16.55), ('ND1', 'HIS', 'CE1', 'HIS', 16.9), ('ND1', 'HIS', 'NE2', 'HIS', 16.61), ('ND1', 'HIS', 'O', 'HIS', 17.3), ('ND1', 'HIS', 'C', 'HIS', 16.19), ('ND1', 'HIS', 'CA', 'HIS', 16.14), ('ND1', 'HIS', 'N', 'HIS', 16.7)], [('CD2', 'HIS', 'CB', 'HIS', 17.06), ('CD2', 'HIS', 'CG', 'HIS', 16.65), ('CD2', 'HIS', 'ND1', 'HIS', 16.91), ('CD2', 'HIS', 'CD2', 'HIS', 16.19), ('CD2', 'HIS', 'CE1', 'HIS', 16.64), ('CD2', 'HIS', 'NE2', 'HIS', 16.19), ('CD2', 'HIS', 'O', 'HIS', 16.99), ('CD2', 'HIS', 'C', 'HIS', 15.95), ('CD2', 'HIS', 'CA', 'HIS', 16.1), ('CD2', 'HIS', 'N', 'HIS', 16.8)], [('CE1', 'HIS', 'CB', 'HIS', 15.91), ('CE1', 'HIS', 'CG', 'HIS', 15.57), ('CE1', 'HIS', 'ND1', 'HIS', 15.76), ('CE1', 'HIS', 'CD2', 'HIS', 15.29), ('CE1', 'HIS', 'CE1', 'HIS', 15.6), ('CE1', 'HIS', 'NE2', 'HIS', 15.31), ('CE1', 'HIS', 'O', 'HIS', 16.16), ('CE1', 'HIS', 'C', 'HIS', 15.04), ('CE1', 'HIS', 'CA', 'HIS', 14.98), ('CE1', 'HIS', 'N', 'HIS', 15.61)], [('NE2', 'HIS', 'CB', 'HIS', 15.85), ('NE2', 'HIS', 'CG', 'HIS', 15.43), ('NE2', 'HIS', 'ND1', 'HIS', 15.65), ('NE2', 'HIS', 'CD2', 'HIS', 15.02), ('NE2', 'HIS', 'CE1', 'HIS', 15.4), ('NE2', 'HIS', 'NE2', 'HIS', 15.01), ('NE2', 'HIS', 'O', 'HIS', 15.93), ('NE2', 'HIS', 'C', 'HIS', 14.86), ('NE2', 'HIS', 'CA', 'HIS', 14.93), ('NE2', 'HIS', 'N', 'HIS', 15.65)], [('O', 'HIS', 'CB', 'HIS', 21.94), ('O', 'HIS', 'CG', 'HIS', 21.65), ('O', 'HIS', 'ND1', 'HIS', 21.86), ('O', 'HIS', 'CD2', 'HIS', 21.33), ('O', 'HIS', 'CE1', 'HIS', 21.68), ('O', 'HIS', 'NE2', 'HIS', 21.35), ('O', 'HIS', 'O', 'HIS', 21.98), ('O', 'HIS', 'C', 'HIS', 20.92), ('O', 'HIS', 'CA', 'HIS', 20.93), ('O', 'HIS', 'N', 'HIS', 21.45)], [('C', 'HIS', 'CB', 'HIS', 21.64), ('C', 'HIS', 'CG', 'HIS', 21.29), ('C', 'HIS', 'ND1', 'HIS', 21.51), ('C', 'HIS', 'CD2', 'HIS', 20.89), ('C', 'HIS', 'CE1', 'HIS', 21.28), ('C', 'HIS', 'NE2', 'HIS', 20.89), ('C', 'HIS', 'O', 'HIS', 21.58), ('C', 'HIS', 'C', 'HIS', 20.54), ('C', 'HIS', 'CA', 'HIS', 20.63), ('C', 'HIS', 'N', 'HIS', 21.22)], [('CA', 'HIS', 'CB', 'HIS', 20.3), ('CA', 'HIS', 'CG', 'HIS', 19.9), ('CA', 'HIS', 'ND1', 'HIS', 20.11), ('CA', 'HIS', 'CD2', 'HIS', 19.48), ('CA', 'HIS', 'CE1', 'HIS', 19.84), ('CA', 'HIS', 'NE2', 'HIS', 19.45), ('CA', 'HIS', 'O', 'HIS', 20.28), ('CA', 'HIS', 'C', 'HIS', 19.23), ('CA', 'HIS', 'CA', 'HIS', 19.34), ('CA', 'HIS', 'N', 'HIS', 19.97)], [('N', 'HIS', 'CB', 'HIS', 20.15), ('N', 'HIS', 'CG', 'HIS', 19.71), ('N', 'HIS', 'ND1', 'HIS', 19.81), ('N', 'HIS', 'CD2', 'HIS', 19.33), ('N', 'HIS', 'CE1', 'HIS', 19.51), ('N', 'HIS', 'NE2', 'HIS', 19.21), ('N', 'HIS', 'O', 'HIS', 20.36), ('N', 'HIS', 'C', 'HIS', 19.27), ('N', 'HIS', 'CA', 'HIS', 19.28), ('N', 'HIS', 'N', 'HIS', 19.95)], [('CB', 'HIS', 'CB', 'HIS', 19.24), ('CB', 'HIS', 'CG', 'HIS', 17.82), ('CB', 'HIS', 'ND1', 'HIS', 17.11), ('CB', 'HIS', 'CD2', 'HIS', 17.06), ('CB', 'HIS', 'CE1', 'HIS', 15.91), ('CB', 'HIS', 'NE2', 'HIS', 15.85), ('CB', 'HIS', 'O', 'HIS', 21.94), ('CB', 'HIS', 'C', 'HIS', 21.64), ('CB', 'HIS', 'CA', 'HIS', 20.3), ('CB', 'HIS', 'N', 'HIS', 20.15)], [('CG', 'HIS', 'CB', 'HIS', 18.93), ('CG', 'HIS', 'CG', 'HIS', 17.48), ('CG', 'HIS', 'ND1', 'HIS', 16.82), ('CG', 'HIS', 'CD2', 'HIS', 16.65), ('CG', 'HIS', 'CE1', 'HIS', 15.57), ('CG', 'HIS', 'NE2', 'HIS', 15.43), ('CG', 'HIS', 'O', 'HIS', 21.65), ('CG', 'HIS', 'C', 'HIS', 21.29), ('CG', 'HIS', 'CA', 'HIS', 19.9), ('CG', 'HIS', 'N', 'HIS', 19.71)], [('ND1', 'HIS', 'CB', 'HIS', 19.21), ('ND1', 'HIS', 'CG', 'HIS', 17.73), ('ND1', 'HIS', 'ND1', 'HIS', 17.03), ('ND1', 'HIS', 'CD2', 'HIS', 16.91), ('ND1', 'HIS', 'CE1', 'HIS', 15.76), ('ND1', 'HIS', 'NE2', 'HIS', 15.65), ('ND1', 'HIS', 'O', 'HIS', 21.86), ('ND1', 'HIS', 'C', 'HIS', 21.51), ('ND1', 'HIS', 'CA', 'HIS', 20.11), ('ND1', 'HIS', 'N', 'HIS', 19.81)], [('CD2', 'HIS', 'CB', 'HIS', 18.56), ('CD2', 'HIS', 'CG', 'HIS', 17.11), ('CD2', 'HIS', 'ND1', 'HIS', 16.55), ('CD2', 'HIS', 'CD2', 'HIS', 16.19), ('CD2', 'HIS', 'CE1', 'HIS', 15.29), ('CD2', 'HIS', 'NE2', 'HIS', 15.02), ('CD2', 'HIS', 'O', 'HIS', 21.33), ('CD2', 'HIS', 'C', 'HIS', 20.89), ('CD2', 'HIS', 'CA', 'HIS', 19.48), ('CD2', 'HIS', 'N', 'HIS', 19.33)], [('CE1', 'HIS', 'CB', 'HIS', 19.02), ('CE1', 'HIS', 'CG', 'HIS', 17.54), ('CE1', 'HIS', 'ND1', 'HIS', 16.9), ('CE1', 'HIS', 'CD2', 'HIS', 16.64), ('CE1', 'HIS', 'CE1', 'HIS', 15.6), ('CE1', 'HIS', 'NE2', 'HIS', 15.4), ('CE1', 'HIS', 'O', 'HIS', 21.68), ('CE1', 'HIS', 'C', 'HIS', 21.28), ('CE1', 'HIS', 'CA', 'HIS', 19.84), ('CE1', 'HIS', 'N', 'HIS', 19.51)], [('NE2', 'HIS', 'CB', 'HIS', 18.62), ('NE2', 'HIS', 'CG', 'HIS', 17.15), ('NE2', 'HIS', 'ND1', 'HIS', 16.61), ('NE2', 'HIS', 'CD2', 'HIS', 16.19), ('NE2', 'HIS', 'CE1', 'HIS', 15.31), ('NE2', 'HIS', 'NE2', 'HIS', 15.01), ('NE2', 'HIS', 'O', 'HIS', 21.35), ('NE2', 'HIS', 'C', 'HIS', 20.89), ('NE2', 'HIS', 'CA', 'HIS', 19.45), ('NE2', 'HIS', 'N', 'HIS', 19.21)], [('O', 'HIS', 'CB', 'HIS', 19.15), ('O', 'HIS', 'CG', 'HIS', 17.81), ('O', 'HIS', 'ND1', 'HIS', 17.3), ('O', 'HIS', 'CD2', 'HIS', 16.99), ('O', 'HIS', 'CE1', 'HIS', 16.16), ('O', 'HIS', 'NE2', 'HIS', 15.93), ('O', 'HIS', 'O', 'HIS', 21.98), ('O', 'HIS', 'C', 'HIS', 21.58), ('O', 'HIS', 'CA', 'HIS', 20.28), ('O', 'HIS', 'N', 'HIS', 20.36)], [('C', 'HIS', 'CB', 'HIS', 18.11), ('C', 'HIS', 'CG', 'HIS', 16.76), ('C', 'HIS', 'ND1', 'HIS', 16.19), ('C', 'HIS', 'CD2', 'HIS', 15.95), ('C', 'HIS', 'CE1', 'HIS', 15.04), ('C', 'HIS', 'NE2', 'HIS', 14.86), ('C', 'HIS', 'O', 'HIS', 20.92), ('C', 'HIS', 'C', 'HIS', 20.54), ('C', 'HIS', 'CA', 'HIS', 19.23), ('C', 'HIS', 'N', 'HIS', 19.27)], [('CA', 'HIS', 'CB', 'HIS', 18.21), ('CA', 'HIS', 'CG', 'HIS', 16.83), ('CA', 'HIS', 'ND1', 'HIS', 16.14), ('CA', 'HIS', 'CD2', 'HIS', 16.1), ('CA', 'HIS', 'CE1', 'HIS', 14.98), ('CA', 'HIS', 'NE2', 'HIS', 14.93), ('CA', 'HIS', 'O', 'HIS', 20.93), ('CA', 'HIS', 'C', 'HIS', 20.63), ('CA', 'HIS', 'CA', 'HIS', 19.34), ('CA', 'HIS', 'N', 'HIS', 19.28)], [('N', 'HIS', 'CB', 'HIS', 18.77), ('N', 'HIS', 'CG', 'HIS', 17.44), ('N', 'HIS', 'ND1', 'HIS', 16.7), ('N', 'HIS', 'CD2', 'HIS', 16.8), ('N', 'HIS', 'CE1', 'HIS', 15.61), ('N', 'HIS', 'NE2', 'HIS', 15.65), ('N', 'HIS', 'O', 'HIS', 21.45), ('N', 'HIS', 'C', 'HIS', 21.22), ('N', 'HIS', 'CA', 'HIS', 19.97), ('N', 'HIS', 'N', 'HIS', 19.95)]]}
ASN_ASPI = { 
	'distances':
		[[6.81, 7.42, 8.08, 7.61], [6.34, 6.88, 7.76, 6.8], [5.75, 6.0, 6.89, 5.75], [7.1, 7.77, 8.77, 7.6]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ASPI', 6.81), ('CB', 'ASN', 'CG', 'ASPI', 7.42), ('CB', 'ASN', 'OD1', 'ASPI', 8.08), ('CB', 'ASN', 'OD2', 'ASPI', 7.61)], [('CG', 'ASN', 'CB', 'ASPI', 6.34), ('CG', 'ASN', 'CG', 'ASPI', 6.88), ('CG', 'ASN', 'OD1', 'ASPI', 7.76), ('CG', 'ASN', 'OD2', 'ASPI', 6.8)], [('OD1', 'ASN', 'CB', 'ASPI', 5.75), ('OD1', 'ASN', 'CG', 'ASPI', 6.0), ('OD1', 'ASN', 'OD1', 'ASPI', 6.89), ('OD1', 'ASN', 'OD2', 'ASPI', 5.75)], [('ND2', 'ASN', 'CB', 'ASPI', 7.1), ('ND2', 'ASN', 'CG', 'ASPI', 7.77), ('ND2', 'ASN', 'OD1', 'ASPI', 8.77), ('ND2', 'ASN', 'OD2', 'ASPI', 7.6)]]}
ASP_ASN = { 
	'distances':
		[[17.05, 15.9, 14.81, 16.25], [15.77, 14.66, 13.54, 15.09], [15.57, 14.46, 13.31, 14.93], [15.07, 14.01, 12.91, 14.48], [6.81, 6.34, 5.75, 7.1], [7.42, 6.88, 6.0, 7.77], [8.08, 7.76, 6.89, 8.77], [7.61, 6.8, 5.75, 7.6]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASN', 17.05), ('CB', 'ASP', 'CG', 'ASN', 15.9), ('CB', 'ASP', 'OD1', 'ASN', 14.81), ('CB', 'ASP', 'ND2', 'ASN', 16.25)], [('CG', 'ASP', 'CB', 'ASN', 15.77), ('CG', 'ASP', 'CG', 'ASN', 14.66), ('CG', 'ASP', 'OD1', 'ASN', 13.54), ('CG', 'ASP', 'ND2', 'ASN', 15.09)], [('OD1', 'ASP', 'CB', 'ASN', 15.57), ('OD1', 'ASP', 'CG', 'ASN', 14.46), ('OD1', 'ASP', 'OD1', 'ASN', 13.31), ('OD1', 'ASP', 'ND2', 'ASN', 14.93)], [('OD2', 'ASP', 'CB', 'ASN', 15.07), ('OD2', 'ASP', 'CG', 'ASN', 14.01), ('OD2', 'ASP', 'OD1', 'ASN', 12.91), ('OD2', 'ASP', 'ND2', 'ASN', 14.48)], [('CB', 'ASP', 'CB', 'ASN', 6.81), ('CB', 'ASP', 'CG', 'ASN', 6.34), ('CB', 'ASP', 'OD1', 'ASN', 5.75), ('CB', 'ASP', 'ND2', 'ASN', 7.1)], [('CG', 'ASP', 'CB', 'ASN', 7.42), ('CG', 'ASP', 'CG', 'ASN', 6.88), ('CG', 'ASP', 'OD1', 'ASN', 6.0), ('CG', 'ASP', 'ND2', 'ASN', 7.77)], [('OD1', 'ASP', 'CB', 'ASN', 8.08), ('OD1', 'ASP', 'CG', 'ASN', 7.76), ('OD1', 'ASP', 'OD1', 'ASN', 6.89), ('OD1', 'ASP', 'ND2', 'ASN', 8.77)], [('OD2', 'ASP', 'CB', 'ASN', 7.61), ('OD2', 'ASP', 'CG', 'ASN', 6.8), ('OD2', 'ASP', 'OD1', 'ASN', 5.75), ('OD2', 'ASP', 'ND2', 'ASN', 7.6)]]}
ASP_LYS = { 
	'distances':
		[[13.1, 11.63, 11.44, 10.11, 10.36], [12.49, 10.98, 10.64, 9.22, 9.31], [13.05, 11.55, 11.03, 9.57, 9.43], [11.63, 10.11, 9.83, 8.41, 8.6], [7.49, 6.93, 6.03, 5.91, 5.47], [8.43, 7.58, 6.58, 5.99, 5.3], [9.42, 8.55, 7.67, 7.0, 6.4], [8.4, 7.43, 6.25, 5.45, 4.45]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 13.1), ('CB', 'ASP', 'CG', 'LYS', 11.63), ('CB', 'ASP', 'CD', 'LYS', 11.44), ('CB', 'ASP', 'CE', 'LYS', 10.11), ('CB', 'ASP', 'NZ', 'LYS', 10.36)], [('CG', 'ASP', 'CB', 'LYS', 12.49), ('CG', 'ASP', 'CG', 'LYS', 10.98), ('CG', 'ASP', 'CD', 'LYS', 10.64), ('CG', 'ASP', 'CE', 'LYS', 9.22), ('CG', 'ASP', 'NZ', 'LYS', 9.31)], [('OD1', 'ASP', 'CB', 'LYS', 13.05), ('OD1', 'ASP', 'CG', 'LYS', 11.55), ('OD1', 'ASP', 'CD', 'LYS', 11.03), ('OD1', 'ASP', 'CE', 'LYS', 9.57), ('OD1', 'ASP', 'NZ', 'LYS', 9.43)], [('OD2', 'ASP', 'CB', 'LYS', 11.63), ('OD2', 'ASP', 'CG', 'LYS', 10.11), ('OD2', 'ASP', 'CD', 'LYS', 9.83), ('OD2', 'ASP', 'CE', 'LYS', 8.41), ('OD2', 'ASP', 'NZ', 'LYS', 8.6)], [('CB', 'ASP', 'CB', 'LYS', 7.49), ('CB', 'ASP', 'CG', 'LYS', 6.93), ('CB', 'ASP', 'CD', 'LYS', 6.03), ('CB', 'ASP', 'CE', 'LYS', 5.91), ('CB', 'ASP', 'NZ', 'LYS', 5.47)], [('CG', 'ASP', 'CB', 'LYS', 8.43), ('CG', 'ASP', 'CG', 'LYS', 7.58), ('CG', 'ASP', 'CD', 'LYS', 6.58), ('CG', 'ASP', 'CE', 'LYS', 5.99), ('CG', 'ASP', 'NZ', 'LYS', 5.3)], [('OD1', 'ASP', 'CB', 'LYS', 9.42), ('OD1', 'ASP', 'CG', 'LYS', 8.55), ('OD1', 'ASP', 'CD', 'LYS', 7.67), ('OD1', 'ASP', 'CE', 'LYS', 7.0), ('OD1', 'ASP', 'NZ', 'LYS', 6.4)], [('OD2', 'ASP', 'CB', 'LYS', 8.4), ('OD2', 'ASP', 'CG', 'LYS', 7.43), ('OD2', 'ASP', 'CD', 'LYS', 6.25), ('OD2', 'ASP', 'CE', 'LYS', 5.45), ('OD2', 'ASP', 'NZ', 'LYS', 4.45)]]}
CYS_HIS = { 
	'distances':
		[[18.82, 18.08, 17.15, 18.27, 16.79, 17.48, 20.61, 20.91, 20.3, 20.51], [17.43, 16.61, 15.64, 16.76, 15.21, 15.91, 19.31, 19.58, 18.9, 19.04], [14.42, 15.63, 16.34, 16.38, 17.41, 17.45, 14.37, 13.91, 13.29, 12.18], [13.09, 14.21, 14.87, 14.95, 15.9, 15.96, 13.21, 12.63, 11.94, 10.95]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 18.82), ('CB', 'CYS', 'CG', 'HIS', 18.08), ('CB', 'CYS', 'ND1', 'HIS', 17.15), ('CB', 'CYS', 'CD2', 'HIS', 18.27), ('CB', 'CYS', 'CE1', 'HIS', 16.79), ('CB', 'CYS', 'NE2', 'HIS', 17.48), ('CB', 'CYS', 'O', 'HIS', 20.61), ('CB', 'CYS', 'C', 'HIS', 20.91), ('CB', 'CYS', 'CA', 'HIS', 20.3), ('CB', 'CYS', 'N', 'HIS', 20.51)], [('SG', 'CYS', 'CB', 'HIS', 17.43), ('SG', 'CYS', 'CG', 'HIS', 16.61), ('SG', 'CYS', 'ND1', 'HIS', 15.64), ('SG', 'CYS', 'CD2', 'HIS', 16.76), ('SG', 'CYS', 'CE1', 'HIS', 15.21), ('SG', 'CYS', 'NE2', 'HIS', 15.91), ('SG', 'CYS', 'O', 'HIS', 19.31), ('SG', 'CYS', 'C', 'HIS', 19.58), ('SG', 'CYS', 'CA', 'HIS', 18.9), ('SG', 'CYS', 'N', 'HIS', 19.04)], [('CB', 'CYS', 'CB', 'HIS', 14.42), ('CB', 'CYS', 'CG', 'HIS', 15.63), ('CB', 'CYS', 'ND1', 'HIS', 16.34), ('CB', 'CYS', 'CD2', 'HIS', 16.38), ('CB', 'CYS', 'CE1', 'HIS', 17.41), ('CB', 'CYS', 'NE2', 'HIS', 17.45), ('CB', 'CYS', 'O', 'HIS', 14.37), ('CB', 'CYS', 'C', 'HIS', 13.91), ('CB', 'CYS', 'CA', 'HIS', 13.29), ('CB', 'CYS', 'N', 'HIS', 12.18)], [('SG', 'CYS', 'CB', 'HIS', 13.09), ('SG', 'CYS', 'CG', 'HIS', 14.21), ('SG', 'CYS', 'ND1', 'HIS', 14.87), ('SG', 'CYS', 'CD2', 'HIS', 14.95), ('SG', 'CYS', 'CE1', 'HIS', 15.9), ('SG', 'CYS', 'NE2', 'HIS', 15.96), ('SG', 'CYS', 'O', 'HIS', 13.21), ('SG', 'CYS', 'C', 'HIS', 12.63), ('SG', 'CYS', 'CA', 'HIS', 11.94), ('SG', 'CYS', 'N', 'HIS', 10.95)]]}
LYS_ASN = { 
	'distances':
		[[10.48, 9.54, 9.39, 9.21], [10.53, 9.5, 9.12, 9.35], [9.37, 8.24, 7.77, 8.14], [9.71, 8.55, 7.83, 8.65], [8.72, 7.5, 6.64, 7.7]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASN', 10.48), ('CB', 'LYS', 'CG', 'ASN', 9.54), ('CB', 'LYS', 'OD1', 'ASN', 9.39), ('CB', 'LYS', 'ND2', 'ASN', 9.21)], [('CG', 'LYS', 'CB', 'ASN', 10.53), ('CG', 'LYS', 'CG', 'ASN', 9.5), ('CG', 'LYS', 'OD1', 'ASN', 9.12), ('CG', 'LYS', 'ND2', 'ASN', 9.35)], [('CD', 'LYS', 'CB', 'ASN', 9.37), ('CD', 'LYS', 'CG', 'ASN', 8.24), ('CD', 'LYS', 'OD1', 'ASN', 7.77), ('CD', 'LYS', 'ND2', 'ASN', 8.14)], [('CE', 'LYS', 'CB', 'ASN', 9.71), ('CE', 'LYS', 'CG', 'ASN', 8.55), ('CE', 'LYS', 'OD1', 'ASN', 7.83), ('CE', 'LYS', 'ND2', 'ASN', 8.65)], [('NZ', 'LYS', 'CB', 'ASN', 8.72), ('NZ', 'LYS', 'CG', 'ASN', 7.5), ('NZ', 'LYS', 'OD1', 'ASN', 6.64), ('NZ', 'LYS', 'ND2', 'ASN', 7.7)]]}
ASP_ASP = { 
	'distances':
		[[13.03, 12.07, 12.24, 11.31], [11.79, 10.74, 10.87, 9.98], [11.92, 10.77, 10.89, 9.92], [10.84, 9.83, 9.92, 9.17], [13.03, 11.79, 11.92, 10.84], [12.07, 10.74, 10.77, 9.83], [12.24, 10.87, 10.89, 9.92], [11.31, 9.98, 9.92, 9.17]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 13.03), ('CB', 'ASP', 'CG', 'ASP', 12.07), ('CB', 'ASP', 'OD1', 'ASP', 12.24), ('CB', 'ASP', 'OD2', 'ASP', 11.31)], [('CG', 'ASP', 'CB', 'ASP', 11.79), ('CG', 'ASP', 'CG', 'ASP', 10.74), ('CG', 'ASP', 'OD1', 'ASP', 10.87), ('CG', 'ASP', 'OD2', 'ASP', 9.98)], [('OD1', 'ASP', 'CB', 'ASP', 11.92), ('OD1', 'ASP', 'CG', 'ASP', 10.77), ('OD1', 'ASP', 'OD1', 'ASP', 10.89), ('OD1', 'ASP', 'OD2', 'ASP', 9.92)], [('OD2', 'ASP', 'CB', 'ASP', 10.84), ('OD2', 'ASP', 'CG', 'ASP', 9.83), ('OD2', 'ASP', 'OD1', 'ASP', 9.92), ('OD2', 'ASP', 'OD2', 'ASP', 9.17)], [('CB', 'ASP', 'CB', 'ASP', 13.03), ('CB', 'ASP', 'CG', 'ASP', 11.79), ('CB', 'ASP', 'OD1', 'ASP', 11.92), ('CB', 'ASP', 'OD2', 'ASP', 10.84)], [('CG', 'ASP', 'CB', 'ASP', 12.07), ('CG', 'ASP', 'CG', 'ASP', 10.74), ('CG', 'ASP', 'OD1', 'ASP', 10.77), ('CG', 'ASP', 'OD2', 'ASP', 9.83)], [('OD1', 'ASP', 'CB', 'ASP', 12.24), ('OD1', 'ASP', 'CG', 'ASP', 10.87), ('OD1', 'ASP', 'OD1', 'ASP', 10.89), ('OD1', 'ASP', 'OD2', 'ASP', 9.92)], [('OD2', 'ASP', 'CB', 'ASP', 11.31), ('OD2', 'ASP', 'CG', 'ASP', 9.98), ('OD2', 'ASP', 'OD1', 'ASP', 9.92), ('OD2', 'ASP', 'OD2', 'ASP', 9.17)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_HIS, d, 'P_1b3r_3_3_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_CYS, d, 'P_1b3r_3_3_1_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_HIS, d, 'P_1b3r_3_3_1_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_ASPI, d, 'P_1b3r_3_3_1_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_CYS, d, 'P_1b3r_3_3_1_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ASN_HIS, d, 'P_1b3r_3_3_1_1')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(CYS_ASPI, d, 'P_1b3r_3_3_1_1')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ASN_CYS, d, 'P_1b3r_3_3_1_1')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(HIS_HIS, d, 'P_1b3r_3_3_1_1')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(ASN_ASPI, d, 'P_1b3r_3_3_1_1')
	if match10 == []:
		 flag = True
		 break
	match11 , totTime11 = cmd.detect(ASP_ASN, d, 'P_1b3r_3_3_1_1')
	if match11 == []:
		 flag = True
		 break
	match12 , totTime12 = cmd.detect(ASP_LYS, d, 'P_1b3r_3_3_1_1')
	if match12 == []:
		 flag = True
		 break
	match13 , totTime13 = cmd.detect(CYS_HIS, d, 'P_1b3r_3_3_1_1')
	if match13 == []:
		 flag = True
		 break
	match14 , totTime14 = cmd.detect(LYS_ASN, d, 'P_1b3r_3_3_1_1')
	if match14 == []:
		 flag = True
		 break
	match15 , totTime15 = cmd.detect(ASP_ASP, d, 'P_1b3r_3_3_1_1')
	if match15 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_HIS' :  match1,
		'LYS_CYS' :  match2,
		'ASP_HIS' :  match3,
		'HIS_ASPI' :  match4,
		'ASP_CYS' :  match5,
		'ASN_HIS' :  match6,
		'CYS_ASPI' :  match7,
		'ASN_CYS' :  match8,
		'HIS_HIS' :  match9,
		'ASN_ASPI' :  match10,
		'ASP_ASN' :  match11,
		'ASP_LYS' :  match12,
		'CYS_HIS' :  match13,
		'LYS_ASN' :  match14,
		'ASP_ASP' :  match15}