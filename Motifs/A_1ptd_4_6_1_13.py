'''
FUNC:A_1ptd_4_6_1_13
PDB:1ptd
EC:4.6.1.13
RESI:his,arg,his,asp
LOCI:a-32,69,82,274;
'''
import motifFunctions as cmd
ASP_ARG = { 
	'distances':
		[[16.23, 14.95, 15.4, 14.38, 13.73, 14.06, 12.9], [15.13, 13.83, 14.24, 13.2, 12.46, 12.74, 11.62], [14.14, 12.8, 13.18, 12.11, 11.45, 11.81, 10.6], [15.3, 14.02, 14.45, 13.41, 12.56, 12.7, 11.73]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 16.23), ('CB', 'ASP', 'CG', 'ARG', 14.95), ('CB', 'ASP', 'CD', 'ARG', 15.4), ('CB', 'ASP', 'NE', 'ARG', 14.38), ('CB', 'ASP', 'CZ', 'ARG', 13.73), ('CB', 'ASP', 'NH1', 'ARG', 14.06), ('CB', 'ASP', 'NH2', 'ARG', 12.9)], [('CG', 'ASP', 'CB', 'ARG', 15.13), ('CG', 'ASP', 'CG', 'ARG', 13.83), ('CG', 'ASP', 'CD', 'ARG', 14.24), ('CG', 'ASP', 'NE', 'ARG', 13.2), ('CG', 'ASP', 'CZ', 'ARG', 12.46), ('CG', 'ASP', 'NH1', 'ARG', 12.74), ('CG', 'ASP', 'NH2', 'ARG', 11.62)], [('OD1', 'ASP', 'CB', 'ARG', 14.14), ('OD1', 'ASP', 'CG', 'ARG', 12.8), ('OD1', 'ASP', 'CD', 'ARG', 13.18), ('OD1', 'ASP', 'NE', 'ARG', 12.11), ('OD1', 'ASP', 'CZ', 'ARG', 11.45), ('OD1', 'ASP', 'NH1', 'ARG', 11.81), ('OD1', 'ASP', 'NH2', 'ARG', 10.6)], [('OD2', 'ASP', 'CB', 'ARG', 15.3), ('OD2', 'ASP', 'CG', 'ARG', 14.02), ('OD2', 'ASP', 'CD', 'ARG', 14.45), ('OD2', 'ASP', 'NE', 'ARG', 13.41), ('OD2', 'ASP', 'CZ', 'ARG', 12.56), ('OD2', 'ASP', 'NH1', 'ARG', 12.7), ('OD2', 'ASP', 'NH2', 'ARG', 11.73)]]}
HIS_ARG = { 
	'distances':
		[[12.31, 10.88, 10.97, 9.78, 9.34, 10.06, 8.39], [11.72, 10.27, 10.38, 9.17, 8.51, 9.08, 7.55], [11.87, 10.5, 10.79, 9.7, 8.94, 9.27, 8.1], [11.17, 9.7, 9.64, 8.35, 7.56, 8.12, 6.48], [11.45, 10.1, 10.37, 9.29, 8.36, 8.5, 7.55], [11.0, 9.59, 9.64, 8.44, 7.46, 7.72, 6.5], [8.79, 8.91, 10.18, 10.64, 10.22, 9.24, 10.99], [9.3, 9.14, 10.27, 10.49, 9.86, 8.85, 10.46], [9.43, 9.02, 10.12, 10.14, 9.44, 8.57, 9.86], [9.91, 9.72, 10.69, 10.83, 10.06, 8.93, 10.59], [10.07, 9.5, 10.43, 10.26, 9.38, 8.48, 9.64], [10.35, 9.91, 10.76, 10.68, 9.75, 8.7, 10.09]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 12.31), ('CB', 'HIS', 'CG', 'ARG', 10.88), ('CB', 'HIS', 'CD', 'ARG', 10.97), ('CB', 'HIS', 'NE', 'ARG', 9.78), ('CB', 'HIS', 'CZ', 'ARG', 9.34), ('CB', 'HIS', 'NH1', 'ARG', 10.06), ('CB', 'HIS', 'NH2', 'ARG', 8.39)], [('CG', 'HIS', 'CB', 'ARG', 11.72), ('CG', 'HIS', 'CG', 'ARG', 10.27), ('CG', 'HIS', 'CD', 'ARG', 10.38), ('CG', 'HIS', 'NE', 'ARG', 9.17), ('CG', 'HIS', 'CZ', 'ARG', 8.51), ('CG', 'HIS', 'NH1', 'ARG', 9.08), ('CG', 'HIS', 'NH2', 'ARG', 7.55)], [('ND1', 'HIS', 'CB', 'ARG', 11.87), ('ND1', 'HIS', 'CG', 'ARG', 10.5), ('ND1', 'HIS', 'CD', 'ARG', 10.79), ('ND1', 'HIS', 'NE', 'ARG', 9.7), ('ND1', 'HIS', 'CZ', 'ARG', 8.94), ('ND1', 'HIS', 'NH1', 'ARG', 9.27), ('ND1', 'HIS', 'NH2', 'ARG', 8.1)], [('CD2', 'HIS', 'CB', 'ARG', 11.17), ('CD2', 'HIS', 'CG', 'ARG', 9.7), ('CD2', 'HIS', 'CD', 'ARG', 9.64), ('CD2', 'HIS', 'NE', 'ARG', 8.35), ('CD2', 'HIS', 'CZ', 'ARG', 7.56), ('CD2', 'HIS', 'NH1', 'ARG', 8.12), ('CD2', 'HIS', 'NH2', 'ARG', 6.48)], [('CE1', 'HIS', 'CB', 'ARG', 11.45), ('CE1', 'HIS', 'CG', 'ARG', 10.1), ('CE1', 'HIS', 'CD', 'ARG', 10.37), ('CE1', 'HIS', 'NE', 'ARG', 9.29), ('CE1', 'HIS', 'CZ', 'ARG', 8.36), ('CE1', 'HIS', 'NH1', 'ARG', 8.5), ('CE1', 'HIS', 'NH2', 'ARG', 7.55)], [('NE2', 'HIS', 'CB', 'ARG', 11.0), ('NE2', 'HIS', 'CG', 'ARG', 9.59), ('NE2', 'HIS', 'CD', 'ARG', 9.64), ('NE2', 'HIS', 'NE', 'ARG', 8.44), ('NE2', 'HIS', 'CZ', 'ARG', 7.46), ('NE2', 'HIS', 'NH1', 'ARG', 7.72), ('NE2', 'HIS', 'NH2', 'ARG', 6.5)], [('CB', 'HIS', 'CB', 'ARG', 8.79), ('CB', 'HIS', 'CG', 'ARG', 8.91), ('CB', 'HIS', 'CD', 'ARG', 10.18), ('CB', 'HIS', 'NE', 'ARG', 10.64), ('CB', 'HIS', 'CZ', 'ARG', 10.22), ('CB', 'HIS', 'NH1', 'ARG', 9.24), ('CB', 'HIS', 'NH2', 'ARG', 10.99)], [('CG', 'HIS', 'CB', 'ARG', 9.3), ('CG', 'HIS', 'CG', 'ARG', 9.14), ('CG', 'HIS', 'CD', 'ARG', 10.27), ('CG', 'HIS', 'NE', 'ARG', 10.49), ('CG', 'HIS', 'CZ', 'ARG', 9.86), ('CG', 'HIS', 'NH1', 'ARG', 8.85), ('CG', 'HIS', 'NH2', 'ARG', 10.46)], [('ND1', 'HIS', 'CB', 'ARG', 9.43), ('ND1', 'HIS', 'CG', 'ARG', 9.02), ('ND1', 'HIS', 'CD', 'ARG', 10.12), ('ND1', 'HIS', 'NE', 'ARG', 10.14), ('ND1', 'HIS', 'CZ', 'ARG', 9.44), ('ND1', 'HIS', 'NH1', 'ARG', 8.57), ('ND1', 'HIS', 'NH2', 'ARG', 9.86)], [('CD2', 'HIS', 'CB', 'ARG', 9.91), ('CD2', 'HIS', 'CG', 'ARG', 9.72), ('CD2', 'HIS', 'CD', 'ARG', 10.69), ('CD2', 'HIS', 'NE', 'ARG', 10.83), ('CD2', 'HIS', 'CZ', 'ARG', 10.06), ('CD2', 'HIS', 'NH1', 'ARG', 8.93), ('CD2', 'HIS', 'NH2', 'ARG', 10.59)], [('CE1', 'HIS', 'CB', 'ARG', 10.07), ('CE1', 'HIS', 'CG', 'ARG', 9.5), ('CE1', 'HIS', 'CD', 'ARG', 10.43), ('CE1', 'HIS', 'NE', 'ARG', 10.26), ('CE1', 'HIS', 'CZ', 'ARG', 9.38), ('CE1', 'HIS', 'NH1', 'ARG', 8.48), ('CE1', 'HIS', 'NH2', 'ARG', 9.64)], [('NE2', 'HIS', 'CB', 'ARG', 10.35), ('NE2', 'HIS', 'CG', 'ARG', 9.91), ('NE2', 'HIS', 'CD', 'ARG', 10.76), ('NE2', 'HIS', 'NE', 'ARG', 10.68), ('NE2', 'HIS', 'CZ', 'ARG', 9.75), ('NE2', 'HIS', 'NH1', 'ARG', 8.7), ('NE2', 'HIS', 'NH2', 'ARG', 10.09)]]}
ARG_HISI = { 
	'distances':
		[[8.79, 9.3, 9.43, 9.91, 10.07, 10.35], [8.91, 9.14, 9.02, 9.72, 9.5, 9.91], [10.18, 10.27, 10.12, 10.69, 10.43, 10.76], [10.64, 10.49, 10.14, 10.83, 10.26, 10.68], [10.22, 9.86, 9.44, 10.06, 9.38, 9.75], [9.24, 8.85, 8.57, 8.93, 8.48, 8.7], [10.99, 10.46, 9.86, 10.59, 9.64, 10.09]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'HISI', 8.79), ('CB', 'ARG', 'CG', 'HISI', 9.3), ('CB', 'ARG', 'ND1', 'HISI', 9.43), ('CB', 'ARG', 'CD2', 'HISI', 9.91), ('CB', 'ARG', 'CE1', 'HISI', 10.07), ('CB', 'ARG', 'NE2', 'HISI', 10.35)], [('CG', 'ARG', 'CB', 'HISI', 8.91), ('CG', 'ARG', 'CG', 'HISI', 9.14), ('CG', 'ARG', 'ND1', 'HISI', 9.02), ('CG', 'ARG', 'CD2', 'HISI', 9.72), ('CG', 'ARG', 'CE1', 'HISI', 9.5), ('CG', 'ARG', 'NE2', 'HISI', 9.91)], [('CD', 'ARG', 'CB', 'HISI', 10.18), ('CD', 'ARG', 'CG', 'HISI', 10.27), ('CD', 'ARG', 'ND1', 'HISI', 10.12), ('CD', 'ARG', 'CD2', 'HISI', 10.69), ('CD', 'ARG', 'CE1', 'HISI', 10.43), ('CD', 'ARG', 'NE2', 'HISI', 10.76)], [('NE', 'ARG', 'CB', 'HISI', 10.64), ('NE', 'ARG', 'CG', 'HISI', 10.49), ('NE', 'ARG', 'ND1', 'HISI', 10.14), ('NE', 'ARG', 'CD2', 'HISI', 10.83), ('NE', 'ARG', 'CE1', 'HISI', 10.26), ('NE', 'ARG', 'NE2', 'HISI', 10.68)], [('CZ', 'ARG', 'CB', 'HISI', 10.22), ('CZ', 'ARG', 'CG', 'HISI', 9.86), ('CZ', 'ARG', 'ND1', 'HISI', 9.44), ('CZ', 'ARG', 'CD2', 'HISI', 10.06), ('CZ', 'ARG', 'CE1', 'HISI', 9.38), ('CZ', 'ARG', 'NE2', 'HISI', 9.75)], [('NH1', 'ARG', 'CB', 'HISI', 9.24), ('NH1', 'ARG', 'CG', 'HISI', 8.85), ('NH1', 'ARG', 'ND1', 'HISI', 8.57), ('NH1', 'ARG', 'CD2', 'HISI', 8.93), ('NH1', 'ARG', 'CE1', 'HISI', 8.48), ('NH1', 'ARG', 'NE2', 'HISI', 8.7)], [('NH2', 'ARG', 'CB', 'HISI', 10.99), ('NH2', 'ARG', 'CG', 'HISI', 10.46), ('NH2', 'ARG', 'ND1', 'HISI', 9.86), ('NH2', 'ARG', 'CD2', 'HISI', 10.59), ('NH2', 'ARG', 'CE1', 'HISI', 9.64), ('NH2', 'ARG', 'NE2', 'HISI', 10.09)]]}
ASP_HIS = { 
	'distances':
		[[7.25, 7.47, 6.83, 8.64, 7.77, 8.77], [6.43, 6.32, 5.53, 7.38, 6.35, 7.38], [5.21, 5.19, 4.57, 6.37, 5.63, 6.55], [7.22, 6.77, 5.78, 7.61, 6.24, 7.32], [14.9, 13.98, 12.6, 14.4, 12.21, 13.34], [13.84, 12.85, 11.47, 13.19, 10.99, 12.09], [13.39, 12.48, 11.11, 12.87, 10.7, 11.83], [13.54, 12.44, 11.09, 12.65, 10.47, 11.49]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 7.25), ('CB', 'ASP', 'CG', 'HIS', 7.47), ('CB', 'ASP', 'ND1', 'HIS', 6.83), ('CB', 'ASP', 'CD2', 'HIS', 8.64), ('CB', 'ASP', 'CE1', 'HIS', 7.77), ('CB', 'ASP', 'NE2', 'HIS', 8.77)], [('CG', 'ASP', 'CB', 'HIS', 6.43), ('CG', 'ASP', 'CG', 'HIS', 6.32), ('CG', 'ASP', 'ND1', 'HIS', 5.53), ('CG', 'ASP', 'CD2', 'HIS', 7.38), ('CG', 'ASP', 'CE1', 'HIS', 6.35), ('CG', 'ASP', 'NE2', 'HIS', 7.38)], [('OD1', 'ASP', 'CB', 'HIS', 5.21), ('OD1', 'ASP', 'CG', 'HIS', 5.19), ('OD1', 'ASP', 'ND1', 'HIS', 4.57), ('OD1', 'ASP', 'CD2', 'HIS', 6.37), ('OD1', 'ASP', 'CE1', 'HIS', 5.63), ('OD1', 'ASP', 'NE2', 'HIS', 6.55)], [('OD2', 'ASP', 'CB', 'HIS', 7.22), ('OD2', 'ASP', 'CG', 'HIS', 6.77), ('OD2', 'ASP', 'ND1', 'HIS', 5.78), ('OD2', 'ASP', 'CD2', 'HIS', 7.61), ('OD2', 'ASP', 'CE1', 'HIS', 6.24), ('OD2', 'ASP', 'NE2', 'HIS', 7.32)], [('CB', 'ASP', 'CB', 'HIS', 14.9), ('CB', 'ASP', 'CG', 'HIS', 13.98), ('CB', 'ASP', 'ND1', 'HIS', 12.6), ('CB', 'ASP', 'CD2', 'HIS', 14.4), ('CB', 'ASP', 'CE1', 'HIS', 12.21), ('CB', 'ASP', 'NE2', 'HIS', 13.34)], [('CG', 'ASP', 'CB', 'HIS', 13.84), ('CG', 'ASP', 'CG', 'HIS', 12.85), ('CG', 'ASP', 'ND1', 'HIS', 11.47), ('CG', 'ASP', 'CD2', 'HIS', 13.19), ('CG', 'ASP', 'CE1', 'HIS', 10.99), ('CG', 'ASP', 'NE2', 'HIS', 12.09)], [('OD1', 'ASP', 'CB', 'HIS', 13.39), ('OD1', 'ASP', 'CG', 'HIS', 12.48), ('OD1', 'ASP', 'ND1', 'HIS', 11.11), ('OD1', 'ASP', 'CD2', 'HIS', 12.87), ('OD1', 'ASP', 'CE1', 'HIS', 10.7), ('OD1', 'ASP', 'NE2', 'HIS', 11.83)], [('OD2', 'ASP', 'CB', 'HIS', 13.54), ('OD2', 'ASP', 'CG', 'HIS', 12.44), ('OD2', 'ASP', 'ND1', 'HIS', 11.09), ('OD2', 'ASP', 'CD2', 'HIS', 12.65), ('OD2', 'ASP', 'CE1', 'HIS', 10.47), ('OD2', 'ASP', 'NE2', 'HIS', 11.49)]]}
HIS_HIS = { 
	'distances':
		[[13.41, 12.69, 11.44, 13.14, 11.18, 12.25], [12.42, 11.58, 10.35, 11.92, 9.95, 10.96], [11.66, 10.74, 9.44, 11.07, 9.0, 10.05], [12.21, 11.33, 10.2, 11.54, 9.71, 10.58], [10.96, 9.93, 8.68, 10.1, 8.08, 9.03], [11.31, 10.3, 9.17, 10.4, 8.55, 9.37], [13.41, 12.42, 11.66, 12.21, 10.96, 11.31], [12.69, 11.58, 10.74, 11.33, 9.93, 10.3], [11.44, 10.35, 9.44, 10.2, 8.68, 9.17], [13.14, 11.92, 11.07, 11.54, 10.1, 10.4], [11.18, 9.95, 9.0, 9.71, 8.08, 8.55], [12.25, 10.96, 10.05, 10.58, 9.03, 9.37]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 13.41), ('CB', 'HIS', 'CG', 'HIS', 12.69), ('CB', 'HIS', 'ND1', 'HIS', 11.44), ('CB', 'HIS', 'CD2', 'HIS', 13.14), ('CB', 'HIS', 'CE1', 'HIS', 11.18), ('CB', 'HIS', 'NE2', 'HIS', 12.25)], [('CG', 'HIS', 'CB', 'HIS', 12.42), ('CG', 'HIS', 'CG', 'HIS', 11.58), ('CG', 'HIS', 'ND1', 'HIS', 10.35), ('CG', 'HIS', 'CD2', 'HIS', 11.92), ('CG', 'HIS', 'CE1', 'HIS', 9.95), ('CG', 'HIS', 'NE2', 'HIS', 10.96)], [('ND1', 'HIS', 'CB', 'HIS', 11.66), ('ND1', 'HIS', 'CG', 'HIS', 10.74), ('ND1', 'HIS', 'ND1', 'HIS', 9.44), ('ND1', 'HIS', 'CD2', 'HIS', 11.07), ('ND1', 'HIS', 'CE1', 'HIS', 9.0), ('ND1', 'HIS', 'NE2', 'HIS', 10.05)], [('CD2', 'HIS', 'CB', 'HIS', 12.21), ('CD2', 'HIS', 'CG', 'HIS', 11.33), ('CD2', 'HIS', 'ND1', 'HIS', 10.2), ('CD2', 'HIS', 'CD2', 'HIS', 11.54), ('CD2', 'HIS', 'CE1', 'HIS', 9.71), ('CD2', 'HIS', 'NE2', 'HIS', 10.58)], [('CE1', 'HIS', 'CB', 'HIS', 10.96), ('CE1', 'HIS', 'CG', 'HIS', 9.93), ('CE1', 'HIS', 'ND1', 'HIS', 8.68), ('CE1', 'HIS', 'CD2', 'HIS', 10.1), ('CE1', 'HIS', 'CE1', 'HIS', 8.08), ('CE1', 'HIS', 'NE2', 'HIS', 9.03)], [('NE2', 'HIS', 'CB', 'HIS', 11.31), ('NE2', 'HIS', 'CG', 'HIS', 10.3), ('NE2', 'HIS', 'ND1', 'HIS', 9.17), ('NE2', 'HIS', 'CD2', 'HIS', 10.4), ('NE2', 'HIS', 'CE1', 'HIS', 8.55), ('NE2', 'HIS', 'NE2', 'HIS', 9.37)], [('CB', 'HIS', 'CB', 'HIS', 13.41), ('CB', 'HIS', 'CG', 'HIS', 12.42), ('CB', 'HIS', 'ND1', 'HIS', 11.66), ('CB', 'HIS', 'CD2', 'HIS', 12.21), ('CB', 'HIS', 'CE1', 'HIS', 10.96), ('CB', 'HIS', 'NE2', 'HIS', 11.31)], [('CG', 'HIS', 'CB', 'HIS', 12.69), ('CG', 'HIS', 'CG', 'HIS', 11.58), ('CG', 'HIS', 'ND1', 'HIS', 10.74), ('CG', 'HIS', 'CD2', 'HIS', 11.33), ('CG', 'HIS', 'CE1', 'HIS', 9.93), ('CG', 'HIS', 'NE2', 'HIS', 10.3)], [('ND1', 'HIS', 'CB', 'HIS', 11.44), ('ND1', 'HIS', 'CG', 'HIS', 10.35), ('ND1', 'HIS', 'ND1', 'HIS', 9.44), ('ND1', 'HIS', 'CD2', 'HIS', 10.2), ('ND1', 'HIS', 'CE1', 'HIS', 8.68), ('ND1', 'HIS', 'NE2', 'HIS', 9.17)], [('CD2', 'HIS', 'CB', 'HIS', 13.14), ('CD2', 'HIS', 'CG', 'HIS', 11.92), ('CD2', 'HIS', 'ND1', 'HIS', 11.07), ('CD2', 'HIS', 'CD2', 'HIS', 11.54), ('CD2', 'HIS', 'CE1', 'HIS', 10.1), ('CD2', 'HIS', 'NE2', 'HIS', 10.4)], [('CE1', 'HIS', 'CB', 'HIS', 11.18), ('CE1', 'HIS', 'CG', 'HIS', 9.95), ('CE1', 'HIS', 'ND1', 'HIS', 9.0), ('CE1', 'HIS', 'CD2', 'HIS', 9.71), ('CE1', 'HIS', 'CE1', 'HIS', 8.08), ('CE1', 'HIS', 'NE2', 'HIS', 8.55)], [('NE2', 'HIS', 'CB', 'HIS', 12.25), ('NE2', 'HIS', 'CG', 'HIS', 10.96), ('NE2', 'HIS', 'ND1', 'HIS', 10.05), ('NE2', 'HIS', 'CD2', 'HIS', 10.58), ('NE2', 'HIS', 'CE1', 'HIS', 9.03), ('NE2', 'HIS', 'NE2', 'HIS', 9.37)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ARG, d, 'A_1ptd_4_6_1_13')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ARG, d, 'A_1ptd_4_6_1_13')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_HISI, d, 'A_1ptd_4_6_1_13')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_HIS, d, 'A_1ptd_4_6_1_13')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_HIS, d, 'A_1ptd_4_6_1_13')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ARG' :  match1,
		'HIS_ARG' :  match2,
		'ARG_HISI' :  match3,
		'ASP_HIS' :  match4,
		'HIS_HIS' :  match5}