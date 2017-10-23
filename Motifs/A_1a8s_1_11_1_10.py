'''
FUNC:A_1a8s_1_11_1_10
PDB:1a8s
EC:1.11.1.10
RESI:trp,ser,thr,asp,his
LOCI:a-28,94,95,224,253;
'''
import motifFunctions as cmd
TRP_HIS = { 
	'distances':
		[[12.76, 11.46, 11.58, 10.21, 10.45, 9.47], [13.67, 12.44, 12.65, 11.19, 11.58, 10.56], [15.02, 13.78, 13.95, 12.54, 12.85, 11.87], [13.38, 12.27, 12.6, 11.05, 11.64, 10.58], [15.57, 14.42, 14.67, 13.19, 13.63, 12.63], [14.67, 13.6, 13.94, 12.39, 12.99, 11.95], [12.32, 11.3, 11.74, 10.1, 10.89, 9.79], [14.98, 14.02, 14.46, 12.86, 13.61, 12.56], [12.66, 11.78, 12.33, 10.66, 11.6, 10.51], [14.06, 13.2, 13.73, 12.08, 12.99, 11.92], [10.91, 9.8, 10.31, 8.47, 9.41, 8.16], [12.15, 11.01, 11.45, 9.68, 10.49, 9.28], [12.72, 11.45, 11.68, 10.16, 10.59, 9.52], [12.03, 10.7, 10.81, 9.44, 9.67, 8.68]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'HIS', 12.76), ('CB', 'TRP', 'CG', 'HIS', 11.46), ('CB', 'TRP', 'ND1', 'HIS', 11.58), ('CB', 'TRP', 'CD2', 'HIS', 10.21), ('CB', 'TRP', 'CE1', 'HIS', 10.45), ('CB', 'TRP', 'NE2', 'HIS', 9.47)], [('CG', 'TRP', 'CB', 'HIS', 13.67), ('CG', 'TRP', 'CG', 'HIS', 12.44), ('CG', 'TRP', 'ND1', 'HIS', 12.65), ('CG', 'TRP', 'CD2', 'HIS', 11.19), ('CG', 'TRP', 'CE1', 'HIS', 11.58), ('CG', 'TRP', 'NE2', 'HIS', 10.56)], [('CD1', 'TRP', 'CB', 'HIS', 15.02), ('CD1', 'TRP', 'CG', 'HIS', 13.78), ('CD1', 'TRP', 'ND1', 'HIS', 13.95), ('CD1', 'TRP', 'CD2', 'HIS', 12.54), ('CD1', 'TRP', 'CE1', 'HIS', 12.85), ('CD1', 'TRP', 'NE2', 'HIS', 11.87)], [('CD2', 'TRP', 'CB', 'HIS', 13.38), ('CD2', 'TRP', 'CG', 'HIS', 12.27), ('CD2', 'TRP', 'ND1', 'HIS', 12.6), ('CD2', 'TRP', 'CD2', 'HIS', 11.05), ('CD2', 'TRP', 'CE1', 'HIS', 11.64), ('CD2', 'TRP', 'NE2', 'HIS', 10.58)], [('NE1', 'TRP', 'CB', 'HIS', 15.57), ('NE1', 'TRP', 'CG', 'HIS', 14.42), ('NE1', 'TRP', 'ND1', 'HIS', 14.67), ('NE1', 'TRP', 'CD2', 'HIS', 13.19), ('NE1', 'TRP', 'CE1', 'HIS', 13.63), ('NE1', 'TRP', 'NE2', 'HIS', 12.63)], [('CE2', 'TRP', 'CB', 'HIS', 14.67), ('CE2', 'TRP', 'CG', 'HIS', 13.6), ('CE2', 'TRP', 'ND1', 'HIS', 13.94), ('CE2', 'TRP', 'CD2', 'HIS', 12.39), ('CE2', 'TRP', 'CE1', 'HIS', 12.99), ('CE2', 'TRP', 'NE2', 'HIS', 11.95)], [('CE3', 'TRP', 'CB', 'HIS', 12.32), ('CE3', 'TRP', 'CG', 'HIS', 11.3), ('CE3', 'TRP', 'ND1', 'HIS', 11.74), ('CE3', 'TRP', 'CD2', 'HIS', 10.1), ('CE3', 'TRP', 'CE1', 'HIS', 10.89), ('CE3', 'TRP', 'NE2', 'HIS', 9.79)], [('CZ2', 'TRP', 'CB', 'HIS', 14.98), ('CZ2', 'TRP', 'CG', 'HIS', 14.02), ('CZ2', 'TRP', 'ND1', 'HIS', 14.46), ('CZ2', 'TRP', 'CD2', 'HIS', 12.86), ('CZ2', 'TRP', 'CE1', 'HIS', 13.61), ('CZ2', 'TRP', 'NE2', 'HIS', 12.56)], [('CZ3', 'TRP', 'CB', 'HIS', 12.66), ('CZ3', 'TRP', 'CG', 'HIS', 11.78), ('CZ3', 'TRP', 'ND1', 'HIS', 12.33), ('CZ3', 'TRP', 'CD2', 'HIS', 10.66), ('CZ3', 'TRP', 'CE1', 'HIS', 11.6), ('CZ3', 'TRP', 'NE2', 'HIS', 10.51)], [('CH2', 'TRP', 'CB', 'HIS', 14.06), ('CH2', 'TRP', 'CG', 'HIS', 13.2), ('CH2', 'TRP', 'ND1', 'HIS', 13.73), ('CH2', 'TRP', 'CD2', 'HIS', 12.08), ('CH2', 'TRP', 'CE1', 'HIS', 12.99), ('CH2', 'TRP', 'NE2', 'HIS', 11.92)], [('O', 'TRP', 'CB', 'HIS', 10.91), ('O', 'TRP', 'CG', 'HIS', 9.8), ('O', 'TRP', 'ND1', 'HIS', 10.31), ('O', 'TRP', 'CD2', 'HIS', 8.47), ('O', 'TRP', 'CE1', 'HIS', 9.41), ('O', 'TRP', 'NE2', 'HIS', 8.16)], [('C', 'TRP', 'CB', 'HIS', 12.15), ('C', 'TRP', 'CG', 'HIS', 11.01), ('C', 'TRP', 'ND1', 'HIS', 11.45), ('C', 'TRP', 'CD2', 'HIS', 9.68), ('C', 'TRP', 'CE1', 'HIS', 10.49), ('C', 'TRP', 'NE2', 'HIS', 9.28)], [('CA', 'TRP', 'CB', 'HIS', 12.72), ('CA', 'TRP', 'CG', 'HIS', 11.45), ('CA', 'TRP', 'ND1', 'HIS', 11.68), ('CA', 'TRP', 'CD2', 'HIS', 10.16), ('CA', 'TRP', 'CE1', 'HIS', 10.59), ('CA', 'TRP', 'NE2', 'HIS', 9.52)], [('N', 'TRP', 'CB', 'HIS', 12.03), ('N', 'TRP', 'CG', 'HIS', 10.7), ('N', 'TRP', 'ND1', 'HIS', 10.81), ('N', 'TRP', 'CD2', 'HIS', 9.44), ('N', 'TRP', 'CE1', 'HIS', 9.67), ('N', 'TRP', 'NE2', 'HIS', 8.68)]]}
ASP_HIS = { 
	'distances':
		[[6.62, 7.2, 6.71, 8.48, 7.84, 8.82], [5.55, 5.86, 5.28, 7.08, 6.38, 7.35], [5.17, 5.47, 5.17, 6.58, 6.2, 6.96], [5.67, 5.62, 4.69, 6.77, 5.68, 6.82]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 6.62), ('CB', 'ASP', 'CG', 'HIS', 7.2), ('CB', 'ASP', 'ND1', 'HIS', 6.71), ('CB', 'ASP', 'CD2', 'HIS', 8.48), ('CB', 'ASP', 'CE1', 'HIS', 7.84), ('CB', 'ASP', 'NE2', 'HIS', 8.82)], [('CG', 'ASP', 'CB', 'HIS', 5.55), ('CG', 'ASP', 'CG', 'HIS', 5.86), ('CG', 'ASP', 'ND1', 'HIS', 5.28), ('CG', 'ASP', 'CD2', 'HIS', 7.08), ('CG', 'ASP', 'CE1', 'HIS', 6.38), ('CG', 'ASP', 'NE2', 'HIS', 7.35)], [('OD1', 'ASP', 'CB', 'HIS', 5.17), ('OD1', 'ASP', 'CG', 'HIS', 5.47), ('OD1', 'ASP', 'ND1', 'HIS', 5.17), ('OD1', 'ASP', 'CD2', 'HIS', 6.58), ('OD1', 'ASP', 'CE1', 'HIS', 6.2), ('OD1', 'ASP', 'NE2', 'HIS', 6.96)], [('OD2', 'ASP', 'CB', 'HIS', 5.67), ('OD2', 'ASP', 'CG', 'HIS', 5.62), ('OD2', 'ASP', 'ND1', 'HIS', 4.69), ('OD2', 'ASP', 'CD2', 'HIS', 6.77), ('OD2', 'ASP', 'CE1', 'HIS', 5.68), ('OD2', 'ASP', 'NE2', 'HIS', 6.82)]]}
THR_HIS = { 
	'distances':
		[[13.31, 11.82, 11.35, 10.84, 10.04, 9.61], [12.65, 11.19, 10.77, 10.19, 9.48, 9.0], [14.8, 13.31, 12.83, 12.32, 11.52, 11.1], [14.95, 13.46, 12.69, 12.71, 11.43, 11.38], [13.88, 12.4, 11.69, 11.6, 10.42, 10.29], [12.93, 11.43, 10.76, 10.6, 9.46, 9.28], [11.53, 10.03, 9.37, 9.23, 8.07, 7.9]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'HIS', 13.31), ('CB', 'THR', 'CG', 'HIS', 11.82), ('CB', 'THR', 'ND1', 'HIS', 11.35), ('CB', 'THR', 'CD2', 'HIS', 10.84), ('CB', 'THR', 'CE1', 'HIS', 10.04), ('CB', 'THR', 'NE2', 'HIS', 9.61)], [('OG1', 'THR', 'CB', 'HIS', 12.65), ('OG1', 'THR', 'CG', 'HIS', 11.19), ('OG1', 'THR', 'ND1', 'HIS', 10.77), ('OG1', 'THR', 'CD2', 'HIS', 10.19), ('OG1', 'THR', 'CE1', 'HIS', 9.48), ('OG1', 'THR', 'NE2', 'HIS', 9.0)], [('CG2', 'THR', 'CB', 'HIS', 14.8), ('CG2', 'THR', 'CG', 'HIS', 13.31), ('CG2', 'THR', 'ND1', 'HIS', 12.83), ('CG2', 'THR', 'CD2', 'HIS', 12.32), ('CG2', 'THR', 'CE1', 'HIS', 11.52), ('CG2', 'THR', 'NE2', 'HIS', 11.1)], [('O', 'THR', 'CB', 'HIS', 14.95), ('O', 'THR', 'CG', 'HIS', 13.46), ('O', 'THR', 'ND1', 'HIS', 12.69), ('O', 'THR', 'CD2', 'HIS', 12.71), ('O', 'THR', 'CE1', 'HIS', 11.43), ('O', 'THR', 'NE2', 'HIS', 11.38)], [('C', 'THR', 'CB', 'HIS', 13.88), ('C', 'THR', 'CG', 'HIS', 12.4), ('C', 'THR', 'ND1', 'HIS', 11.69), ('C', 'THR', 'CD2', 'HIS', 11.6), ('C', 'THR', 'CE1', 'HIS', 10.42), ('C', 'THR', 'NE2', 'HIS', 10.29)], [('CA', 'THR', 'CB', 'HIS', 12.93), ('CA', 'THR', 'CG', 'HIS', 11.43), ('CA', 'THR', 'ND1', 'HIS', 10.76), ('CA', 'THR', 'CD2', 'HIS', 10.6), ('CA', 'THR', 'CE1', 'HIS', 9.46), ('CA', 'THR', 'NE2', 'HIS', 9.28)], [('N', 'THR', 'CB', 'HIS', 11.53), ('N', 'THR', 'CG', 'HIS', 10.03), ('N', 'THR', 'ND1', 'HIS', 9.37), ('N', 'THR', 'CD2', 'HIS', 9.23), ('N', 'THR', 'CE1', 'HIS', 8.07), ('N', 'THR', 'NE2', 'HIS', 7.9)]]}
THR_TRP = { 
	'distances':
		[[6.22, 7.44, 7.89, 8.6, 9.18, 9.57, 9.18, 10.86, 10.51, 11.27, 8.22, 8.02, 6.73, 5.94], [5.55, 6.67, 7.25, 7.65, 8.42, 8.65, 8.12, 9.86, 9.39, 10.19, 7.65, 7.57, 6.45, 5.91], [6.77, 7.72, 7.82, 8.98, 9.08, 9.72, 9.79, 11.05, 11.09, 11.66, 9.2, 8.78, 7.37, 6.87], [9.4, 10.6, 10.88, 11.8, 12.17, 12.7, 12.39, 14.0, 13.7, 14.46, 11.21, 11.04, 9.72, 8.72], [8.57, 9.88, 10.31, 11.05, 11.62, 12.05, 11.54, 13.34, 12.88, 13.72, 10.13, 10.04, 8.79, 7.68], [7.55, 8.84, 9.38, 9.89, 10.63, 10.93, 10.31, 12.17, 11.6, 12.47, 9.18, 9.18, 8.0, 6.99], [7.55, 8.95, 9.73, 9.86, 10.95, 11.05, 10.04, 12.22, 11.31, 12.33, 8.58, 8.82, 7.85, 6.66]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'TRP', 6.22), ('CB', 'THR', 'CG', 'TRP', 7.44), ('CB', 'THR', 'CD1', 'TRP', 7.89), ('CB', 'THR', 'CD2', 'TRP', 8.6), ('CB', 'THR', 'NE1', 'TRP', 9.18), ('CB', 'THR', 'CE2', 'TRP', 9.57), ('CB', 'THR', 'CE3', 'TRP', 9.18), ('CB', 'THR', 'CZ2', 'TRP', 10.86), ('CB', 'THR', 'CZ3', 'TRP', 10.51), ('CB', 'THR', 'CH2', 'TRP', 11.27), ('CB', 'THR', 'O', 'TRP', 8.22), ('CB', 'THR', 'C', 'TRP', 8.02), ('CB', 'THR', 'CA', 'TRP', 6.73), ('CB', 'THR', 'N', 'TRP', 5.94)], [('OG1', 'THR', 'CB', 'TRP', 5.55), ('OG1', 'THR', 'CG', 'TRP', 6.67), ('OG1', 'THR', 'CD1', 'TRP', 7.25), ('OG1', 'THR', 'CD2', 'TRP', 7.65), ('OG1', 'THR', 'NE1', 'TRP', 8.42), ('OG1', 'THR', 'CE2', 'TRP', 8.65), ('OG1', 'THR', 'CE3', 'TRP', 8.12), ('OG1', 'THR', 'CZ2', 'TRP', 9.86), ('OG1', 'THR', 'CZ3', 'TRP', 9.39), ('OG1', 'THR', 'CH2', 'TRP', 10.19), ('OG1', 'THR', 'O', 'TRP', 7.65), ('OG1', 'THR', 'C', 'TRP', 7.57), ('OG1', 'THR', 'CA', 'TRP', 6.45), ('OG1', 'THR', 'N', 'TRP', 5.91)], [('CG2', 'THR', 'CB', 'TRP', 6.77), ('CG2', 'THR', 'CG', 'TRP', 7.72), ('CG2', 'THR', 'CD1', 'TRP', 7.82), ('CG2', 'THR', 'CD2', 'TRP', 8.98), ('CG2', 'THR', 'NE1', 'TRP', 9.08), ('CG2', 'THR', 'CE2', 'TRP', 9.72), ('CG2', 'THR', 'CE3', 'TRP', 9.79), ('CG2', 'THR', 'CZ2', 'TRP', 11.05), ('CG2', 'THR', 'CZ3', 'TRP', 11.09), ('CG2', 'THR', 'CH2', 'TRP', 11.66), ('CG2', 'THR', 'O', 'TRP', 9.2), ('CG2', 'THR', 'C', 'TRP', 8.78), ('CG2', 'THR', 'CA', 'TRP', 7.37), ('CG2', 'THR', 'N', 'TRP', 6.87)], [('O', 'THR', 'CB', 'TRP', 9.4), ('O', 'THR', 'CG', 'TRP', 10.6), ('O', 'THR', 'CD1', 'TRP', 10.88), ('O', 'THR', 'CD2', 'TRP', 11.8), ('O', 'THR', 'NE1', 'TRP', 12.17), ('O', 'THR', 'CE2', 'TRP', 12.7), ('O', 'THR', 'CE3', 'TRP', 12.39), ('O', 'THR', 'CZ2', 'TRP', 14.0), ('O', 'THR', 'CZ3', 'TRP', 13.7), ('O', 'THR', 'CH2', 'TRP', 14.46), ('O', 'THR', 'O', 'TRP', 11.21), ('O', 'THR', 'C', 'TRP', 11.04), ('O', 'THR', 'CA', 'TRP', 9.72), ('O', 'THR', 'N', 'TRP', 8.72)], [('C', 'THR', 'CB', 'TRP', 8.57), ('C', 'THR', 'CG', 'TRP', 9.88), ('C', 'THR', 'CD1', 'TRP', 10.31), ('C', 'THR', 'CD2', 'TRP', 11.05), ('C', 'THR', 'NE1', 'TRP', 11.62), ('C', 'THR', 'CE2', 'TRP', 12.05), ('C', 'THR', 'CE3', 'TRP', 11.54), ('C', 'THR', 'CZ2', 'TRP', 13.34), ('C', 'THR', 'CZ3', 'TRP', 12.88), ('C', 'THR', 'CH2', 'TRP', 13.72), ('C', 'THR', 'O', 'TRP', 10.13), ('C', 'THR', 'C', 'TRP', 10.04), ('C', 'THR', 'CA', 'TRP', 8.79), ('C', 'THR', 'N', 'TRP', 7.68)], [('CA', 'THR', 'CB', 'TRP', 7.55), ('CA', 'THR', 'CG', 'TRP', 8.84), ('CA', 'THR', 'CD1', 'TRP', 9.38), ('CA', 'THR', 'CD2', 'TRP', 9.89), ('CA', 'THR', 'NE1', 'TRP', 10.63), ('CA', 'THR', 'CE2', 'TRP', 10.93), ('CA', 'THR', 'CE3', 'TRP', 10.31), ('CA', 'THR', 'CZ2', 'TRP', 12.17), ('CA', 'THR', 'CZ3', 'TRP', 11.6), ('CA', 'THR', 'CH2', 'TRP', 12.47), ('CA', 'THR', 'O', 'TRP', 9.18), ('CA', 'THR', 'C', 'TRP', 9.18), ('CA', 'THR', 'CA', 'TRP', 8.0), ('CA', 'THR', 'N', 'TRP', 6.99)], [('N', 'THR', 'CB', 'TRP', 7.55), ('N', 'THR', 'CG', 'TRP', 8.95), ('N', 'THR', 'CD1', 'TRP', 9.73), ('N', 'THR', 'CD2', 'TRP', 9.86), ('N', 'THR', 'NE1', 'TRP', 10.95), ('N', 'THR', 'CE2', 'TRP', 11.05), ('N', 'THR', 'CE3', 'TRP', 10.04), ('N', 'THR', 'CZ2', 'TRP', 12.22), ('N', 'THR', 'CZ3', 'TRP', 11.31), ('N', 'THR', 'CH2', 'TRP', 12.33), ('N', 'THR', 'O', 'TRP', 8.58), ('N', 'THR', 'C', 'TRP', 8.82), ('N', 'THR', 'CA', 'TRP', 7.85), ('N', 'THR', 'N', 'TRP', 6.66)]]}
THR_ASP = { 
	'distances':
		[[15.57, 14.15, 13.84, 13.38], [14.91, 13.47, 13.04, 12.82], [16.98, 15.56, 15.24, 14.8], [16.51, 15.21, 15.19, 14.25], [15.68, 14.35, 14.3, 13.39], [14.78, 13.41, 13.24, 12.55], [13.49, 12.11, 11.96, 11.22]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ASP', 15.57), ('CB', 'THR', 'CG', 'ASP', 14.15), ('CB', 'THR', 'OD1', 'ASP', 13.84), ('CB', 'THR', 'OD2', 'ASP', 13.38)], [('OG1', 'THR', 'CB', 'ASP', 14.91), ('OG1', 'THR', 'CG', 'ASP', 13.47), ('OG1', 'THR', 'OD1', 'ASP', 13.04), ('OG1', 'THR', 'OD2', 'ASP', 12.82)], [('CG2', 'THR', 'CB', 'ASP', 16.98), ('CG2', 'THR', 'CG', 'ASP', 15.56), ('CG2', 'THR', 'OD1', 'ASP', 15.24), ('CG2', 'THR', 'OD2', 'ASP', 14.8)], [('O', 'THR', 'CB', 'ASP', 16.51), ('O', 'THR', 'CG', 'ASP', 15.21), ('O', 'THR', 'OD1', 'ASP', 15.19), ('O', 'THR', 'OD2', 'ASP', 14.25)], [('C', 'THR', 'CB', 'ASP', 15.68), ('C', 'THR', 'CG', 'ASP', 14.35), ('C', 'THR', 'OD1', 'ASP', 14.3), ('C', 'THR', 'OD2', 'ASP', 13.39)], [('CA', 'THR', 'CB', 'ASP', 14.78), ('CA', 'THR', 'CG', 'ASP', 13.41), ('CA', 'THR', 'OD1', 'ASP', 13.24), ('CA', 'THR', 'OD2', 'ASP', 12.55)], [('N', 'THR', 'CB', 'ASP', 13.49), ('N', 'THR', 'CG', 'ASP', 12.11), ('N', 'THR', 'OD1', 'ASP', 11.96), ('N', 'THR', 'OD2', 'ASP', 11.22)]]}
THR_SER = { 
	'distances':
		[[6.98, 7.16], [6.87, 6.67], [8.47, 8.63], [8.18, 8.67], [7.07, 7.65], [6.32, 6.59], [4.86, 5.24]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'SER', 6.98), ('CB', 'THR', 'OG', 'SER', 7.16)], [('OG1', 'THR', 'CB', 'SER', 6.87), ('OG1', 'THR', 'OG', 'SER', 6.67)], [('CG2', 'THR', 'CB', 'SER', 8.47), ('CG2', 'THR', 'OG', 'SER', 8.63)], [('O', 'THR', 'CB', 'SER', 8.18), ('O', 'THR', 'OG', 'SER', 8.67)], [('C', 'THR', 'CB', 'SER', 7.07), ('C', 'THR', 'OG', 'SER', 7.65)], [('CA', 'THR', 'CB', 'SER', 6.32), ('CA', 'THR', 'OG', 'SER', 6.59)], [('N', 'THR', 'CB', 'SER', 4.86), ('N', 'THR', 'OG', 'SER', 5.24)]]}
TRP_SER = { 
	'distances':
		[[8.45, 8.28], [9.87, 9.55], [10.97, 10.69], [10.43, 9.94], [12.06, 11.66], [11.8, 11.29], [10.16, 9.56], [12.77, 12.16], [11.27, 10.57], [12.54, 11.84], [8.16, 8.11], [8.86, 8.9], [8.44, 8.57], [7.18, 7.53]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'SER', 8.45), ('CB', 'TRP', 'OG', 'SER', 8.28)], [('CG', 'TRP', 'CB', 'SER', 9.87), ('CG', 'TRP', 'OG', 'SER', 9.55)], [('CD1', 'TRP', 'CB', 'SER', 10.97), ('CD1', 'TRP', 'OG', 'SER', 10.69)], [('CD2', 'TRP', 'CB', 'SER', 10.43), ('CD2', 'TRP', 'OG', 'SER', 9.94)], [('NE1', 'TRP', 'CB', 'SER', 12.06), ('NE1', 'TRP', 'OG', 'SER', 11.66)], [('CE2', 'TRP', 'CB', 'SER', 11.8), ('CE2', 'TRP', 'OG', 'SER', 11.29)], [('CE3', 'TRP', 'CB', 'SER', 10.16), ('CE3', 'TRP', 'OG', 'SER', 9.56)], [('CZ2', 'TRP', 'CB', 'SER', 12.77), ('CZ2', 'TRP', 'OG', 'SER', 12.16)], [('CZ3', 'TRP', 'CB', 'SER', 11.27), ('CZ3', 'TRP', 'OG', 'SER', 10.57)], [('CH2', 'TRP', 'CB', 'SER', 12.54), ('CH2', 'TRP', 'OG', 'SER', 11.84)], [('O', 'TRP', 'CB', 'SER', 8.16), ('O', 'TRP', 'OG', 'SER', 8.11)], [('C', 'TRP', 'CB', 'SER', 8.86), ('C', 'TRP', 'OG', 'SER', 8.9)], [('CA', 'TRP', 'CB', 'SER', 8.44), ('CA', 'TRP', 'OG', 'SER', 8.57)], [('N', 'TRP', 'CB', 'SER', 7.18), ('N', 'TRP', 'OG', 'SER', 7.53)]]}
TRP_ASP = { 
	'distances':
		[[16.0, 14.51, 13.84, 14.05], [16.92, 15.44, 14.67, 15.09], [18.19, 16.72, 15.95, 16.36], [16.68, 15.24, 14.36, 15.02], [18.76, 17.31, 16.45, 17.05], [17.92, 16.49, 15.57, 16.32], [15.7, 14.28, 13.34, 14.15], [18.22, 16.84, 15.84, 16.78], [16.02, 14.65, 13.62, 14.66], [17.34, 15.99, 14.94, 16.02], [14.79, 13.33, 12.64, 12.96], [15.97, 14.5, 13.82, 14.09], [16.27, 14.78, 14.18, 14.26], [15.46, 13.98, 13.5, 13.35]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'ASP', 16.0), ('CB', 'TRP', 'CG', 'ASP', 14.51), ('CB', 'TRP', 'OD1', 'ASP', 13.84), ('CB', 'TRP', 'OD2', 'ASP', 14.05)], [('CG', 'TRP', 'CB', 'ASP', 16.92), ('CG', 'TRP', 'CG', 'ASP', 15.44), ('CG', 'TRP', 'OD1', 'ASP', 14.67), ('CG', 'TRP', 'OD2', 'ASP', 15.09)], [('CD1', 'TRP', 'CB', 'ASP', 18.19), ('CD1', 'TRP', 'CG', 'ASP', 16.72), ('CD1', 'TRP', 'OD1', 'ASP', 15.95), ('CD1', 'TRP', 'OD2', 'ASP', 16.36)], [('CD2', 'TRP', 'CB', 'ASP', 16.68), ('CD2', 'TRP', 'CG', 'ASP', 15.24), ('CD2', 'TRP', 'OD1', 'ASP', 14.36), ('CD2', 'TRP', 'OD2', 'ASP', 15.02)], [('NE1', 'TRP', 'CB', 'ASP', 18.76), ('NE1', 'TRP', 'CG', 'ASP', 17.31), ('NE1', 'TRP', 'OD1', 'ASP', 16.45), ('NE1', 'TRP', 'OD2', 'ASP', 17.05)], [('CE2', 'TRP', 'CB', 'ASP', 17.92), ('CE2', 'TRP', 'CG', 'ASP', 16.49), ('CE2', 'TRP', 'OD1', 'ASP', 15.57), ('CE2', 'TRP', 'OD2', 'ASP', 16.32)], [('CE3', 'TRP', 'CB', 'ASP', 15.7), ('CE3', 'TRP', 'CG', 'ASP', 14.28), ('CE3', 'TRP', 'OD1', 'ASP', 13.34), ('CE3', 'TRP', 'OD2', 'ASP', 14.15)], [('CZ2', 'TRP', 'CB', 'ASP', 18.22), ('CZ2', 'TRP', 'CG', 'ASP', 16.84), ('CZ2', 'TRP', 'OD1', 'ASP', 15.84), ('CZ2', 'TRP', 'OD2', 'ASP', 16.78)], [('CZ3', 'TRP', 'CB', 'ASP', 16.02), ('CZ3', 'TRP', 'CG', 'ASP', 14.65), ('CZ3', 'TRP', 'OD1', 'ASP', 13.62), ('CZ3', 'TRP', 'OD2', 'ASP', 14.66)], [('CH2', 'TRP', 'CB', 'ASP', 17.34), ('CH2', 'TRP', 'CG', 'ASP', 15.99), ('CH2', 'TRP', 'OD1', 'ASP', 14.94), ('CH2', 'TRP', 'OD2', 'ASP', 16.02)], [('O', 'TRP', 'CB', 'ASP', 14.79), ('O', 'TRP', 'CG', 'ASP', 13.33), ('O', 'TRP', 'OD1', 'ASP', 12.64), ('O', 'TRP', 'OD2', 'ASP', 12.96)], [('C', 'TRP', 'CB', 'ASP', 15.97), ('C', 'TRP', 'CG', 'ASP', 14.5), ('C', 'TRP', 'OD1', 'ASP', 13.82), ('C', 'TRP', 'OD2', 'ASP', 14.09)], [('CA', 'TRP', 'CB', 'ASP', 16.27), ('CA', 'TRP', 'CG', 'ASP', 14.78), ('CA', 'TRP', 'OD1', 'ASP', 14.18), ('CA', 'TRP', 'OD2', 'ASP', 14.26)], [('N', 'TRP', 'CB', 'ASP', 15.46), ('N', 'TRP', 'CG', 'ASP', 13.98), ('N', 'TRP', 'OD1', 'ASP', 13.5), ('N', 'TRP', 'OD2', 'ASP', 13.35)]]}
SER_HIS = { 
	'distances':
		[[8.84, 7.37, 6.76, 6.65, 5.53, 5.37], [8.37, 6.88, 6.22, 6.19, 4.9, 4.81]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 8.84), ('CB', 'SER', 'CG', 'HIS', 7.37), ('CB', 'SER', 'ND1', 'HIS', 6.76), ('CB', 'SER', 'CD2', 'HIS', 6.65), ('CB', 'SER', 'CE1', 'HIS', 5.53), ('CB', 'SER', 'NE2', 'HIS', 5.37)], [('OG', 'SER', 'CB', 'HIS', 8.37), ('OG', 'SER', 'CG', 'HIS', 6.88), ('OG', 'SER', 'ND1', 'HIS', 6.22), ('OG', 'SER', 'CD2', 'HIS', 6.19), ('OG', 'SER', 'CE1', 'HIS', 4.9), ('OG', 'SER', 'NE2', 'HIS', 4.81)]]}
SER_ASP = { 
	'distances':
		[[11.15, 9.75, 9.67, 8.83], [10.48, 9.04, 8.8, 8.27]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 11.15), ('CB', 'SER', 'CG', 'ASP', 9.75), ('CB', 'SER', 'OD1', 'ASP', 9.67), ('CB', 'SER', 'OD2', 'ASP', 8.83)], [('OG', 'SER', 'CB', 'ASP', 10.48), ('OG', 'SER', 'CG', 'ASP', 9.04), ('OG', 'SER', 'OD1', 'ASP', 8.8), ('OG', 'SER', 'OD2', 'ASP', 8.27)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TRP_HIS, d, 'A_1a8s_1_11_1_10')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'A_1a8s_1_11_1_10')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(THR_HIS, d, 'A_1a8s_1_11_1_10')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(THR_TRP, d, 'A_1a8s_1_11_1_10')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(THR_ASP, d, 'A_1a8s_1_11_1_10')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(THR_SER, d, 'A_1a8s_1_11_1_10')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(TRP_SER, d, 'A_1a8s_1_11_1_10')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(TRP_ASP, d, 'A_1a8s_1_11_1_10')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(SER_HIS, d, 'A_1a8s_1_11_1_10')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(SER_ASP, d, 'A_1a8s_1_11_1_10')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TRP_HIS' :  match1,
		'ASP_HIS' :  match2,
		'THR_HIS' :  match3,
		'THR_TRP' :  match4,
		'THR_ASP' :  match5,
		'THR_SER' :  match6,
		'TRP_SER' :  match7,
		'TRP_ASP' :  match8,
		'SER_HIS' :  match9,
		'SER_ASP' :  match10}