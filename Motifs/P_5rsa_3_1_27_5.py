'''
FUNC:P_5rsa_3_1_27_5
PDB:5rsa
EC:3.1.27.5
RESI:his,lys,his
LOCI:a-12,41,119;
'''
import motifFunctions as cmd
HIS_LYS = { 
	'distances':
		[[13.7, 12.83, 11.31, 10.8, 9.36, 15.11, 15.17, 15.04, 15.97], [12.58, 11.6, 10.11, 9.45, 7.99, 14.11, 14.07, 13.9, 14.92], [11.66, 10.68, 9.24, 8.58, 7.11, 12.98, 12.97, 12.92, 13.97], [12.42, 11.34, 9.87, 9.08, 7.65, 14.23, 14.06, 13.76, 14.82], [10.9, 9.79, 8.4, 7.54, 6.05, 12.39, 12.24, 12.14, 13.28], [11.34, 10.18, 8.77, 7.84, 6.39, 13.15, 12.91, 12.63, 13.77], [15.15, 14.48, 12.99, 12.71, 11.35, 16.15, 16.43, 16.43, 17.23], [14.71, 14.07, 12.55, 12.33, 11.01, 15.93, 16.18, 16.05, 16.8], [13.36, 12.65, 11.12, 10.85, 9.51, 14.71, 14.88, 14.72, 15.52], [12.7, 12.05, 10.5, 10.33, 9.09, 14.32, 14.45, 14.12, 14.87], [15.71, 14.29, 13.33, 11.95, 11.0, 17.84, 17.2, 16.78, 18.09], [15.43, 13.97, 13.12, 11.66, 10.78, 17.38, 16.7, 16.39, 17.76], [14.21, 12.74, 11.97, 10.48, 9.71, 16.14, 15.42, 15.11, 16.5], [16.41, 14.93, 14.15, 12.65, 11.8, 18.21, 17.51, 17.29, 18.69], [14.53, 13.04, 12.41, 10.88, 10.18, 16.25, 15.51, 15.32, 16.75], [15.86, 14.37, 13.72, 12.19, 11.44, 17.51, 16.79, 16.64, 18.08], [16.77, 15.39, 14.25, 12.94, 11.7, 18.55, 18.09, 17.89, 19.2], [15.61, 14.23, 13.09, 11.78, 10.57, 17.47, 17.0, 16.74, 18.04], [15.49, 14.12, 13.0, 11.7, 10.6, 17.59, 17.05, 16.64, 17.91], [16.6, 15.27, 14.1, 12.88, 11.76, 18.8, 18.28, 17.81, 19.03]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'LYS', 13.7), ('CB', 'HIS', 'CG', 'LYS', 12.83), ('CB', 'HIS', 'CD', 'LYS', 11.31), ('CB', 'HIS', 'CE', 'LYS', 10.8), ('CB', 'HIS', 'NZ', 'LYS', 9.36), ('CB', 'HIS', 'O', 'LYS', 15.11), ('CB', 'HIS', 'C', 'LYS', 15.17), ('CB', 'HIS', 'CA', 'LYS', 15.04), ('CB', 'HIS', 'N', 'LYS', 15.97)], [('CG', 'HIS', 'CB', 'LYS', 12.58), ('CG', 'HIS', 'CG', 'LYS', 11.6), ('CG', 'HIS', 'CD', 'LYS', 10.11), ('CG', 'HIS', 'CE', 'LYS', 9.45), ('CG', 'HIS', 'NZ', 'LYS', 7.99), ('CG', 'HIS', 'O', 'LYS', 14.11), ('CG', 'HIS', 'C', 'LYS', 14.07), ('CG', 'HIS', 'CA', 'LYS', 13.9), ('CG', 'HIS', 'N', 'LYS', 14.92)], [('ND1', 'HIS', 'CB', 'LYS', 11.66), ('ND1', 'HIS', 'CG', 'LYS', 10.68), ('ND1', 'HIS', 'CD', 'LYS', 9.24), ('ND1', 'HIS', 'CE', 'LYS', 8.58), ('ND1', 'HIS', 'NZ', 'LYS', 7.11), ('ND1', 'HIS', 'O', 'LYS', 12.98), ('ND1', 'HIS', 'C', 'LYS', 12.97), ('ND1', 'HIS', 'CA', 'LYS', 12.92), ('ND1', 'HIS', 'N', 'LYS', 13.97)], [('CD2', 'HIS', 'CB', 'LYS', 12.42), ('CD2', 'HIS', 'CG', 'LYS', 11.34), ('CD2', 'HIS', 'CD', 'LYS', 9.87), ('CD2', 'HIS', 'CE', 'LYS', 9.08), ('CD2', 'HIS', 'NZ', 'LYS', 7.65), ('CD2', 'HIS', 'O', 'LYS', 14.23), ('CD2', 'HIS', 'C', 'LYS', 14.06), ('CD2', 'HIS', 'CA', 'LYS', 13.76), ('CD2', 'HIS', 'N', 'LYS', 14.82)], [('CE1', 'HIS', 'CB', 'LYS', 10.9), ('CE1', 'HIS', 'CG', 'LYS', 9.79), ('CE1', 'HIS', 'CD', 'LYS', 8.4), ('CE1', 'HIS', 'CE', 'LYS', 7.54), ('CE1', 'HIS', 'NZ', 'LYS', 6.05), ('CE1', 'HIS', 'O', 'LYS', 12.39), ('CE1', 'HIS', 'C', 'LYS', 12.24), ('CE1', 'HIS', 'CA', 'LYS', 12.14), ('CE1', 'HIS', 'N', 'LYS', 13.28)], [('NE2', 'HIS', 'CB', 'LYS', 11.34), ('NE2', 'HIS', 'CG', 'LYS', 10.18), ('NE2', 'HIS', 'CD', 'LYS', 8.77), ('NE2', 'HIS', 'CE', 'LYS', 7.84), ('NE2', 'HIS', 'NZ', 'LYS', 6.39), ('NE2', 'HIS', 'O', 'LYS', 13.15), ('NE2', 'HIS', 'C', 'LYS', 12.91), ('NE2', 'HIS', 'CA', 'LYS', 12.63), ('NE2', 'HIS', 'N', 'LYS', 13.77)], [('O', 'HIS', 'CB', 'LYS', 15.15), ('O', 'HIS', 'CG', 'LYS', 14.48), ('O', 'HIS', 'CD', 'LYS', 12.99), ('O', 'HIS', 'CE', 'LYS', 12.71), ('O', 'HIS', 'NZ', 'LYS', 11.35), ('O', 'HIS', 'O', 'LYS', 16.15), ('O', 'HIS', 'C', 'LYS', 16.43), ('O', 'HIS', 'CA', 'LYS', 16.43), ('O', 'HIS', 'N', 'LYS', 17.23)], [('C', 'HIS', 'CB', 'LYS', 14.71), ('C', 'HIS', 'CG', 'LYS', 14.07), ('C', 'HIS', 'CD', 'LYS', 12.55), ('C', 'HIS', 'CE', 'LYS', 12.33), ('C', 'HIS', 'NZ', 'LYS', 11.01), ('C', 'HIS', 'O', 'LYS', 15.93), ('C', 'HIS', 'C', 'LYS', 16.18), ('C', 'HIS', 'CA', 'LYS', 16.05), ('C', 'HIS', 'N', 'LYS', 16.8)], [('CA', 'HIS', 'CB', 'LYS', 13.36), ('CA', 'HIS', 'CG', 'LYS', 12.65), ('CA', 'HIS', 'CD', 'LYS', 11.12), ('CA', 'HIS', 'CE', 'LYS', 10.85), ('CA', 'HIS', 'NZ', 'LYS', 9.51), ('CA', 'HIS', 'O', 'LYS', 14.71), ('CA', 'HIS', 'C', 'LYS', 14.88), ('CA', 'HIS', 'CA', 'LYS', 14.72), ('CA', 'HIS', 'N', 'LYS', 15.52)], [('N', 'HIS', 'CB', 'LYS', 12.7), ('N', 'HIS', 'CG', 'LYS', 12.05), ('N', 'HIS', 'CD', 'LYS', 10.5), ('N', 'HIS', 'CE', 'LYS', 10.33), ('N', 'HIS', 'NZ', 'LYS', 9.09), ('N', 'HIS', 'O', 'LYS', 14.32), ('N', 'HIS', 'C', 'LYS', 14.45), ('N', 'HIS', 'CA', 'LYS', 14.12), ('N', 'HIS', 'N', 'LYS', 14.87)], [('CB', 'HIS', 'CB', 'LYS', 15.71), ('CB', 'HIS', 'CG', 'LYS', 14.29), ('CB', 'HIS', 'CD', 'LYS', 13.33), ('CB', 'HIS', 'CE', 'LYS', 11.95), ('CB', 'HIS', 'NZ', 'LYS', 11.0), ('CB', 'HIS', 'O', 'LYS', 17.84), ('CB', 'HIS', 'C', 'LYS', 17.2), ('CB', 'HIS', 'CA', 'LYS', 16.78), ('CB', 'HIS', 'N', 'LYS', 18.09)], [('CG', 'HIS', 'CB', 'LYS', 15.43), ('CG', 'HIS', 'CG', 'LYS', 13.97), ('CG', 'HIS', 'CD', 'LYS', 13.12), ('CG', 'HIS', 'CE', 'LYS', 11.66), ('CG', 'HIS', 'NZ', 'LYS', 10.78), ('CG', 'HIS', 'O', 'LYS', 17.38), ('CG', 'HIS', 'C', 'LYS', 16.7), ('CG', 'HIS', 'CA', 'LYS', 16.39), ('CG', 'HIS', 'N', 'LYS', 17.76)], [('ND1', 'HIS', 'CB', 'LYS', 14.21), ('ND1', 'HIS', 'CG', 'LYS', 12.74), ('ND1', 'HIS', 'CD', 'LYS', 11.97), ('ND1', 'HIS', 'CE', 'LYS', 10.48), ('ND1', 'HIS', 'NZ', 'LYS', 9.71), ('ND1', 'HIS', 'O', 'LYS', 16.14), ('ND1', 'HIS', 'C', 'LYS', 15.42), ('ND1', 'HIS', 'CA', 'LYS', 15.11), ('ND1', 'HIS', 'N', 'LYS', 16.5)], [('CD2', 'HIS', 'CB', 'LYS', 16.41), ('CD2', 'HIS', 'CG', 'LYS', 14.93), ('CD2', 'HIS', 'CD', 'LYS', 14.15), ('CD2', 'HIS', 'CE', 'LYS', 12.65), ('CD2', 'HIS', 'NZ', 'LYS', 11.8), ('CD2', 'HIS', 'O', 'LYS', 18.21), ('CD2', 'HIS', 'C', 'LYS', 17.51), ('CD2', 'HIS', 'CA', 'LYS', 17.29), ('CD2', 'HIS', 'N', 'LYS', 18.69)], [('CE1', 'HIS', 'CB', 'LYS', 14.53), ('CE1', 'HIS', 'CG', 'LYS', 13.04), ('CE1', 'HIS', 'CD', 'LYS', 12.41), ('CE1', 'HIS', 'CE', 'LYS', 10.88), ('CE1', 'HIS', 'NZ', 'LYS', 10.18), ('CE1', 'HIS', 'O', 'LYS', 16.25), ('CE1', 'HIS', 'C', 'LYS', 15.51), ('CE1', 'HIS', 'CA', 'LYS', 15.32), ('CE1', 'HIS', 'N', 'LYS', 16.75)], [('NE2', 'HIS', 'CB', 'LYS', 15.86), ('NE2', 'HIS', 'CG', 'LYS', 14.37), ('NE2', 'HIS', 'CD', 'LYS', 13.72), ('NE2', 'HIS', 'CE', 'LYS', 12.19), ('NE2', 'HIS', 'NZ', 'LYS', 11.44), ('NE2', 'HIS', 'O', 'LYS', 17.51), ('NE2', 'HIS', 'C', 'LYS', 16.79), ('NE2', 'HIS', 'CA', 'LYS', 16.64), ('NE2', 'HIS', 'N', 'LYS', 18.08)], [('O', 'HIS', 'CB', 'LYS', 16.77), ('O', 'HIS', 'CG', 'LYS', 15.39), ('O', 'HIS', 'CD', 'LYS', 14.25), ('O', 'HIS', 'CE', 'LYS', 12.94), ('O', 'HIS', 'NZ', 'LYS', 11.7), ('O', 'HIS', 'O', 'LYS', 18.55), ('O', 'HIS', 'C', 'LYS', 18.09), ('O', 'HIS', 'CA', 'LYS', 17.89), ('O', 'HIS', 'N', 'LYS', 19.2)], [('C', 'HIS', 'CB', 'LYS', 15.61), ('C', 'HIS', 'CG', 'LYS', 14.23), ('C', 'HIS', 'CD', 'LYS', 13.09), ('C', 'HIS', 'CE', 'LYS', 11.78), ('C', 'HIS', 'NZ', 'LYS', 10.57), ('C', 'HIS', 'O', 'LYS', 17.47), ('C', 'HIS', 'C', 'LYS', 17.0), ('C', 'HIS', 'CA', 'LYS', 16.74), ('C', 'HIS', 'N', 'LYS', 18.04)], [('CA', 'HIS', 'CB', 'LYS', 15.49), ('CA', 'HIS', 'CG', 'LYS', 14.12), ('CA', 'HIS', 'CD', 'LYS', 13.0), ('CA', 'HIS', 'CE', 'LYS', 11.7), ('CA', 'HIS', 'NZ', 'LYS', 10.6), ('CA', 'HIS', 'O', 'LYS', 17.59), ('CA', 'HIS', 'C', 'LYS', 17.05), ('CA', 'HIS', 'CA', 'LYS', 16.64), ('CA', 'HIS', 'N', 'LYS', 17.91)], [('N', 'HIS', 'CB', 'LYS', 16.6), ('N', 'HIS', 'CG', 'LYS', 15.27), ('N', 'HIS', 'CD', 'LYS', 14.1), ('N', 'HIS', 'CE', 'LYS', 12.88), ('N', 'HIS', 'NZ', 'LYS', 11.76), ('N', 'HIS', 'O', 'LYS', 18.8), ('N', 'HIS', 'C', 'LYS', 18.28), ('N', 'HIS', 'CA', 'LYS', 17.81), ('N', 'HIS', 'N', 'LYS', 19.03)]]}
HIS_HIS = { 
	'distances':
		[[10.97, 11.44, 11.38, 12.36, 12.19, 12.79, 9.52, 8.99, 9.58, 9.95], [9.92, 10.3, 10.09, 11.28, 10.9, 11.61, 8.84, 8.12, 8.65, 9.23], [10.31, 10.45, 10.05, 11.37, 10.71, 11.49, 9.34, 8.57, 9.19, 10.0], [8.79, 9.26, 9.06, 10.34, 9.99, 10.73, 8.1, 7.23, 7.53, 8.13], [9.51, 9.56, 9.01, 10.52, 9.66, 10.55, 8.97, 8.06, 8.55, 9.52], [8.51, 8.75, 8.31, 9.83, 9.14, 10.03, 8.21, 7.21, 7.49, 8.38], [13.48, 13.94, 13.91, 14.75, 14.64, 15.16, 11.68, 11.34, 12.06, 12.31], [13.27, 13.84, 13.79, 14.76, 14.63, 15.22, 11.74, 11.3, 11.84, 12.03], [12.23, 12.74, 12.58, 13.72, 13.42, 14.11, 10.99, 10.4, 10.87, 11.21], [12.17, 12.77, 12.55, 13.87, 13.49, 14.28, 11.34, 10.62, 10.85, 11.14], [10.97, 9.92, 10.31, 8.79, 9.51, 8.51, 13.48, 13.27, 12.23, 12.17], [11.44, 10.3, 10.45, 9.26, 9.56, 8.75, 13.94, 13.84, 12.74, 12.77], [11.38, 10.09, 10.05, 9.06, 9.01, 8.31, 13.91, 13.79, 12.58, 12.55], [12.36, 11.28, 11.37, 10.34, 10.52, 9.83, 14.75, 14.76, 13.72, 13.87], [12.19, 10.9, 10.71, 9.99, 9.66, 9.14, 14.64, 14.63, 13.42, 13.49], [12.79, 11.61, 11.49, 10.73, 10.55, 10.03, 15.16, 15.22, 14.11, 14.28], [9.52, 8.84, 9.34, 8.1, 8.97, 8.21, 11.68, 11.74, 10.99, 11.34], [8.99, 8.12, 8.57, 7.23, 8.06, 7.21, 11.34, 11.3, 10.4, 10.62], [9.58, 8.65, 9.19, 7.53, 8.55, 7.49, 12.06, 11.84, 10.87, 10.85], [9.95, 9.23, 10.0, 8.13, 9.52, 8.38, 12.31, 12.03, 11.21, 11.14]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 10.97), ('CB', 'HIS', 'CG', 'HIS', 11.44), ('CB', 'HIS', 'ND1', 'HIS', 11.38), ('CB', 'HIS', 'CD2', 'HIS', 12.36), ('CB', 'HIS', 'CE1', 'HIS', 12.19), ('CB', 'HIS', 'NE2', 'HIS', 12.79), ('CB', 'HIS', 'O', 'HIS', 9.52), ('CB', 'HIS', 'C', 'HIS', 8.99), ('CB', 'HIS', 'CA', 'HIS', 9.58), ('CB', 'HIS', 'N', 'HIS', 9.95)], [('CG', 'HIS', 'CB', 'HIS', 9.92), ('CG', 'HIS', 'CG', 'HIS', 10.3), ('CG', 'HIS', 'ND1', 'HIS', 10.09), ('CG', 'HIS', 'CD2', 'HIS', 11.28), ('CG', 'HIS', 'CE1', 'HIS', 10.9), ('CG', 'HIS', 'NE2', 'HIS', 11.61), ('CG', 'HIS', 'O', 'HIS', 8.84), ('CG', 'HIS', 'C', 'HIS', 8.12), ('CG', 'HIS', 'CA', 'HIS', 8.65), ('CG', 'HIS', 'N', 'HIS', 9.23)], [('ND1', 'HIS', 'CB', 'HIS', 10.31), ('ND1', 'HIS', 'CG', 'HIS', 10.45), ('ND1', 'HIS', 'ND1', 'HIS', 10.05), ('ND1', 'HIS', 'CD2', 'HIS', 11.37), ('ND1', 'HIS', 'CE1', 'HIS', 10.71), ('ND1', 'HIS', 'NE2', 'HIS', 11.49), ('ND1', 'HIS', 'O', 'HIS', 9.34), ('ND1', 'HIS', 'C', 'HIS', 8.57), ('ND1', 'HIS', 'CA', 'HIS', 9.19), ('ND1', 'HIS', 'N', 'HIS', 10.0)], [('CD2', 'HIS', 'CB', 'HIS', 8.79), ('CD2', 'HIS', 'CG', 'HIS', 9.26), ('CD2', 'HIS', 'ND1', 'HIS', 9.06), ('CD2', 'HIS', 'CD2', 'HIS', 10.34), ('CD2', 'HIS', 'CE1', 'HIS', 9.99), ('CD2', 'HIS', 'NE2', 'HIS', 10.73), ('CD2', 'HIS', 'O', 'HIS', 8.1), ('CD2', 'HIS', 'C', 'HIS', 7.23), ('CD2', 'HIS', 'CA', 'HIS', 7.53), ('CD2', 'HIS', 'N', 'HIS', 8.13)], [('CE1', 'HIS', 'CB', 'HIS', 9.51), ('CE1', 'HIS', 'CG', 'HIS', 9.56), ('CE1', 'HIS', 'ND1', 'HIS', 9.01), ('CE1', 'HIS', 'CD2', 'HIS', 10.52), ('CE1', 'HIS', 'CE1', 'HIS', 9.66), ('CE1', 'HIS', 'NE2', 'HIS', 10.55), ('CE1', 'HIS', 'O', 'HIS', 8.97), ('CE1', 'HIS', 'C', 'HIS', 8.06), ('CE1', 'HIS', 'CA', 'HIS', 8.55), ('CE1', 'HIS', 'N', 'HIS', 9.52)], [('NE2', 'HIS', 'CB', 'HIS', 8.51), ('NE2', 'HIS', 'CG', 'HIS', 8.75), ('NE2', 'HIS', 'ND1', 'HIS', 8.31), ('NE2', 'HIS', 'CD2', 'HIS', 9.83), ('NE2', 'HIS', 'CE1', 'HIS', 9.14), ('NE2', 'HIS', 'NE2', 'HIS', 10.03), ('NE2', 'HIS', 'O', 'HIS', 8.21), ('NE2', 'HIS', 'C', 'HIS', 7.21), ('NE2', 'HIS', 'CA', 'HIS', 7.49), ('NE2', 'HIS', 'N', 'HIS', 8.38)], [('O', 'HIS', 'CB', 'HIS', 13.48), ('O', 'HIS', 'CG', 'HIS', 13.94), ('O', 'HIS', 'ND1', 'HIS', 13.91), ('O', 'HIS', 'CD2', 'HIS', 14.75), ('O', 'HIS', 'CE1', 'HIS', 14.64), ('O', 'HIS', 'NE2', 'HIS', 15.16), ('O', 'HIS', 'O', 'HIS', 11.68), ('O', 'HIS', 'C', 'HIS', 11.34), ('O', 'HIS', 'CA', 'HIS', 12.06), ('O', 'HIS', 'N', 'HIS', 12.31)], [('C', 'HIS', 'CB', 'HIS', 13.27), ('C', 'HIS', 'CG', 'HIS', 13.84), ('C', 'HIS', 'ND1', 'HIS', 13.79), ('C', 'HIS', 'CD2', 'HIS', 14.76), ('C', 'HIS', 'CE1', 'HIS', 14.63), ('C', 'HIS', 'NE2', 'HIS', 15.22), ('C', 'HIS', 'O', 'HIS', 11.74), ('C', 'HIS', 'C', 'HIS', 11.3), ('C', 'HIS', 'CA', 'HIS', 11.84), ('C', 'HIS', 'N', 'HIS', 12.03)], [('CA', 'HIS', 'CB', 'HIS', 12.23), ('CA', 'HIS', 'CG', 'HIS', 12.74), ('CA', 'HIS', 'ND1', 'HIS', 12.58), ('CA', 'HIS', 'CD2', 'HIS', 13.72), ('CA', 'HIS', 'CE1', 'HIS', 13.42), ('CA', 'HIS', 'NE2', 'HIS', 14.11), ('CA', 'HIS', 'O', 'HIS', 10.99), ('CA', 'HIS', 'C', 'HIS', 10.4), ('CA', 'HIS', 'CA', 'HIS', 10.87), ('CA', 'HIS', 'N', 'HIS', 11.21)], [('N', 'HIS', 'CB', 'HIS', 12.17), ('N', 'HIS', 'CG', 'HIS', 12.77), ('N', 'HIS', 'ND1', 'HIS', 12.55), ('N', 'HIS', 'CD2', 'HIS', 13.87), ('N', 'HIS', 'CE1', 'HIS', 13.49), ('N', 'HIS', 'NE2', 'HIS', 14.28), ('N', 'HIS', 'O', 'HIS', 11.34), ('N', 'HIS', 'C', 'HIS', 10.62), ('N', 'HIS', 'CA', 'HIS', 10.85), ('N', 'HIS', 'N', 'HIS', 11.14)], [('CB', 'HIS', 'CB', 'HIS', 10.97), ('CB', 'HIS', 'CG', 'HIS', 9.92), ('CB', 'HIS', 'ND1', 'HIS', 10.31), ('CB', 'HIS', 'CD2', 'HIS', 8.79), ('CB', 'HIS', 'CE1', 'HIS', 9.51), ('CB', 'HIS', 'NE2', 'HIS', 8.51), ('CB', 'HIS', 'O', 'HIS', 13.48), ('CB', 'HIS', 'C', 'HIS', 13.27), ('CB', 'HIS', 'CA', 'HIS', 12.23), ('CB', 'HIS', 'N', 'HIS', 12.17)], [('CG', 'HIS', 'CB', 'HIS', 11.44), ('CG', 'HIS', 'CG', 'HIS', 10.3), ('CG', 'HIS', 'ND1', 'HIS', 10.45), ('CG', 'HIS', 'CD2', 'HIS', 9.26), ('CG', 'HIS', 'CE1', 'HIS', 9.56), ('CG', 'HIS', 'NE2', 'HIS', 8.75), ('CG', 'HIS', 'O', 'HIS', 13.94), ('CG', 'HIS', 'C', 'HIS', 13.84), ('CG', 'HIS', 'CA', 'HIS', 12.74), ('CG', 'HIS', 'N', 'HIS', 12.77)], [('ND1', 'HIS', 'CB', 'HIS', 11.38), ('ND1', 'HIS', 'CG', 'HIS', 10.09), ('ND1', 'HIS', 'ND1', 'HIS', 10.05), ('ND1', 'HIS', 'CD2', 'HIS', 9.06), ('ND1', 'HIS', 'CE1', 'HIS', 9.01), ('ND1', 'HIS', 'NE2', 'HIS', 8.31), ('ND1', 'HIS', 'O', 'HIS', 13.91), ('ND1', 'HIS', 'C', 'HIS', 13.79), ('ND1', 'HIS', 'CA', 'HIS', 12.58), ('ND1', 'HIS', 'N', 'HIS', 12.55)], [('CD2', 'HIS', 'CB', 'HIS', 12.36), ('CD2', 'HIS', 'CG', 'HIS', 11.28), ('CD2', 'HIS', 'ND1', 'HIS', 11.37), ('CD2', 'HIS', 'CD2', 'HIS', 10.34), ('CD2', 'HIS', 'CE1', 'HIS', 10.52), ('CD2', 'HIS', 'NE2', 'HIS', 9.83), ('CD2', 'HIS', 'O', 'HIS', 14.75), ('CD2', 'HIS', 'C', 'HIS', 14.76), ('CD2', 'HIS', 'CA', 'HIS', 13.72), ('CD2', 'HIS', 'N', 'HIS', 13.87)], [('CE1', 'HIS', 'CB', 'HIS', 12.19), ('CE1', 'HIS', 'CG', 'HIS', 10.9), ('CE1', 'HIS', 'ND1', 'HIS', 10.71), ('CE1', 'HIS', 'CD2', 'HIS', 9.99), ('CE1', 'HIS', 'CE1', 'HIS', 9.66), ('CE1', 'HIS', 'NE2', 'HIS', 9.14), ('CE1', 'HIS', 'O', 'HIS', 14.64), ('CE1', 'HIS', 'C', 'HIS', 14.63), ('CE1', 'HIS', 'CA', 'HIS', 13.42), ('CE1', 'HIS', 'N', 'HIS', 13.49)], [('NE2', 'HIS', 'CB', 'HIS', 12.79), ('NE2', 'HIS', 'CG', 'HIS', 11.61), ('NE2', 'HIS', 'ND1', 'HIS', 11.49), ('NE2', 'HIS', 'CD2', 'HIS', 10.73), ('NE2', 'HIS', 'CE1', 'HIS', 10.55), ('NE2', 'HIS', 'NE2', 'HIS', 10.03), ('NE2', 'HIS', 'O', 'HIS', 15.16), ('NE2', 'HIS', 'C', 'HIS', 15.22), ('NE2', 'HIS', 'CA', 'HIS', 14.11), ('NE2', 'HIS', 'N', 'HIS', 14.28)], [('O', 'HIS', 'CB', 'HIS', 9.52), ('O', 'HIS', 'CG', 'HIS', 8.84), ('O', 'HIS', 'ND1', 'HIS', 9.34), ('O', 'HIS', 'CD2', 'HIS', 8.1), ('O', 'HIS', 'CE1', 'HIS', 8.97), ('O', 'HIS', 'NE2', 'HIS', 8.21), ('O', 'HIS', 'O', 'HIS', 11.68), ('O', 'HIS', 'C', 'HIS', 11.74), ('O', 'HIS', 'CA', 'HIS', 10.99), ('O', 'HIS', 'N', 'HIS', 11.34)], [('C', 'HIS', 'CB', 'HIS', 8.99), ('C', 'HIS', 'CG', 'HIS', 8.12), ('C', 'HIS', 'ND1', 'HIS', 8.57), ('C', 'HIS', 'CD2', 'HIS', 7.23), ('C', 'HIS', 'CE1', 'HIS', 8.06), ('C', 'HIS', 'NE2', 'HIS', 7.21), ('C', 'HIS', 'O', 'HIS', 11.34), ('C', 'HIS', 'C', 'HIS', 11.3), ('C', 'HIS', 'CA', 'HIS', 10.4), ('C', 'HIS', 'N', 'HIS', 10.62)], [('CA', 'HIS', 'CB', 'HIS', 9.58), ('CA', 'HIS', 'CG', 'HIS', 8.65), ('CA', 'HIS', 'ND1', 'HIS', 9.19), ('CA', 'HIS', 'CD2', 'HIS', 7.53), ('CA', 'HIS', 'CE1', 'HIS', 8.55), ('CA', 'HIS', 'NE2', 'HIS', 7.49), ('CA', 'HIS', 'O', 'HIS', 12.06), ('CA', 'HIS', 'C', 'HIS', 11.84), ('CA', 'HIS', 'CA', 'HIS', 10.87), ('CA', 'HIS', 'N', 'HIS', 10.85)], [('N', 'HIS', 'CB', 'HIS', 9.95), ('N', 'HIS', 'CG', 'HIS', 9.23), ('N', 'HIS', 'ND1', 'HIS', 10.0), ('N', 'HIS', 'CD2', 'HIS', 8.13), ('N', 'HIS', 'CE1', 'HIS', 9.52), ('N', 'HIS', 'NE2', 'HIS', 8.38), ('N', 'HIS', 'O', 'HIS', 12.31), ('N', 'HIS', 'C', 'HIS', 12.03), ('N', 'HIS', 'CA', 'HIS', 11.21), ('N', 'HIS', 'N', 'HIS', 11.14)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_LYS, d, 'P_5rsa_3_1_27_5')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_HIS, d, 'P_5rsa_3_1_27_5')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_LYS' :  match1,
		'HIS_HIS' :  match2}