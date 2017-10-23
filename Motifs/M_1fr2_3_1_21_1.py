'''
FUNC:M_1fr2_3_1_21_1
PDB:1fr2
EC:3.1.21.1
RESI:arg,glu,his,his,zn
LOCI:b-5,100,102,103,301;
'''
import motifFunctions as cmd
HIS_ZN = { 
	'distances':
		[[5.52], [5.08], [4.0], [6.16], [4.89], [6.05], [7.59], [8.26], [7.89], [9.53], [9.0], [9.9]],
	'comparisons':
		[[('CB', 'HIS', 'ZN', 'ZN', 5.52)], [('CG', 'HIS', 'ZN', 'ZN', 5.08)], [('ND1', 'HIS', 'ZN', 'ZN', 4.0)], [('CD2', 'HIS', 'ZN', 'ZN', 6.16)], [('CE1', 'HIS', 'ZN', 'ZN', 4.89)], [('NE2', 'HIS', 'ZN', 'ZN', 6.05)], [('CB', 'HIS', 'ZN', 'ZN', 7.59)], [('CG', 'HIS', 'ZN', 'ZN', 8.26)], [('ND1', 'HIS', 'ZN', 'ZN', 7.89)], [('CD2', 'HIS', 'ZN', 'ZN', 9.53)], [('CE1', 'HIS', 'ZN', 'ZN', 9.0)], [('NE2', 'HIS', 'ZN', 'ZN', 9.9)]]}
HIS_HIS = { 
	'distances':
		[[7.8, 8.28, 8.17, 9.17, 8.98, 9.55], [7.48, 8.28, 8.38, 9.3, 9.39, 9.9], [7.33, 8.25, 8.27, 9.43, 9.41, 10.05], [7.8, 8.78, 9.13, 9.73, 10.16, 10.5], [7.58, 8.73, 8.95, 9.91, 10.17, 10.7], [7.85, 9.04, 9.44, 10.09, 10.6, 10.97], [7.8, 7.48, 7.33, 7.8, 7.58, 7.85], [8.28, 8.28, 8.25, 8.78, 8.73, 9.04], [8.17, 8.38, 8.27, 9.13, 8.95, 9.44], [9.17, 9.3, 9.43, 9.73, 9.91, 10.09], [8.98, 9.39, 9.41, 10.16, 10.17, 10.6], [9.55, 9.9, 10.05, 10.5, 10.7, 10.97]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 7.8), ('CB', 'HIS', 'CG', 'HIS', 8.28), ('CB', 'HIS', 'ND1', 'HIS', 8.17), ('CB', 'HIS', 'CD2', 'HIS', 9.17), ('CB', 'HIS', 'CE1', 'HIS', 8.98), ('CB', 'HIS', 'NE2', 'HIS', 9.55)], [('CG', 'HIS', 'CB', 'HIS', 7.48), ('CG', 'HIS', 'CG', 'HIS', 8.28), ('CG', 'HIS', 'ND1', 'HIS', 8.38), ('CG', 'HIS', 'CD2', 'HIS', 9.3), ('CG', 'HIS', 'CE1', 'HIS', 9.39), ('CG', 'HIS', 'NE2', 'HIS', 9.9)], [('ND1', 'HIS', 'CB', 'HIS', 7.33), ('ND1', 'HIS', 'CG', 'HIS', 8.25), ('ND1', 'HIS', 'ND1', 'HIS', 8.27), ('ND1', 'HIS', 'CD2', 'HIS', 9.43), ('ND1', 'HIS', 'CE1', 'HIS', 9.41), ('ND1', 'HIS', 'NE2', 'HIS', 10.05)], [('CD2', 'HIS', 'CB', 'HIS', 7.8), ('CD2', 'HIS', 'CG', 'HIS', 8.78), ('CD2', 'HIS', 'ND1', 'HIS', 9.13), ('CD2', 'HIS', 'CD2', 'HIS', 9.73), ('CD2', 'HIS', 'CE1', 'HIS', 10.16), ('CD2', 'HIS', 'NE2', 'HIS', 10.5)], [('CE1', 'HIS', 'CB', 'HIS', 7.58), ('CE1', 'HIS', 'CG', 'HIS', 8.73), ('CE1', 'HIS', 'ND1', 'HIS', 8.95), ('CE1', 'HIS', 'CD2', 'HIS', 9.91), ('CE1', 'HIS', 'CE1', 'HIS', 10.17), ('CE1', 'HIS', 'NE2', 'HIS', 10.7)], [('NE2', 'HIS', 'CB', 'HIS', 7.85), ('NE2', 'HIS', 'CG', 'HIS', 9.04), ('NE2', 'HIS', 'ND1', 'HIS', 9.44), ('NE2', 'HIS', 'CD2', 'HIS', 10.09), ('NE2', 'HIS', 'CE1', 'HIS', 10.6), ('NE2', 'HIS', 'NE2', 'HIS', 10.97)], [('CB', 'HIS', 'CB', 'HIS', 7.8), ('CB', 'HIS', 'CG', 'HIS', 7.48), ('CB', 'HIS', 'ND1', 'HIS', 7.33), ('CB', 'HIS', 'CD2', 'HIS', 7.8), ('CB', 'HIS', 'CE1', 'HIS', 7.58), ('CB', 'HIS', 'NE2', 'HIS', 7.85)], [('CG', 'HIS', 'CB', 'HIS', 8.28), ('CG', 'HIS', 'CG', 'HIS', 8.28), ('CG', 'HIS', 'ND1', 'HIS', 8.25), ('CG', 'HIS', 'CD2', 'HIS', 8.78), ('CG', 'HIS', 'CE1', 'HIS', 8.73), ('CG', 'HIS', 'NE2', 'HIS', 9.04)], [('ND1', 'HIS', 'CB', 'HIS', 8.17), ('ND1', 'HIS', 'CG', 'HIS', 8.38), ('ND1', 'HIS', 'ND1', 'HIS', 8.27), ('ND1', 'HIS', 'CD2', 'HIS', 9.13), ('ND1', 'HIS', 'CE1', 'HIS', 8.95), ('ND1', 'HIS', 'NE2', 'HIS', 9.44)], [('CD2', 'HIS', 'CB', 'HIS', 9.17), ('CD2', 'HIS', 'CG', 'HIS', 9.3), ('CD2', 'HIS', 'ND1', 'HIS', 9.43), ('CD2', 'HIS', 'CD2', 'HIS', 9.73), ('CD2', 'HIS', 'CE1', 'HIS', 9.91), ('CD2', 'HIS', 'NE2', 'HIS', 10.09)], [('CE1', 'HIS', 'CB', 'HIS', 8.98), ('CE1', 'HIS', 'CG', 'HIS', 9.39), ('CE1', 'HIS', 'ND1', 'HIS', 9.41), ('CE1', 'HIS', 'CD2', 'HIS', 10.16), ('CE1', 'HIS', 'CE1', 'HIS', 10.17), ('CE1', 'HIS', 'NE2', 'HIS', 10.6)], [('NE2', 'HIS', 'CB', 'HIS', 9.55), ('NE2', 'HIS', 'CG', 'HIS', 9.9), ('NE2', 'HIS', 'ND1', 'HIS', 10.05), ('NE2', 'HIS', 'CD2', 'HIS', 10.5), ('NE2', 'HIS', 'CE1', 'HIS', 10.7), ('NE2', 'HIS', 'NE2', 'HIS', 10.97)]]}
HIS_ARG = { 
	'distances':
		[[14.12, 14.46, 13.25, 12.49, 11.41, 10.95, 10.97], [14.6, 14.95, 13.76, 12.84, 11.71, 11.38, 11.08], [14.26, 14.54, 13.3, 12.3, 11.1, 10.8, 10.39], [15.58, 16.02, 14.87, 13.9, 12.79, 12.55, 12.08], [15.05, 15.37, 14.16, 13.08, 11.88, 11.69, 11.04], [15.83, 16.24, 15.09, 14.02, 12.87, 12.71, 12.03], [10.9, 11.71, 10.97, 9.81, 9.08, 9.51, 8.18], [9.69, 10.58, 9.94, 8.89, 8.32, 8.79, 7.61], [8.71, 9.48, 8.72, 7.74, 7.12, 7.5, 6.56], [9.55, 10.63, 10.19, 9.26, 8.91, 9.46, 8.34], [7.93, 8.83, 8.24, 7.45, 7.09, 7.5, 6.82], [8.49, 9.58, 9.2, 8.43, 8.23, 8.74, 7.9]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 14.12), ('CB', 'HIS', 'CG', 'ARG', 14.46), ('CB', 'HIS', 'CD', 'ARG', 13.25), ('CB', 'HIS', 'NE', 'ARG', 12.49), ('CB', 'HIS', 'CZ', 'ARG', 11.41), ('CB', 'HIS', 'NH1', 'ARG', 10.95), ('CB', 'HIS', 'NH2', 'ARG', 10.97)], [('CG', 'HIS', 'CB', 'ARG', 14.6), ('CG', 'HIS', 'CG', 'ARG', 14.95), ('CG', 'HIS', 'CD', 'ARG', 13.76), ('CG', 'HIS', 'NE', 'ARG', 12.84), ('CG', 'HIS', 'CZ', 'ARG', 11.71), ('CG', 'HIS', 'NH1', 'ARG', 11.38), ('CG', 'HIS', 'NH2', 'ARG', 11.08)], [('ND1', 'HIS', 'CB', 'ARG', 14.26), ('ND1', 'HIS', 'CG', 'ARG', 14.54), ('ND1', 'HIS', 'CD', 'ARG', 13.3), ('ND1', 'HIS', 'NE', 'ARG', 12.3), ('ND1', 'HIS', 'CZ', 'ARG', 11.1), ('ND1', 'HIS', 'NH1', 'ARG', 10.8), ('ND1', 'HIS', 'NH2', 'ARG', 10.39)], [('CD2', 'HIS', 'CB', 'ARG', 15.58), ('CD2', 'HIS', 'CG', 'ARG', 16.02), ('CD2', 'HIS', 'CD', 'ARG', 14.87), ('CD2', 'HIS', 'NE', 'ARG', 13.9), ('CD2', 'HIS', 'CZ', 'ARG', 12.79), ('CD2', 'HIS', 'NH1', 'ARG', 12.55), ('CD2', 'HIS', 'NH2', 'ARG', 12.08)], [('CE1', 'HIS', 'CB', 'ARG', 15.05), ('CE1', 'HIS', 'CG', 'ARG', 15.37), ('CE1', 'HIS', 'CD', 'ARG', 14.16), ('CE1', 'HIS', 'NE', 'ARG', 13.08), ('CE1', 'HIS', 'CZ', 'ARG', 11.88), ('CE1', 'HIS', 'NH1', 'ARG', 11.69), ('CE1', 'HIS', 'NH2', 'ARG', 11.04)], [('NE2', 'HIS', 'CB', 'ARG', 15.83), ('NE2', 'HIS', 'CG', 'ARG', 16.24), ('NE2', 'HIS', 'CD', 'ARG', 15.09), ('NE2', 'HIS', 'NE', 'ARG', 14.02), ('NE2', 'HIS', 'CZ', 'ARG', 12.87), ('NE2', 'HIS', 'NH1', 'ARG', 12.71), ('NE2', 'HIS', 'NH2', 'ARG', 12.03)], [('CB', 'HIS', 'CB', 'ARG', 10.9), ('CB', 'HIS', 'CG', 'ARG', 11.71), ('CB', 'HIS', 'CD', 'ARG', 10.97), ('CB', 'HIS', 'NE', 'ARG', 9.81), ('CB', 'HIS', 'CZ', 'ARG', 9.08), ('CB', 'HIS', 'NH1', 'ARG', 9.51), ('CB', 'HIS', 'NH2', 'ARG', 8.18)], [('CG', 'HIS', 'CB', 'ARG', 9.69), ('CG', 'HIS', 'CG', 'ARG', 10.58), ('CG', 'HIS', 'CD', 'ARG', 9.94), ('CG', 'HIS', 'NE', 'ARG', 8.89), ('CG', 'HIS', 'CZ', 'ARG', 8.32), ('CG', 'HIS', 'NH1', 'ARG', 8.79), ('CG', 'HIS', 'NH2', 'ARG', 7.61)], [('ND1', 'HIS', 'CB', 'ARG', 8.71), ('ND1', 'HIS', 'CG', 'ARG', 9.48), ('ND1', 'HIS', 'CD', 'ARG', 8.72), ('ND1', 'HIS', 'NE', 'ARG', 7.74), ('ND1', 'HIS', 'CZ', 'ARG', 7.12), ('ND1', 'HIS', 'NH1', 'ARG', 7.5), ('ND1', 'HIS', 'NH2', 'ARG', 6.56)], [('CD2', 'HIS', 'CB', 'ARG', 9.55), ('CD2', 'HIS', 'CG', 'ARG', 10.63), ('CD2', 'HIS', 'CD', 'ARG', 10.19), ('CD2', 'HIS', 'NE', 'ARG', 9.26), ('CD2', 'HIS', 'CZ', 'ARG', 8.91), ('CD2', 'HIS', 'NH1', 'ARG', 9.46), ('CD2', 'HIS', 'NH2', 'ARG', 8.34)], [('CE1', 'HIS', 'CB', 'ARG', 7.93), ('CE1', 'HIS', 'CG', 'ARG', 8.83), ('CE1', 'HIS', 'CD', 'ARG', 8.24), ('CE1', 'HIS', 'NE', 'ARG', 7.45), ('CE1', 'HIS', 'CZ', 'ARG', 7.09), ('CE1', 'HIS', 'NH1', 'ARG', 7.5), ('CE1', 'HIS', 'NH2', 'ARG', 6.82)], [('NE2', 'HIS', 'CB', 'ARG', 8.49), ('NE2', 'HIS', 'CG', 'ARG', 9.58), ('NE2', 'HIS', 'CD', 'ARG', 9.2), ('NE2', 'HIS', 'NE', 'ARG', 8.43), ('NE2', 'HIS', 'CZ', 'ARG', 8.23), ('NE2', 'HIS', 'NH1', 'ARG', 8.74), ('NE2', 'HIS', 'NH2', 'ARG', 7.9)]]}
ARG_ZN = { 
	'distances':
		[[13.09], [13.17], [11.84], [10.88], [9.61], [9.18], [8.96]],
	'comparisons':
		[[('CB', 'ARG', 'ZN', 'ZN', 13.09)], [('CG', 'ARG', 'ZN', 'ZN', 13.17)], [('CD', 'ARG', 'ZN', 'ZN', 11.84)], [('NE', 'ARG', 'ZN', 'ZN', 10.88)], [('CZ', 'ARG', 'ZN', 'ZN', 9.61)], [('NH1', 'ARG', 'ZN', 'ZN', 9.18)], [('NH2', 'ARG', 'ZN', 'ZN', 8.96)]]}
ZN_HISI = { 
	'distances':
		[7.59, 8.26, 7.89, 9.53, 9.0, 9.9],
	'comparisons':
		[('ZN', 'ZN', 'CB', 'HISI', 7.59), ('ZN', 'ZN', 'CG', 'HISI', 8.26), ('ZN', 'ZN', 'ND1', 'HISI', 7.89), ('ZN', 'ZN', 'CD2', 'HISI', 9.53), ('ZN', 'ZN', 'CE1', 'HISI', 9.0), ('ZN', 'ZN', 'NE2', 'HISI', 9.9)]}
GLU_ARG = { 
	'distances':
		[[14.86, 14.64, 13.31, 13.26, 12.33, 11.22, 12.65], [15.58, 15.2, 13.86, 13.93, 13.02, 11.82, 13.43], [15.84, 15.36, 13.94, 13.94, 12.95, 11.73, 13.31], [15.53, 15.09, 13.63, 13.49, 12.41, 11.24, 12.64], [16.53, 15.95, 14.54, 14.62, 13.66, 12.4, 14.08]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 14.86), ('CB', 'GLU', 'CG', 'ARG', 14.64), ('CB', 'GLU', 'CD', 'ARG', 13.31), ('CB', 'GLU', 'NE', 'ARG', 13.26), ('CB', 'GLU', 'CZ', 'ARG', 12.33), ('CB', 'GLU', 'NH1', 'ARG', 11.22), ('CB', 'GLU', 'NH2', 'ARG', 12.65)], [('CG', 'GLU', 'CB', 'ARG', 15.58), ('CG', 'GLU', 'CG', 'ARG', 15.2), ('CG', 'GLU', 'CD', 'ARG', 13.86), ('CG', 'GLU', 'NE', 'ARG', 13.93), ('CG', 'GLU', 'CZ', 'ARG', 13.02), ('CG', 'GLU', 'NH1', 'ARG', 11.82), ('CG', 'GLU', 'NH2', 'ARG', 13.43)], [('CD', 'GLU', 'CB', 'ARG', 15.84), ('CD', 'GLU', 'CG', 'ARG', 15.36), ('CD', 'GLU', 'CD', 'ARG', 13.94), ('CD', 'GLU', 'NE', 'ARG', 13.94), ('CD', 'GLU', 'CZ', 'ARG', 12.95), ('CD', 'GLU', 'NH1', 'ARG', 11.73), ('CD', 'GLU', 'NH2', 'ARG', 13.31)], [('OE1', 'GLU', 'CB', 'ARG', 15.53), ('OE1', 'GLU', 'CG', 'ARG', 15.09), ('OE1', 'GLU', 'CD', 'ARG', 13.63), ('OE1', 'GLU', 'NE', 'ARG', 13.49), ('OE1', 'GLU', 'CZ', 'ARG', 12.41), ('OE1', 'GLU', 'NH1', 'ARG', 11.24), ('OE1', 'GLU', 'NH2', 'ARG', 12.64)], [('OE2', 'GLU', 'CB', 'ARG', 16.53), ('OE2', 'GLU', 'CG', 'ARG', 15.95), ('OE2', 'GLU', 'CD', 'ARG', 14.54), ('OE2', 'GLU', 'NE', 'ARG', 14.62), ('OE2', 'GLU', 'CZ', 'ARG', 13.66), ('OE2', 'GLU', 'NH1', 'ARG', 12.4), ('OE2', 'GLU', 'NH2', 'ARG', 14.08)]]}
GLU_ZN = { 
	'distances':
		[[9.22], [10.27], [9.95], [8.85], [11.0]],
	'comparisons':
		[[('CB', 'GLU', 'ZN', 'ZN', 9.22)], [('CG', 'GLU', 'ZN', 'ZN', 10.27)], [('CD', 'GLU', 'ZN', 'ZN', 9.95)], [('OE1', 'GLU', 'ZN', 'ZN', 8.85)], [('OE2', 'GLU', 'ZN', 'ZN', 11.0)]]}
GLU_HISI = { 
	'distances':
		[[12.72, 12.51, 11.65, 13.2, 11.87, 12.82], [14.06, 13.83, 12.9, 14.55, 13.1, 14.11], [14.28, 14.16, 13.22, 15.01, 13.55, 14.63], [13.46, 13.46, 12.56, 14.39, 13.01, 14.11], [15.42, 15.29, 14.3, 16.14, 14.61, 15.72]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HISI', 12.72), ('CB', 'GLU', 'CG', 'HISI', 12.51), ('CB', 'GLU', 'ND1', 'HISI', 11.65), ('CB', 'GLU', 'CD2', 'HISI', 13.2), ('CB', 'GLU', 'CE1', 'HISI', 11.87), ('CB', 'GLU', 'NE2', 'HISI', 12.82)], [('CG', 'GLU', 'CB', 'HISI', 14.06), ('CG', 'GLU', 'CG', 'HISI', 13.83), ('CG', 'GLU', 'ND1', 'HISI', 12.9), ('CG', 'GLU', 'CD2', 'HISI', 14.55), ('CG', 'GLU', 'CE1', 'HISI', 13.1), ('CG', 'GLU', 'NE2', 'HISI', 14.11)], [('CD', 'GLU', 'CB', 'HISI', 14.28), ('CD', 'GLU', 'CG', 'HISI', 14.16), ('CD', 'GLU', 'ND1', 'HISI', 13.22), ('CD', 'GLU', 'CD2', 'HISI', 15.01), ('CD', 'GLU', 'CE1', 'HISI', 13.55), ('CD', 'GLU', 'NE2', 'HISI', 14.63)], [('OE1', 'GLU', 'CB', 'HISI', 13.46), ('OE1', 'GLU', 'CG', 'HISI', 13.46), ('OE1', 'GLU', 'ND1', 'HISI', 12.56), ('OE1', 'GLU', 'CD2', 'HISI', 14.39), ('OE1', 'GLU', 'CE1', 'HISI', 13.01), ('OE1', 'GLU', 'NE2', 'HISI', 14.11)], [('OE2', 'GLU', 'CB', 'HISI', 15.42), ('OE2', 'GLU', 'CG', 'HISI', 15.29), ('OE2', 'GLU', 'ND1', 'HISI', 14.3), ('OE2', 'GLU', 'CD2', 'HISI', 16.14), ('OE2', 'GLU', 'CE1', 'HISI', 14.61), ('OE2', 'GLU', 'NE2', 'HISI', 15.72)]]}
HIS_GLU = { 
	'distances':
		[[8.21, 9.63, 9.89, 9.08, 11.12], [9.45, 10.79, 10.87, 9.92, 12.05], [9.82, 11.03, 10.9, 9.84, 12.03], [10.6, 11.94, 12.03, 11.08, 13.21], [11.06, 12.24, 12.04, 10.94, 13.13], [11.5, 12.75, 12.68, 11.63, 13.81], [12.72, 14.06, 14.28, 13.46, 15.42], [12.51, 13.83, 14.16, 13.46, 15.29], [11.65, 12.9, 13.22, 12.56, 14.3], [13.2, 14.55, 15.01, 14.39, 16.14], [11.87, 13.1, 13.55, 13.01, 14.61], [12.82, 14.11, 14.63, 14.11, 15.72]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 8.21), ('CB', 'HIS', 'CG', 'GLU', 9.63), ('CB', 'HIS', 'CD', 'GLU', 9.89), ('CB', 'HIS', 'OE1', 'GLU', 9.08), ('CB', 'HIS', 'OE2', 'GLU', 11.12)], [('CG', 'HIS', 'CB', 'GLU', 9.45), ('CG', 'HIS', 'CG', 'GLU', 10.79), ('CG', 'HIS', 'CD', 'GLU', 10.87), ('CG', 'HIS', 'OE1', 'GLU', 9.92), ('CG', 'HIS', 'OE2', 'GLU', 12.05)], [('ND1', 'HIS', 'CB', 'GLU', 9.82), ('ND1', 'HIS', 'CG', 'GLU', 11.03), ('ND1', 'HIS', 'CD', 'GLU', 10.9), ('ND1', 'HIS', 'OE1', 'GLU', 9.84), ('ND1', 'HIS', 'OE2', 'GLU', 12.03)], [('CD2', 'HIS', 'CB', 'GLU', 10.6), ('CD2', 'HIS', 'CG', 'GLU', 11.94), ('CD2', 'HIS', 'CD', 'GLU', 12.03), ('CD2', 'HIS', 'OE1', 'GLU', 11.08), ('CD2', 'HIS', 'OE2', 'GLU', 13.21)], [('CE1', 'HIS', 'CB', 'GLU', 11.06), ('CE1', 'HIS', 'CG', 'GLU', 12.24), ('CE1', 'HIS', 'CD', 'GLU', 12.04), ('CE1', 'HIS', 'OE1', 'GLU', 10.94), ('CE1', 'HIS', 'OE2', 'GLU', 13.13)], [('NE2', 'HIS', 'CB', 'GLU', 11.5), ('NE2', 'HIS', 'CG', 'GLU', 12.75), ('NE2', 'HIS', 'CD', 'GLU', 12.68), ('NE2', 'HIS', 'OE1', 'GLU', 11.63), ('NE2', 'HIS', 'OE2', 'GLU', 13.81)], [('CB', 'HIS', 'CB', 'GLU', 12.72), ('CB', 'HIS', 'CG', 'GLU', 14.06), ('CB', 'HIS', 'CD', 'GLU', 14.28), ('CB', 'HIS', 'OE1', 'GLU', 13.46), ('CB', 'HIS', 'OE2', 'GLU', 15.42)], [('CG', 'HIS', 'CB', 'GLU', 12.51), ('CG', 'HIS', 'CG', 'GLU', 13.83), ('CG', 'HIS', 'CD', 'GLU', 14.16), ('CG', 'HIS', 'OE1', 'GLU', 13.46), ('CG', 'HIS', 'OE2', 'GLU', 15.29)], [('ND1', 'HIS', 'CB', 'GLU', 11.65), ('ND1', 'HIS', 'CG', 'GLU', 12.9), ('ND1', 'HIS', 'CD', 'GLU', 13.22), ('ND1', 'HIS', 'OE1', 'GLU', 12.56), ('ND1', 'HIS', 'OE2', 'GLU', 14.3)], [('CD2', 'HIS', 'CB', 'GLU', 13.2), ('CD2', 'HIS', 'CG', 'GLU', 14.55), ('CD2', 'HIS', 'CD', 'GLU', 15.01), ('CD2', 'HIS', 'OE1', 'GLU', 14.39), ('CD2', 'HIS', 'OE2', 'GLU', 16.14)], [('CE1', 'HIS', 'CB', 'GLU', 11.87), ('CE1', 'HIS', 'CG', 'GLU', 13.1), ('CE1', 'HIS', 'CD', 'GLU', 13.55), ('CE1', 'HIS', 'OE1', 'GLU', 13.01), ('CE1', 'HIS', 'OE2', 'GLU', 14.61)], [('NE2', 'HIS', 'CB', 'GLU', 12.82), ('NE2', 'HIS', 'CG', 'GLU', 14.11), ('NE2', 'HIS', 'CD', 'GLU', 14.63), ('NE2', 'HIS', 'OE1', 'GLU', 14.11), ('NE2', 'HIS', 'OE2', 'GLU', 15.72)]]}
ARG_HISI = { 
	'distances':
		[[10.9, 9.69, 8.71, 9.55, 7.93, 8.49], [11.71, 10.58, 9.48, 10.63, 8.83, 9.58], [10.97, 9.94, 8.72, 10.19, 8.24, 9.2], [9.81, 8.89, 7.74, 9.26, 7.45, 8.43], [9.08, 8.32, 7.12, 8.91, 7.09, 8.23], [9.51, 8.79, 7.5, 9.46, 7.5, 8.74], [8.18, 7.61, 6.56, 8.34, 6.82, 7.9]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'HISI', 10.9), ('CB', 'ARG', 'CG', 'HISI', 9.69), ('CB', 'ARG', 'ND1', 'HISI', 8.71), ('CB', 'ARG', 'CD2', 'HISI', 9.55), ('CB', 'ARG', 'CE1', 'HISI', 7.93), ('CB', 'ARG', 'NE2', 'HISI', 8.49)], [('CG', 'ARG', 'CB', 'HISI', 11.71), ('CG', 'ARG', 'CG', 'HISI', 10.58), ('CG', 'ARG', 'ND1', 'HISI', 9.48), ('CG', 'ARG', 'CD2', 'HISI', 10.63), ('CG', 'ARG', 'CE1', 'HISI', 8.83), ('CG', 'ARG', 'NE2', 'HISI', 9.58)], [('CD', 'ARG', 'CB', 'HISI', 10.97), ('CD', 'ARG', 'CG', 'HISI', 9.94), ('CD', 'ARG', 'ND1', 'HISI', 8.72), ('CD', 'ARG', 'CD2', 'HISI', 10.19), ('CD', 'ARG', 'CE1', 'HISI', 8.24), ('CD', 'ARG', 'NE2', 'HISI', 9.2)], [('NE', 'ARG', 'CB', 'HISI', 9.81), ('NE', 'ARG', 'CG', 'HISI', 8.89), ('NE', 'ARG', 'ND1', 'HISI', 7.74), ('NE', 'ARG', 'CD2', 'HISI', 9.26), ('NE', 'ARG', 'CE1', 'HISI', 7.45), ('NE', 'ARG', 'NE2', 'HISI', 8.43)], [('CZ', 'ARG', 'CB', 'HISI', 9.08), ('CZ', 'ARG', 'CG', 'HISI', 8.32), ('CZ', 'ARG', 'ND1', 'HISI', 7.12), ('CZ', 'ARG', 'CD2', 'HISI', 8.91), ('CZ', 'ARG', 'CE1', 'HISI', 7.09), ('CZ', 'ARG', 'NE2', 'HISI', 8.23)], [('NH1', 'ARG', 'CB', 'HISI', 9.51), ('NH1', 'ARG', 'CG', 'HISI', 8.79), ('NH1', 'ARG', 'ND1', 'HISI', 7.5), ('NH1', 'ARG', 'CD2', 'HISI', 9.46), ('NH1', 'ARG', 'CE1', 'HISI', 7.5), ('NH1', 'ARG', 'NE2', 'HISI', 8.74)], [('NH2', 'ARG', 'CB', 'HISI', 8.18), ('NH2', 'ARG', 'CG', 'HISI', 7.61), ('NH2', 'ARG', 'ND1', 'HISI', 6.56), ('NH2', 'ARG', 'CD2', 'HISI', 8.34), ('NH2', 'ARG', 'CE1', 'HISI', 6.82), ('NH2', 'ARG', 'NE2', 'HISI', 7.9)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ZN, d, 'M_1fr2_3_1_21_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_HIS, d, 'M_1fr2_3_1_21_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ARG, d, 'M_1fr2_3_1_21_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ARG_ZN, d, 'M_1fr2_3_1_21_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ZN_HISI, d, 'M_1fr2_3_1_21_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLU_ARG, d, 'M_1fr2_3_1_21_1')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(GLU_ZN, d, 'M_1fr2_3_1_21_1')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(GLU_HISI, d, 'M_1fr2_3_1_21_1')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(HIS_GLU, d, 'M_1fr2_3_1_21_1')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(ARG_HISI, d, 'M_1fr2_3_1_21_1')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ZN' :  match1,
		'HIS_HIS' :  match2,
		'HIS_ARG' :  match3,
		'ARG_ZN' :  match4,
		'ZN_HISI' :  match5,
		'GLU_ARG' :  match6,
		'GLU_ZN' :  match7,
		'GLU_HISI' :  match8,
		'HIS_GLU' :  match9,
		'ARG_HISI' :  match10}