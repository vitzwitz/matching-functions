'''
FUNC:A_1bqc_3_2_1_78
PDB:1bqc
EC:3.2.1.78
RESI:asn,glu,his,tyr,glu
LOCI:a-127,128,196,198,225;
'''
import motifFunctions as cmd
GLU_GLU = { 
	'distances':
		[[10.26, 8.75, 8.33, 9.3, 7.2], [9.71, 8.26, 7.94, 8.89, 6.96], [8.77, 7.36, 6.83, 7.64, 5.89], [8.8, 7.39, 6.55, 7.21, 5.47], [8.26, 6.99, 6.64, 7.39, 5.97], [10.26, 9.71, 8.77, 8.8, 8.26], [8.75, 8.26, 7.36, 7.39, 6.99], [8.33, 7.94, 6.83, 6.55, 6.64], [9.3, 8.89, 7.64, 7.21, 7.39], [7.2, 6.96, 5.89, 5.47, 5.97]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 10.26), ('CB', 'GLU', 'CG', 'GLU', 8.75), ('CB', 'GLU', 'CD', 'GLU', 8.33), ('CB', 'GLU', 'OE1', 'GLU', 9.3), ('CB', 'GLU', 'OE2', 'GLU', 7.2)], [('CG', 'GLU', 'CB', 'GLU', 9.71), ('CG', 'GLU', 'CG', 'GLU', 8.26), ('CG', 'GLU', 'CD', 'GLU', 7.94), ('CG', 'GLU', 'OE1', 'GLU', 8.89), ('CG', 'GLU', 'OE2', 'GLU', 6.96)], [('CD', 'GLU', 'CB', 'GLU', 8.77), ('CD', 'GLU', 'CG', 'GLU', 7.36), ('CD', 'GLU', 'CD', 'GLU', 6.83), ('CD', 'GLU', 'OE1', 'GLU', 7.64), ('CD', 'GLU', 'OE2', 'GLU', 5.89)], [('OE1', 'GLU', 'CB', 'GLU', 8.8), ('OE1', 'GLU', 'CG', 'GLU', 7.39), ('OE1', 'GLU', 'CD', 'GLU', 6.55), ('OE1', 'GLU', 'OE1', 'GLU', 7.21), ('OE1', 'GLU', 'OE2', 'GLU', 5.47)], [('OE2', 'GLU', 'CB', 'GLU', 8.26), ('OE2', 'GLU', 'CG', 'GLU', 6.99), ('OE2', 'GLU', 'CD', 'GLU', 6.64), ('OE2', 'GLU', 'OE1', 'GLU', 7.39), ('OE2', 'GLU', 'OE2', 'GLU', 5.97)], [('CB', 'GLU', 'CB', 'GLU', 10.26), ('CB', 'GLU', 'CG', 'GLU', 9.71), ('CB', 'GLU', 'CD', 'GLU', 8.77), ('CB', 'GLU', 'OE1', 'GLU', 8.8), ('CB', 'GLU', 'OE2', 'GLU', 8.26)], [('CG', 'GLU', 'CB', 'GLU', 8.75), ('CG', 'GLU', 'CG', 'GLU', 8.26), ('CG', 'GLU', 'CD', 'GLU', 7.36), ('CG', 'GLU', 'OE1', 'GLU', 7.39), ('CG', 'GLU', 'OE2', 'GLU', 6.99)], [('CD', 'GLU', 'CB', 'GLU', 8.33), ('CD', 'GLU', 'CG', 'GLU', 7.94), ('CD', 'GLU', 'CD', 'GLU', 6.83), ('CD', 'GLU', 'OE1', 'GLU', 6.55), ('CD', 'GLU', 'OE2', 'GLU', 6.64)], [('OE1', 'GLU', 'CB', 'GLU', 9.3), ('OE1', 'GLU', 'CG', 'GLU', 8.89), ('OE1', 'GLU', 'CD', 'GLU', 7.64), ('OE1', 'GLU', 'OE1', 'GLU', 7.21), ('OE1', 'GLU', 'OE2', 'GLU', 7.39)], [('OE2', 'GLU', 'CB', 'GLU', 7.2), ('OE2', 'GLU', 'CG', 'GLU', 6.96), ('OE2', 'GLU', 'CD', 'GLU', 5.89), ('OE2', 'GLU', 'OE1', 'GLU', 5.47), ('OE2', 'GLU', 'OE2', 'GLU', 5.97)]]}
GLU_TYR = { 
	'distances':
		[[9.41, 8.07, 8.03, 7.15, 7.1, 6.02, 6.0, 5.4], [10.52, 9.14, 9.09, 8.11, 8.04, 6.87, 6.83, 5.94], [10.25, 8.85, 8.86, 7.75, 7.81, 6.45, 6.5, 5.58], [9.2, 7.78, 7.78, 6.72, 6.76, 5.4, 5.44, 4.61], [11.3, 9.93, 9.99, 8.78, 8.95, 7.52, 7.63, 6.7], [12.39, 11.7, 12.56, 10.39, 12.24, 9.99, 11.01, 10.97], [11.27, 10.47, 11.27, 9.12, 10.89, 8.63, 9.63, 9.56], [10.19, 9.35, 10.1, 8.05, 9.73, 7.54, 8.51, 8.5], [10.44, 9.67, 10.41, 8.47, 10.08, 8.04, 8.95, 8.98], [9.23, 8.28, 8.97, 6.96, 8.55, 6.35, 7.3, 7.31]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'TYR', 9.41), ('CB', 'GLU', 'CG', 'TYR', 8.07), ('CB', 'GLU', 'CD1', 'TYR', 8.03), ('CB', 'GLU', 'CD2', 'TYR', 7.15), ('CB', 'GLU', 'CE1', 'TYR', 7.1), ('CB', 'GLU', 'CE2', 'TYR', 6.02), ('CB', 'GLU', 'CZ', 'TYR', 6.0), ('CB', 'GLU', 'OH', 'TYR', 5.4)], [('CG', 'GLU', 'CB', 'TYR', 10.52), ('CG', 'GLU', 'CG', 'TYR', 9.14), ('CG', 'GLU', 'CD1', 'TYR', 9.09), ('CG', 'GLU', 'CD2', 'TYR', 8.11), ('CG', 'GLU', 'CE1', 'TYR', 8.04), ('CG', 'GLU', 'CE2', 'TYR', 6.87), ('CG', 'GLU', 'CZ', 'TYR', 6.83), ('CG', 'GLU', 'OH', 'TYR', 5.94)], [('CD', 'GLU', 'CB', 'TYR', 10.25), ('CD', 'GLU', 'CG', 'TYR', 8.85), ('CD', 'GLU', 'CD1', 'TYR', 8.86), ('CD', 'GLU', 'CD2', 'TYR', 7.75), ('CD', 'GLU', 'CE1', 'TYR', 7.81), ('CD', 'GLU', 'CE2', 'TYR', 6.45), ('CD', 'GLU', 'CZ', 'TYR', 6.5), ('CD', 'GLU', 'OH', 'TYR', 5.58)], [('OE1', 'GLU', 'CB', 'TYR', 9.2), ('OE1', 'GLU', 'CG', 'TYR', 7.78), ('OE1', 'GLU', 'CD1', 'TYR', 7.78), ('OE1', 'GLU', 'CD2', 'TYR', 6.72), ('OE1', 'GLU', 'CE1', 'TYR', 6.76), ('OE1', 'GLU', 'CE2', 'TYR', 5.4), ('OE1', 'GLU', 'CZ', 'TYR', 5.44), ('OE1', 'GLU', 'OH', 'TYR', 4.61)], [('OE2', 'GLU', 'CB', 'TYR', 11.3), ('OE2', 'GLU', 'CG', 'TYR', 9.93), ('OE2', 'GLU', 'CD1', 'TYR', 9.99), ('OE2', 'GLU', 'CD2', 'TYR', 8.78), ('OE2', 'GLU', 'CE1', 'TYR', 8.95), ('OE2', 'GLU', 'CE2', 'TYR', 7.52), ('OE2', 'GLU', 'CZ', 'TYR', 7.63), ('OE2', 'GLU', 'OH', 'TYR', 6.7)], [('CB', 'GLU', 'CB', 'TYR', 12.39), ('CB', 'GLU', 'CG', 'TYR', 11.7), ('CB', 'GLU', 'CD1', 'TYR', 12.56), ('CB', 'GLU', 'CD2', 'TYR', 10.39), ('CB', 'GLU', 'CE1', 'TYR', 12.24), ('CB', 'GLU', 'CE2', 'TYR', 9.99), ('CB', 'GLU', 'CZ', 'TYR', 11.01), ('CB', 'GLU', 'OH', 'TYR', 10.97)], [('CG', 'GLU', 'CB', 'TYR', 11.27), ('CG', 'GLU', 'CG', 'TYR', 10.47), ('CG', 'GLU', 'CD1', 'TYR', 11.27), ('CG', 'GLU', 'CD2', 'TYR', 9.12), ('CG', 'GLU', 'CE1', 'TYR', 10.89), ('CG', 'GLU', 'CE2', 'TYR', 8.63), ('CG', 'GLU', 'CZ', 'TYR', 9.63), ('CG', 'GLU', 'OH', 'TYR', 9.56)], [('CD', 'GLU', 'CB', 'TYR', 10.19), ('CD', 'GLU', 'CG', 'TYR', 9.35), ('CD', 'GLU', 'CD1', 'TYR', 10.1), ('CD', 'GLU', 'CD2', 'TYR', 8.05), ('CD', 'GLU', 'CE1', 'TYR', 9.73), ('CD', 'GLU', 'CE2', 'TYR', 7.54), ('CD', 'GLU', 'CZ', 'TYR', 8.51), ('CD', 'GLU', 'OH', 'TYR', 8.5)], [('OE1', 'GLU', 'CB', 'TYR', 10.44), ('OE1', 'GLU', 'CG', 'TYR', 9.67), ('OE1', 'GLU', 'CD1', 'TYR', 10.41), ('OE1', 'GLU', 'CD2', 'TYR', 8.47), ('OE1', 'GLU', 'CE1', 'TYR', 10.08), ('OE1', 'GLU', 'CE2', 'TYR', 8.04), ('OE1', 'GLU', 'CZ', 'TYR', 8.95), ('OE1', 'GLU', 'OH', 'TYR', 8.98)], [('OE2', 'GLU', 'CB', 'TYR', 9.23), ('OE2', 'GLU', 'CG', 'TYR', 8.28), ('OE2', 'GLU', 'CD1', 'TYR', 8.97), ('OE2', 'GLU', 'CD2', 'TYR', 6.96), ('OE2', 'GLU', 'CE1', 'TYR', 8.55), ('OE2', 'GLU', 'CE2', 'TYR', 6.35), ('OE2', 'GLU', 'CZ', 'TYR', 7.3), ('OE2', 'GLU', 'OH', 'TYR', 7.31)]]}
GLU_HIS = { 
	'distances':
		[[5.99, 5.63, 5.8, 5.8, 6.11, 6.1], [6.7, 5.9, 5.62, 5.89, 5.51, 5.66], [6.84, 6.07, 5.33, 6.42, 5.35, 6.03], [6.7, 6.28, 5.57, 6.95, 6.0, 6.81], [7.54, 6.54, 5.54, 6.75, 5.19, 6.0], [8.33, 7.68, 6.66, 8.29, 6.76, 7.8], [6.97, 6.27, 5.18, 6.98, 5.42, 6.55], [6.86, 6.44, 5.3, 7.41, 5.88, 7.13], [7.94, 7.65, 6.52, 8.65, 7.08, 8.36], [5.98, 5.68, 4.6, 6.76, 5.45, 6.66]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 5.99), ('CB', 'GLU', 'CG', 'HIS', 5.63), ('CB', 'GLU', 'ND1', 'HIS', 5.8), ('CB', 'GLU', 'CD2', 'HIS', 5.8), ('CB', 'GLU', 'CE1', 'HIS', 6.11), ('CB', 'GLU', 'NE2', 'HIS', 6.1)], [('CG', 'GLU', 'CB', 'HIS', 6.7), ('CG', 'GLU', 'CG', 'HIS', 5.9), ('CG', 'GLU', 'ND1', 'HIS', 5.62), ('CG', 'GLU', 'CD2', 'HIS', 5.89), ('CG', 'GLU', 'CE1', 'HIS', 5.51), ('CG', 'GLU', 'NE2', 'HIS', 5.66)], [('CD', 'GLU', 'CB', 'HIS', 6.84), ('CD', 'GLU', 'CG', 'HIS', 6.07), ('CD', 'GLU', 'ND1', 'HIS', 5.33), ('CD', 'GLU', 'CD2', 'HIS', 6.42), ('CD', 'GLU', 'CE1', 'HIS', 5.35), ('CD', 'GLU', 'NE2', 'HIS', 6.03)], [('OE1', 'GLU', 'CB', 'HIS', 6.7), ('OE1', 'GLU', 'CG', 'HIS', 6.28), ('OE1', 'GLU', 'ND1', 'HIS', 5.57), ('OE1', 'GLU', 'CD2', 'HIS', 6.95), ('OE1', 'GLU', 'CE1', 'HIS', 6.0), ('OE1', 'GLU', 'NE2', 'HIS', 6.81)], [('OE2', 'GLU', 'CB', 'HIS', 7.54), ('OE2', 'GLU', 'CG', 'HIS', 6.54), ('OE2', 'GLU', 'ND1', 'HIS', 5.54), ('OE2', 'GLU', 'CD2', 'HIS', 6.75), ('OE2', 'GLU', 'CE1', 'HIS', 5.19), ('OE2', 'GLU', 'NE2', 'HIS', 6.0)], [('CB', 'GLU', 'CB', 'HIS', 8.33), ('CB', 'GLU', 'CG', 'HIS', 7.68), ('CB', 'GLU', 'ND1', 'HIS', 6.66), ('CB', 'GLU', 'CD2', 'HIS', 8.29), ('CB', 'GLU', 'CE1', 'HIS', 6.76), ('CB', 'GLU', 'NE2', 'HIS', 7.8)], [('CG', 'GLU', 'CB', 'HIS', 6.97), ('CG', 'GLU', 'CG', 'HIS', 6.27), ('CG', 'GLU', 'ND1', 'HIS', 5.18), ('CG', 'GLU', 'CD2', 'HIS', 6.98), ('CG', 'GLU', 'CE1', 'HIS', 5.42), ('CG', 'GLU', 'NE2', 'HIS', 6.55)], [('CD', 'GLU', 'CB', 'HIS', 6.86), ('CD', 'GLU', 'CG', 'HIS', 6.44), ('CD', 'GLU', 'ND1', 'HIS', 5.3), ('CD', 'GLU', 'CD2', 'HIS', 7.41), ('CD', 'GLU', 'CE1', 'HIS', 5.88), ('CD', 'GLU', 'NE2', 'HIS', 7.13)], [('OE1', 'GLU', 'CB', 'HIS', 7.94), ('OE1', 'GLU', 'CG', 'HIS', 7.65), ('OE1', 'GLU', 'ND1', 'HIS', 6.52), ('OE1', 'GLU', 'CD2', 'HIS', 8.65), ('OE1', 'GLU', 'CE1', 'HIS', 7.08), ('OE1', 'GLU', 'NE2', 'HIS', 8.36)], [('OE2', 'GLU', 'CB', 'HIS', 5.98), ('OE2', 'GLU', 'CG', 'HIS', 5.68), ('OE2', 'GLU', 'ND1', 'HIS', 4.6), ('OE2', 'GLU', 'CD2', 'HIS', 6.76), ('OE2', 'GLU', 'CE1', 'HIS', 5.45), ('OE2', 'GLU', 'NE2', 'HIS', 6.66)]]}
TYR_GLUI = { 
	'distances':
		[[12.39, 11.27, 10.19, 10.44, 9.23], [11.7, 10.47, 9.35, 9.67, 8.28], [12.56, 11.27, 10.1, 10.41, 8.97], [10.39, 9.12, 8.05, 8.47, 6.96], [12.24, 10.89, 9.73, 10.08, 8.55], [9.99, 8.63, 7.54, 8.04, 6.35], [11.01, 9.63, 8.51, 8.95, 7.3], [10.97, 9.56, 8.5, 8.98, 7.31]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'GLUI', 12.39), ('CB', 'TYR', 'CG', 'GLUI', 11.27), ('CB', 'TYR', 'CD', 'GLUI', 10.19), ('CB', 'TYR', 'OE1', 'GLUI', 10.44), ('CB', 'TYR', 'OE2', 'GLUI', 9.23)], [('CG', 'TYR', 'CB', 'GLUI', 11.7), ('CG', 'TYR', 'CG', 'GLUI', 10.47), ('CG', 'TYR', 'CD', 'GLUI', 9.35), ('CG', 'TYR', 'OE1', 'GLUI', 9.67), ('CG', 'TYR', 'OE2', 'GLUI', 8.28)], [('CD1', 'TYR', 'CB', 'GLUI', 12.56), ('CD1', 'TYR', 'CG', 'GLUI', 11.27), ('CD1', 'TYR', 'CD', 'GLUI', 10.1), ('CD1', 'TYR', 'OE1', 'GLUI', 10.41), ('CD1', 'TYR', 'OE2', 'GLUI', 8.97)], [('CD2', 'TYR', 'CB', 'GLUI', 10.39), ('CD2', 'TYR', 'CG', 'GLUI', 9.12), ('CD2', 'TYR', 'CD', 'GLUI', 8.05), ('CD2', 'TYR', 'OE1', 'GLUI', 8.47), ('CD2', 'TYR', 'OE2', 'GLUI', 6.96)], [('CE1', 'TYR', 'CB', 'GLUI', 12.24), ('CE1', 'TYR', 'CG', 'GLUI', 10.89), ('CE1', 'TYR', 'CD', 'GLUI', 9.73), ('CE1', 'TYR', 'OE1', 'GLUI', 10.08), ('CE1', 'TYR', 'OE2', 'GLUI', 8.55)], [('CE2', 'TYR', 'CB', 'GLUI', 9.99), ('CE2', 'TYR', 'CG', 'GLUI', 8.63), ('CE2', 'TYR', 'CD', 'GLUI', 7.54), ('CE2', 'TYR', 'OE1', 'GLUI', 8.04), ('CE2', 'TYR', 'OE2', 'GLUI', 6.35)], [('CZ', 'TYR', 'CB', 'GLUI', 11.01), ('CZ', 'TYR', 'CG', 'GLUI', 9.63), ('CZ', 'TYR', 'CD', 'GLUI', 8.51), ('CZ', 'TYR', 'OE1', 'GLUI', 8.95), ('CZ', 'TYR', 'OE2', 'GLUI', 7.3)], [('OH', 'TYR', 'CB', 'GLUI', 10.97), ('OH', 'TYR', 'CG', 'GLUI', 9.56), ('OH', 'TYR', 'CD', 'GLUI', 8.5), ('OH', 'TYR', 'OE1', 'GLUI', 8.98), ('OH', 'TYR', 'OE2', 'GLUI', 7.31)]]}
HIS_TYR = { 
	'distances':
		[[8.32, 7.58, 8.41, 6.37, 8.25, 6.15, 7.22, 7.59], [9.59, 8.69, 9.37, 7.4, 8.96, 6.86, 7.77, 7.79], [9.93, 8.92, 9.54, 7.57, 9.02, 6.85, 7.72, 7.57], [10.75, 9.82, 10.39, 8.59, 9.9, 7.96, 8.71, 8.56], [11.19, 10.12, 10.64, 8.79, 9.99, 7.94, 8.65, 8.27], [11.66, 10.63, 11.12, 9.35, 10.48, 8.55, 9.2, 8.83]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'TYR', 8.32), ('CB', 'HIS', 'CG', 'TYR', 7.58), ('CB', 'HIS', 'CD1', 'TYR', 8.41), ('CB', 'HIS', 'CD2', 'TYR', 6.37), ('CB', 'HIS', 'CE1', 'TYR', 8.25), ('CB', 'HIS', 'CE2', 'TYR', 6.15), ('CB', 'HIS', 'CZ', 'TYR', 7.22), ('CB', 'HIS', 'OH', 'TYR', 7.59)], [('CG', 'HIS', 'CB', 'TYR', 9.59), ('CG', 'HIS', 'CG', 'TYR', 8.69), ('CG', 'HIS', 'CD1', 'TYR', 9.37), ('CG', 'HIS', 'CD2', 'TYR', 7.4), ('CG', 'HIS', 'CE1', 'TYR', 8.96), ('CG', 'HIS', 'CE2', 'TYR', 6.86), ('CG', 'HIS', 'CZ', 'TYR', 7.77), ('CG', 'HIS', 'OH', 'TYR', 7.79)], [('ND1', 'HIS', 'CB', 'TYR', 9.93), ('ND1', 'HIS', 'CG', 'TYR', 8.92), ('ND1', 'HIS', 'CD1', 'TYR', 9.54), ('ND1', 'HIS', 'CD2', 'TYR', 7.57), ('ND1', 'HIS', 'CE1', 'TYR', 9.02), ('ND1', 'HIS', 'CE2', 'TYR', 6.85), ('ND1', 'HIS', 'CZ', 'TYR', 7.72), ('ND1', 'HIS', 'OH', 'TYR', 7.57)], [('CD2', 'HIS', 'CB', 'TYR', 10.75), ('CD2', 'HIS', 'CG', 'TYR', 9.82), ('CD2', 'HIS', 'CD1', 'TYR', 10.39), ('CD2', 'HIS', 'CD2', 'TYR', 8.59), ('CD2', 'HIS', 'CE1', 'TYR', 9.9), ('CD2', 'HIS', 'CE2', 'TYR', 7.96), ('CD2', 'HIS', 'CZ', 'TYR', 8.71), ('CD2', 'HIS', 'OH', 'TYR', 8.56)], [('CE1', 'HIS', 'CB', 'TYR', 11.19), ('CE1', 'HIS', 'CG', 'TYR', 10.12), ('CE1', 'HIS', 'CD1', 'TYR', 10.64), ('CE1', 'HIS', 'CD2', 'TYR', 8.79), ('CE1', 'HIS', 'CE1', 'TYR', 9.99), ('CE1', 'HIS', 'CE2', 'TYR', 7.94), ('CE1', 'HIS', 'CZ', 'TYR', 8.65), ('CE1', 'HIS', 'OH', 'TYR', 8.27)], [('NE2', 'HIS', 'CB', 'TYR', 11.66), ('NE2', 'HIS', 'CG', 'TYR', 10.63), ('NE2', 'HIS', 'CD1', 'TYR', 11.12), ('NE2', 'HIS', 'CD2', 'TYR', 9.35), ('NE2', 'HIS', 'CE1', 'TYR', 10.48), ('NE2', 'HIS', 'CE2', 'TYR', 8.55), ('NE2', 'HIS', 'CZ', 'TYR', 9.2), ('NE2', 'HIS', 'OH', 'TYR', 8.83)]]}
ASN_TYR = { 
	'distances':
		[[15.3, 14.21, 14.64, 12.9, 13.84, 11.97, 12.5, 11.84], [13.86, 12.74, 13.15, 11.45, 12.36, 10.5, 11.02, 10.38], [13.31, 12.23, 12.65, 10.97, 11.9, 10.08, 10.61, 10.04], [13.28, 12.12, 12.49, 10.81, 11.66, 9.81, 10.3, 9.62]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'TYR', 15.3), ('CB', 'ASN', 'CG', 'TYR', 14.21), ('CB', 'ASN', 'CD1', 'TYR', 14.64), ('CB', 'ASN', 'CD2', 'TYR', 12.9), ('CB', 'ASN', 'CE1', 'TYR', 13.84), ('CB', 'ASN', 'CE2', 'TYR', 11.97), ('CB', 'ASN', 'CZ', 'TYR', 12.5), ('CB', 'ASN', 'OH', 'TYR', 11.84)], [('CG', 'ASN', 'CB', 'TYR', 13.86), ('CG', 'ASN', 'CG', 'TYR', 12.74), ('CG', 'ASN', 'CD1', 'TYR', 13.15), ('CG', 'ASN', 'CD2', 'TYR', 11.45), ('CG', 'ASN', 'CE1', 'TYR', 12.36), ('CG', 'ASN', 'CE2', 'TYR', 10.5), ('CG', 'ASN', 'CZ', 'TYR', 11.02), ('CG', 'ASN', 'OH', 'TYR', 10.38)], [('OD1', 'ASN', 'CB', 'TYR', 13.31), ('OD1', 'ASN', 'CG', 'TYR', 12.23), ('OD1', 'ASN', 'CD1', 'TYR', 12.65), ('OD1', 'ASN', 'CD2', 'TYR', 10.97), ('OD1', 'ASN', 'CE1', 'TYR', 11.9), ('OD1', 'ASN', 'CE2', 'TYR', 10.08), ('OD1', 'ASN', 'CZ', 'TYR', 10.61), ('OD1', 'ASN', 'OH', 'TYR', 10.04)], [('ND2', 'ASN', 'CB', 'TYR', 13.28), ('ND2', 'ASN', 'CG', 'TYR', 12.12), ('ND2', 'ASN', 'CD1', 'TYR', 12.49), ('ND2', 'ASN', 'CD2', 'TYR', 10.81), ('ND2', 'ASN', 'CE1', 'TYR', 11.66), ('ND2', 'ASN', 'CE2', 'TYR', 9.81), ('ND2', 'ASN', 'CZ', 'TYR', 10.3), ('ND2', 'ASN', 'OH', 'TYR', 9.62)]]}
ASN_GLUI = { 
	'distances':
		[[6.63, 6.74, 7.47, 7.79, 8.12], [5.97, 5.72, 6.2, 6.57, 6.73], [5.69, 5.51, 5.61, 5.69, 6.25], [6.33, 5.65, 6.14, 6.82, 6.37]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'GLUI', 6.63), ('CB', 'ASN', 'CG', 'GLUI', 6.74), ('CB', 'ASN', 'CD', 'GLUI', 7.47), ('CB', 'ASN', 'OE1', 'GLUI', 7.79), ('CB', 'ASN', 'OE2', 'GLUI', 8.12)], [('CG', 'ASN', 'CB', 'GLUI', 5.97), ('CG', 'ASN', 'CG', 'GLUI', 5.72), ('CG', 'ASN', 'CD', 'GLUI', 6.2), ('CG', 'ASN', 'OE1', 'GLUI', 6.57), ('CG', 'ASN', 'OE2', 'GLUI', 6.73)], [('OD1', 'ASN', 'CB', 'GLUI', 5.69), ('OD1', 'ASN', 'CG', 'GLUI', 5.51), ('OD1', 'ASN', 'CD', 'GLUI', 5.61), ('OD1', 'ASN', 'OE1', 'GLUI', 5.69), ('OD1', 'ASN', 'OE2', 'GLUI', 6.25)], [('ND2', 'ASN', 'CB', 'GLUI', 6.33), ('ND2', 'ASN', 'CG', 'GLUI', 5.65), ('ND2', 'ASN', 'CD', 'GLUI', 6.14), ('ND2', 'ASN', 'OE1', 'GLUI', 6.82), ('ND2', 'ASN', 'OE2', 'GLUI', 6.37)]]}
HIS_ASN = { 
	'distances':
		[[10.68, 9.51, 9.57, 8.61], [9.42, 8.33, 8.56, 7.33], [8.21, 7.03, 7.2, 6.09], [9.39, 8.48, 8.95, 7.34], [7.34, 6.32, 6.79, 5.21], [8.16, 7.34, 7.97, 6.15]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 10.68), ('CB', 'HIS', 'CG', 'ASN', 9.51), ('CB', 'HIS', 'OD1', 'ASN', 9.57), ('CB', 'HIS', 'ND2', 'ASN', 8.61)], [('CG', 'HIS', 'CB', 'ASN', 9.42), ('CG', 'HIS', 'CG', 'ASN', 8.33), ('CG', 'HIS', 'OD1', 'ASN', 8.56), ('CG', 'HIS', 'ND2', 'ASN', 7.33)], [('ND1', 'HIS', 'CB', 'ASN', 8.21), ('ND1', 'HIS', 'CG', 'ASN', 7.03), ('ND1', 'HIS', 'OD1', 'ASN', 7.2), ('ND1', 'HIS', 'ND2', 'ASN', 6.09)], [('CD2', 'HIS', 'CB', 'ASN', 9.39), ('CD2', 'HIS', 'CG', 'ASN', 8.48), ('CD2', 'HIS', 'OD1', 'ASN', 8.95), ('CD2', 'HIS', 'ND2', 'ASN', 7.34)], [('CE1', 'HIS', 'CB', 'ASN', 7.34), ('CE1', 'HIS', 'CG', 'ASN', 6.32), ('CE1', 'HIS', 'OD1', 'ASN', 6.79), ('CE1', 'HIS', 'ND2', 'ASN', 5.21)], [('NE2', 'HIS', 'CB', 'ASN', 8.16), ('NE2', 'HIS', 'CG', 'ASN', 7.34), ('NE2', 'HIS', 'OD1', 'ASN', 7.97), ('NE2', 'HIS', 'ND2', 'ASN', 6.15)]]}
GLU_ASN = { 
	'distances':
		[[10.67, 9.43, 9.59, 8.28], [9.44, 8.25, 8.51, 7.09], [8.61, 7.27, 7.31, 6.28], [9.25, 7.81, 7.59, 7.0], [7.46, 6.17, 6.31, 5.2], [6.63, 5.97, 5.69, 6.33], [6.74, 5.72, 5.51, 5.65], [7.47, 6.2, 5.61, 6.14], [7.79, 6.57, 5.69, 6.82], [8.12, 6.73, 6.25, 6.37]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASN', 10.67), ('CB', 'GLU', 'CG', 'ASN', 9.43), ('CB', 'GLU', 'OD1', 'ASN', 9.59), ('CB', 'GLU', 'ND2', 'ASN', 8.28)], [('CG', 'GLU', 'CB', 'ASN', 9.44), ('CG', 'GLU', 'CG', 'ASN', 8.25), ('CG', 'GLU', 'OD1', 'ASN', 8.51), ('CG', 'GLU', 'ND2', 'ASN', 7.09)], [('CD', 'GLU', 'CB', 'ASN', 8.61), ('CD', 'GLU', 'CG', 'ASN', 7.27), ('CD', 'GLU', 'OD1', 'ASN', 7.31), ('CD', 'GLU', 'ND2', 'ASN', 6.28)], [('OE1', 'GLU', 'CB', 'ASN', 9.25), ('OE1', 'GLU', 'CG', 'ASN', 7.81), ('OE1', 'GLU', 'OD1', 'ASN', 7.59), ('OE1', 'GLU', 'ND2', 'ASN', 7.0)], [('OE2', 'GLU', 'CB', 'ASN', 7.46), ('OE2', 'GLU', 'CG', 'ASN', 6.17), ('OE2', 'GLU', 'OD1', 'ASN', 6.31), ('OE2', 'GLU', 'ND2', 'ASN', 5.2)], [('CB', 'GLU', 'CB', 'ASN', 6.63), ('CB', 'GLU', 'CG', 'ASN', 5.97), ('CB', 'GLU', 'OD1', 'ASN', 5.69), ('CB', 'GLU', 'ND2', 'ASN', 6.33)], [('CG', 'GLU', 'CB', 'ASN', 6.74), ('CG', 'GLU', 'CG', 'ASN', 5.72), ('CG', 'GLU', 'OD1', 'ASN', 5.51), ('CG', 'GLU', 'ND2', 'ASN', 5.65)], [('CD', 'GLU', 'CB', 'ASN', 7.47), ('CD', 'GLU', 'CG', 'ASN', 6.2), ('CD', 'GLU', 'OD1', 'ASN', 5.61), ('CD', 'GLU', 'ND2', 'ASN', 6.14)], [('OE1', 'GLU', 'CB', 'ASN', 7.79), ('OE1', 'GLU', 'CG', 'ASN', 6.57), ('OE1', 'GLU', 'OD1', 'ASN', 5.69), ('OE1', 'GLU', 'ND2', 'ASN', 6.82)], [('OE2', 'GLU', 'CB', 'ASN', 8.12), ('OE2', 'GLU', 'CG', 'ASN', 6.73), ('OE2', 'GLU', 'OD1', 'ASN', 6.25), ('OE2', 'GLU', 'ND2', 'ASN', 6.37)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_GLU, d, 'A_1bqc_3_2_1_78')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_TYR, d, 'A_1bqc_3_2_1_78')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_HIS, d, 'A_1bqc_3_2_1_78')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(TYR_GLUI, d, 'A_1bqc_3_2_1_78')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_TYR, d, 'A_1bqc_3_2_1_78')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ASN_TYR, d, 'A_1bqc_3_2_1_78')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(ASN_GLUI, d, 'A_1bqc_3_2_1_78')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(HIS_ASN, d, 'A_1bqc_3_2_1_78')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(GLU_ASN, d, 'A_1bqc_3_2_1_78')
	if match9 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_GLU' :  match1,
		'GLU_TYR' :  match2,
		'GLU_HIS' :  match3,
		'TYR_GLUI' :  match4,
		'HIS_TYR' :  match5,
		'ASN_TYR' :  match6,
		'ASN_GLUI' :  match7,
		'HIS_ASN' :  match8,
		'GLU_ASN' :  match9}