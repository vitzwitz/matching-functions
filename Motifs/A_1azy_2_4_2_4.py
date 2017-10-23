'''
FUNC:A_1azy_2_4_2_4
PDB:1azy
EC:2.4.2.4
RESI:his,arg,lys
LOCI:a-85,171,190;
'''
import motifFunctions as cmd
LYS_HIS = { 
	'distances':
		[[9.51, 8.45, 8.64, 7.41, 7.81, 6.97, 12.38, 11.5, 10.56, 11.47], [10.57, 9.37, 9.38, 8.3, 8.37, 7.62, 13.29, 12.4, 11.59, 12.6], [11.72, 10.55, 10.47, 9.58, 9.5, 8.88, 14.45, 13.49, 12.63, 13.61], [12.76, 11.49, 11.26, 10.52, 10.18, 9.66, 15.34, 14.37, 13.62, 14.69], [13.74, 12.46, 12.3, 11.39, 11.17, 10.54, 16.33, 15.41, 14.7, 15.78], [10.14, 9.57, 10.13, 8.75, 9.73, 8.88, 13.21, 12.42, 11.16, 11.64], [9.41, 8.73, 9.29, 7.79, 8.81, 7.87, 12.47, 11.7, 10.53, 11.13], [10.06, 9.16, 9.57, 8.09, 8.87, 7.9, 13.04, 12.25, 11.21, 11.98], [10.2, 9.29, 9.8, 8.08, 9.06, 7.94, 13.11, 12.42, 11.49, 12.28]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'HIS', 9.51), ('CB', 'LYS', 'CG', 'HIS', 8.45), ('CB', 'LYS', 'ND1', 'HIS', 8.64), ('CB', 'LYS', 'CD2', 'HIS', 7.41), ('CB', 'LYS', 'CE1', 'HIS', 7.81), ('CB', 'LYS', 'NE2', 'HIS', 6.97), ('CB', 'LYS', 'O', 'HIS', 12.38), ('CB', 'LYS', 'C', 'HIS', 11.5), ('CB', 'LYS', 'CA', 'HIS', 10.56), ('CB', 'LYS', 'N', 'HIS', 11.47)], [('CG', 'LYS', 'CB', 'HIS', 10.57), ('CG', 'LYS', 'CG', 'HIS', 9.37), ('CG', 'LYS', 'ND1', 'HIS', 9.38), ('CG', 'LYS', 'CD2', 'HIS', 8.3), ('CG', 'LYS', 'CE1', 'HIS', 8.37), ('CG', 'LYS', 'NE2', 'HIS', 7.62), ('CG', 'LYS', 'O', 'HIS', 13.29), ('CG', 'LYS', 'C', 'HIS', 12.4), ('CG', 'LYS', 'CA', 'HIS', 11.59), ('CG', 'LYS', 'N', 'HIS', 12.6)], [('CD', 'LYS', 'CB', 'HIS', 11.72), ('CD', 'LYS', 'CG', 'HIS', 10.55), ('CD', 'LYS', 'ND1', 'HIS', 10.47), ('CD', 'LYS', 'CD2', 'HIS', 9.58), ('CD', 'LYS', 'CE1', 'HIS', 9.5), ('CD', 'LYS', 'NE2', 'HIS', 8.88), ('CD', 'LYS', 'O', 'HIS', 14.45), ('CD', 'LYS', 'C', 'HIS', 13.49), ('CD', 'LYS', 'CA', 'HIS', 12.63), ('CD', 'LYS', 'N', 'HIS', 13.61)], [('CE', 'LYS', 'CB', 'HIS', 12.76), ('CE', 'LYS', 'CG', 'HIS', 11.49), ('CE', 'LYS', 'ND1', 'HIS', 11.26), ('CE', 'LYS', 'CD2', 'HIS', 10.52), ('CE', 'LYS', 'CE1', 'HIS', 10.18), ('CE', 'LYS', 'NE2', 'HIS', 9.66), ('CE', 'LYS', 'O', 'HIS', 15.34), ('CE', 'LYS', 'C', 'HIS', 14.37), ('CE', 'LYS', 'CA', 'HIS', 13.62), ('CE', 'LYS', 'N', 'HIS', 14.69)], [('NZ', 'LYS', 'CB', 'HIS', 13.74), ('NZ', 'LYS', 'CG', 'HIS', 12.46), ('NZ', 'LYS', 'ND1', 'HIS', 12.3), ('NZ', 'LYS', 'CD2', 'HIS', 11.39), ('NZ', 'LYS', 'CE1', 'HIS', 11.17), ('NZ', 'LYS', 'NE2', 'HIS', 10.54), ('NZ', 'LYS', 'O', 'HIS', 16.33), ('NZ', 'LYS', 'C', 'HIS', 15.41), ('NZ', 'LYS', 'CA', 'HIS', 14.7), ('NZ', 'LYS', 'N', 'HIS', 15.78)], [('O', 'LYS', 'CB', 'HIS', 10.14), ('O', 'LYS', 'CG', 'HIS', 9.57), ('O', 'LYS', 'ND1', 'HIS', 10.13), ('O', 'LYS', 'CD2', 'HIS', 8.75), ('O', 'LYS', 'CE1', 'HIS', 9.73), ('O', 'LYS', 'NE2', 'HIS', 8.88), ('O', 'LYS', 'O', 'HIS', 13.21), ('O', 'LYS', 'C', 'HIS', 12.42), ('O', 'LYS', 'CA', 'HIS', 11.16), ('O', 'LYS', 'N', 'HIS', 11.64)], [('C', 'LYS', 'CB', 'HIS', 9.41), ('C', 'LYS', 'CG', 'HIS', 8.73), ('C', 'LYS', 'ND1', 'HIS', 9.29), ('C', 'LYS', 'CD2', 'HIS', 7.79), ('C', 'LYS', 'CE1', 'HIS', 8.81), ('C', 'LYS', 'NE2', 'HIS', 7.87), ('C', 'LYS', 'O', 'HIS', 12.47), ('C', 'LYS', 'C', 'HIS', 11.7), ('C', 'LYS', 'CA', 'HIS', 10.53), ('C', 'LYS', 'N', 'HIS', 11.13)], [('CA', 'LYS', 'CB', 'HIS', 10.06), ('CA', 'LYS', 'CG', 'HIS', 9.16), ('CA', 'LYS', 'ND1', 'HIS', 9.57), ('CA', 'LYS', 'CD2', 'HIS', 8.09), ('CA', 'LYS', 'CE1', 'HIS', 8.87), ('CA', 'LYS', 'NE2', 'HIS', 7.9), ('CA', 'LYS', 'O', 'HIS', 13.04), ('CA', 'LYS', 'C', 'HIS', 12.25), ('CA', 'LYS', 'CA', 'HIS', 11.21), ('CA', 'LYS', 'N', 'HIS', 11.98)], [('N', 'LYS', 'CB', 'HIS', 10.2), ('N', 'LYS', 'CG', 'HIS', 9.29), ('N', 'LYS', 'ND1', 'HIS', 9.8), ('N', 'LYS', 'CD2', 'HIS', 8.08), ('N', 'LYS', 'CE1', 'HIS', 9.06), ('N', 'LYS', 'NE2', 'HIS', 7.94), ('N', 'LYS', 'O', 'HIS', 13.11), ('N', 'LYS', 'C', 'HIS', 12.42), ('N', 'LYS', 'CA', 'HIS', 11.49), ('N', 'LYS', 'N', 'HIS', 12.28)]]}
LYS_ARG = { 
	'distances':
		[[16.94, 16.92, 15.71, 15.42, 14.25, 13.17, 14.26, 19.51, 18.62, 18.17, 18.01], [15.77, 15.81, 14.66, 14.43, 13.31, 12.21, 13.39, 18.32, 17.39, 16.94, 16.72], [16.36, 16.44, 15.38, 15.25, 14.19, 13.08, 14.36, 18.89, 17.9, 17.44, 17.09], [15.45, 15.61, 14.66, 14.58, 13.59, 12.5, 13.81, 17.89, 16.86, 16.44, 16.01], [14.5, 14.58, 13.66, 13.71, 12.79, 11.64, 13.15, 17.06, 16.0, 15.47, 14.97], [19.86, 19.68, 18.41, 18.22, 17.07, 15.93, 17.14, 22.58, 21.68, 21.11, 20.92], [18.84, 18.68, 17.38, 17.14, 15.97, 14.85, 16.0, 21.54, 20.67, 20.13, 19.99], [17.46, 17.31, 16.05, 15.86, 14.71, 13.57, 14.81, 20.18, 19.28, 18.72, 18.53], [16.59, 16.34, 15.04, 14.85, 13.71, 12.56, 13.84, 19.39, 18.52, 17.9, 17.77]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ARG', 16.94), ('CB', 'LYS', 'CG', 'ARG', 16.92), ('CB', 'LYS', 'CD', 'ARG', 15.71), ('CB', 'LYS', 'NE', 'ARG', 15.42), ('CB', 'LYS', 'CZ', 'ARG', 14.25), ('CB', 'LYS', 'NH1', 'ARG', 13.17), ('CB', 'LYS', 'NH2', 'ARG', 14.26), ('CB', 'LYS', 'O', 'ARG', 19.51), ('CB', 'LYS', 'C', 'ARG', 18.62), ('CB', 'LYS', 'CA', 'ARG', 18.17), ('CB', 'LYS', 'N', 'ARG', 18.01)], [('CG', 'LYS', 'CB', 'ARG', 15.77), ('CG', 'LYS', 'CG', 'ARG', 15.81), ('CG', 'LYS', 'CD', 'ARG', 14.66), ('CG', 'LYS', 'NE', 'ARG', 14.43), ('CG', 'LYS', 'CZ', 'ARG', 13.31), ('CG', 'LYS', 'NH1', 'ARG', 12.21), ('CG', 'LYS', 'NH2', 'ARG', 13.39), ('CG', 'LYS', 'O', 'ARG', 18.32), ('CG', 'LYS', 'C', 'ARG', 17.39), ('CG', 'LYS', 'CA', 'ARG', 16.94), ('CG', 'LYS', 'N', 'ARG', 16.72)], [('CD', 'LYS', 'CB', 'ARG', 16.36), ('CD', 'LYS', 'CG', 'ARG', 16.44), ('CD', 'LYS', 'CD', 'ARG', 15.38), ('CD', 'LYS', 'NE', 'ARG', 15.25), ('CD', 'LYS', 'CZ', 'ARG', 14.19), ('CD', 'LYS', 'NH1', 'ARG', 13.08), ('CD', 'LYS', 'NH2', 'ARG', 14.36), ('CD', 'LYS', 'O', 'ARG', 18.89), ('CD', 'LYS', 'C', 'ARG', 17.9), ('CD', 'LYS', 'CA', 'ARG', 17.44), ('CD', 'LYS', 'N', 'ARG', 17.09)], [('CE', 'LYS', 'CB', 'ARG', 15.45), ('CE', 'LYS', 'CG', 'ARG', 15.61), ('CE', 'LYS', 'CD', 'ARG', 14.66), ('CE', 'LYS', 'NE', 'ARG', 14.58), ('CE', 'LYS', 'CZ', 'ARG', 13.59), ('CE', 'LYS', 'NH1', 'ARG', 12.5), ('CE', 'LYS', 'NH2', 'ARG', 13.81), ('CE', 'LYS', 'O', 'ARG', 17.89), ('CE', 'LYS', 'C', 'ARG', 16.86), ('CE', 'LYS', 'CA', 'ARG', 16.44), ('CE', 'LYS', 'N', 'ARG', 16.01)], [('NZ', 'LYS', 'CB', 'ARG', 14.5), ('NZ', 'LYS', 'CG', 'ARG', 14.58), ('NZ', 'LYS', 'CD', 'ARG', 13.66), ('NZ', 'LYS', 'NE', 'ARG', 13.71), ('NZ', 'LYS', 'CZ', 'ARG', 12.79), ('NZ', 'LYS', 'NH1', 'ARG', 11.64), ('NZ', 'LYS', 'NH2', 'ARG', 13.15), ('NZ', 'LYS', 'O', 'ARG', 17.06), ('NZ', 'LYS', 'C', 'ARG', 16.0), ('NZ', 'LYS', 'CA', 'ARG', 15.47), ('NZ', 'LYS', 'N', 'ARG', 14.97)], [('O', 'LYS', 'CB', 'ARG', 19.86), ('O', 'LYS', 'CG', 'ARG', 19.68), ('O', 'LYS', 'CD', 'ARG', 18.41), ('O', 'LYS', 'NE', 'ARG', 18.22), ('O', 'LYS', 'CZ', 'ARG', 17.07), ('O', 'LYS', 'NH1', 'ARG', 15.93), ('O', 'LYS', 'NH2', 'ARG', 17.14), ('O', 'LYS', 'O', 'ARG', 22.58), ('O', 'LYS', 'C', 'ARG', 21.68), ('O', 'LYS', 'CA', 'ARG', 21.11), ('O', 'LYS', 'N', 'ARG', 20.92)], [('C', 'LYS', 'CB', 'ARG', 18.84), ('C', 'LYS', 'CG', 'ARG', 18.68), ('C', 'LYS', 'CD', 'ARG', 17.38), ('C', 'LYS', 'NE', 'ARG', 17.14), ('C', 'LYS', 'CZ', 'ARG', 15.97), ('C', 'LYS', 'NH1', 'ARG', 14.85), ('C', 'LYS', 'NH2', 'ARG', 16.0), ('C', 'LYS', 'O', 'ARG', 21.54), ('C', 'LYS', 'C', 'ARG', 20.67), ('C', 'LYS', 'CA', 'ARG', 20.13), ('C', 'LYS', 'N', 'ARG', 19.99)], [('CA', 'LYS', 'CB', 'ARG', 17.46), ('CA', 'LYS', 'CG', 'ARG', 17.31), ('CA', 'LYS', 'CD', 'ARG', 16.05), ('CA', 'LYS', 'NE', 'ARG', 15.86), ('CA', 'LYS', 'CZ', 'ARG', 14.71), ('CA', 'LYS', 'NH1', 'ARG', 13.57), ('CA', 'LYS', 'NH2', 'ARG', 14.81), ('CA', 'LYS', 'O', 'ARG', 20.18), ('CA', 'LYS', 'C', 'ARG', 19.28), ('CA', 'LYS', 'CA', 'ARG', 18.72), ('CA', 'LYS', 'N', 'ARG', 18.53)], [('N', 'LYS', 'CB', 'ARG', 16.59), ('N', 'LYS', 'CG', 'ARG', 16.34), ('N', 'LYS', 'CD', 'ARG', 15.04), ('N', 'LYS', 'NE', 'ARG', 14.85), ('N', 'LYS', 'CZ', 'ARG', 13.71), ('N', 'LYS', 'NH1', 'ARG', 12.56), ('N', 'LYS', 'NH2', 'ARG', 13.84), ('N', 'LYS', 'O', 'ARG', 19.39), ('N', 'LYS', 'C', 'ARG', 18.52), ('N', 'LYS', 'CA', 'ARG', 17.9), ('N', 'LYS', 'N', 'ARG', 17.77)]]}
HIS_ARG = { 
	'distances':
		[[20.72, 20.83, 19.51, 18.64, 17.32, 16.73, 16.67, 22.67, 22.17, 22.08, 22.46], [19.37, 19.53, 18.23, 17.37, 16.05, 15.45, 15.42, 21.33, 20.8, 20.72, 21.06], [19.09, 19.36, 18.13, 17.23, 15.92, 15.37, 15.25, 20.9, 20.37, 20.39, 20.72], [18.32, 18.41, 17.1, 16.29, 14.97, 14.31, 14.41, 20.4, 19.83, 19.68, 20.0], [17.9, 18.18, 16.98, 16.11, 14.8, 14.23, 14.16, 19.73, 19.17, 19.17, 19.48], [17.37, 17.55, 16.29, 15.47, 14.16, 13.51, 13.6, 19.38, 18.8, 18.7, 18.98], [21.89, 22.1, 20.84, 19.8, 18.5, 18.13, 17.66, 23.51, 23.15, 23.23, 23.76], [21.51, 21.76, 20.51, 19.5, 18.2, 17.78, 17.4, 23.16, 22.74, 22.82, 23.29], [21.73, 21.93, 20.65, 19.73, 18.41, 17.88, 17.71, 23.55, 23.07, 23.06, 23.45], [23.06, 23.21, 21.91, 21.0, 19.68, 19.13, 18.99, 24.92, 24.44, 24.41, 24.8]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 20.72), ('CB', 'HIS', 'CG', 'ARG', 20.83), ('CB', 'HIS', 'CD', 'ARG', 19.51), ('CB', 'HIS', 'NE', 'ARG', 18.64), ('CB', 'HIS', 'CZ', 'ARG', 17.32), ('CB', 'HIS', 'NH1', 'ARG', 16.73), ('CB', 'HIS', 'NH2', 'ARG', 16.67), ('CB', 'HIS', 'O', 'ARG', 22.67), ('CB', 'HIS', 'C', 'ARG', 22.17), ('CB', 'HIS', 'CA', 'ARG', 22.08), ('CB', 'HIS', 'N', 'ARG', 22.46)], [('CG', 'HIS', 'CB', 'ARG', 19.37), ('CG', 'HIS', 'CG', 'ARG', 19.53), ('CG', 'HIS', 'CD', 'ARG', 18.23), ('CG', 'HIS', 'NE', 'ARG', 17.37), ('CG', 'HIS', 'CZ', 'ARG', 16.05), ('CG', 'HIS', 'NH1', 'ARG', 15.45), ('CG', 'HIS', 'NH2', 'ARG', 15.42), ('CG', 'HIS', 'O', 'ARG', 21.33), ('CG', 'HIS', 'C', 'ARG', 20.8), ('CG', 'HIS', 'CA', 'ARG', 20.72), ('CG', 'HIS', 'N', 'ARG', 21.06)], [('ND1', 'HIS', 'CB', 'ARG', 19.09), ('ND1', 'HIS', 'CG', 'ARG', 19.36), ('ND1', 'HIS', 'CD', 'ARG', 18.13), ('ND1', 'HIS', 'NE', 'ARG', 17.23), ('ND1', 'HIS', 'CZ', 'ARG', 15.92), ('ND1', 'HIS', 'NH1', 'ARG', 15.37), ('ND1', 'HIS', 'NH2', 'ARG', 15.25), ('ND1', 'HIS', 'O', 'ARG', 20.9), ('ND1', 'HIS', 'C', 'ARG', 20.37), ('ND1', 'HIS', 'CA', 'ARG', 20.39), ('ND1', 'HIS', 'N', 'ARG', 20.72)], [('CD2', 'HIS', 'CB', 'ARG', 18.32), ('CD2', 'HIS', 'CG', 'ARG', 18.41), ('CD2', 'HIS', 'CD', 'ARG', 17.1), ('CD2', 'HIS', 'NE', 'ARG', 16.29), ('CD2', 'HIS', 'CZ', 'ARG', 14.97), ('CD2', 'HIS', 'NH1', 'ARG', 14.31), ('CD2', 'HIS', 'NH2', 'ARG', 14.41), ('CD2', 'HIS', 'O', 'ARG', 20.4), ('CD2', 'HIS', 'C', 'ARG', 19.83), ('CD2', 'HIS', 'CA', 'ARG', 19.68), ('CD2', 'HIS', 'N', 'ARG', 20.0)], [('CE1', 'HIS', 'CB', 'ARG', 17.9), ('CE1', 'HIS', 'CG', 'ARG', 18.18), ('CE1', 'HIS', 'CD', 'ARG', 16.98), ('CE1', 'HIS', 'NE', 'ARG', 16.11), ('CE1', 'HIS', 'CZ', 'ARG', 14.8), ('CE1', 'HIS', 'NH1', 'ARG', 14.23), ('CE1', 'HIS', 'NH2', 'ARG', 14.16), ('CE1', 'HIS', 'O', 'ARG', 19.73), ('CE1', 'HIS', 'C', 'ARG', 19.17), ('CE1', 'HIS', 'CA', 'ARG', 19.17), ('CE1', 'HIS', 'N', 'ARG', 19.48)], [('NE2', 'HIS', 'CB', 'ARG', 17.37), ('NE2', 'HIS', 'CG', 'ARG', 17.55), ('NE2', 'HIS', 'CD', 'ARG', 16.29), ('NE2', 'HIS', 'NE', 'ARG', 15.47), ('NE2', 'HIS', 'CZ', 'ARG', 14.16), ('NE2', 'HIS', 'NH1', 'ARG', 13.51), ('NE2', 'HIS', 'NH2', 'ARG', 13.6), ('NE2', 'HIS', 'O', 'ARG', 19.38), ('NE2', 'HIS', 'C', 'ARG', 18.8), ('NE2', 'HIS', 'CA', 'ARG', 18.7), ('NE2', 'HIS', 'N', 'ARG', 18.98)], [('O', 'HIS', 'CB', 'ARG', 21.89), ('O', 'HIS', 'CG', 'ARG', 22.1), ('O', 'HIS', 'CD', 'ARG', 20.84), ('O', 'HIS', 'NE', 'ARG', 19.8), ('O', 'HIS', 'CZ', 'ARG', 18.5), ('O', 'HIS', 'NH1', 'ARG', 18.13), ('O', 'HIS', 'NH2', 'ARG', 17.66), ('O', 'HIS', 'O', 'ARG', 23.51), ('O', 'HIS', 'C', 'ARG', 23.15), ('O', 'HIS', 'CA', 'ARG', 23.23), ('O', 'HIS', 'N', 'ARG', 23.76)], [('C', 'HIS', 'CB', 'ARG', 21.51), ('C', 'HIS', 'CG', 'ARG', 21.76), ('C', 'HIS', 'CD', 'ARG', 20.51), ('C', 'HIS', 'NE', 'ARG', 19.5), ('C', 'HIS', 'CZ', 'ARG', 18.2), ('C', 'HIS', 'NH1', 'ARG', 17.78), ('C', 'HIS', 'NH2', 'ARG', 17.4), ('C', 'HIS', 'O', 'ARG', 23.16), ('C', 'HIS', 'C', 'ARG', 22.74), ('C', 'HIS', 'CA', 'ARG', 22.82), ('C', 'HIS', 'N', 'ARG', 23.29)], [('CA', 'HIS', 'CB', 'ARG', 21.73), ('CA', 'HIS', 'CG', 'ARG', 21.93), ('CA', 'HIS', 'CD', 'ARG', 20.65), ('CA', 'HIS', 'NE', 'ARG', 19.73), ('CA', 'HIS', 'CZ', 'ARG', 18.41), ('CA', 'HIS', 'NH1', 'ARG', 17.88), ('CA', 'HIS', 'NH2', 'ARG', 17.71), ('CA', 'HIS', 'O', 'ARG', 23.55), ('CA', 'HIS', 'C', 'ARG', 23.07), ('CA', 'HIS', 'CA', 'ARG', 23.06), ('CA', 'HIS', 'N', 'ARG', 23.45)], [('N', 'HIS', 'CB', 'ARG', 23.06), ('N', 'HIS', 'CG', 'ARG', 23.21), ('N', 'HIS', 'CD', 'ARG', 21.91), ('N', 'HIS', 'NE', 'ARG', 21.0), ('N', 'HIS', 'CZ', 'ARG', 19.68), ('N', 'HIS', 'NH1', 'ARG', 19.13), ('N', 'HIS', 'NH2', 'ARG', 18.99), ('N', 'HIS', 'O', 'ARG', 24.92), ('N', 'HIS', 'C', 'ARG', 24.44), ('N', 'HIS', 'CA', 'ARG', 24.41), ('N', 'HIS', 'N', 'ARG', 24.8)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_HIS, d, 'A_1azy_2_4_2_4')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_ARG, d, 'A_1azy_2_4_2_4')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ARG, d, 'A_1azy_2_4_2_4')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_HIS' :  match1,
		'LYS_ARG' :  match2,
		'HIS_ARG' :  match3}