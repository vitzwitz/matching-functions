'''
FUNC:A_1kra_3_5_1_5
PDB:1kra
EC:3.5.1.5
RESI:his,asp,his,arg
LOCI:c-219,221,320,336;
'''
import motifFunctions as cmd
HIS_ARG = { 
	'distances':
		[[16.45, 15.09, 14.08, 13.34, 12.18, 11.63, 11.76], [15.24, 13.94, 12.87, 12.06, 10.86, 10.35, 10.38], [14.46, 13.19, 12.04, 11.31, 10.08, 9.42, 9.7], [14.82, 13.55, 12.52, 11.56, 10.37, 10.05, 9.72], [13.53, 12.32, 11.13, 10.29, 9.02, 8.46, 8.55], [13.74, 12.53, 11.43, 10.44, 9.21, 8.87, 8.53], [11.57, 11.01, 9.52, 8.97, 7.87, 7.14, 7.79], [10.93, 10.24, 8.77, 8.02, 6.81, 6.22, 6.53], [11.71, 10.87, 9.45, 8.58, 7.28, 6.73, 6.81], [9.8, 9.14, 7.72, 6.83, 5.65, 5.33, 5.28], [11.21, 10.3, 8.98, 7.94, 6.63, 6.32, 5.93], [10.03, 9.22, 7.9, 6.8, 5.53, 5.44, 4.79]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 16.45), ('CB', 'HIS', 'CG', 'ARG', 15.09), ('CB', 'HIS', 'CD', 'ARG', 14.08), ('CB', 'HIS', 'NE', 'ARG', 13.34), ('CB', 'HIS', 'CZ', 'ARG', 12.18), ('CB', 'HIS', 'NH1', 'ARG', 11.63), ('CB', 'HIS', 'NH2', 'ARG', 11.76)], [('CG', 'HIS', 'CB', 'ARG', 15.24), ('CG', 'HIS', 'CG', 'ARG', 13.94), ('CG', 'HIS', 'CD', 'ARG', 12.87), ('CG', 'HIS', 'NE', 'ARG', 12.06), ('CG', 'HIS', 'CZ', 'ARG', 10.86), ('CG', 'HIS', 'NH1', 'ARG', 10.35), ('CG', 'HIS', 'NH2', 'ARG', 10.38)], [('ND1', 'HIS', 'CB', 'ARG', 14.46), ('ND1', 'HIS', 'CG', 'ARG', 13.19), ('ND1', 'HIS', 'CD', 'ARG', 12.04), ('ND1', 'HIS', 'NE', 'ARG', 11.31), ('ND1', 'HIS', 'CZ', 'ARG', 10.08), ('ND1', 'HIS', 'NH1', 'ARG', 9.42), ('ND1', 'HIS', 'NH2', 'ARG', 9.7)], [('CD2', 'HIS', 'CB', 'ARG', 14.82), ('CD2', 'HIS', 'CG', 'ARG', 13.55), ('CD2', 'HIS', 'CD', 'ARG', 12.52), ('CD2', 'HIS', 'NE', 'ARG', 11.56), ('CD2', 'HIS', 'CZ', 'ARG', 10.37), ('CD2', 'HIS', 'NH1', 'ARG', 10.05), ('CD2', 'HIS', 'NH2', 'ARG', 9.72)], [('CE1', 'HIS', 'CB', 'ARG', 13.53), ('CE1', 'HIS', 'CG', 'ARG', 12.32), ('CE1', 'HIS', 'CD', 'ARG', 11.13), ('CE1', 'HIS', 'NE', 'ARG', 10.29), ('CE1', 'HIS', 'CZ', 'ARG', 9.02), ('CE1', 'HIS', 'NH1', 'ARG', 8.46), ('CE1', 'HIS', 'NH2', 'ARG', 8.55)], [('NE2', 'HIS', 'CB', 'ARG', 13.74), ('NE2', 'HIS', 'CG', 'ARG', 12.53), ('NE2', 'HIS', 'CD', 'ARG', 11.43), ('NE2', 'HIS', 'NE', 'ARG', 10.44), ('NE2', 'HIS', 'CZ', 'ARG', 9.21), ('NE2', 'HIS', 'NH1', 'ARG', 8.87), ('NE2', 'HIS', 'NH2', 'ARG', 8.53)], [('CB', 'HIS', 'CB', 'ARG', 11.57), ('CB', 'HIS', 'CG', 'ARG', 11.01), ('CB', 'HIS', 'CD', 'ARG', 9.52), ('CB', 'HIS', 'NE', 'ARG', 8.97), ('CB', 'HIS', 'CZ', 'ARG', 7.87), ('CB', 'HIS', 'NH1', 'ARG', 7.14), ('CB', 'HIS', 'NH2', 'ARG', 7.79)], [('CG', 'HIS', 'CB', 'ARG', 10.93), ('CG', 'HIS', 'CG', 'ARG', 10.24), ('CG', 'HIS', 'CD', 'ARG', 8.77), ('CG', 'HIS', 'NE', 'ARG', 8.02), ('CG', 'HIS', 'CZ', 'ARG', 6.81), ('CG', 'HIS', 'NH1', 'ARG', 6.22), ('CG', 'HIS', 'NH2', 'ARG', 6.53)], [('ND1', 'HIS', 'CB', 'ARG', 11.71), ('ND1', 'HIS', 'CG', 'ARG', 10.87), ('ND1', 'HIS', 'CD', 'ARG', 9.45), ('ND1', 'HIS', 'NE', 'ARG', 8.58), ('ND1', 'HIS', 'CZ', 'ARG', 7.28), ('ND1', 'HIS', 'NH1', 'ARG', 6.73), ('ND1', 'HIS', 'NH2', 'ARG', 6.81)], [('CD2', 'HIS', 'CB', 'ARG', 9.8), ('CD2', 'HIS', 'CG', 'ARG', 9.14), ('CD2', 'HIS', 'CD', 'ARG', 7.72), ('CD2', 'HIS', 'NE', 'ARG', 6.83), ('CD2', 'HIS', 'CZ', 'ARG', 5.65), ('CD2', 'HIS', 'NH1', 'ARG', 5.33), ('CD2', 'HIS', 'NH2', 'ARG', 5.28)], [('CE1', 'HIS', 'CB', 'ARG', 11.21), ('CE1', 'HIS', 'CG', 'ARG', 10.3), ('CE1', 'HIS', 'CD', 'ARG', 8.98), ('CE1', 'HIS', 'NE', 'ARG', 7.94), ('CE1', 'HIS', 'CZ', 'ARG', 6.63), ('CE1', 'HIS', 'NH1', 'ARG', 6.32), ('CE1', 'HIS', 'NH2', 'ARG', 5.93)], [('NE2', 'HIS', 'CB', 'ARG', 10.03), ('NE2', 'HIS', 'CG', 'ARG', 9.22), ('NE2', 'HIS', 'CD', 'ARG', 7.9), ('NE2', 'HIS', 'NE', 'ARG', 6.8), ('NE2', 'HIS', 'CZ', 'ARG', 5.53), ('NE2', 'HIS', 'NH1', 'ARG', 5.44), ('NE2', 'HIS', 'NH2', 'ARG', 4.79)]]}
ARG_HISI = { 
	'distances':
		[[11.57, 10.93, 11.71, 9.8, 11.21, 10.03], [11.01, 10.24, 10.87, 9.14, 10.3, 9.22], [9.52, 8.77, 9.45, 7.72, 8.98, 7.9], [8.97, 8.02, 8.58, 6.83, 7.94, 6.8], [7.87, 6.81, 7.28, 5.65, 6.63, 5.53], [7.14, 6.22, 6.73, 5.33, 6.32, 5.44], [7.79, 6.53, 6.81, 5.28, 5.93, 4.79]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'HISI', 11.57), ('CB', 'ARG', 'CG', 'HISI', 10.93), ('CB', 'ARG', 'ND1', 'HISI', 11.71), ('CB', 'ARG', 'CD2', 'HISI', 9.8), ('CB', 'ARG', 'CE1', 'HISI', 11.21), ('CB', 'ARG', 'NE2', 'HISI', 10.03)], [('CG', 'ARG', 'CB', 'HISI', 11.01), ('CG', 'ARG', 'CG', 'HISI', 10.24), ('CG', 'ARG', 'ND1', 'HISI', 10.87), ('CG', 'ARG', 'CD2', 'HISI', 9.14), ('CG', 'ARG', 'CE1', 'HISI', 10.3), ('CG', 'ARG', 'NE2', 'HISI', 9.22)], [('CD', 'ARG', 'CB', 'HISI', 9.52), ('CD', 'ARG', 'CG', 'HISI', 8.77), ('CD', 'ARG', 'ND1', 'HISI', 9.45), ('CD', 'ARG', 'CD2', 'HISI', 7.72), ('CD', 'ARG', 'CE1', 'HISI', 8.98), ('CD', 'ARG', 'NE2', 'HISI', 7.9)], [('NE', 'ARG', 'CB', 'HISI', 8.97), ('NE', 'ARG', 'CG', 'HISI', 8.02), ('NE', 'ARG', 'ND1', 'HISI', 8.58), ('NE', 'ARG', 'CD2', 'HISI', 6.83), ('NE', 'ARG', 'CE1', 'HISI', 7.94), ('NE', 'ARG', 'NE2', 'HISI', 6.8)], [('CZ', 'ARG', 'CB', 'HISI', 7.87), ('CZ', 'ARG', 'CG', 'HISI', 6.81), ('CZ', 'ARG', 'ND1', 'HISI', 7.28), ('CZ', 'ARG', 'CD2', 'HISI', 5.65), ('CZ', 'ARG', 'CE1', 'HISI', 6.63), ('CZ', 'ARG', 'NE2', 'HISI', 5.53)], [('NH1', 'ARG', 'CB', 'HISI', 7.14), ('NH1', 'ARG', 'CG', 'HISI', 6.22), ('NH1', 'ARG', 'ND1', 'HISI', 6.73), ('NH1', 'ARG', 'CD2', 'HISI', 5.33), ('NH1', 'ARG', 'CE1', 'HISI', 6.32), ('NH1', 'ARG', 'NE2', 'HISI', 5.44)], [('NH2', 'ARG', 'CB', 'HISI', 7.79), ('NH2', 'ARG', 'CG', 'HISI', 6.53), ('NH2', 'ARG', 'ND1', 'HISI', 6.81), ('NH2', 'ARG', 'CD2', 'HISI', 5.28), ('NH2', 'ARG', 'CE1', 'HISI', 5.93), ('NH2', 'ARG', 'NE2', 'HISI', 4.79)]]}
HIS_ASP = { 
	'distances':
		[[7.03, 7.65, 7.8, 8.37], [6.52, 6.78, 6.88, 7.36], [5.37, 5.45, 5.5, 6.12], [7.39, 7.36, 7.43, 7.72], [5.81, 5.37, 5.33, 5.75], [7.02, 6.62, 6.62, 6.83], [8.15, 6.71, 6.66, 5.89], [8.06, 6.58, 6.38, 5.9], [7.2, 5.81, 5.76, 5.17], [9.1, 7.62, 7.22, 7.09], [7.88, 6.59, 6.37, 6.17], [8.98, 7.61, 7.2, 7.2]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.03), ('CB', 'HIS', 'CG', 'ASP', 7.65), ('CB', 'HIS', 'OD1', 'ASP', 7.8), ('CB', 'HIS', 'OD2', 'ASP', 8.37)], [('CG', 'HIS', 'CB', 'ASP', 6.52), ('CG', 'HIS', 'CG', 'ASP', 6.78), ('CG', 'HIS', 'OD1', 'ASP', 6.88), ('CG', 'HIS', 'OD2', 'ASP', 7.36)], [('ND1', 'HIS', 'CB', 'ASP', 5.37), ('ND1', 'HIS', 'CG', 'ASP', 5.45), ('ND1', 'HIS', 'OD1', 'ASP', 5.5), ('ND1', 'HIS', 'OD2', 'ASP', 6.12)], [('CD2', 'HIS', 'CB', 'ASP', 7.39), ('CD2', 'HIS', 'CG', 'ASP', 7.36), ('CD2', 'HIS', 'OD1', 'ASP', 7.43), ('CD2', 'HIS', 'OD2', 'ASP', 7.72)], [('CE1', 'HIS', 'CB', 'ASP', 5.81), ('CE1', 'HIS', 'CG', 'ASP', 5.37), ('CE1', 'HIS', 'OD1', 'ASP', 5.33), ('CE1', 'HIS', 'OD2', 'ASP', 5.75)], [('NE2', 'HIS', 'CB', 'ASP', 7.02), ('NE2', 'HIS', 'CG', 'ASP', 6.62), ('NE2', 'HIS', 'OD1', 'ASP', 6.62), ('NE2', 'HIS', 'OD2', 'ASP', 6.83)], [('CB', 'HIS', 'CB', 'ASP', 8.15), ('CB', 'HIS', 'CG', 'ASP', 6.71), ('CB', 'HIS', 'OD1', 'ASP', 6.66), ('CB', 'HIS', 'OD2', 'ASP', 5.89)], [('CG', 'HIS', 'CB', 'ASP', 8.06), ('CG', 'HIS', 'CG', 'ASP', 6.58), ('CG', 'HIS', 'OD1', 'ASP', 6.38), ('CG', 'HIS', 'OD2', 'ASP', 5.9)], [('ND1', 'HIS', 'CB', 'ASP', 7.2), ('ND1', 'HIS', 'CG', 'ASP', 5.81), ('ND1', 'HIS', 'OD1', 'ASP', 5.76), ('ND1', 'HIS', 'OD2', 'ASP', 5.17)], [('CD2', 'HIS', 'CB', 'ASP', 9.1), ('CD2', 'HIS', 'CG', 'ASP', 7.62), ('CD2', 'HIS', 'OD1', 'ASP', 7.22), ('CD2', 'HIS', 'OD2', 'ASP', 7.09)], [('CE1', 'HIS', 'CB', 'ASP', 7.88), ('CE1', 'HIS', 'CG', 'ASP', 6.59), ('CE1', 'HIS', 'OD1', 'ASP', 6.37), ('CE1', 'HIS', 'OD2', 'ASP', 6.17)], [('NE2', 'HIS', 'CB', 'ASP', 8.98), ('NE2', 'HIS', 'CG', 'ASP', 7.61), ('NE2', 'HIS', 'OD1', 'ASP', 7.2), ('NE2', 'HIS', 'OD2', 'ASP', 7.2)]]}
ASP_ARG = { 
	'distances':
		[[15.32, 14.2, 12.87, 12.41, 11.16, 10.17, 11.07], [13.97, 12.91, 11.54, 11.05, 9.8, 8.8, 9.73], [12.94, 11.84, 10.5, 10.1, 8.9, 7.83, 8.97], [14.02, 13.07, 11.64, 11.06, 9.79, 8.87, 9.6]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 15.32), ('CB', 'ASP', 'CG', 'ARG', 14.2), ('CB', 'ASP', 'CD', 'ARG', 12.87), ('CB', 'ASP', 'NE', 'ARG', 12.41), ('CB', 'ASP', 'CZ', 'ARG', 11.16), ('CB', 'ASP', 'NH1', 'ARG', 10.17), ('CB', 'ASP', 'NH2', 'ARG', 11.07)], [('CG', 'ASP', 'CB', 'ARG', 13.97), ('CG', 'ASP', 'CG', 'ARG', 12.91), ('CG', 'ASP', 'CD', 'ARG', 11.54), ('CG', 'ASP', 'NE', 'ARG', 11.05), ('CG', 'ASP', 'CZ', 'ARG', 9.8), ('CG', 'ASP', 'NH1', 'ARG', 8.8), ('CG', 'ASP', 'NH2', 'ARG', 9.73)], [('OD1', 'ASP', 'CB', 'ARG', 12.94), ('OD1', 'ASP', 'CG', 'ARG', 11.84), ('OD1', 'ASP', 'CD', 'ARG', 10.5), ('OD1', 'ASP', 'NE', 'ARG', 10.1), ('OD1', 'ASP', 'CZ', 'ARG', 8.9), ('OD1', 'ASP', 'NH1', 'ARG', 7.83), ('OD1', 'ASP', 'NH2', 'ARG', 8.97)], [('OD2', 'ASP', 'CB', 'ARG', 14.02), ('OD2', 'ASP', 'CG', 'ARG', 13.07), ('OD2', 'ASP', 'CD', 'ARG', 11.64), ('OD2', 'ASP', 'NE', 'ARG', 11.06), ('OD2', 'ASP', 'CZ', 'ARG', 9.79), ('OD2', 'ASP', 'NH1', 'ARG', 8.87), ('OD2', 'ASP', 'NH2', 'ARG', 9.6)]]}
HIS_HIS = { 
	'distances':
		[[11.55, 10.71, 9.44, 11.18, 9.18, 10.3], [10.25, 9.32, 8.03, 9.74, 7.71, 8.83], [9.06, 8.24, 7.01, 8.77, 6.88, 8.02], [10.11, 9.02, 7.7, 9.29, 7.15, 8.22], [8.11, 7.13, 5.87, 7.57, 5.6, 6.75], [8.82, 7.68, 6.37, 7.92, 5.78, 6.87], [11.55, 10.25, 9.06, 10.11, 8.11, 8.82], [10.71, 9.32, 8.24, 9.02, 7.13, 7.68], [9.44, 8.03, 7.01, 7.7, 5.87, 6.37], [11.18, 9.74, 8.77, 9.29, 7.57, 7.92], [9.18, 7.71, 6.88, 7.15, 5.6, 5.78], [10.3, 8.83, 8.02, 8.22, 6.75, 6.87]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 11.55), ('CB', 'HIS', 'CG', 'HIS', 10.71), ('CB', 'HIS', 'ND1', 'HIS', 9.44), ('CB', 'HIS', 'CD2', 'HIS', 11.18), ('CB', 'HIS', 'CE1', 'HIS', 9.18), ('CB', 'HIS', 'NE2', 'HIS', 10.3)], [('CG', 'HIS', 'CB', 'HIS', 10.25), ('CG', 'HIS', 'CG', 'HIS', 9.32), ('CG', 'HIS', 'ND1', 'HIS', 8.03), ('CG', 'HIS', 'CD2', 'HIS', 9.74), ('CG', 'HIS', 'CE1', 'HIS', 7.71), ('CG', 'HIS', 'NE2', 'HIS', 8.83)], [('ND1', 'HIS', 'CB', 'HIS', 9.06), ('ND1', 'HIS', 'CG', 'HIS', 8.24), ('ND1', 'HIS', 'ND1', 'HIS', 7.01), ('ND1', 'HIS', 'CD2', 'HIS', 8.77), ('ND1', 'HIS', 'CE1', 'HIS', 6.88), ('ND1', 'HIS', 'NE2', 'HIS', 8.02)], [('CD2', 'HIS', 'CB', 'HIS', 10.11), ('CD2', 'HIS', 'CG', 'HIS', 9.02), ('CD2', 'HIS', 'ND1', 'HIS', 7.7), ('CD2', 'HIS', 'CD2', 'HIS', 9.29), ('CD2', 'HIS', 'CE1', 'HIS', 7.15), ('CD2', 'HIS', 'NE2', 'HIS', 8.22)], [('CE1', 'HIS', 'CB', 'HIS', 8.11), ('CE1', 'HIS', 'CG', 'HIS', 7.13), ('CE1', 'HIS', 'ND1', 'HIS', 5.87), ('CE1', 'HIS', 'CD2', 'HIS', 7.57), ('CE1', 'HIS', 'CE1', 'HIS', 5.6), ('CE1', 'HIS', 'NE2', 'HIS', 6.75)], [('NE2', 'HIS', 'CB', 'HIS', 8.82), ('NE2', 'HIS', 'CG', 'HIS', 7.68), ('NE2', 'HIS', 'ND1', 'HIS', 6.37), ('NE2', 'HIS', 'CD2', 'HIS', 7.92), ('NE2', 'HIS', 'CE1', 'HIS', 5.78), ('NE2', 'HIS', 'NE2', 'HIS', 6.87)], [('CB', 'HIS', 'CB', 'HIS', 11.55), ('CB', 'HIS', 'CG', 'HIS', 10.25), ('CB', 'HIS', 'ND1', 'HIS', 9.06), ('CB', 'HIS', 'CD2', 'HIS', 10.11), ('CB', 'HIS', 'CE1', 'HIS', 8.11), ('CB', 'HIS', 'NE2', 'HIS', 8.82)], [('CG', 'HIS', 'CB', 'HIS', 10.71), ('CG', 'HIS', 'CG', 'HIS', 9.32), ('CG', 'HIS', 'ND1', 'HIS', 8.24), ('CG', 'HIS', 'CD2', 'HIS', 9.02), ('CG', 'HIS', 'CE1', 'HIS', 7.13), ('CG', 'HIS', 'NE2', 'HIS', 7.68)], [('ND1', 'HIS', 'CB', 'HIS', 9.44), ('ND1', 'HIS', 'CG', 'HIS', 8.03), ('ND1', 'HIS', 'ND1', 'HIS', 7.01), ('ND1', 'HIS', 'CD2', 'HIS', 7.7), ('ND1', 'HIS', 'CE1', 'HIS', 5.87), ('ND1', 'HIS', 'NE2', 'HIS', 6.37)], [('CD2', 'HIS', 'CB', 'HIS', 11.18), ('CD2', 'HIS', 'CG', 'HIS', 9.74), ('CD2', 'HIS', 'ND1', 'HIS', 8.77), ('CD2', 'HIS', 'CD2', 'HIS', 9.29), ('CD2', 'HIS', 'CE1', 'HIS', 7.57), ('CD2', 'HIS', 'NE2', 'HIS', 7.92)], [('CE1', 'HIS', 'CB', 'HIS', 9.18), ('CE1', 'HIS', 'CG', 'HIS', 7.71), ('CE1', 'HIS', 'ND1', 'HIS', 6.88), ('CE1', 'HIS', 'CD2', 'HIS', 7.15), ('CE1', 'HIS', 'CE1', 'HIS', 5.6), ('CE1', 'HIS', 'NE2', 'HIS', 5.78)], [('NE2', 'HIS', 'CB', 'HIS', 10.3), ('NE2', 'HIS', 'CG', 'HIS', 8.83), ('NE2', 'HIS', 'ND1', 'HIS', 8.02), ('NE2', 'HIS', 'CD2', 'HIS', 8.22), ('NE2', 'HIS', 'CE1', 'HIS', 6.75), ('NE2', 'HIS', 'NE2', 'HIS', 6.87)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ARG, d, 'A_1kra_3_5_1_5')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_HISI, d, 'A_1kra_3_5_1_5')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASP, d, 'A_1kra_3_5_1_5')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_ARG, d, 'A_1kra_3_5_1_5')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_HIS, d, 'A_1kra_3_5_1_5')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ARG' :  match1,
		'ARG_HISI' :  match2,
		'HIS_ASP' :  match3,
		'ASP_ARG' :  match4,
		'HIS_HIS' :  match5}