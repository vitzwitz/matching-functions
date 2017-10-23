'''
FUNC:A_2hgs_6_3_2_3
PDB:2hgs
EC:6.3.2.3
RESI:arg,ser,gly,arg
LOCI:a-125,151,369,450;
'''
import motifFunctions as cmd
SER_GLY = { 
	'distances':
		[[11.33, 11.61, 10.83, 11.53], [11.26, 11.49, 10.56, 11.2], [12.52, 12.7, 12.11, 12.67], [12.65, 12.89, 12.24, 12.85], [12.29, 12.46, 11.64, 12.19], [11.85, 11.86, 10.91, 11.28]],
	'comparisons':
		[[('CB', 'SER', 'O', 'GLY', 11.33), ('CB', 'SER', 'C', 'GLY', 11.61), ('CB', 'SER', 'CA', 'GLY', 10.83), ('CB', 'SER', 'N', 'GLY', 11.53)], [('OG', 'SER', 'O', 'GLY', 11.26), ('OG', 'SER', 'C', 'GLY', 11.49), ('OG', 'SER', 'CA', 'GLY', 10.56), ('OG', 'SER', 'N', 'GLY', 11.2)], [('O', 'SER', 'O', 'GLY', 12.52), ('O', 'SER', 'C', 'GLY', 12.7), ('O', 'SER', 'CA', 'GLY', 12.11), ('O', 'SER', 'N', 'GLY', 12.67)], [('C', 'SER', 'O', 'GLY', 12.65), ('C', 'SER', 'C', 'GLY', 12.89), ('C', 'SER', 'CA', 'GLY', 12.24), ('C', 'SER', 'N', 'GLY', 12.85)], [('CA', 'SER', 'O', 'GLY', 12.29), ('CA', 'SER', 'C', 'GLY', 12.46), ('CA', 'SER', 'CA', 'GLY', 11.64), ('CA', 'SER', 'N', 'GLY', 12.19)], [('N', 'SER', 'O', 'GLY', 11.85), ('N', 'SER', 'C', 'GLY', 11.86), ('N', 'SER', 'CA', 'GLY', 10.91), ('N', 'SER', 'N', 'GLY', 11.28)]]}
GLY_ARGI = { 
	'distances':
		[[12.89, 12.5, 11.05, 11.02, 10.07, 8.74, 10.64, 15.2, 14.93, 14.39, 15.28], [13.19, 12.81, 11.32, 11.1, 10.03, 8.75, 10.42, 15.41, 15.24, 14.71, 15.51], [13.64, 13.1, 11.57, 11.28, 10.19, 8.96, 10.52, 16.0, 15.83, 15.17, 15.85], [14.27, 13.75, 12.22, 11.74, 10.56, 9.44, 10.66, 16.49, 16.43, 15.79, 16.37]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ARGI', 12.89), ('O', 'GLY', 'CG', 'ARGI', 12.5), ('O', 'GLY', 'CD', 'ARGI', 11.05), ('O', 'GLY', 'NE', 'ARGI', 11.02), ('O', 'GLY', 'CZ', 'ARGI', 10.07), ('O', 'GLY', 'NH1', 'ARGI', 8.74), ('O', 'GLY', 'NH2', 'ARGI', 10.64), ('O', 'GLY', 'O', 'ARGI', 15.2), ('O', 'GLY', 'C', 'ARGI', 14.93), ('O', 'GLY', 'CA', 'ARGI', 14.39), ('O', 'GLY', 'N', 'ARGI', 15.28)], [('C', 'GLY', 'CB', 'ARGI', 13.19), ('C', 'GLY', 'CG', 'ARGI', 12.81), ('C', 'GLY', 'CD', 'ARGI', 11.32), ('C', 'GLY', 'NE', 'ARGI', 11.1), ('C', 'GLY', 'CZ', 'ARGI', 10.03), ('C', 'GLY', 'NH1', 'ARGI', 8.75), ('C', 'GLY', 'NH2', 'ARGI', 10.42), ('C', 'GLY', 'O', 'ARGI', 15.41), ('C', 'GLY', 'C', 'ARGI', 15.24), ('C', 'GLY', 'CA', 'ARGI', 14.71), ('C', 'GLY', 'N', 'ARGI', 15.51)], [('CA', 'GLY', 'CB', 'ARGI', 13.64), ('CA', 'GLY', 'CG', 'ARGI', 13.1), ('CA', 'GLY', 'CD', 'ARGI', 11.57), ('CA', 'GLY', 'NE', 'ARGI', 11.28), ('CA', 'GLY', 'CZ', 'ARGI', 10.19), ('CA', 'GLY', 'NH1', 'ARGI', 8.96), ('CA', 'GLY', 'NH2', 'ARGI', 10.52), ('CA', 'GLY', 'O', 'ARGI', 16.0), ('CA', 'GLY', 'C', 'ARGI', 15.83), ('CA', 'GLY', 'CA', 'ARGI', 15.17), ('CA', 'GLY', 'N', 'ARGI', 15.85)], [('N', 'GLY', 'CB', 'ARGI', 14.27), ('N', 'GLY', 'CG', 'ARGI', 13.75), ('N', 'GLY', 'CD', 'ARGI', 12.22), ('N', 'GLY', 'NE', 'ARGI', 11.74), ('N', 'GLY', 'CZ', 'ARGI', 10.56), ('N', 'GLY', 'NH1', 'ARGI', 9.44), ('N', 'GLY', 'NH2', 'ARGI', 10.66), ('N', 'GLY', 'O', 'ARGI', 16.49), ('N', 'GLY', 'C', 'ARGI', 16.43), ('N', 'GLY', 'CA', 'ARGI', 15.79), ('N', 'GLY', 'N', 'ARGI', 16.37)]]}
SER_ARG = { 
	'distances':
		[[9.92, 10.38, 9.56, 9.39, 8.38, 7.17, 8.77, 12.02, 12.2, 11.21, 11.13], [10.48, 11.15, 10.49, 10.26, 9.17, 8.0, 9.44, 12.35, 12.62, 11.65, 11.36], [7.79, 7.73, 6.68, 6.85, 6.3, 5.13, 7.2, 10.38, 10.26, 9.26, 9.66], [8.62, 8.73, 7.8, 7.98, 7.32, 6.07, 8.12, 11.19, 11.11, 10.02, 10.24], [8.73, 9.16, 8.45, 8.5, 7.65, 6.35, 8.31, 11.07, 11.11, 10.01, 9.97], [7.79, 8.47, 7.94, 7.86, 6.92, 5.67, 7.5, 9.88, 10.02, 8.98, 8.81], [12.68, 11.27, 10.31, 10.69, 10.66, 10.14, 11.45, 15.79, 15.16, 13.78, 14.04], [13.89, 12.52, 11.47, 11.76, 11.58, 10.96, 12.29, 16.99, 16.4, 15.05, 15.33], [10.37, 8.88, 8.24, 8.53, 8.84, 8.85, 9.53, 13.31, 12.74, 11.26, 11.23], [11.38, 9.88, 9.21, 9.59, 9.85, 9.72, 10.6, 14.37, 13.75, 12.27, 12.31], [12.49, 11.02, 10.18, 10.44, 10.48, 10.19, 11.15, 15.51, 14.94, 13.49, 13.57], [12.66, 11.25, 10.27, 10.29, 10.14, 9.83, 10.64, 15.6, 15.15, 13.75, 13.78]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ARG', 9.92), ('CB', 'SER', 'CG', 'ARG', 10.38), ('CB', 'SER', 'CD', 'ARG', 9.56), ('CB', 'SER', 'NE', 'ARG', 9.39), ('CB', 'SER', 'CZ', 'ARG', 8.38), ('CB', 'SER', 'NH1', 'ARG', 7.17), ('CB', 'SER', 'NH2', 'ARG', 8.77), ('CB', 'SER', 'O', 'ARG', 12.02), ('CB', 'SER', 'C', 'ARG', 12.2), ('CB', 'SER', 'CA', 'ARG', 11.21), ('CB', 'SER', 'N', 'ARG', 11.13)], [('OG', 'SER', 'CB', 'ARG', 10.48), ('OG', 'SER', 'CG', 'ARG', 11.15), ('OG', 'SER', 'CD', 'ARG', 10.49), ('OG', 'SER', 'NE', 'ARG', 10.26), ('OG', 'SER', 'CZ', 'ARG', 9.17), ('OG', 'SER', 'NH1', 'ARG', 8.0), ('OG', 'SER', 'NH2', 'ARG', 9.44), ('OG', 'SER', 'O', 'ARG', 12.35), ('OG', 'SER', 'C', 'ARG', 12.62), ('OG', 'SER', 'CA', 'ARG', 11.65), ('OG', 'SER', 'N', 'ARG', 11.36)], [('O', 'SER', 'CB', 'ARG', 7.79), ('O', 'SER', 'CG', 'ARG', 7.73), ('O', 'SER', 'CD', 'ARG', 6.68), ('O', 'SER', 'NE', 'ARG', 6.85), ('O', 'SER', 'CZ', 'ARG', 6.3), ('O', 'SER', 'NH1', 'ARG', 5.13), ('O', 'SER', 'NH2', 'ARG', 7.2), ('O', 'SER', 'O', 'ARG', 10.38), ('O', 'SER', 'C', 'ARG', 10.26), ('O', 'SER', 'CA', 'ARG', 9.26), ('O', 'SER', 'N', 'ARG', 9.66)], [('C', 'SER', 'CB', 'ARG', 8.62), ('C', 'SER', 'CG', 'ARG', 8.73), ('C', 'SER', 'CD', 'ARG', 7.8), ('C', 'SER', 'NE', 'ARG', 7.98), ('C', 'SER', 'CZ', 'ARG', 7.32), ('C', 'SER', 'NH1', 'ARG', 6.07), ('C', 'SER', 'NH2', 'ARG', 8.12), ('C', 'SER', 'O', 'ARG', 11.19), ('C', 'SER', 'C', 'ARG', 11.11), ('C', 'SER', 'CA', 'ARG', 10.02), ('C', 'SER', 'N', 'ARG', 10.24)], [('CA', 'SER', 'CB', 'ARG', 8.73), ('CA', 'SER', 'CG', 'ARG', 9.16), ('CA', 'SER', 'CD', 'ARG', 8.45), ('CA', 'SER', 'NE', 'ARG', 8.5), ('CA', 'SER', 'CZ', 'ARG', 7.65), ('CA', 'SER', 'NH1', 'ARG', 6.35), ('CA', 'SER', 'NH2', 'ARG', 8.31), ('CA', 'SER', 'O', 'ARG', 11.07), ('CA', 'SER', 'C', 'ARG', 11.11), ('CA', 'SER', 'CA', 'ARG', 10.01), ('CA', 'SER', 'N', 'ARG', 9.97)], [('N', 'SER', 'CB', 'ARG', 7.79), ('N', 'SER', 'CG', 'ARG', 8.47), ('N', 'SER', 'CD', 'ARG', 7.94), ('N', 'SER', 'NE', 'ARG', 7.86), ('N', 'SER', 'CZ', 'ARG', 6.92), ('N', 'SER', 'NH1', 'ARG', 5.67), ('N', 'SER', 'NH2', 'ARG', 7.5), ('N', 'SER', 'O', 'ARG', 9.88), ('N', 'SER', 'C', 'ARG', 10.02), ('N', 'SER', 'CA', 'ARG', 8.98), ('N', 'SER', 'N', 'ARG', 8.81)], [('CB', 'SER', 'CB', 'ARG', 12.68), ('CB', 'SER', 'CG', 'ARG', 11.27), ('CB', 'SER', 'CD', 'ARG', 10.31), ('CB', 'SER', 'NE', 'ARG', 10.69), ('CB', 'SER', 'CZ', 'ARG', 10.66), ('CB', 'SER', 'NH1', 'ARG', 10.14), ('CB', 'SER', 'NH2', 'ARG', 11.45), ('CB', 'SER', 'O', 'ARG', 15.79), ('CB', 'SER', 'C', 'ARG', 15.16), ('CB', 'SER', 'CA', 'ARG', 13.78), ('CB', 'SER', 'N', 'ARG', 14.04)], [('OG', 'SER', 'CB', 'ARG', 13.89), ('OG', 'SER', 'CG', 'ARG', 12.52), ('OG', 'SER', 'CD', 'ARG', 11.47), ('OG', 'SER', 'NE', 'ARG', 11.76), ('OG', 'SER', 'CZ', 'ARG', 11.58), ('OG', 'SER', 'NH1', 'ARG', 10.96), ('OG', 'SER', 'NH2', 'ARG', 12.29), ('OG', 'SER', 'O', 'ARG', 16.99), ('OG', 'SER', 'C', 'ARG', 16.4), ('OG', 'SER', 'CA', 'ARG', 15.05), ('OG', 'SER', 'N', 'ARG', 15.33)], [('O', 'SER', 'CB', 'ARG', 10.37), ('O', 'SER', 'CG', 'ARG', 8.88), ('O', 'SER', 'CD', 'ARG', 8.24), ('O', 'SER', 'NE', 'ARG', 8.53), ('O', 'SER', 'CZ', 'ARG', 8.84), ('O', 'SER', 'NH1', 'ARG', 8.85), ('O', 'SER', 'NH2', 'ARG', 9.53), ('O', 'SER', 'O', 'ARG', 13.31), ('O', 'SER', 'C', 'ARG', 12.74), ('O', 'SER', 'CA', 'ARG', 11.26), ('O', 'SER', 'N', 'ARG', 11.23)], [('C', 'SER', 'CB', 'ARG', 11.38), ('C', 'SER', 'CG', 'ARG', 9.88), ('C', 'SER', 'CD', 'ARG', 9.21), ('C', 'SER', 'NE', 'ARG', 9.59), ('C', 'SER', 'CZ', 'ARG', 9.85), ('C', 'SER', 'NH1', 'ARG', 9.72), ('C', 'SER', 'NH2', 'ARG', 10.6), ('C', 'SER', 'O', 'ARG', 14.37), ('C', 'SER', 'C', 'ARG', 13.75), ('C', 'SER', 'CA', 'ARG', 12.27), ('C', 'SER', 'N', 'ARG', 12.31)], [('CA', 'SER', 'CB', 'ARG', 12.49), ('CA', 'SER', 'CG', 'ARG', 11.02), ('CA', 'SER', 'CD', 'ARG', 10.18), ('CA', 'SER', 'NE', 'ARG', 10.44), ('CA', 'SER', 'CZ', 'ARG', 10.48), ('CA', 'SER', 'NH1', 'ARG', 10.19), ('CA', 'SER', 'NH2', 'ARG', 11.15), ('CA', 'SER', 'O', 'ARG', 15.51), ('CA', 'SER', 'C', 'ARG', 14.94), ('CA', 'SER', 'CA', 'ARG', 13.49), ('CA', 'SER', 'N', 'ARG', 13.57)], [('N', 'SER', 'CB', 'ARG', 12.66), ('N', 'SER', 'CG', 'ARG', 11.25), ('N', 'SER', 'CD', 'ARG', 10.27), ('N', 'SER', 'NE', 'ARG', 10.29), ('N', 'SER', 'CZ', 'ARG', 10.14), ('N', 'SER', 'NH1', 'ARG', 9.83), ('N', 'SER', 'NH2', 'ARG', 10.64), ('N', 'SER', 'O', 'ARG', 15.6), ('N', 'SER', 'C', 'ARG', 15.15), ('N', 'SER', 'CA', 'ARG', 13.75), ('N', 'SER', 'N', 'ARG', 13.78)]]}
ARG_ARG = { 
	'distances':
		[[12.02, 10.93, 10.28, 9.47, 9.3, 9.8, 8.91, 14.02, 14.05, 12.84, 12.27], [11.01, 9.97, 9.53, 8.73, 8.78, 9.5, 8.39, 12.87, 12.9, 11.69, 11.0], [9.64, 8.52, 8.08, 7.41, 7.6, 8.33, 7.44, 11.72, 11.65, 10.37, 9.79], [9.1, 8.06, 7.35, 6.5, 6.43, 7.08, 6.21, 11.25, 11.23, 10.03, 9.63], [9.3, 8.19, 7.21, 6.47, 6.18, 6.49, 6.18, 11.72, 11.61, 10.41, 10.22], [9.86, 8.59, 7.63, 7.2, 7.05, 7.18, 7.29, 12.49, 12.25, 10.95, 10.8], [9.22, 8.27, 7.08, 6.2, 5.53, 5.61, 5.45, 11.59, 11.54, 10.47, 10.44], [13.23, 12.43, 11.63, 10.49, 9.94, 10.38, 9.12, 14.83, 15.11, 14.14, 13.6], [13.22, 12.39, 11.74, 10.65, 10.27, 10.85, 9.49, 14.76, 15.02, 14.02, 13.35], [13.29, 12.29, 11.67, 10.75, 10.51, 11.04, 9.95, 15.08, 15.21, 14.07, 13.4], [14.45, 13.39, 12.66, 11.79, 11.45, 11.82, 10.93, 16.37, 16.47, 15.3, 14.71], [12.02, 11.01, 9.64, 9.1, 9.3, 9.86, 9.22, 13.23, 13.22, 13.29, 14.45], [10.93, 9.97, 8.52, 8.06, 8.19, 8.59, 8.27, 12.43, 12.39, 12.29, 13.39], [10.28, 9.53, 8.08, 7.35, 7.21, 7.63, 7.08, 11.63, 11.74, 11.67, 12.66], [9.47, 8.73, 7.41, 6.5, 6.47, 7.2, 6.2, 10.49, 10.65, 10.75, 11.79], [9.3, 8.78, 7.6, 6.43, 6.18, 7.05, 5.53, 9.94, 10.27, 10.51, 11.45], [9.8, 9.5, 8.33, 7.08, 6.49, 7.18, 5.61, 10.38, 10.85, 11.04, 11.82], [8.91, 8.39, 7.44, 6.21, 6.18, 7.29, 5.45, 9.12, 9.49, 9.95, 10.93], [14.02, 12.87, 11.72, 11.25, 11.72, 12.49, 11.59, 14.83, 14.76, 15.08, 16.37], [14.05, 12.9, 11.65, 11.23, 11.61, 12.25, 11.54, 15.11, 15.02, 15.21, 16.47], [12.84, 11.69, 10.37, 10.03, 10.41, 10.95, 10.47, 14.14, 14.02, 14.07, 15.3], [12.27, 11.0, 9.79, 9.63, 10.22, 10.8, 10.44, 13.6, 13.35, 13.4, 14.71]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ARG', 12.02), ('CB', 'ARG', 'CG', 'ARG', 10.93), ('CB', 'ARG', 'CD', 'ARG', 10.28), ('CB', 'ARG', 'NE', 'ARG', 9.47), ('CB', 'ARG', 'CZ', 'ARG', 9.3), ('CB', 'ARG', 'NH1', 'ARG', 9.8), ('CB', 'ARG', 'NH2', 'ARG', 8.91), ('CB', 'ARG', 'O', 'ARG', 14.02), ('CB', 'ARG', 'C', 'ARG', 14.05), ('CB', 'ARG', 'CA', 'ARG', 12.84), ('CB', 'ARG', 'N', 'ARG', 12.27)], [('CG', 'ARG', 'CB', 'ARG', 11.01), ('CG', 'ARG', 'CG', 'ARG', 9.97), ('CG', 'ARG', 'CD', 'ARG', 9.53), ('CG', 'ARG', 'NE', 'ARG', 8.73), ('CG', 'ARG', 'CZ', 'ARG', 8.78), ('CG', 'ARG', 'NH1', 'ARG', 9.5), ('CG', 'ARG', 'NH2', 'ARG', 8.39), ('CG', 'ARG', 'O', 'ARG', 12.87), ('CG', 'ARG', 'C', 'ARG', 12.9), ('CG', 'ARG', 'CA', 'ARG', 11.69), ('CG', 'ARG', 'N', 'ARG', 11.0)], [('CD', 'ARG', 'CB', 'ARG', 9.64), ('CD', 'ARG', 'CG', 'ARG', 8.52), ('CD', 'ARG', 'CD', 'ARG', 8.08), ('CD', 'ARG', 'NE', 'ARG', 7.41), ('CD', 'ARG', 'CZ', 'ARG', 7.6), ('CD', 'ARG', 'NH1', 'ARG', 8.33), ('CD', 'ARG', 'NH2', 'ARG', 7.44), ('CD', 'ARG', 'O', 'ARG', 11.72), ('CD', 'ARG', 'C', 'ARG', 11.65), ('CD', 'ARG', 'CA', 'ARG', 10.37), ('CD', 'ARG', 'N', 'ARG', 9.79)], [('NE', 'ARG', 'CB', 'ARG', 9.1), ('NE', 'ARG', 'CG', 'ARG', 8.06), ('NE', 'ARG', 'CD', 'ARG', 7.35), ('NE', 'ARG', 'NE', 'ARG', 6.5), ('NE', 'ARG', 'CZ', 'ARG', 6.43), ('NE', 'ARG', 'NH1', 'ARG', 7.08), ('NE', 'ARG', 'NH2', 'ARG', 6.21), ('NE', 'ARG', 'O', 'ARG', 11.25), ('NE', 'ARG', 'C', 'ARG', 11.23), ('NE', 'ARG', 'CA', 'ARG', 10.03), ('NE', 'ARG', 'N', 'ARG', 9.63)], [('CZ', 'ARG', 'CB', 'ARG', 9.3), ('CZ', 'ARG', 'CG', 'ARG', 8.19), ('CZ', 'ARG', 'CD', 'ARG', 7.21), ('CZ', 'ARG', 'NE', 'ARG', 6.47), ('CZ', 'ARG', 'CZ', 'ARG', 6.18), ('CZ', 'ARG', 'NH1', 'ARG', 6.49), ('CZ', 'ARG', 'NH2', 'ARG', 6.18), ('CZ', 'ARG', 'O', 'ARG', 11.72), ('CZ', 'ARG', 'C', 'ARG', 11.61), ('CZ', 'ARG', 'CA', 'ARG', 10.41), ('CZ', 'ARG', 'N', 'ARG', 10.22)], [('NH1', 'ARG', 'CB', 'ARG', 9.86), ('NH1', 'ARG', 'CG', 'ARG', 8.59), ('NH1', 'ARG', 'CD', 'ARG', 7.63), ('NH1', 'ARG', 'NE', 'ARG', 7.2), ('NH1', 'ARG', 'CZ', 'ARG', 7.05), ('NH1', 'ARG', 'NH1', 'ARG', 7.18), ('NH1', 'ARG', 'NH2', 'ARG', 7.29), ('NH1', 'ARG', 'O', 'ARG', 12.49), ('NH1', 'ARG', 'C', 'ARG', 12.25), ('NH1', 'ARG', 'CA', 'ARG', 10.95), ('NH1', 'ARG', 'N', 'ARG', 10.8)], [('NH2', 'ARG', 'CB', 'ARG', 9.22), ('NH2', 'ARG', 'CG', 'ARG', 8.27), ('NH2', 'ARG', 'CD', 'ARG', 7.08), ('NH2', 'ARG', 'NE', 'ARG', 6.2), ('NH2', 'ARG', 'CZ', 'ARG', 5.53), ('NH2', 'ARG', 'NH1', 'ARG', 5.61), ('NH2', 'ARG', 'NH2', 'ARG', 5.45), ('NH2', 'ARG', 'O', 'ARG', 11.59), ('NH2', 'ARG', 'C', 'ARG', 11.54), ('NH2', 'ARG', 'CA', 'ARG', 10.47), ('NH2', 'ARG', 'N', 'ARG', 10.44)], [('O', 'ARG', 'CB', 'ARG', 13.23), ('O', 'ARG', 'CG', 'ARG', 12.43), ('O', 'ARG', 'CD', 'ARG', 11.63), ('O', 'ARG', 'NE', 'ARG', 10.49), ('O', 'ARG', 'CZ', 'ARG', 9.94), ('O', 'ARG', 'NH1', 'ARG', 10.38), ('O', 'ARG', 'NH2', 'ARG', 9.12), ('O', 'ARG', 'O', 'ARG', 14.83), ('O', 'ARG', 'C', 'ARG', 15.11), ('O', 'ARG', 'CA', 'ARG', 14.14), ('O', 'ARG', 'N', 'ARG', 13.6)], [('C', 'ARG', 'CB', 'ARG', 13.22), ('C', 'ARG', 'CG', 'ARG', 12.39), ('C', 'ARG', 'CD', 'ARG', 11.74), ('C', 'ARG', 'NE', 'ARG', 10.65), ('C', 'ARG', 'CZ', 'ARG', 10.27), ('C', 'ARG', 'NH1', 'ARG', 10.85), ('C', 'ARG', 'NH2', 'ARG', 9.49), ('C', 'ARG', 'O', 'ARG', 14.76), ('C', 'ARG', 'C', 'ARG', 15.02), ('C', 'ARG', 'CA', 'ARG', 14.02), ('C', 'ARG', 'N', 'ARG', 13.35)], [('CA', 'ARG', 'CB', 'ARG', 13.29), ('CA', 'ARG', 'CG', 'ARG', 12.29), ('CA', 'ARG', 'CD', 'ARG', 11.67), ('CA', 'ARG', 'NE', 'ARG', 10.75), ('CA', 'ARG', 'CZ', 'ARG', 10.51), ('CA', 'ARG', 'NH1', 'ARG', 11.04), ('CA', 'ARG', 'NH2', 'ARG', 9.95), ('CA', 'ARG', 'O', 'ARG', 15.08), ('CA', 'ARG', 'C', 'ARG', 15.21), ('CA', 'ARG', 'CA', 'ARG', 14.07), ('CA', 'ARG', 'N', 'ARG', 13.4)], [('N', 'ARG', 'CB', 'ARG', 14.45), ('N', 'ARG', 'CG', 'ARG', 13.39), ('N', 'ARG', 'CD', 'ARG', 12.66), ('N', 'ARG', 'NE', 'ARG', 11.79), ('N', 'ARG', 'CZ', 'ARG', 11.45), ('N', 'ARG', 'NH1', 'ARG', 11.82), ('N', 'ARG', 'NH2', 'ARG', 10.93), ('N', 'ARG', 'O', 'ARG', 16.37), ('N', 'ARG', 'C', 'ARG', 16.47), ('N', 'ARG', 'CA', 'ARG', 15.3), ('N', 'ARG', 'N', 'ARG', 14.71)], [('CB', 'ARG', 'CB', 'ARG', 12.02), ('CB', 'ARG', 'CG', 'ARG', 11.01), ('CB', 'ARG', 'CD', 'ARG', 9.64), ('CB', 'ARG', 'NE', 'ARG', 9.1), ('CB', 'ARG', 'CZ', 'ARG', 9.3), ('CB', 'ARG', 'NH1', 'ARG', 9.86), ('CB', 'ARG', 'NH2', 'ARG', 9.22), ('CB', 'ARG', 'O', 'ARG', 13.23), ('CB', 'ARG', 'C', 'ARG', 13.22), ('CB', 'ARG', 'CA', 'ARG', 13.29), ('CB', 'ARG', 'N', 'ARG', 14.45)], [('CG', 'ARG', 'CB', 'ARG', 10.93), ('CG', 'ARG', 'CG', 'ARG', 9.97), ('CG', 'ARG', 'CD', 'ARG', 8.52), ('CG', 'ARG', 'NE', 'ARG', 8.06), ('CG', 'ARG', 'CZ', 'ARG', 8.19), ('CG', 'ARG', 'NH1', 'ARG', 8.59), ('CG', 'ARG', 'NH2', 'ARG', 8.27), ('CG', 'ARG', 'O', 'ARG', 12.43), ('CG', 'ARG', 'C', 'ARG', 12.39), ('CG', 'ARG', 'CA', 'ARG', 12.29), ('CG', 'ARG', 'N', 'ARG', 13.39)], [('CD', 'ARG', 'CB', 'ARG', 10.28), ('CD', 'ARG', 'CG', 'ARG', 9.53), ('CD', 'ARG', 'CD', 'ARG', 8.08), ('CD', 'ARG', 'NE', 'ARG', 7.35), ('CD', 'ARG', 'CZ', 'ARG', 7.21), ('CD', 'ARG', 'NH1', 'ARG', 7.63), ('CD', 'ARG', 'NH2', 'ARG', 7.08), ('CD', 'ARG', 'O', 'ARG', 11.63), ('CD', 'ARG', 'C', 'ARG', 11.74), ('CD', 'ARG', 'CA', 'ARG', 11.67), ('CD', 'ARG', 'N', 'ARG', 12.66)], [('NE', 'ARG', 'CB', 'ARG', 9.47), ('NE', 'ARG', 'CG', 'ARG', 8.73), ('NE', 'ARG', 'CD', 'ARG', 7.41), ('NE', 'ARG', 'NE', 'ARG', 6.5), ('NE', 'ARG', 'CZ', 'ARG', 6.47), ('NE', 'ARG', 'NH1', 'ARG', 7.2), ('NE', 'ARG', 'NH2', 'ARG', 6.2), ('NE', 'ARG', 'O', 'ARG', 10.49), ('NE', 'ARG', 'C', 'ARG', 10.65), ('NE', 'ARG', 'CA', 'ARG', 10.75), ('NE', 'ARG', 'N', 'ARG', 11.79)], [('CZ', 'ARG', 'CB', 'ARG', 9.3), ('CZ', 'ARG', 'CG', 'ARG', 8.78), ('CZ', 'ARG', 'CD', 'ARG', 7.6), ('CZ', 'ARG', 'NE', 'ARG', 6.43), ('CZ', 'ARG', 'CZ', 'ARG', 6.18), ('CZ', 'ARG', 'NH1', 'ARG', 7.05), ('CZ', 'ARG', 'NH2', 'ARG', 5.53), ('CZ', 'ARG', 'O', 'ARG', 9.94), ('CZ', 'ARG', 'C', 'ARG', 10.27), ('CZ', 'ARG', 'CA', 'ARG', 10.51), ('CZ', 'ARG', 'N', 'ARG', 11.45)], [('NH1', 'ARG', 'CB', 'ARG', 9.8), ('NH1', 'ARG', 'CG', 'ARG', 9.5), ('NH1', 'ARG', 'CD', 'ARG', 8.33), ('NH1', 'ARG', 'NE', 'ARG', 7.08), ('NH1', 'ARG', 'CZ', 'ARG', 6.49), ('NH1', 'ARG', 'NH1', 'ARG', 7.18), ('NH1', 'ARG', 'NH2', 'ARG', 5.61), ('NH1', 'ARG', 'O', 'ARG', 10.38), ('NH1', 'ARG', 'C', 'ARG', 10.85), ('NH1', 'ARG', 'CA', 'ARG', 11.04), ('NH1', 'ARG', 'N', 'ARG', 11.82)], [('NH2', 'ARG', 'CB', 'ARG', 8.91), ('NH2', 'ARG', 'CG', 'ARG', 8.39), ('NH2', 'ARG', 'CD', 'ARG', 7.44), ('NH2', 'ARG', 'NE', 'ARG', 6.21), ('NH2', 'ARG', 'CZ', 'ARG', 6.18), ('NH2', 'ARG', 'NH1', 'ARG', 7.29), ('NH2', 'ARG', 'NH2', 'ARG', 5.45), ('NH2', 'ARG', 'O', 'ARG', 9.12), ('NH2', 'ARG', 'C', 'ARG', 9.49), ('NH2', 'ARG', 'CA', 'ARG', 9.95), ('NH2', 'ARG', 'N', 'ARG', 10.93)], [('O', 'ARG', 'CB', 'ARG', 14.02), ('O', 'ARG', 'CG', 'ARG', 12.87), ('O', 'ARG', 'CD', 'ARG', 11.72), ('O', 'ARG', 'NE', 'ARG', 11.25), ('O', 'ARG', 'CZ', 'ARG', 11.72), ('O', 'ARG', 'NH1', 'ARG', 12.49), ('O', 'ARG', 'NH2', 'ARG', 11.59), ('O', 'ARG', 'O', 'ARG', 14.83), ('O', 'ARG', 'C', 'ARG', 14.76), ('O', 'ARG', 'CA', 'ARG', 15.08), ('O', 'ARG', 'N', 'ARG', 16.37)], [('C', 'ARG', 'CB', 'ARG', 14.05), ('C', 'ARG', 'CG', 'ARG', 12.9), ('C', 'ARG', 'CD', 'ARG', 11.65), ('C', 'ARG', 'NE', 'ARG', 11.23), ('C', 'ARG', 'CZ', 'ARG', 11.61), ('C', 'ARG', 'NH1', 'ARG', 12.25), ('C', 'ARG', 'NH2', 'ARG', 11.54), ('C', 'ARG', 'O', 'ARG', 15.11), ('C', 'ARG', 'C', 'ARG', 15.02), ('C', 'ARG', 'CA', 'ARG', 15.21), ('C', 'ARG', 'N', 'ARG', 16.47)], [('CA', 'ARG', 'CB', 'ARG', 12.84), ('CA', 'ARG', 'CG', 'ARG', 11.69), ('CA', 'ARG', 'CD', 'ARG', 10.37), ('CA', 'ARG', 'NE', 'ARG', 10.03), ('CA', 'ARG', 'CZ', 'ARG', 10.41), ('CA', 'ARG', 'NH1', 'ARG', 10.95), ('CA', 'ARG', 'NH2', 'ARG', 10.47), ('CA', 'ARG', 'O', 'ARG', 14.14), ('CA', 'ARG', 'C', 'ARG', 14.02), ('CA', 'ARG', 'CA', 'ARG', 14.07), ('CA', 'ARG', 'N', 'ARG', 15.3)], [('N', 'ARG', 'CB', 'ARG', 12.27), ('N', 'ARG', 'CG', 'ARG', 11.0), ('N', 'ARG', 'CD', 'ARG', 9.79), ('N', 'ARG', 'NE', 'ARG', 9.63), ('N', 'ARG', 'CZ', 'ARG', 10.22), ('N', 'ARG', 'NH1', 'ARG', 10.8), ('N', 'ARG', 'NH2', 'ARG', 10.44), ('N', 'ARG', 'O', 'ARG', 13.6), ('N', 'ARG', 'C', 'ARG', 13.35), ('N', 'ARG', 'CA', 'ARG', 13.4), ('N', 'ARG', 'N', 'ARG', 14.71)]]}
ARG_GLY = { 
	'distances':
		[[14.3, 13.9, 13.1, 12.88], [14.71, 14.38, 13.73, 13.62], [13.82, 13.61, 13.08, 13.14], [12.55, 12.31, 11.82, 11.86], [11.39, 11.16, 10.61, 10.7], [11.49, 11.35, 10.7, 10.9], [10.3, 9.99, 9.5, 9.55], [14.36, 13.69, 12.86, 12.28], [15.24, 14.64, 13.84, 13.33], [15.36, 14.85, 13.98, 13.6], [15.47, 14.92, 13.91, 13.46], [12.89, 13.19, 13.64, 14.27], [12.5, 12.81, 13.1, 13.75], [11.05, 11.32, 11.57, 12.22], [11.02, 11.1, 11.28, 11.74], [10.07, 10.03, 10.19, 10.56], [8.74, 8.75, 8.96, 9.44], [10.64, 10.42, 10.52, 10.66], [15.2, 15.41, 16.0, 16.49], [14.93, 15.24, 15.83, 16.43], [14.39, 14.71, 15.17, 15.79], [15.28, 15.51, 15.85, 16.37]],
	'comparisons':
		[[('CB', 'ARG', 'O', 'GLY', 14.3), ('CB', 'ARG', 'C', 'GLY', 13.9), ('CB', 'ARG', 'CA', 'GLY', 13.1), ('CB', 'ARG', 'N', 'GLY', 12.88)], [('CG', 'ARG', 'O', 'GLY', 14.71), ('CG', 'ARG', 'C', 'GLY', 14.38), ('CG', 'ARG', 'CA', 'GLY', 13.73), ('CG', 'ARG', 'N', 'GLY', 13.62)], [('CD', 'ARG', 'O', 'GLY', 13.82), ('CD', 'ARG', 'C', 'GLY', 13.61), ('CD', 'ARG', 'CA', 'GLY', 13.08), ('CD', 'ARG', 'N', 'GLY', 13.14)], [('NE', 'ARG', 'O', 'GLY', 12.55), ('NE', 'ARG', 'C', 'GLY', 12.31), ('NE', 'ARG', 'CA', 'GLY', 11.82), ('NE', 'ARG', 'N', 'GLY', 11.86)], [('CZ', 'ARG', 'O', 'GLY', 11.39), ('CZ', 'ARG', 'C', 'GLY', 11.16), ('CZ', 'ARG', 'CA', 'GLY', 10.61), ('CZ', 'ARG', 'N', 'GLY', 10.7)], [('NH1', 'ARG', 'O', 'GLY', 11.49), ('NH1', 'ARG', 'C', 'GLY', 11.35), ('NH1', 'ARG', 'CA', 'GLY', 10.7), ('NH1', 'ARG', 'N', 'GLY', 10.9)], [('NH2', 'ARG', 'O', 'GLY', 10.3), ('NH2', 'ARG', 'C', 'GLY', 9.99), ('NH2', 'ARG', 'CA', 'GLY', 9.5), ('NH2', 'ARG', 'N', 'GLY', 9.55)], [('O', 'ARG', 'O', 'GLY', 14.36), ('O', 'ARG', 'C', 'GLY', 13.69), ('O', 'ARG', 'CA', 'GLY', 12.86), ('O', 'ARG', 'N', 'GLY', 12.28)], [('C', 'ARG', 'O', 'GLY', 15.24), ('C', 'ARG', 'C', 'GLY', 14.64), ('C', 'ARG', 'CA', 'GLY', 13.84), ('C', 'ARG', 'N', 'GLY', 13.33)], [('CA', 'ARG', 'O', 'GLY', 15.36), ('CA', 'ARG', 'C', 'GLY', 14.85), ('CA', 'ARG', 'CA', 'GLY', 13.98), ('CA', 'ARG', 'N', 'GLY', 13.6)], [('N', 'ARG', 'O', 'GLY', 15.47), ('N', 'ARG', 'C', 'GLY', 14.92), ('N', 'ARG', 'CA', 'GLY', 13.91), ('N', 'ARG', 'N', 'GLY', 13.46)], [('CB', 'ARG', 'O', 'GLY', 12.89), ('CB', 'ARG', 'C', 'GLY', 13.19), ('CB', 'ARG', 'CA', 'GLY', 13.64), ('CB', 'ARG', 'N', 'GLY', 14.27)], [('CG', 'ARG', 'O', 'GLY', 12.5), ('CG', 'ARG', 'C', 'GLY', 12.81), ('CG', 'ARG', 'CA', 'GLY', 13.1), ('CG', 'ARG', 'N', 'GLY', 13.75)], [('CD', 'ARG', 'O', 'GLY', 11.05), ('CD', 'ARG', 'C', 'GLY', 11.32), ('CD', 'ARG', 'CA', 'GLY', 11.57), ('CD', 'ARG', 'N', 'GLY', 12.22)], [('NE', 'ARG', 'O', 'GLY', 11.02), ('NE', 'ARG', 'C', 'GLY', 11.1), ('NE', 'ARG', 'CA', 'GLY', 11.28), ('NE', 'ARG', 'N', 'GLY', 11.74)], [('CZ', 'ARG', 'O', 'GLY', 10.07), ('CZ', 'ARG', 'C', 'GLY', 10.03), ('CZ', 'ARG', 'CA', 'GLY', 10.19), ('CZ', 'ARG', 'N', 'GLY', 10.56)], [('NH1', 'ARG', 'O', 'GLY', 8.74), ('NH1', 'ARG', 'C', 'GLY', 8.75), ('NH1', 'ARG', 'CA', 'GLY', 8.96), ('NH1', 'ARG', 'N', 'GLY', 9.44)], [('NH2', 'ARG', 'O', 'GLY', 10.64), ('NH2', 'ARG', 'C', 'GLY', 10.42), ('NH2', 'ARG', 'CA', 'GLY', 10.52), ('NH2', 'ARG', 'N', 'GLY', 10.66)], [('O', 'ARG', 'O', 'GLY', 15.2), ('O', 'ARG', 'C', 'GLY', 15.41), ('O', 'ARG', 'CA', 'GLY', 16.0), ('O', 'ARG', 'N', 'GLY', 16.49)], [('C', 'ARG', 'O', 'GLY', 14.93), ('C', 'ARG', 'C', 'GLY', 15.24), ('C', 'ARG', 'CA', 'GLY', 15.83), ('C', 'ARG', 'N', 'GLY', 16.43)], [('CA', 'ARG', 'O', 'GLY', 14.39), ('CA', 'ARG', 'C', 'GLY', 14.71), ('CA', 'ARG', 'CA', 'GLY', 15.17), ('CA', 'ARG', 'N', 'GLY', 15.79)], [('N', 'ARG', 'O', 'GLY', 15.28), ('N', 'ARG', 'C', 'GLY', 15.51), ('N', 'ARG', 'CA', 'GLY', 15.85), ('N', 'ARG', 'N', 'GLY', 16.37)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_GLY, d, 'A_2hgs_6_3_2_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLY_ARGI, d, 'A_2hgs_6_3_2_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_ARG, d, 'A_2hgs_6_3_2_3')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ARG_ARG, d, 'A_2hgs_6_3_2_3')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ARG_GLY, d, 'A_2hgs_6_3_2_3')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_GLY' :  match1,
		'GLY_ARGI' :  match2,
		'SER_ARG' :  match3,
		'ARG_ARG' :  match4,
		'ARG_GLY' :  match5}