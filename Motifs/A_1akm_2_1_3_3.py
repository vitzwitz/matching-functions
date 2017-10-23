'''
FUNC:A_1akm_2_1_3_3
PDB:1akm
EC:2.1.3.3
RESI:arg,his,gln,asp,cys,arg
LOCI:a-106,133,136,231,273,319;
'''
import motifFunctions as cmd
ASP_CYS = { 
	'distances':
		[[7.53, 5.95], [7.1, 5.34], [7.07, 5.46], [7.26, 5.44]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'CYS', 7.53), ('CB', 'ASP', 'SG', 'CYS', 5.95)], [('CG', 'ASP', 'CB', 'CYS', 7.1), ('CG', 'ASP', 'SG', 'CYS', 5.34)], [('OD1', 'ASP', 'CB', 'CYS', 7.07), ('OD1', 'ASP', 'SG', 'CYS', 5.46)], [('OD2', 'ASP', 'CB', 'CYS', 7.26), ('OD2', 'ASP', 'SG', 'CYS', 5.44)]]}
HIS_ASP = { 
	'distances':
		[[12.31, 11.82, 12.54, 10.9], [12.01, 11.38, 11.95, 10.52], [12.96, 12.21, 12.66, 11.37], [10.84, 10.19, 10.7, 9.41], [12.53, 11.7, 12.02, 10.95], [11.25, 10.47, 10.8, 9.76]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 12.31), ('CB', 'HIS', 'CG', 'ASP', 11.82), ('CB', 'HIS', 'OD1', 'ASP', 12.54), ('CB', 'HIS', 'OD2', 'ASP', 10.9)], [('CG', 'HIS', 'CB', 'ASP', 12.01), ('CG', 'HIS', 'CG', 'ASP', 11.38), ('CG', 'HIS', 'OD1', 'ASP', 11.95), ('CG', 'HIS', 'OD2', 'ASP', 10.52)], [('ND1', 'HIS', 'CB', 'ASP', 12.96), ('ND1', 'HIS', 'CG', 'ASP', 12.21), ('ND1', 'HIS', 'OD1', 'ASP', 12.66), ('ND1', 'HIS', 'OD2', 'ASP', 11.37)], [('CD2', 'HIS', 'CB', 'ASP', 10.84), ('CD2', 'HIS', 'CG', 'ASP', 10.19), ('CD2', 'HIS', 'OD1', 'ASP', 10.7), ('CD2', 'HIS', 'OD2', 'ASP', 9.41)], [('CE1', 'HIS', 'CB', 'ASP', 12.53), ('CE1', 'HIS', 'CG', 'ASP', 11.7), ('CE1', 'HIS', 'OD1', 'ASP', 12.02), ('CE1', 'HIS', 'OD2', 'ASP', 10.95)], [('NE2', 'HIS', 'CB', 'ASP', 11.25), ('NE2', 'HIS', 'CG', 'ASP', 10.47), ('NE2', 'HIS', 'OD1', 'ASP', 10.8), ('NE2', 'HIS', 'OD2', 'ASP', 9.76)]]}
HIS_CYS = { 
	'distances':
		[[10.04, 10.01], [9.14, 9.26], [9.67, 9.94], [7.76, 7.91], [8.84, 9.24], [7.6, 7.95]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYS', 10.04), ('CB', 'HIS', 'SG', 'CYS', 10.01)], [('CG', 'HIS', 'CB', 'CYS', 9.14), ('CG', 'HIS', 'SG', 'CYS', 9.26)], [('ND1', 'HIS', 'CB', 'CYS', 9.67), ('ND1', 'HIS', 'SG', 'CYS', 9.94)], [('CD2', 'HIS', 'CB', 'CYS', 7.76), ('CD2', 'HIS', 'SG', 'CYS', 7.91)], [('CE1', 'HIS', 'CB', 'CYS', 8.84), ('CE1', 'HIS', 'SG', 'CYS', 9.24)], [('NE2', 'HIS', 'CB', 'CYS', 7.6), ('NE2', 'HIS', 'SG', 'CYS', 7.95)]]}
HIS_ARG = { 
	'distances':
		[[13.28, 11.91, 11.33, 9.89, 9.4, 10.3, 8.16], [11.99, 10.62, 9.99, 8.56, 7.98, 8.84, 6.75], [11.42, 10.12, 9.3, 7.88, 7.12, 7.87, 5.81], [11.37, 9.93, 9.47, 8.1, 7.61, 8.49, 6.55], [10.41, 9.1, 8.29, 6.9, 6.08, 6.78, 4.83], [10.38, 8.96, 8.41, 7.06, 6.45, 7.24, 5.42], [11.73, 11.22, 10.78, 10.54, 9.65, 8.86, 9.83], [10.94, 10.38, 9.74, 9.45, 8.44, 7.57, 8.62], [9.8, 9.34, 8.65, 8.5, 7.56, 6.54, 7.95], [11.54, 10.85, 10.05, 9.55, 8.39, 7.6, 8.33], [9.76, 9.22, 8.3, 8.01, 6.92, 5.85, 7.21], [10.85, 10.16, 9.21, 8.7, 7.49, 6.6, 7.46]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 13.28), ('CB', 'HIS', 'CG', 'ARG', 11.91), ('CB', 'HIS', 'CD', 'ARG', 11.33), ('CB', 'HIS', 'NE', 'ARG', 9.89), ('CB', 'HIS', 'CZ', 'ARG', 9.4), ('CB', 'HIS', 'NH1', 'ARG', 10.3), ('CB', 'HIS', 'NH2', 'ARG', 8.16)], [('CG', 'HIS', 'CB', 'ARG', 11.99), ('CG', 'HIS', 'CG', 'ARG', 10.62), ('CG', 'HIS', 'CD', 'ARG', 9.99), ('CG', 'HIS', 'NE', 'ARG', 8.56), ('CG', 'HIS', 'CZ', 'ARG', 7.98), ('CG', 'HIS', 'NH1', 'ARG', 8.84), ('CG', 'HIS', 'NH2', 'ARG', 6.75)], [('ND1', 'HIS', 'CB', 'ARG', 11.42), ('ND1', 'HIS', 'CG', 'ARG', 10.12), ('ND1', 'HIS', 'CD', 'ARG', 9.3), ('ND1', 'HIS', 'NE', 'ARG', 7.88), ('ND1', 'HIS', 'CZ', 'ARG', 7.12), ('ND1', 'HIS', 'NH1', 'ARG', 7.87), ('ND1', 'HIS', 'NH2', 'ARG', 5.81)], [('CD2', 'HIS', 'CB', 'ARG', 11.37), ('CD2', 'HIS', 'CG', 'ARG', 9.93), ('CD2', 'HIS', 'CD', 'ARG', 9.47), ('CD2', 'HIS', 'NE', 'ARG', 8.1), ('CD2', 'HIS', 'CZ', 'ARG', 7.61), ('CD2', 'HIS', 'NH1', 'ARG', 8.49), ('CD2', 'HIS', 'NH2', 'ARG', 6.55)], [('CE1', 'HIS', 'CB', 'ARG', 10.41), ('CE1', 'HIS', 'CG', 'ARG', 9.1), ('CE1', 'HIS', 'CD', 'ARG', 8.29), ('CE1', 'HIS', 'NE', 'ARG', 6.9), ('CE1', 'HIS', 'CZ', 'ARG', 6.08), ('CE1', 'HIS', 'NH1', 'ARG', 6.78), ('CE1', 'HIS', 'NH2', 'ARG', 4.83)], [('NE2', 'HIS', 'CB', 'ARG', 10.38), ('NE2', 'HIS', 'CG', 'ARG', 8.96), ('NE2', 'HIS', 'CD', 'ARG', 8.41), ('NE2', 'HIS', 'NE', 'ARG', 7.06), ('NE2', 'HIS', 'CZ', 'ARG', 6.45), ('NE2', 'HIS', 'NH1', 'ARG', 7.24), ('NE2', 'HIS', 'NH2', 'ARG', 5.42)], [('CB', 'HIS', 'CB', 'ARG', 11.73), ('CB', 'HIS', 'CG', 'ARG', 11.22), ('CB', 'HIS', 'CD', 'ARG', 10.78), ('CB', 'HIS', 'NE', 'ARG', 10.54), ('CB', 'HIS', 'CZ', 'ARG', 9.65), ('CB', 'HIS', 'NH1', 'ARG', 8.86), ('CB', 'HIS', 'NH2', 'ARG', 9.83)], [('CG', 'HIS', 'CB', 'ARG', 10.94), ('CG', 'HIS', 'CG', 'ARG', 10.38), ('CG', 'HIS', 'CD', 'ARG', 9.74), ('CG', 'HIS', 'NE', 'ARG', 9.45), ('CG', 'HIS', 'CZ', 'ARG', 8.44), ('CG', 'HIS', 'NH1', 'ARG', 7.57), ('CG', 'HIS', 'NH2', 'ARG', 8.62)], [('ND1', 'HIS', 'CB', 'ARG', 9.8), ('ND1', 'HIS', 'CG', 'ARG', 9.34), ('ND1', 'HIS', 'CD', 'ARG', 8.65), ('ND1', 'HIS', 'NE', 'ARG', 8.5), ('ND1', 'HIS', 'CZ', 'ARG', 7.56), ('ND1', 'HIS', 'NH1', 'ARG', 6.54), ('ND1', 'HIS', 'NH2', 'ARG', 7.95)], [('CD2', 'HIS', 'CB', 'ARG', 11.54), ('CD2', 'HIS', 'CG', 'ARG', 10.85), ('CD2', 'HIS', 'CD', 'ARG', 10.05), ('CD2', 'HIS', 'NE', 'ARG', 9.55), ('CD2', 'HIS', 'CZ', 'ARG', 8.39), ('CD2', 'HIS', 'NH1', 'ARG', 7.6), ('CD2', 'HIS', 'NH2', 'ARG', 8.33)], [('CE1', 'HIS', 'CB', 'ARG', 9.76), ('CE1', 'HIS', 'CG', 'ARG', 9.22), ('CE1', 'HIS', 'CD', 'ARG', 8.3), ('CE1', 'HIS', 'NE', 'ARG', 8.01), ('CE1', 'HIS', 'CZ', 'ARG', 6.92), ('CE1', 'HIS', 'NH1', 'ARG', 5.85), ('CE1', 'HIS', 'NH2', 'ARG', 7.21)], [('NE2', 'HIS', 'CB', 'ARG', 10.85), ('NE2', 'HIS', 'CG', 'ARG', 10.16), ('NE2', 'HIS', 'CD', 'ARG', 9.21), ('NE2', 'HIS', 'NE', 'ARG', 8.7), ('NE2', 'HIS', 'CZ', 'ARG', 7.49), ('NE2', 'HIS', 'NH1', 'ARG', 6.6), ('NE2', 'HIS', 'NH2', 'ARG', 7.46)]]}
GLN_CYS = { 
	'distances':
		[[7.59, 8.59], [6.29, 7.41], [5.55, 6.97], [5.63, 6.88], [5.58, 7.28]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'CYS', 7.59), ('CB', 'GLN', 'SG', 'CYS', 8.59)], [('CG', 'GLN', 'CB', 'CYS', 6.29), ('CG', 'GLN', 'SG', 'CYS', 7.41)], [('CD', 'GLN', 'CB', 'CYS', 5.55), ('CD', 'GLN', 'SG', 'CYS', 6.97)], [('OE1', 'GLN', 'CB', 'CYS', 5.63), ('OE1', 'GLN', 'SG', 'CYS', 6.88)], [('NE2', 'GLN', 'CB', 'CYS', 5.58), ('NE2', 'GLN', 'SG', 'CYS', 7.28)]]}
ARG_ARG = { 
	'distances':
		[[14.98, 14.84, 13.43, 13.33, 12.37, 11.39, 12.53], [14.29, 14.05, 12.65, 12.46, 11.4, 10.4, 11.49], [12.92, 12.76, 11.38, 11.31, 10.34, 9.27, 10.6], [12.13, 11.93, 10.6, 10.53, 9.49, 8.34, 9.79], [10.82, 10.59, 9.26, 9.2, 8.19, 7.03, 8.57], [10.26, 10.03, 8.63, 8.59, 7.7, 6.65, 8.13], [10.12, 9.86, 8.63, 8.59, 7.56, 6.3, 8.02], [14.98, 14.29, 12.92, 12.13, 10.82, 10.26, 10.12], [14.84, 14.05, 12.76, 11.93, 10.59, 10.03, 9.86], [13.43, 12.65, 11.38, 10.6, 9.26, 8.63, 8.63], [13.33, 12.46, 11.31, 10.53, 9.2, 8.59, 8.59], [12.37, 11.4, 10.34, 9.49, 8.19, 7.7, 7.56], [11.39, 10.4, 9.27, 8.34, 7.03, 6.65, 6.3], [12.53, 11.49, 10.6, 9.79, 8.57, 8.13, 8.02]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ARG', 14.98), ('CB', 'ARG', 'CG', 'ARG', 14.84), ('CB', 'ARG', 'CD', 'ARG', 13.43), ('CB', 'ARG', 'NE', 'ARG', 13.33), ('CB', 'ARG', 'CZ', 'ARG', 12.37), ('CB', 'ARG', 'NH1', 'ARG', 11.39), ('CB', 'ARG', 'NH2', 'ARG', 12.53)], [('CG', 'ARG', 'CB', 'ARG', 14.29), ('CG', 'ARG', 'CG', 'ARG', 14.05), ('CG', 'ARG', 'CD', 'ARG', 12.65), ('CG', 'ARG', 'NE', 'ARG', 12.46), ('CG', 'ARG', 'CZ', 'ARG', 11.4), ('CG', 'ARG', 'NH1', 'ARG', 10.4), ('CG', 'ARG', 'NH2', 'ARG', 11.49)], [('CD', 'ARG', 'CB', 'ARG', 12.92), ('CD', 'ARG', 'CG', 'ARG', 12.76), ('CD', 'ARG', 'CD', 'ARG', 11.38), ('CD', 'ARG', 'NE', 'ARG', 11.31), ('CD', 'ARG', 'CZ', 'ARG', 10.34), ('CD', 'ARG', 'NH1', 'ARG', 9.27), ('CD', 'ARG', 'NH2', 'ARG', 10.6)], [('NE', 'ARG', 'CB', 'ARG', 12.13), ('NE', 'ARG', 'CG', 'ARG', 11.93), ('NE', 'ARG', 'CD', 'ARG', 10.6), ('NE', 'ARG', 'NE', 'ARG', 10.53), ('NE', 'ARG', 'CZ', 'ARG', 9.49), ('NE', 'ARG', 'NH1', 'ARG', 8.34), ('NE', 'ARG', 'NH2', 'ARG', 9.79)], [('CZ', 'ARG', 'CB', 'ARG', 10.82), ('CZ', 'ARG', 'CG', 'ARG', 10.59), ('CZ', 'ARG', 'CD', 'ARG', 9.26), ('CZ', 'ARG', 'NE', 'ARG', 9.2), ('CZ', 'ARG', 'CZ', 'ARG', 8.19), ('CZ', 'ARG', 'NH1', 'ARG', 7.03), ('CZ', 'ARG', 'NH2', 'ARG', 8.57)], [('NH1', 'ARG', 'CB', 'ARG', 10.26), ('NH1', 'ARG', 'CG', 'ARG', 10.03), ('NH1', 'ARG', 'CD', 'ARG', 8.63), ('NH1', 'ARG', 'NE', 'ARG', 8.59), ('NH1', 'ARG', 'CZ', 'ARG', 7.7), ('NH1', 'ARG', 'NH1', 'ARG', 6.65), ('NH1', 'ARG', 'NH2', 'ARG', 8.13)], [('NH2', 'ARG', 'CB', 'ARG', 10.12), ('NH2', 'ARG', 'CG', 'ARG', 9.86), ('NH2', 'ARG', 'CD', 'ARG', 8.63), ('NH2', 'ARG', 'NE', 'ARG', 8.59), ('NH2', 'ARG', 'CZ', 'ARG', 7.56), ('NH2', 'ARG', 'NH1', 'ARG', 6.3), ('NH2', 'ARG', 'NH2', 'ARG', 8.02)], [('CB', 'ARG', 'CB', 'ARG', 14.98), ('CB', 'ARG', 'CG', 'ARG', 14.29), ('CB', 'ARG', 'CD', 'ARG', 12.92), ('CB', 'ARG', 'NE', 'ARG', 12.13), ('CB', 'ARG', 'CZ', 'ARG', 10.82), ('CB', 'ARG', 'NH1', 'ARG', 10.26), ('CB', 'ARG', 'NH2', 'ARG', 10.12)], [('CG', 'ARG', 'CB', 'ARG', 14.84), ('CG', 'ARG', 'CG', 'ARG', 14.05), ('CG', 'ARG', 'CD', 'ARG', 12.76), ('CG', 'ARG', 'NE', 'ARG', 11.93), ('CG', 'ARG', 'CZ', 'ARG', 10.59), ('CG', 'ARG', 'NH1', 'ARG', 10.03), ('CG', 'ARG', 'NH2', 'ARG', 9.86)], [('CD', 'ARG', 'CB', 'ARG', 13.43), ('CD', 'ARG', 'CG', 'ARG', 12.65), ('CD', 'ARG', 'CD', 'ARG', 11.38), ('CD', 'ARG', 'NE', 'ARG', 10.6), ('CD', 'ARG', 'CZ', 'ARG', 9.26), ('CD', 'ARG', 'NH1', 'ARG', 8.63), ('CD', 'ARG', 'NH2', 'ARG', 8.63)], [('NE', 'ARG', 'CB', 'ARG', 13.33), ('NE', 'ARG', 'CG', 'ARG', 12.46), ('NE', 'ARG', 'CD', 'ARG', 11.31), ('NE', 'ARG', 'NE', 'ARG', 10.53), ('NE', 'ARG', 'CZ', 'ARG', 9.2), ('NE', 'ARG', 'NH1', 'ARG', 8.59), ('NE', 'ARG', 'NH2', 'ARG', 8.59)], [('CZ', 'ARG', 'CB', 'ARG', 12.37), ('CZ', 'ARG', 'CG', 'ARG', 11.4), ('CZ', 'ARG', 'CD', 'ARG', 10.34), ('CZ', 'ARG', 'NE', 'ARG', 9.49), ('CZ', 'ARG', 'CZ', 'ARG', 8.19), ('CZ', 'ARG', 'NH1', 'ARG', 7.7), ('CZ', 'ARG', 'NH2', 'ARG', 7.56)], [('NH1', 'ARG', 'CB', 'ARG', 11.39), ('NH1', 'ARG', 'CG', 'ARG', 10.4), ('NH1', 'ARG', 'CD', 'ARG', 9.27), ('NH1', 'ARG', 'NE', 'ARG', 8.34), ('NH1', 'ARG', 'CZ', 'ARG', 7.03), ('NH1', 'ARG', 'NH1', 'ARG', 6.65), ('NH1', 'ARG', 'NH2', 'ARG', 6.3)], [('NH2', 'ARG', 'CB', 'ARG', 12.53), ('NH2', 'ARG', 'CG', 'ARG', 11.49), ('NH2', 'ARG', 'CD', 'ARG', 10.6), ('NH2', 'ARG', 'NE', 'ARG', 9.79), ('NH2', 'ARG', 'CZ', 'ARG', 8.57), ('NH2', 'ARG', 'NH1', 'ARG', 8.13), ('NH2', 'ARG', 'NH2', 'ARG', 8.02)]]}
GLN_ASP = { 
	'distances':
		[[11.89, 11.54, 11.95, 11.1], [10.71, 10.45, 10.83, 10.16], [10.64, 10.24, 10.41, 10.07], [10.72, 10.12, 10.21, 9.85], [10.87, 10.58, 10.65, 10.59]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'ASP', 11.89), ('CB', 'GLN', 'CG', 'ASP', 11.54), ('CB', 'GLN', 'OD1', 'ASP', 11.95), ('CB', 'GLN', 'OD2', 'ASP', 11.1)], [('CG', 'GLN', 'CB', 'ASP', 10.71), ('CG', 'GLN', 'CG', 'ASP', 10.45), ('CG', 'GLN', 'OD1', 'ASP', 10.83), ('CG', 'GLN', 'OD2', 'ASP', 10.16)], [('CD', 'GLN', 'CB', 'ASP', 10.64), ('CD', 'GLN', 'CG', 'ASP', 10.24), ('CD', 'GLN', 'OD1', 'ASP', 10.41), ('CD', 'GLN', 'OD2', 'ASP', 10.07)], [('OE1', 'GLN', 'CB', 'ASP', 10.72), ('OE1', 'GLN', 'CG', 'ASP', 10.12), ('OE1', 'GLN', 'OD1', 'ASP', 10.21), ('OE1', 'GLN', 'OD2', 'ASP', 9.85)], [('NE2', 'GLN', 'CB', 'ASP', 10.87), ('NE2', 'GLN', 'CG', 'ASP', 10.58), ('NE2', 'GLN', 'OD1', 'ASP', 10.65), ('NE2', 'GLN', 'OD2', 'ASP', 10.59)]]}
ARG_ASP = { 
	'distances':
		[[16.04, 15.44, 15.17, 15.45], [14.7, 14.11, 13.9, 14.06], [15.16, 14.45, 14.29, 14.27], [14.4, 13.7, 13.65, 13.41], [14.35, 13.52, 13.48, 13.13], [14.95, 14.01, 13.86, 13.61], [14.0, 13.16, 13.24, 12.64], [18.68, 17.46, 17.54, 16.55], [17.46, 16.21, 16.26, 15.29], [16.64, 15.39, 15.37, 14.54], [15.46, 14.15, 14.1, 13.32], [14.29, 13.01, 12.97, 12.22], [14.3, 13.11, 13.12, 12.34], [13.25, 11.92, 11.81, 11.15]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 16.04), ('CB', 'ARG', 'CG', 'ASP', 15.44), ('CB', 'ARG', 'OD1', 'ASP', 15.17), ('CB', 'ARG', 'OD2', 'ASP', 15.45)], [('CG', 'ARG', 'CB', 'ASP', 14.7), ('CG', 'ARG', 'CG', 'ASP', 14.11), ('CG', 'ARG', 'OD1', 'ASP', 13.9), ('CG', 'ARG', 'OD2', 'ASP', 14.06)], [('CD', 'ARG', 'CB', 'ASP', 15.16), ('CD', 'ARG', 'CG', 'ASP', 14.45), ('CD', 'ARG', 'OD1', 'ASP', 14.29), ('CD', 'ARG', 'OD2', 'ASP', 14.27)], [('NE', 'ARG', 'CB', 'ASP', 14.4), ('NE', 'ARG', 'CG', 'ASP', 13.7), ('NE', 'ARG', 'OD1', 'ASP', 13.65), ('NE', 'ARG', 'OD2', 'ASP', 13.41)], [('CZ', 'ARG', 'CB', 'ASP', 14.35), ('CZ', 'ARG', 'CG', 'ASP', 13.52), ('CZ', 'ARG', 'OD1', 'ASP', 13.48), ('CZ', 'ARG', 'OD2', 'ASP', 13.13)], [('NH1', 'ARG', 'CB', 'ASP', 14.95), ('NH1', 'ARG', 'CG', 'ASP', 14.01), ('NH1', 'ARG', 'OD1', 'ASP', 13.86), ('NH1', 'ARG', 'OD2', 'ASP', 13.61)], [('NH2', 'ARG', 'CB', 'ASP', 14.0), ('NH2', 'ARG', 'CG', 'ASP', 13.16), ('NH2', 'ARG', 'OD1', 'ASP', 13.24), ('NH2', 'ARG', 'OD2', 'ASP', 12.64)], [('CB', 'ARG', 'CB', 'ASP', 18.68), ('CB', 'ARG', 'CG', 'ASP', 17.46), ('CB', 'ARG', 'OD1', 'ASP', 17.54), ('CB', 'ARG', 'OD2', 'ASP', 16.55)], [('CG', 'ARG', 'CB', 'ASP', 17.46), ('CG', 'ARG', 'CG', 'ASP', 16.21), ('CG', 'ARG', 'OD1', 'ASP', 16.26), ('CG', 'ARG', 'OD2', 'ASP', 15.29)], [('CD', 'ARG', 'CB', 'ASP', 16.64), ('CD', 'ARG', 'CG', 'ASP', 15.39), ('CD', 'ARG', 'OD1', 'ASP', 15.37), ('CD', 'ARG', 'OD2', 'ASP', 14.54)], [('NE', 'ARG', 'CB', 'ASP', 15.46), ('NE', 'ARG', 'CG', 'ASP', 14.15), ('NE', 'ARG', 'OD1', 'ASP', 14.1), ('NE', 'ARG', 'OD2', 'ASP', 13.32)], [('CZ', 'ARG', 'CB', 'ASP', 14.29), ('CZ', 'ARG', 'CG', 'ASP', 13.01), ('CZ', 'ARG', 'OD1', 'ASP', 12.97), ('CZ', 'ARG', 'OD2', 'ASP', 12.22)], [('NH1', 'ARG', 'CB', 'ASP', 14.3), ('NH1', 'ARG', 'CG', 'ASP', 13.11), ('NH1', 'ARG', 'OD1', 'ASP', 13.12), ('NH1', 'ARG', 'OD2', 'ASP', 12.34)], [('NH2', 'ARG', 'CB', 'ASP', 13.25), ('NH2', 'ARG', 'CG', 'ASP', 11.92), ('NH2', 'ARG', 'OD1', 'ASP', 11.81), ('NH2', 'ARG', 'OD2', 'ASP', 11.15)]]}
GLN_ARG = { 
	'distances':
		[[9.33, 7.94, 7.81, 6.56, 6.82, 8.08, 6.21], [9.35, 7.91, 8.12, 7.06, 7.46, 8.65, 7.08], [8.26, 6.8, 7.14, 6.26, 6.73, 7.8, 6.65], [8.12, 6.63, 6.71, 5.74, 5.92, 6.87, 5.8], [7.77, 6.41, 7.13, 6.58, 7.32, 8.32, 7.52], [13.4, 12.98, 11.98, 11.7, 10.51, 9.43, 10.58], [14.4, 13.85, 12.79, 12.33, 11.07, 10.12, 10.92], [14.23, 13.64, 12.45, 11.92, 10.62, 9.72, 10.4], [13.17, 12.53, 11.31, 10.74, 9.44, 8.57, 9.2], [15.31, 14.73, 13.49, 12.95, 11.65, 10.77, 11.38]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'ARG', 9.33), ('CB', 'GLN', 'CG', 'ARG', 7.94), ('CB', 'GLN', 'CD', 'ARG', 7.81), ('CB', 'GLN', 'NE', 'ARG', 6.56), ('CB', 'GLN', 'CZ', 'ARG', 6.82), ('CB', 'GLN', 'NH1', 'ARG', 8.08), ('CB', 'GLN', 'NH2', 'ARG', 6.21)], [('CG', 'GLN', 'CB', 'ARG', 9.35), ('CG', 'GLN', 'CG', 'ARG', 7.91), ('CG', 'GLN', 'CD', 'ARG', 8.12), ('CG', 'GLN', 'NE', 'ARG', 7.06), ('CG', 'GLN', 'CZ', 'ARG', 7.46), ('CG', 'GLN', 'NH1', 'ARG', 8.65), ('CG', 'GLN', 'NH2', 'ARG', 7.08)], [('CD', 'GLN', 'CB', 'ARG', 8.26), ('CD', 'GLN', 'CG', 'ARG', 6.8), ('CD', 'GLN', 'CD', 'ARG', 7.14), ('CD', 'GLN', 'NE', 'ARG', 6.26), ('CD', 'GLN', 'CZ', 'ARG', 6.73), ('CD', 'GLN', 'NH1', 'ARG', 7.8), ('CD', 'GLN', 'NH2', 'ARG', 6.65)], [('OE1', 'GLN', 'CB', 'ARG', 8.12), ('OE1', 'GLN', 'CG', 'ARG', 6.63), ('OE1', 'GLN', 'CD', 'ARG', 6.71), ('OE1', 'GLN', 'NE', 'ARG', 5.74), ('OE1', 'GLN', 'CZ', 'ARG', 5.92), ('OE1', 'GLN', 'NH1', 'ARG', 6.87), ('OE1', 'GLN', 'NH2', 'ARG', 5.8)], [('NE2', 'GLN', 'CB', 'ARG', 7.77), ('NE2', 'GLN', 'CG', 'ARG', 6.41), ('NE2', 'GLN', 'CD', 'ARG', 7.13), ('NE2', 'GLN', 'NE', 'ARG', 6.58), ('NE2', 'GLN', 'CZ', 'ARG', 7.32), ('NE2', 'GLN', 'NH1', 'ARG', 8.32), ('NE2', 'GLN', 'NH2', 'ARG', 7.52)], [('CB', 'GLN', 'CB', 'ARG', 13.4), ('CB', 'GLN', 'CG', 'ARG', 12.98), ('CB', 'GLN', 'CD', 'ARG', 11.98), ('CB', 'GLN', 'NE', 'ARG', 11.7), ('CB', 'GLN', 'CZ', 'ARG', 10.51), ('CB', 'GLN', 'NH1', 'ARG', 9.43), ('CB', 'GLN', 'NH2', 'ARG', 10.58)], [('CG', 'GLN', 'CB', 'ARG', 14.4), ('CG', 'GLN', 'CG', 'ARG', 13.85), ('CG', 'GLN', 'CD', 'ARG', 12.79), ('CG', 'GLN', 'NE', 'ARG', 12.33), ('CG', 'GLN', 'CZ', 'ARG', 11.07), ('CG', 'GLN', 'NH1', 'ARG', 10.12), ('CG', 'GLN', 'NH2', 'ARG', 10.92)], [('CD', 'GLN', 'CB', 'ARG', 14.23), ('CD', 'GLN', 'CG', 'ARG', 13.64), ('CD', 'GLN', 'CD', 'ARG', 12.45), ('CD', 'GLN', 'NE', 'ARG', 11.92), ('CD', 'GLN', 'CZ', 'ARG', 10.62), ('CD', 'GLN', 'NH1', 'ARG', 9.72), ('CD', 'GLN', 'NH2', 'ARG', 10.4)], [('OE1', 'GLN', 'CB', 'ARG', 13.17), ('OE1', 'GLN', 'CG', 'ARG', 12.53), ('OE1', 'GLN', 'CD', 'ARG', 11.31), ('OE1', 'GLN', 'NE', 'ARG', 10.74), ('OE1', 'GLN', 'CZ', 'ARG', 9.44), ('OE1', 'GLN', 'NH1', 'ARG', 8.57), ('OE1', 'GLN', 'NH2', 'ARG', 9.2)], [('NE2', 'GLN', 'CB', 'ARG', 15.31), ('NE2', 'GLN', 'CG', 'ARG', 14.73), ('NE2', 'GLN', 'CD', 'ARG', 13.49), ('NE2', 'GLN', 'NE', 'ARG', 12.95), ('NE2', 'GLN', 'CZ', 'ARG', 11.65), ('NE2', 'GLN', 'NH1', 'ARG', 10.77), ('NE2', 'GLN', 'NH2', 'ARG', 11.38)]]}
HIS_GLN = { 
	'distances':
		[[6.56, 7.42, 8.4, 8.19, 9.68], [5.77, 6.65, 7.37, 6.95, 8.68], [6.09, 7.16, 7.63, 7.02, 8.92], [5.24, 5.74, 6.3, 5.84, 7.62], [5.82, 6.71, 6.85, 6.04, 8.11], [5.29, 5.82, 5.94, 5.17, 7.24]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLN', 6.56), ('CB', 'HIS', 'CG', 'GLN', 7.42), ('CB', 'HIS', 'CD', 'GLN', 8.4), ('CB', 'HIS', 'OE1', 'GLN', 8.19), ('CB', 'HIS', 'NE2', 'GLN', 9.68)], [('CG', 'HIS', 'CB', 'GLN', 5.77), ('CG', 'HIS', 'CG', 'GLN', 6.65), ('CG', 'HIS', 'CD', 'GLN', 7.37), ('CG', 'HIS', 'OE1', 'GLN', 6.95), ('CG', 'HIS', 'NE2', 'GLN', 8.68)], [('ND1', 'HIS', 'CB', 'GLN', 6.09), ('ND1', 'HIS', 'CG', 'GLN', 7.16), ('ND1', 'HIS', 'CD', 'GLN', 7.63), ('ND1', 'HIS', 'OE1', 'GLN', 7.02), ('ND1', 'HIS', 'NE2', 'GLN', 8.92)], [('CD2', 'HIS', 'CB', 'GLN', 5.24), ('CD2', 'HIS', 'CG', 'GLN', 5.74), ('CD2', 'HIS', 'CD', 'GLN', 6.3), ('CD2', 'HIS', 'OE1', 'GLN', 5.84), ('CD2', 'HIS', 'NE2', 'GLN', 7.62)], [('CE1', 'HIS', 'CB', 'GLN', 5.82), ('CE1', 'HIS', 'CG', 'GLN', 6.71), ('CE1', 'HIS', 'CD', 'GLN', 6.85), ('CE1', 'HIS', 'OE1', 'GLN', 6.04), ('CE1', 'HIS', 'NE2', 'GLN', 8.11)], [('NE2', 'HIS', 'CB', 'GLN', 5.29), ('NE2', 'HIS', 'CG', 'GLN', 5.82), ('NE2', 'HIS', 'CD', 'GLN', 5.94), ('NE2', 'HIS', 'OE1', 'GLN', 5.17), ('NE2', 'HIS', 'NE2', 'GLN', 7.24)]]}
ARG_CYS = { 
	'distances':
		[[10.52, 12.18], [9.18, 10.82], [9.73, 11.21], [9.12, 10.49], [9.32, 10.47], [10.0, 11.06], [9.28, 10.23], [15.72, 15.79], [14.78, 14.71], [13.62, 13.68], [12.69, 12.62], [11.36, 11.33], [10.92, 11.1], [10.63, 10.44]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'CYS', 10.52), ('CB', 'ARG', 'SG', 'CYS', 12.18)], [('CG', 'ARG', 'CB', 'CYS', 9.18), ('CG', 'ARG', 'SG', 'CYS', 10.82)], [('CD', 'ARG', 'CB', 'CYS', 9.73), ('CD', 'ARG', 'SG', 'CYS', 11.21)], [('NE', 'ARG', 'CB', 'CYS', 9.12), ('NE', 'ARG', 'SG', 'CYS', 10.49)], [('CZ', 'ARG', 'CB', 'CYS', 9.32), ('CZ', 'ARG', 'SG', 'CYS', 10.47)], [('NH1', 'ARG', 'CB', 'CYS', 10.0), ('NH1', 'ARG', 'SG', 'CYS', 11.06)], [('NH2', 'ARG', 'CB', 'CYS', 9.28), ('NH2', 'ARG', 'SG', 'CYS', 10.23)], [('CB', 'ARG', 'CB', 'CYS', 15.72), ('CB', 'ARG', 'SG', 'CYS', 15.79)], [('CG', 'ARG', 'CB', 'CYS', 14.78), ('CG', 'ARG', 'SG', 'CYS', 14.71)], [('CD', 'ARG', 'CB', 'CYS', 13.62), ('CD', 'ARG', 'SG', 'CYS', 13.68)], [('NE', 'ARG', 'CB', 'CYS', 12.69), ('NE', 'ARG', 'SG', 'CYS', 12.62)], [('CZ', 'ARG', 'CB', 'CYS', 11.36), ('CZ', 'ARG', 'SG', 'CYS', 11.33)], [('NH1', 'ARG', 'CB', 'CYS', 10.92), ('NH1', 'ARG', 'SG', 'CYS', 11.1)], [('NH2', 'ARG', 'CB', 'CYS', 10.63), ('NH2', 'ARG', 'SG', 'CYS', 10.44)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_CYS, d, 'A_1akm_2_1_3_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'A_1akm_2_1_3_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_CYS, d, 'A_1akm_2_1_3_3')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_ARG, d, 'A_1akm_2_1_3_3')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLN_CYS, d, 'A_1akm_2_1_3_3')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ARG_ARG, d, 'A_1akm_2_1_3_3')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(GLN_ASP, d, 'A_1akm_2_1_3_3')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ARG_ASP, d, 'A_1akm_2_1_3_3')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(GLN_ARG, d, 'A_1akm_2_1_3_3')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(HIS_GLN, d, 'A_1akm_2_1_3_3')
	if match10 == []:
		 flag = True
		 break
	match11 , totTime11 = cmd.detect(ARG_CYS, d, 'A_1akm_2_1_3_3')
	if match11 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_CYS' :  match1,
		'HIS_ASP' :  match2,
		'HIS_CYS' :  match3,
		'HIS_ARG' :  match4,
		'GLN_CYS' :  match5,
		'ARG_ARG' :  match6,
		'GLN_ASP' :  match7,
		'ARG_ASP' :  match8,
		'GLN_ARG' :  match9,
		'HIS_GLN' :  match10,
		'ARG_CYS' :  match11}