'''
FUNC:A_1fhl_3_2_1_89
PDB:1fhl
EC:3.2.1.89
RESI:arg,glu,glu
LOCI:a-45,136,246;
'''
import motifFunctions as cmd
ARG_GLU = { 
	'distances':
		[[9.91, 8.95, 9.86, 10.86, 9.78, 11.78, 10.87, 9.53, 9.28], [9.31, 8.23, 9.01, 10.11, 8.76, 11.42, 10.59, 9.15, 8.83], [7.87, 6.76, 7.57, 8.64, 7.41, 10.11, 9.25, 7.79, 7.62], [7.31, 6.16, 6.85, 8.03, 6.51, 9.68, 8.97, 7.46, 7.16], [6.62, 5.31, 5.72, 6.91, 5.25, 9.29, 8.6, 7.1, 7.01], [6.44, 4.99, 5.22, 6.28, 4.87, 9.27, 8.44, 7.01, 7.27], [6.56, 5.34, 5.52, 6.74, 4.81, 9.21, 8.7, 7.25, 7.04], [11.66, 10.5, 11.09, 11.92, 10.95, 13.83, 12.77, 11.49, 11.61], [11.72, 10.56, 11.18, 12.11, 10.94, 13.88, 12.9, 11.55, 11.5], [11.39, 10.36, 11.19, 12.18, 11.03, 13.29, 12.36, 11.03, 10.8], [12.02, 11.12, 12.05, 12.97, 12.03, 13.67, 12.71, 11.5, 11.29], [14.97, 13.83, 14.3, 15.31, 13.8, 17.08, 16.26, 14.92, 13.8], [13.61, 12.53, 13.09, 14.1, 12.68, 15.66, 14.83, 13.51, 12.35], [12.64, 11.46, 11.9, 12.91, 11.41, 14.84, 14.06, 12.68, 11.62], [11.3, 10.16, 10.7, 11.75, 10.27, 13.47, 12.66, 11.28, 10.22], [10.22, 9.04, 9.51, 10.51, 9.09, 12.46, 11.73, 10.33, 9.33], [10.52, 9.28, 9.53, 10.43, 9.06, 12.83, 12.22, 10.83, 9.9], [9.0, 7.86, 8.47, 9.52, 8.14, 11.22, 10.45, 9.05, 8.06], [16.35, 15.26, 15.6, 16.42, 15.18, 18.39, 17.71, 16.45, 15.27], [16.03, 14.99, 15.46, 16.33, 15.09, 17.99, 17.25, 16.02, 14.79], [16.1, 15.02, 15.53, 16.5, 15.1, 18.1, 17.29, 16.0, 14.8], [17.33, 16.2, 16.65, 17.62, 16.14, 19.41, 18.6, 17.28, 16.12]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'GLU', 9.91), ('CB', 'ARG', 'CG', 'GLU', 8.95), ('CB', 'ARG', 'CD', 'GLU', 9.86), ('CB', 'ARG', 'OE1', 'GLU', 10.86), ('CB', 'ARG', 'OE2', 'GLU', 9.78), ('CB', 'ARG', 'O', 'GLU', 11.78), ('CB', 'ARG', 'C', 'GLU', 10.87), ('CB', 'ARG', 'CA', 'GLU', 9.53), ('CB', 'ARG', 'N', 'GLU', 9.28)], [('CG', 'ARG', 'CB', 'GLU', 9.31), ('CG', 'ARG', 'CG', 'GLU', 8.23), ('CG', 'ARG', 'CD', 'GLU', 9.01), ('CG', 'ARG', 'OE1', 'GLU', 10.11), ('CG', 'ARG', 'OE2', 'GLU', 8.76), ('CG', 'ARG', 'O', 'GLU', 11.42), ('CG', 'ARG', 'C', 'GLU', 10.59), ('CG', 'ARG', 'CA', 'GLU', 9.15), ('CG', 'ARG', 'N', 'GLU', 8.83)], [('CD', 'ARG', 'CB', 'GLU', 7.87), ('CD', 'ARG', 'CG', 'GLU', 6.76), ('CD', 'ARG', 'CD', 'GLU', 7.57), ('CD', 'ARG', 'OE1', 'GLU', 8.64), ('CD', 'ARG', 'OE2', 'GLU', 7.41), ('CD', 'ARG', 'O', 'GLU', 10.11), ('CD', 'ARG', 'C', 'GLU', 9.25), ('CD', 'ARG', 'CA', 'GLU', 7.79), ('CD', 'ARG', 'N', 'GLU', 7.62)], [('NE', 'ARG', 'CB', 'GLU', 7.31), ('NE', 'ARG', 'CG', 'GLU', 6.16), ('NE', 'ARG', 'CD', 'GLU', 6.85), ('NE', 'ARG', 'OE1', 'GLU', 8.03), ('NE', 'ARG', 'OE2', 'GLU', 6.51), ('NE', 'ARG', 'O', 'GLU', 9.68), ('NE', 'ARG', 'C', 'GLU', 8.97), ('NE', 'ARG', 'CA', 'GLU', 7.46), ('NE', 'ARG', 'N', 'GLU', 7.16)], [('CZ', 'ARG', 'CB', 'GLU', 6.62), ('CZ', 'ARG', 'CG', 'GLU', 5.31), ('CZ', 'ARG', 'CD', 'GLU', 5.72), ('CZ', 'ARG', 'OE1', 'GLU', 6.91), ('CZ', 'ARG', 'OE2', 'GLU', 5.25), ('CZ', 'ARG', 'O', 'GLU', 9.29), ('CZ', 'ARG', 'C', 'GLU', 8.6), ('CZ', 'ARG', 'CA', 'GLU', 7.1), ('CZ', 'ARG', 'N', 'GLU', 7.01)], [('NH1', 'ARG', 'CB', 'GLU', 6.44), ('NH1', 'ARG', 'CG', 'GLU', 4.99), ('NH1', 'ARG', 'CD', 'GLU', 5.22), ('NH1', 'ARG', 'OE1', 'GLU', 6.28), ('NH1', 'ARG', 'OE2', 'GLU', 4.87), ('NH1', 'ARG', 'O', 'GLU', 9.27), ('NH1', 'ARG', 'C', 'GLU', 8.44), ('NH1', 'ARG', 'CA', 'GLU', 7.01), ('NH1', 'ARG', 'N', 'GLU', 7.27)], [('NH2', 'ARG', 'CB', 'GLU', 6.56), ('NH2', 'ARG', 'CG', 'GLU', 5.34), ('NH2', 'ARG', 'CD', 'GLU', 5.52), ('NH2', 'ARG', 'OE1', 'GLU', 6.74), ('NH2', 'ARG', 'OE2', 'GLU', 4.81), ('NH2', 'ARG', 'O', 'GLU', 9.21), ('NH2', 'ARG', 'C', 'GLU', 8.7), ('NH2', 'ARG', 'CA', 'GLU', 7.25), ('NH2', 'ARG', 'N', 'GLU', 7.04)], [('O', 'ARG', 'CB', 'GLU', 11.66), ('O', 'ARG', 'CG', 'GLU', 10.5), ('O', 'ARG', 'CD', 'GLU', 11.09), ('O', 'ARG', 'OE1', 'GLU', 11.92), ('O', 'ARG', 'OE2', 'GLU', 10.95), ('O', 'ARG', 'O', 'GLU', 13.83), ('O', 'ARG', 'C', 'GLU', 12.77), ('O', 'ARG', 'CA', 'GLU', 11.49), ('O', 'ARG', 'N', 'GLU', 11.61)], [('C', 'ARG', 'CB', 'GLU', 11.72), ('C', 'ARG', 'CG', 'GLU', 10.56), ('C', 'ARG', 'CD', 'GLU', 11.18), ('C', 'ARG', 'OE1', 'GLU', 12.11), ('C', 'ARG', 'OE2', 'GLU', 10.94), ('C', 'ARG', 'O', 'GLU', 13.88), ('C', 'ARG', 'C', 'GLU', 12.9), ('C', 'ARG', 'CA', 'GLU', 11.55), ('C', 'ARG', 'N', 'GLU', 11.5)], [('CA', 'ARG', 'CB', 'GLU', 11.39), ('CA', 'ARG', 'CG', 'GLU', 10.36), ('CA', 'ARG', 'CD', 'GLU', 11.19), ('CA', 'ARG', 'OE1', 'GLU', 12.18), ('CA', 'ARG', 'OE2', 'GLU', 11.03), ('CA', 'ARG', 'O', 'GLU', 13.29), ('CA', 'ARG', 'C', 'GLU', 12.36), ('CA', 'ARG', 'CA', 'GLU', 11.03), ('CA', 'ARG', 'N', 'GLU', 10.8)], [('N', 'ARG', 'CB', 'GLU', 12.02), ('N', 'ARG', 'CG', 'GLU', 11.12), ('N', 'ARG', 'CD', 'GLU', 12.05), ('N', 'ARG', 'OE1', 'GLU', 12.97), ('N', 'ARG', 'OE2', 'GLU', 12.03), ('N', 'ARG', 'O', 'GLU', 13.67), ('N', 'ARG', 'C', 'GLU', 12.71), ('N', 'ARG', 'CA', 'GLU', 11.5), ('N', 'ARG', 'N', 'GLU', 11.29)], [('CB', 'ARG', 'CB', 'GLU', 14.97), ('CB', 'ARG', 'CG', 'GLU', 13.83), ('CB', 'ARG', 'CD', 'GLU', 14.3), ('CB', 'ARG', 'OE1', 'GLU', 15.31), ('CB', 'ARG', 'OE2', 'GLU', 13.8), ('CB', 'ARG', 'O', 'GLU', 17.08), ('CB', 'ARG', 'C', 'GLU', 16.26), ('CB', 'ARG', 'CA', 'GLU', 14.92), ('CB', 'ARG', 'N', 'GLU', 13.8)], [('CG', 'ARG', 'CB', 'GLU', 13.61), ('CG', 'ARG', 'CG', 'GLU', 12.53), ('CG', 'ARG', 'CD', 'GLU', 13.09), ('CG', 'ARG', 'OE1', 'GLU', 14.1), ('CG', 'ARG', 'OE2', 'GLU', 12.68), ('CG', 'ARG', 'O', 'GLU', 15.66), ('CG', 'ARG', 'C', 'GLU', 14.83), ('CG', 'ARG', 'CA', 'GLU', 13.51), ('CG', 'ARG', 'N', 'GLU', 12.35)], [('CD', 'ARG', 'CB', 'GLU', 12.64), ('CD', 'ARG', 'CG', 'GLU', 11.46), ('CD', 'ARG', 'CD', 'GLU', 11.9), ('CD', 'ARG', 'OE1', 'GLU', 12.91), ('CD', 'ARG', 'OE2', 'GLU', 11.41), ('CD', 'ARG', 'O', 'GLU', 14.84), ('CD', 'ARG', 'C', 'GLU', 14.06), ('CD', 'ARG', 'CA', 'GLU', 12.68), ('CD', 'ARG', 'N', 'GLU', 11.62)], [('NE', 'ARG', 'CB', 'GLU', 11.3), ('NE', 'ARG', 'CG', 'GLU', 10.16), ('NE', 'ARG', 'CD', 'GLU', 10.7), ('NE', 'ARG', 'OE1', 'GLU', 11.75), ('NE', 'ARG', 'OE2', 'GLU', 10.27), ('NE', 'ARG', 'O', 'GLU', 13.47), ('NE', 'ARG', 'C', 'GLU', 12.66), ('NE', 'ARG', 'CA', 'GLU', 11.28), ('NE', 'ARG', 'N', 'GLU', 10.22)], [('CZ', 'ARG', 'CB', 'GLU', 10.22), ('CZ', 'ARG', 'CG', 'GLU', 9.04), ('CZ', 'ARG', 'CD', 'GLU', 9.51), ('CZ', 'ARG', 'OE1', 'GLU', 10.51), ('CZ', 'ARG', 'OE2', 'GLU', 9.09), ('CZ', 'ARG', 'O', 'GLU', 12.46), ('CZ', 'ARG', 'C', 'GLU', 11.73), ('CZ', 'ARG', 'CA', 'GLU', 10.33), ('CZ', 'ARG', 'N', 'GLU', 9.33)], [('NH1', 'ARG', 'CB', 'GLU', 10.52), ('NH1', 'ARG', 'CG', 'GLU', 9.28), ('NH1', 'ARG', 'CD', 'GLU', 9.53), ('NH1', 'ARG', 'OE1', 'GLU', 10.43), ('NH1', 'ARG', 'OE2', 'GLU', 9.06), ('NH1', 'ARG', 'O', 'GLU', 12.83), ('NH1', 'ARG', 'C', 'GLU', 12.22), ('NH1', 'ARG', 'CA', 'GLU', 10.83), ('NH1', 'ARG', 'N', 'GLU', 9.9)], [('NH2', 'ARG', 'CB', 'GLU', 9.0), ('NH2', 'ARG', 'CG', 'GLU', 7.86), ('NH2', 'ARG', 'CD', 'GLU', 8.47), ('NH2', 'ARG', 'OE1', 'GLU', 9.52), ('NH2', 'ARG', 'OE2', 'GLU', 8.14), ('NH2', 'ARG', 'O', 'GLU', 11.22), ('NH2', 'ARG', 'C', 'GLU', 10.45), ('NH2', 'ARG', 'CA', 'GLU', 9.05), ('NH2', 'ARG', 'N', 'GLU', 8.06)], [('O', 'ARG', 'CB', 'GLU', 16.35), ('O', 'ARG', 'CG', 'GLU', 15.26), ('O', 'ARG', 'CD', 'GLU', 15.6), ('O', 'ARG', 'OE1', 'GLU', 16.42), ('O', 'ARG', 'OE2', 'GLU', 15.18), ('O', 'ARG', 'O', 'GLU', 18.39), ('O', 'ARG', 'C', 'GLU', 17.71), ('O', 'ARG', 'CA', 'GLU', 16.45), ('O', 'ARG', 'N', 'GLU', 15.27)], [('C', 'ARG', 'CB', 'GLU', 16.03), ('C', 'ARG', 'CG', 'GLU', 14.99), ('C', 'ARG', 'CD', 'GLU', 15.46), ('C', 'ARG', 'OE1', 'GLU', 16.33), ('C', 'ARG', 'OE2', 'GLU', 15.09), ('C', 'ARG', 'O', 'GLU', 17.99), ('C', 'ARG', 'C', 'GLU', 17.25), ('C', 'ARG', 'CA', 'GLU', 16.02), ('C', 'ARG', 'N', 'GLU', 14.79)], [('CA', 'ARG', 'CB', 'GLU', 16.1), ('CA', 'ARG', 'CG', 'GLU', 15.02), ('CA', 'ARG', 'CD', 'GLU', 15.53), ('CA', 'ARG', 'OE1', 'GLU', 16.5), ('CA', 'ARG', 'OE2', 'GLU', 15.1), ('CA', 'ARG', 'O', 'GLU', 18.1), ('CA', 'ARG', 'C', 'GLU', 17.29), ('CA', 'ARG', 'CA', 'GLU', 16.0), ('CA', 'ARG', 'N', 'GLU', 14.8)], [('N', 'ARG', 'CB', 'GLU', 17.33), ('N', 'ARG', 'CG', 'GLU', 16.2), ('N', 'ARG', 'CD', 'GLU', 16.65), ('N', 'ARG', 'OE1', 'GLU', 17.62), ('N', 'ARG', 'OE2', 'GLU', 16.14), ('N', 'ARG', 'O', 'GLU', 19.41), ('N', 'ARG', 'C', 'GLU', 18.6), ('N', 'ARG', 'CA', 'GLU', 17.28), ('N', 'ARG', 'N', 'GLU', 16.12)]]}
GLU_GLU = { 
	'distances':
		[[10.16, 8.68, 8.37, 9.39, 7.3, 12.83, 12.3, 10.79, 10.55], [9.78, 8.31, 8.14, 9.14, 7.23, 12.42, 11.87, 10.37, 9.93], [8.78, 7.32, 7.0, 7.88, 6.16, 11.41, 11.0, 9.54, 9.17], [9.03, 7.59, 6.95, 7.68, 6.01, 11.67, 11.38, 9.98, 9.78], [7.98, 6.59, 6.48, 7.37, 5.88, 10.54, 10.1, 8.67, 8.16], [12.01, 10.6, 10.2, 11.18, 9.02, 14.59, 14.04, 12.58, 12.6], [12.21, 10.75, 10.35, 11.32, 9.18, 14.85, 14.3, 12.82, 12.7], [11.51, 10.04, 9.81, 10.86, 8.74, 14.15, 13.54, 12.02, 11.74], [11.5, 10.09, 10.09, 11.24, 9.09, 14.05, 13.32, 11.81, 11.48], [10.16, 9.78, 8.78, 9.03, 7.98, 12.01, 12.21, 11.51, 11.5], [8.68, 8.31, 7.32, 7.59, 6.59, 10.6, 10.75, 10.04, 10.09], [8.37, 8.14, 7.0, 6.95, 6.48, 10.2, 10.35, 9.81, 10.09], [9.39, 9.14, 7.88, 7.68, 7.37, 11.18, 11.32, 10.86, 11.24], [7.3, 7.23, 6.16, 6.01, 5.88, 9.02, 9.18, 8.74, 9.09], [12.83, 12.42, 11.41, 11.67, 10.54, 14.59, 14.85, 14.15, 14.05], [12.3, 11.87, 11.0, 11.38, 10.1, 14.04, 14.3, 13.54, 13.32], [10.79, 10.37, 9.54, 9.98, 8.67, 12.58, 12.82, 12.02, 11.81], [10.55, 9.93, 9.17, 9.78, 8.16, 12.6, 12.7, 11.74, 11.48]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 10.16), ('CB', 'GLU', 'CG', 'GLU', 8.68), ('CB', 'GLU', 'CD', 'GLU', 8.37), ('CB', 'GLU', 'OE1', 'GLU', 9.39), ('CB', 'GLU', 'OE2', 'GLU', 7.3), ('CB', 'GLU', 'O', 'GLU', 12.83), ('CB', 'GLU', 'C', 'GLU', 12.3), ('CB', 'GLU', 'CA', 'GLU', 10.79), ('CB', 'GLU', 'N', 'GLU', 10.55)], [('CG', 'GLU', 'CB', 'GLU', 9.78), ('CG', 'GLU', 'CG', 'GLU', 8.31), ('CG', 'GLU', 'CD', 'GLU', 8.14), ('CG', 'GLU', 'OE1', 'GLU', 9.14), ('CG', 'GLU', 'OE2', 'GLU', 7.23), ('CG', 'GLU', 'O', 'GLU', 12.42), ('CG', 'GLU', 'C', 'GLU', 11.87), ('CG', 'GLU', 'CA', 'GLU', 10.37), ('CG', 'GLU', 'N', 'GLU', 9.93)], [('CD', 'GLU', 'CB', 'GLU', 8.78), ('CD', 'GLU', 'CG', 'GLU', 7.32), ('CD', 'GLU', 'CD', 'GLU', 7.0), ('CD', 'GLU', 'OE1', 'GLU', 7.88), ('CD', 'GLU', 'OE2', 'GLU', 6.16), ('CD', 'GLU', 'O', 'GLU', 11.41), ('CD', 'GLU', 'C', 'GLU', 11.0), ('CD', 'GLU', 'CA', 'GLU', 9.54), ('CD', 'GLU', 'N', 'GLU', 9.17)], [('OE1', 'GLU', 'CB', 'GLU', 9.03), ('OE1', 'GLU', 'CG', 'GLU', 7.59), ('OE1', 'GLU', 'CD', 'GLU', 6.95), ('OE1', 'GLU', 'OE1', 'GLU', 7.68), ('OE1', 'GLU', 'OE2', 'GLU', 6.01), ('OE1', 'GLU', 'O', 'GLU', 11.67), ('OE1', 'GLU', 'C', 'GLU', 11.38), ('OE1', 'GLU', 'CA', 'GLU', 9.98), ('OE1', 'GLU', 'N', 'GLU', 9.78)], [('OE2', 'GLU', 'CB', 'GLU', 7.98), ('OE2', 'GLU', 'CG', 'GLU', 6.59), ('OE2', 'GLU', 'CD', 'GLU', 6.48), ('OE2', 'GLU', 'OE1', 'GLU', 7.37), ('OE2', 'GLU', 'OE2', 'GLU', 5.88), ('OE2', 'GLU', 'O', 'GLU', 10.54), ('OE2', 'GLU', 'C', 'GLU', 10.1), ('OE2', 'GLU', 'CA', 'GLU', 8.67), ('OE2', 'GLU', 'N', 'GLU', 8.16)], [('O', 'GLU', 'CB', 'GLU', 12.01), ('O', 'GLU', 'CG', 'GLU', 10.6), ('O', 'GLU', 'CD', 'GLU', 10.2), ('O', 'GLU', 'OE1', 'GLU', 11.18), ('O', 'GLU', 'OE2', 'GLU', 9.02), ('O', 'GLU', 'O', 'GLU', 14.59), ('O', 'GLU', 'C', 'GLU', 14.04), ('O', 'GLU', 'CA', 'GLU', 12.58), ('O', 'GLU', 'N', 'GLU', 12.6)], [('C', 'GLU', 'CB', 'GLU', 12.21), ('C', 'GLU', 'CG', 'GLU', 10.75), ('C', 'GLU', 'CD', 'GLU', 10.35), ('C', 'GLU', 'OE1', 'GLU', 11.32), ('C', 'GLU', 'OE2', 'GLU', 9.18), ('C', 'GLU', 'O', 'GLU', 14.85), ('C', 'GLU', 'C', 'GLU', 14.3), ('C', 'GLU', 'CA', 'GLU', 12.82), ('C', 'GLU', 'N', 'GLU', 12.7)], [('CA', 'GLU', 'CB', 'GLU', 11.51), ('CA', 'GLU', 'CG', 'GLU', 10.04), ('CA', 'GLU', 'CD', 'GLU', 9.81), ('CA', 'GLU', 'OE1', 'GLU', 10.86), ('CA', 'GLU', 'OE2', 'GLU', 8.74), ('CA', 'GLU', 'O', 'GLU', 14.15), ('CA', 'GLU', 'C', 'GLU', 13.54), ('CA', 'GLU', 'CA', 'GLU', 12.02), ('CA', 'GLU', 'N', 'GLU', 11.74)], [('N', 'GLU', 'CB', 'GLU', 11.5), ('N', 'GLU', 'CG', 'GLU', 10.09), ('N', 'GLU', 'CD', 'GLU', 10.09), ('N', 'GLU', 'OE1', 'GLU', 11.24), ('N', 'GLU', 'OE2', 'GLU', 9.09), ('N', 'GLU', 'O', 'GLU', 14.05), ('N', 'GLU', 'C', 'GLU', 13.32), ('N', 'GLU', 'CA', 'GLU', 11.81), ('N', 'GLU', 'N', 'GLU', 11.48)], [('CB', 'GLU', 'CB', 'GLU', 10.16), ('CB', 'GLU', 'CG', 'GLU', 9.78), ('CB', 'GLU', 'CD', 'GLU', 8.78), ('CB', 'GLU', 'OE1', 'GLU', 9.03), ('CB', 'GLU', 'OE2', 'GLU', 7.98), ('CB', 'GLU', 'O', 'GLU', 12.01), ('CB', 'GLU', 'C', 'GLU', 12.21), ('CB', 'GLU', 'CA', 'GLU', 11.51), ('CB', 'GLU', 'N', 'GLU', 11.5)], [('CG', 'GLU', 'CB', 'GLU', 8.68), ('CG', 'GLU', 'CG', 'GLU', 8.31), ('CG', 'GLU', 'CD', 'GLU', 7.32), ('CG', 'GLU', 'OE1', 'GLU', 7.59), ('CG', 'GLU', 'OE2', 'GLU', 6.59), ('CG', 'GLU', 'O', 'GLU', 10.6), ('CG', 'GLU', 'C', 'GLU', 10.75), ('CG', 'GLU', 'CA', 'GLU', 10.04), ('CG', 'GLU', 'N', 'GLU', 10.09)], [('CD', 'GLU', 'CB', 'GLU', 8.37), ('CD', 'GLU', 'CG', 'GLU', 8.14), ('CD', 'GLU', 'CD', 'GLU', 7.0), ('CD', 'GLU', 'OE1', 'GLU', 6.95), ('CD', 'GLU', 'OE2', 'GLU', 6.48), ('CD', 'GLU', 'O', 'GLU', 10.2), ('CD', 'GLU', 'C', 'GLU', 10.35), ('CD', 'GLU', 'CA', 'GLU', 9.81), ('CD', 'GLU', 'N', 'GLU', 10.09)], [('OE1', 'GLU', 'CB', 'GLU', 9.39), ('OE1', 'GLU', 'CG', 'GLU', 9.14), ('OE1', 'GLU', 'CD', 'GLU', 7.88), ('OE1', 'GLU', 'OE1', 'GLU', 7.68), ('OE1', 'GLU', 'OE2', 'GLU', 7.37), ('OE1', 'GLU', 'O', 'GLU', 11.18), ('OE1', 'GLU', 'C', 'GLU', 11.32), ('OE1', 'GLU', 'CA', 'GLU', 10.86), ('OE1', 'GLU', 'N', 'GLU', 11.24)], [('OE2', 'GLU', 'CB', 'GLU', 7.3), ('OE2', 'GLU', 'CG', 'GLU', 7.23), ('OE2', 'GLU', 'CD', 'GLU', 6.16), ('OE2', 'GLU', 'OE1', 'GLU', 6.01), ('OE2', 'GLU', 'OE2', 'GLU', 5.88), ('OE2', 'GLU', 'O', 'GLU', 9.02), ('OE2', 'GLU', 'C', 'GLU', 9.18), ('OE2', 'GLU', 'CA', 'GLU', 8.74), ('OE2', 'GLU', 'N', 'GLU', 9.09)], [('O', 'GLU', 'CB', 'GLU', 12.83), ('O', 'GLU', 'CG', 'GLU', 12.42), ('O', 'GLU', 'CD', 'GLU', 11.41), ('O', 'GLU', 'OE1', 'GLU', 11.67), ('O', 'GLU', 'OE2', 'GLU', 10.54), ('O', 'GLU', 'O', 'GLU', 14.59), ('O', 'GLU', 'C', 'GLU', 14.85), ('O', 'GLU', 'CA', 'GLU', 14.15), ('O', 'GLU', 'N', 'GLU', 14.05)], [('C', 'GLU', 'CB', 'GLU', 12.3), ('C', 'GLU', 'CG', 'GLU', 11.87), ('C', 'GLU', 'CD', 'GLU', 11.0), ('C', 'GLU', 'OE1', 'GLU', 11.38), ('C', 'GLU', 'OE2', 'GLU', 10.1), ('C', 'GLU', 'O', 'GLU', 14.04), ('C', 'GLU', 'C', 'GLU', 14.3), ('C', 'GLU', 'CA', 'GLU', 13.54), ('C', 'GLU', 'N', 'GLU', 13.32)], [('CA', 'GLU', 'CB', 'GLU', 10.79), ('CA', 'GLU', 'CG', 'GLU', 10.37), ('CA', 'GLU', 'CD', 'GLU', 9.54), ('CA', 'GLU', 'OE1', 'GLU', 9.98), ('CA', 'GLU', 'OE2', 'GLU', 8.67), ('CA', 'GLU', 'O', 'GLU', 12.58), ('CA', 'GLU', 'C', 'GLU', 12.82), ('CA', 'GLU', 'CA', 'GLU', 12.02), ('CA', 'GLU', 'N', 'GLU', 11.81)], [('N', 'GLU', 'CB', 'GLU', 10.55), ('N', 'GLU', 'CG', 'GLU', 9.93), ('N', 'GLU', 'CD', 'GLU', 9.17), ('N', 'GLU', 'OE1', 'GLU', 9.78), ('N', 'GLU', 'OE2', 'GLU', 8.16), ('N', 'GLU', 'O', 'GLU', 12.6), ('N', 'GLU', 'C', 'GLU', 12.7), ('N', 'GLU', 'CA', 'GLU', 11.74), ('N', 'GLU', 'N', 'GLU', 11.48)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_GLU, d, 'A_1fhl_3_2_1_89')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_GLU, d, 'A_1fhl_3_2_1_89')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_GLU' :  match1,
		'GLU_GLU' :  match2}