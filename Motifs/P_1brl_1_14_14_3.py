'''
FUNC:P_1brl_1_14_14_3
PDB:1brl
EC:1.14.14.3
RESI:his,his,phe
LOCI:a-44,45,261;
'''
import motifFunctions as cmd
HIS_HIS = { 
	'distances':
		[[6.76, 6.52, 6.41, 6.84, 6.67, 6.92, 5.04, 4.54, 5.67, 6.51], [6.86, 6.98, 6.94, 7.55, 7.49, 7.84, 5.16, 4.61, 5.5, 5.99], [7.5, 7.81, 7.99, 8.32, 8.59, 8.78, 5.35, 5.13, 6.09, 6.27], [6.84, 7.11, 6.93, 7.92, 7.66, 8.22, 5.74, 4.96, 5.41, 5.74], [7.83, 8.36, 8.53, 9.05, 9.29, 9.59, 6.0, 5.69, 6.33, 6.2], [7.48, 8.01, 7.99, 8.86, 8.82, 9.32, 6.22, 5.62, 5.96, 5.89], [6.29, 5.31, 5.12, 5.01, 4.67, 4.58, 5.31, 4.94, 6.02, 7.32], [6.29, 5.58, 5.67, 5.33, 5.48, 5.27, 4.61, 4.47, 5.79, 6.94], [5.68, 5.37, 5.55, 5.53, 5.79, 5.78, 3.74, 3.43, 4.8, 5.77], [4.4, 4.29, 4.48, 4.82, 5.06, 5.25, 3.2, 2.32, 3.42, 4.51], [6.76, 6.86, 7.5, 6.84, 7.83, 7.48, 6.29, 6.29, 5.68, 4.4], [6.52, 6.98, 7.81, 7.11, 8.36, 8.01, 5.31, 5.58, 5.37, 4.29], [6.41, 6.94, 7.99, 6.93, 8.53, 7.99, 5.12, 5.67, 5.55, 4.48], [6.84, 7.55, 8.32, 7.92, 9.05, 8.86, 5.01, 5.33, 5.53, 4.82], [6.67, 7.49, 8.59, 7.66, 9.29, 8.82, 4.67, 5.48, 5.79, 5.06], [6.92, 7.84, 8.78, 8.22, 9.59, 9.32, 4.58, 5.27, 5.78, 5.25], [5.04, 5.16, 5.35, 5.74, 6.0, 6.22, 5.31, 4.61, 3.74, 3.2], [4.54, 4.61, 5.13, 4.96, 5.69, 5.62, 4.94, 4.47, 3.43, 2.32], [5.67, 5.5, 6.09, 5.41, 6.33, 5.96, 6.02, 5.79, 4.8, 3.42], [6.51, 5.99, 6.27, 5.74, 6.2, 5.89, 7.32, 6.94, 5.77, 4.51]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 6.76), ('CB', 'HIS', 'CG', 'HIS', 6.52), ('CB', 'HIS', 'ND1', 'HIS', 6.41), ('CB', 'HIS', 'CD2', 'HIS', 6.84), ('CB', 'HIS', 'CE1', 'HIS', 6.67), ('CB', 'HIS', 'NE2', 'HIS', 6.92), ('CB', 'HIS', 'O', 'HIS', 5.04), ('CB', 'HIS', 'C', 'HIS', 4.54), ('CB', 'HIS', 'CA', 'HIS', 5.67), ('CB', 'HIS', 'N', 'HIS', 6.51)], [('CG', 'HIS', 'CB', 'HIS', 6.86), ('CG', 'HIS', 'CG', 'HIS', 6.98), ('CG', 'HIS', 'ND1', 'HIS', 6.94), ('CG', 'HIS', 'CD2', 'HIS', 7.55), ('CG', 'HIS', 'CE1', 'HIS', 7.49), ('CG', 'HIS', 'NE2', 'HIS', 7.84), ('CG', 'HIS', 'O', 'HIS', 5.16), ('CG', 'HIS', 'C', 'HIS', 4.61), ('CG', 'HIS', 'CA', 'HIS', 5.5), ('CG', 'HIS', 'N', 'HIS', 5.99)], [('ND1', 'HIS', 'CB', 'HIS', 7.5), ('ND1', 'HIS', 'CG', 'HIS', 7.81), ('ND1', 'HIS', 'ND1', 'HIS', 7.99), ('ND1', 'HIS', 'CD2', 'HIS', 8.32), ('ND1', 'HIS', 'CE1', 'HIS', 8.59), ('ND1', 'HIS', 'NE2', 'HIS', 8.78), ('ND1', 'HIS', 'O', 'HIS', 5.35), ('ND1', 'HIS', 'C', 'HIS', 5.13), ('ND1', 'HIS', 'CA', 'HIS', 6.09), ('ND1', 'HIS', 'N', 'HIS', 6.27)], [('CD2', 'HIS', 'CB', 'HIS', 6.84), ('CD2', 'HIS', 'CG', 'HIS', 7.11), ('CD2', 'HIS', 'ND1', 'HIS', 6.93), ('CD2', 'HIS', 'CD2', 'HIS', 7.92), ('CD2', 'HIS', 'CE1', 'HIS', 7.66), ('CD2', 'HIS', 'NE2', 'HIS', 8.22), ('CD2', 'HIS', 'O', 'HIS', 5.74), ('CD2', 'HIS', 'C', 'HIS', 4.96), ('CD2', 'HIS', 'CA', 'HIS', 5.41), ('CD2', 'HIS', 'N', 'HIS', 5.74)], [('CE1', 'HIS', 'CB', 'HIS', 7.83), ('CE1', 'HIS', 'CG', 'HIS', 8.36), ('CE1', 'HIS', 'ND1', 'HIS', 8.53), ('CE1', 'HIS', 'CD2', 'HIS', 9.05), ('CE1', 'HIS', 'CE1', 'HIS', 9.29), ('CE1', 'HIS', 'NE2', 'HIS', 9.59), ('CE1', 'HIS', 'O', 'HIS', 6.0), ('CE1', 'HIS', 'C', 'HIS', 5.69), ('CE1', 'HIS', 'CA', 'HIS', 6.33), ('CE1', 'HIS', 'N', 'HIS', 6.2)], [('NE2', 'HIS', 'CB', 'HIS', 7.48), ('NE2', 'HIS', 'CG', 'HIS', 8.01), ('NE2', 'HIS', 'ND1', 'HIS', 7.99), ('NE2', 'HIS', 'CD2', 'HIS', 8.86), ('NE2', 'HIS', 'CE1', 'HIS', 8.82), ('NE2', 'HIS', 'NE2', 'HIS', 9.32), ('NE2', 'HIS', 'O', 'HIS', 6.22), ('NE2', 'HIS', 'C', 'HIS', 5.62), ('NE2', 'HIS', 'CA', 'HIS', 5.96), ('NE2', 'HIS', 'N', 'HIS', 5.89)], [('O', 'HIS', 'CB', 'HIS', 6.29), ('O', 'HIS', 'CG', 'HIS', 5.31), ('O', 'HIS', 'ND1', 'HIS', 5.12), ('O', 'HIS', 'CD2', 'HIS', 5.01), ('O', 'HIS', 'CE1', 'HIS', 4.67), ('O', 'HIS', 'NE2', 'HIS', 4.58), ('O', 'HIS', 'O', 'HIS', 5.31), ('O', 'HIS', 'C', 'HIS', 4.94), ('O', 'HIS', 'CA', 'HIS', 6.02), ('O', 'HIS', 'N', 'HIS', 7.32)], [('C', 'HIS', 'CB', 'HIS', 6.29), ('C', 'HIS', 'CG', 'HIS', 5.58), ('C', 'HIS', 'ND1', 'HIS', 5.67), ('C', 'HIS', 'CD2', 'HIS', 5.33), ('C', 'HIS', 'CE1', 'HIS', 5.48), ('C', 'HIS', 'NE2', 'HIS', 5.27), ('C', 'HIS', 'O', 'HIS', 4.61), ('C', 'HIS', 'C', 'HIS', 4.47), ('C', 'HIS', 'CA', 'HIS', 5.79), ('C', 'HIS', 'N', 'HIS', 6.94)], [('CA', 'HIS', 'CB', 'HIS', 5.68), ('CA', 'HIS', 'CG', 'HIS', 5.37), ('CA', 'HIS', 'ND1', 'HIS', 5.55), ('CA', 'HIS', 'CD2', 'HIS', 5.53), ('CA', 'HIS', 'CE1', 'HIS', 5.79), ('CA', 'HIS', 'NE2', 'HIS', 5.78), ('CA', 'HIS', 'O', 'HIS', 3.74), ('CA', 'HIS', 'C', 'HIS', 3.43), ('CA', 'HIS', 'CA', 'HIS', 4.8), ('CA', 'HIS', 'N', 'HIS', 5.77)], [('N', 'HIS', 'CB', 'HIS', 4.4), ('N', 'HIS', 'CG', 'HIS', 4.29), ('N', 'HIS', 'ND1', 'HIS', 4.48), ('N', 'HIS', 'CD2', 'HIS', 4.82), ('N', 'HIS', 'CE1', 'HIS', 5.06), ('N', 'HIS', 'NE2', 'HIS', 5.25), ('N', 'HIS', 'O', 'HIS', 3.2), ('N', 'HIS', 'C', 'HIS', 2.32), ('N', 'HIS', 'CA', 'HIS', 3.42), ('N', 'HIS', 'N', 'HIS', 4.51)], [('CB', 'HIS', 'CB', 'HIS', 6.76), ('CB', 'HIS', 'CG', 'HIS', 6.86), ('CB', 'HIS', 'ND1', 'HIS', 7.5), ('CB', 'HIS', 'CD2', 'HIS', 6.84), ('CB', 'HIS', 'CE1', 'HIS', 7.83), ('CB', 'HIS', 'NE2', 'HIS', 7.48), ('CB', 'HIS', 'O', 'HIS', 6.29), ('CB', 'HIS', 'C', 'HIS', 6.29), ('CB', 'HIS', 'CA', 'HIS', 5.68), ('CB', 'HIS', 'N', 'HIS', 4.4)], [('CG', 'HIS', 'CB', 'HIS', 6.52), ('CG', 'HIS', 'CG', 'HIS', 6.98), ('CG', 'HIS', 'ND1', 'HIS', 7.81), ('CG', 'HIS', 'CD2', 'HIS', 7.11), ('CG', 'HIS', 'CE1', 'HIS', 8.36), ('CG', 'HIS', 'NE2', 'HIS', 8.01), ('CG', 'HIS', 'O', 'HIS', 5.31), ('CG', 'HIS', 'C', 'HIS', 5.58), ('CG', 'HIS', 'CA', 'HIS', 5.37), ('CG', 'HIS', 'N', 'HIS', 4.29)], [('ND1', 'HIS', 'CB', 'HIS', 6.41), ('ND1', 'HIS', 'CG', 'HIS', 6.94), ('ND1', 'HIS', 'ND1', 'HIS', 7.99), ('ND1', 'HIS', 'CD2', 'HIS', 6.93), ('ND1', 'HIS', 'CE1', 'HIS', 8.53), ('ND1', 'HIS', 'NE2', 'HIS', 7.99), ('ND1', 'HIS', 'O', 'HIS', 5.12), ('ND1', 'HIS', 'C', 'HIS', 5.67), ('ND1', 'HIS', 'CA', 'HIS', 5.55), ('ND1', 'HIS', 'N', 'HIS', 4.48)], [('CD2', 'HIS', 'CB', 'HIS', 6.84), ('CD2', 'HIS', 'CG', 'HIS', 7.55), ('CD2', 'HIS', 'ND1', 'HIS', 8.32), ('CD2', 'HIS', 'CD2', 'HIS', 7.92), ('CD2', 'HIS', 'CE1', 'HIS', 9.05), ('CD2', 'HIS', 'NE2', 'HIS', 8.86), ('CD2', 'HIS', 'O', 'HIS', 5.01), ('CD2', 'HIS', 'C', 'HIS', 5.33), ('CD2', 'HIS', 'CA', 'HIS', 5.53), ('CD2', 'HIS', 'N', 'HIS', 4.82)], [('CE1', 'HIS', 'CB', 'HIS', 6.67), ('CE1', 'HIS', 'CG', 'HIS', 7.49), ('CE1', 'HIS', 'ND1', 'HIS', 8.59), ('CE1', 'HIS', 'CD2', 'HIS', 7.66), ('CE1', 'HIS', 'CE1', 'HIS', 9.29), ('CE1', 'HIS', 'NE2', 'HIS', 8.82), ('CE1', 'HIS', 'O', 'HIS', 4.67), ('CE1', 'HIS', 'C', 'HIS', 5.48), ('CE1', 'HIS', 'CA', 'HIS', 5.79), ('CE1', 'HIS', 'N', 'HIS', 5.06)], [('NE2', 'HIS', 'CB', 'HIS', 6.92), ('NE2', 'HIS', 'CG', 'HIS', 7.84), ('NE2', 'HIS', 'ND1', 'HIS', 8.78), ('NE2', 'HIS', 'CD2', 'HIS', 8.22), ('NE2', 'HIS', 'CE1', 'HIS', 9.59), ('NE2', 'HIS', 'NE2', 'HIS', 9.32), ('NE2', 'HIS', 'O', 'HIS', 4.58), ('NE2', 'HIS', 'C', 'HIS', 5.27), ('NE2', 'HIS', 'CA', 'HIS', 5.78), ('NE2', 'HIS', 'N', 'HIS', 5.25)], [('O', 'HIS', 'CB', 'HIS', 5.04), ('O', 'HIS', 'CG', 'HIS', 5.16), ('O', 'HIS', 'ND1', 'HIS', 5.35), ('O', 'HIS', 'CD2', 'HIS', 5.74), ('O', 'HIS', 'CE1', 'HIS', 6.0), ('O', 'HIS', 'NE2', 'HIS', 6.22), ('O', 'HIS', 'O', 'HIS', 5.31), ('O', 'HIS', 'C', 'HIS', 4.61), ('O', 'HIS', 'CA', 'HIS', 3.74), ('O', 'HIS', 'N', 'HIS', 3.2)], [('C', 'HIS', 'CB', 'HIS', 4.54), ('C', 'HIS', 'CG', 'HIS', 4.61), ('C', 'HIS', 'ND1', 'HIS', 5.13), ('C', 'HIS', 'CD2', 'HIS', 4.96), ('C', 'HIS', 'CE1', 'HIS', 5.69), ('C', 'HIS', 'NE2', 'HIS', 5.62), ('C', 'HIS', 'O', 'HIS', 4.94), ('C', 'HIS', 'C', 'HIS', 4.47), ('C', 'HIS', 'CA', 'HIS', 3.43), ('C', 'HIS', 'N', 'HIS', 2.32)], [('CA', 'HIS', 'CB', 'HIS', 5.67), ('CA', 'HIS', 'CG', 'HIS', 5.5), ('CA', 'HIS', 'ND1', 'HIS', 6.09), ('CA', 'HIS', 'CD2', 'HIS', 5.41), ('CA', 'HIS', 'CE1', 'HIS', 6.33), ('CA', 'HIS', 'NE2', 'HIS', 5.96), ('CA', 'HIS', 'O', 'HIS', 6.02), ('CA', 'HIS', 'C', 'HIS', 5.79), ('CA', 'HIS', 'CA', 'HIS', 4.8), ('CA', 'HIS', 'N', 'HIS', 3.42)], [('N', 'HIS', 'CB', 'HIS', 6.51), ('N', 'HIS', 'CG', 'HIS', 5.99), ('N', 'HIS', 'ND1', 'HIS', 6.27), ('N', 'HIS', 'CD2', 'HIS', 5.74), ('N', 'HIS', 'CE1', 'HIS', 6.2), ('N', 'HIS', 'NE2', 'HIS', 5.89), ('N', 'HIS', 'O', 'HIS', 7.32), ('N', 'HIS', 'C', 'HIS', 6.94), ('N', 'HIS', 'CA', 'HIS', 5.77), ('N', 'HIS', 'N', 'HIS', 4.51)]]}
HIS_PHE = { 
	'distances':
		[[16.77, 16.33, 15.04, 17.32, 14.82, 17.15, 15.93, 18.82, 17.72, 16.42, 15.23], [17.97, 17.47, 16.15, 18.43, 15.86, 18.2, 16.94, 19.97, 18.9, 17.59, 16.44], [19.16, 18.72, 17.42, 19.72, 17.17, 19.53, 18.28, 21.11, 20.01, 18.74, 17.55], [18.23, 17.63, 16.28, 18.53, 15.88, 18.21, 16.9, 20.25, 19.22, 17.88, 16.8], [20.05, 19.55, 18.21, 20.51, 17.89, 20.25, 18.97, 21.98, 20.91, 19.62, 18.48], [19.56, 18.96, 17.6, 19.87, 17.2, 19.53, 18.22, 21.52, 20.49, 19.16, 18.09], [15.0, 14.58, 13.38, 15.53, 13.21, 15.4, 14.28, 17.31, 16.2, 14.88, 13.66], [16.03, 15.66, 14.46, 16.64, 14.32, 16.54, 15.41, 18.25, 17.12, 15.84, 14.58], [17.09, 16.64, 15.39, 17.59, 15.15, 17.42, 16.22, 19.29, 18.18, 16.87, 15.65], [17.47, 16.9, 15.62, 17.76, 15.25, 17.46, 16.23, 19.78, 18.72, 17.34, 16.2], [18.84, 18.09, 16.86, 18.75, 16.29, 18.27, 17.05, 21.41, 20.43, 18.98, 17.95], [17.49, 16.77, 15.56, 17.43, 15.04, 16.99, 15.81, 20.1, 19.12, 17.67, 16.63], [16.43, 15.64, 14.41, 16.27, 13.83, 15.79, 14.57, 19.03, 18.08, 16.61, 15.63], [17.15, 16.51, 15.36, 17.2, 14.94, 16.84, 15.72, 19.78, 18.77, 17.36, 16.28], [15.37, 14.63, 13.44, 15.28, 12.93, 14.85, 13.69, 18.01, 17.05, 15.6, 14.6], [15.81, 15.17, 14.03, 15.85, 13.62, 15.51, 14.4, 18.46, 17.47, 16.05, 14.99], [19.19, 18.66, 17.42, 19.51, 17.09, 19.23, 18.04, 21.55, 20.47, 19.11, 17.93], [18.53, 17.93, 16.67, 18.75, 16.26, 18.42, 17.19, 20.91, 19.85, 18.46, 17.33], [18.98, 18.26, 16.98, 18.98, 16.45, 18.54, 17.28, 21.43, 20.42, 18.99, 17.93], [20.38, 19.65, 18.35, 20.36, 17.79, 19.89, 18.61, 22.8, 21.8, 20.37, 19.31]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'PHE', 16.77), ('CB', 'HIS', 'CG', 'PHE', 16.33), ('CB', 'HIS', 'CD1', 'PHE', 15.04), ('CB', 'HIS', 'CD2', 'PHE', 17.32), ('CB', 'HIS', 'CE1', 'PHE', 14.82), ('CB', 'HIS', 'CE2', 'PHE', 17.15), ('CB', 'HIS', 'CZ', 'PHE', 15.93), ('CB', 'HIS', 'O', 'PHE', 18.82), ('CB', 'HIS', 'C', 'PHE', 17.72), ('CB', 'HIS', 'CA', 'PHE', 16.42), ('CB', 'HIS', 'N', 'PHE', 15.23)], [('CG', 'HIS', 'CB', 'PHE', 17.97), ('CG', 'HIS', 'CG', 'PHE', 17.47), ('CG', 'HIS', 'CD1', 'PHE', 16.15), ('CG', 'HIS', 'CD2', 'PHE', 18.43), ('CG', 'HIS', 'CE1', 'PHE', 15.86), ('CG', 'HIS', 'CE2', 'PHE', 18.2), ('CG', 'HIS', 'CZ', 'PHE', 16.94), ('CG', 'HIS', 'O', 'PHE', 19.97), ('CG', 'HIS', 'C', 'PHE', 18.9), ('CG', 'HIS', 'CA', 'PHE', 17.59), ('CG', 'HIS', 'N', 'PHE', 16.44)], [('ND1', 'HIS', 'CB', 'PHE', 19.16), ('ND1', 'HIS', 'CG', 'PHE', 18.72), ('ND1', 'HIS', 'CD1', 'PHE', 17.42), ('ND1', 'HIS', 'CD2', 'PHE', 19.72), ('ND1', 'HIS', 'CE1', 'PHE', 17.17), ('ND1', 'HIS', 'CE2', 'PHE', 19.53), ('ND1', 'HIS', 'CZ', 'PHE', 18.28), ('ND1', 'HIS', 'O', 'PHE', 21.11), ('ND1', 'HIS', 'C', 'PHE', 20.01), ('ND1', 'HIS', 'CA', 'PHE', 18.74), ('ND1', 'HIS', 'N', 'PHE', 17.55)], [('CD2', 'HIS', 'CB', 'PHE', 18.23), ('CD2', 'HIS', 'CG', 'PHE', 17.63), ('CD2', 'HIS', 'CD1', 'PHE', 16.28), ('CD2', 'HIS', 'CD2', 'PHE', 18.53), ('CD2', 'HIS', 'CE1', 'PHE', 15.88), ('CD2', 'HIS', 'CE2', 'PHE', 18.21), ('CD2', 'HIS', 'CZ', 'PHE', 16.9), ('CD2', 'HIS', 'O', 'PHE', 20.25), ('CD2', 'HIS', 'C', 'PHE', 19.22), ('CD2', 'HIS', 'CA', 'PHE', 17.88), ('CD2', 'HIS', 'N', 'PHE', 16.8)], [('CE1', 'HIS', 'CB', 'PHE', 20.05), ('CE1', 'HIS', 'CG', 'PHE', 19.55), ('CE1', 'HIS', 'CD1', 'PHE', 18.21), ('CE1', 'HIS', 'CD2', 'PHE', 20.51), ('CE1', 'HIS', 'CE1', 'PHE', 17.89), ('CE1', 'HIS', 'CE2', 'PHE', 20.25), ('CE1', 'HIS', 'CZ', 'PHE', 18.97), ('CE1', 'HIS', 'O', 'PHE', 21.98), ('CE1', 'HIS', 'C', 'PHE', 20.91), ('CE1', 'HIS', 'CA', 'PHE', 19.62), ('CE1', 'HIS', 'N', 'PHE', 18.48)], [('NE2', 'HIS', 'CB', 'PHE', 19.56), ('NE2', 'HIS', 'CG', 'PHE', 18.96), ('NE2', 'HIS', 'CD1', 'PHE', 17.6), ('NE2', 'HIS', 'CD2', 'PHE', 19.87), ('NE2', 'HIS', 'CE1', 'PHE', 17.2), ('NE2', 'HIS', 'CE2', 'PHE', 19.53), ('NE2', 'HIS', 'CZ', 'PHE', 18.22), ('NE2', 'HIS', 'O', 'PHE', 21.52), ('NE2', 'HIS', 'C', 'PHE', 20.49), ('NE2', 'HIS', 'CA', 'PHE', 19.16), ('NE2', 'HIS', 'N', 'PHE', 18.09)], [('O', 'HIS', 'CB', 'PHE', 15.0), ('O', 'HIS', 'CG', 'PHE', 14.58), ('O', 'HIS', 'CD1', 'PHE', 13.38), ('O', 'HIS', 'CD2', 'PHE', 15.53), ('O', 'HIS', 'CE1', 'PHE', 13.21), ('O', 'HIS', 'CE2', 'PHE', 15.4), ('O', 'HIS', 'CZ', 'PHE', 14.28), ('O', 'HIS', 'O', 'PHE', 17.31), ('O', 'HIS', 'C', 'PHE', 16.2), ('O', 'HIS', 'CA', 'PHE', 14.88), ('O', 'HIS', 'N', 'PHE', 13.66)], [('C', 'HIS', 'CB', 'PHE', 16.03), ('C', 'HIS', 'CG', 'PHE', 15.66), ('C', 'HIS', 'CD1', 'PHE', 14.46), ('C', 'HIS', 'CD2', 'PHE', 16.64), ('C', 'HIS', 'CE1', 'PHE', 14.32), ('C', 'HIS', 'CE2', 'PHE', 16.54), ('C', 'HIS', 'CZ', 'PHE', 15.41), ('C', 'HIS', 'O', 'PHE', 18.25), ('C', 'HIS', 'C', 'PHE', 17.12), ('C', 'HIS', 'CA', 'PHE', 15.84), ('C', 'HIS', 'N', 'PHE', 14.58)], [('CA', 'HIS', 'CB', 'PHE', 17.09), ('CA', 'HIS', 'CG', 'PHE', 16.64), ('CA', 'HIS', 'CD1', 'PHE', 15.39), ('CA', 'HIS', 'CD2', 'PHE', 17.59), ('CA', 'HIS', 'CE1', 'PHE', 15.15), ('CA', 'HIS', 'CE2', 'PHE', 17.42), ('CA', 'HIS', 'CZ', 'PHE', 16.22), ('CA', 'HIS', 'O', 'PHE', 19.29), ('CA', 'HIS', 'C', 'PHE', 18.18), ('CA', 'HIS', 'CA', 'PHE', 16.87), ('CA', 'HIS', 'N', 'PHE', 15.65)], [('N', 'HIS', 'CB', 'PHE', 17.47), ('N', 'HIS', 'CG', 'PHE', 16.9), ('N', 'HIS', 'CD1', 'PHE', 15.62), ('N', 'HIS', 'CD2', 'PHE', 17.76), ('N', 'HIS', 'CE1', 'PHE', 15.25), ('N', 'HIS', 'CE2', 'PHE', 17.46), ('N', 'HIS', 'CZ', 'PHE', 16.23), ('N', 'HIS', 'O', 'PHE', 19.78), ('N', 'HIS', 'C', 'PHE', 18.72), ('N', 'HIS', 'CA', 'PHE', 17.34), ('N', 'HIS', 'N', 'PHE', 16.2)], [('CB', 'HIS', 'CB', 'PHE', 18.84), ('CB', 'HIS', 'CG', 'PHE', 18.09), ('CB', 'HIS', 'CD1', 'PHE', 16.86), ('CB', 'HIS', 'CD2', 'PHE', 18.75), ('CB', 'HIS', 'CE1', 'PHE', 16.29), ('CB', 'HIS', 'CE2', 'PHE', 18.27), ('CB', 'HIS', 'CZ', 'PHE', 17.05), ('CB', 'HIS', 'O', 'PHE', 21.41), ('CB', 'HIS', 'C', 'PHE', 20.43), ('CB', 'HIS', 'CA', 'PHE', 18.98), ('CB', 'HIS', 'N', 'PHE', 17.95)], [('CG', 'HIS', 'CB', 'PHE', 17.49), ('CG', 'HIS', 'CG', 'PHE', 16.77), ('CG', 'HIS', 'CD1', 'PHE', 15.56), ('CG', 'HIS', 'CD2', 'PHE', 17.43), ('CG', 'HIS', 'CE1', 'PHE', 15.04), ('CG', 'HIS', 'CE2', 'PHE', 16.99), ('CG', 'HIS', 'CZ', 'PHE', 15.81), ('CG', 'HIS', 'O', 'PHE', 20.1), ('CG', 'HIS', 'C', 'PHE', 19.12), ('CG', 'HIS', 'CA', 'PHE', 17.67), ('CG', 'HIS', 'N', 'PHE', 16.63)], [('ND1', 'HIS', 'CB', 'PHE', 16.43), ('ND1', 'HIS', 'CG', 'PHE', 15.64), ('ND1', 'HIS', 'CD1', 'PHE', 14.41), ('ND1', 'HIS', 'CD2', 'PHE', 16.27), ('ND1', 'HIS', 'CE1', 'PHE', 13.83), ('ND1', 'HIS', 'CE2', 'PHE', 15.79), ('ND1', 'HIS', 'CZ', 'PHE', 14.57), ('ND1', 'HIS', 'O', 'PHE', 19.03), ('ND1', 'HIS', 'C', 'PHE', 18.08), ('ND1', 'HIS', 'CA', 'PHE', 16.61), ('ND1', 'HIS', 'N', 'PHE', 15.63)], [('CD2', 'HIS', 'CB', 'PHE', 17.15), ('CD2', 'HIS', 'CG', 'PHE', 16.51), ('CD2', 'HIS', 'CD1', 'PHE', 15.36), ('CD2', 'HIS', 'CD2', 'PHE', 17.2), ('CD2', 'HIS', 'CE1', 'PHE', 14.94), ('CD2', 'HIS', 'CE2', 'PHE', 16.84), ('CD2', 'HIS', 'CZ', 'PHE', 15.72), ('CD2', 'HIS', 'O', 'PHE', 19.78), ('CD2', 'HIS', 'C', 'PHE', 18.77), ('CD2', 'HIS', 'CA', 'PHE', 17.36), ('CD2', 'HIS', 'N', 'PHE', 16.28)], [('CE1', 'HIS', 'CB', 'PHE', 15.37), ('CE1', 'HIS', 'CG', 'PHE', 14.63), ('CE1', 'HIS', 'CD1', 'PHE', 13.44), ('CE1', 'HIS', 'CD2', 'PHE', 15.28), ('CE1', 'HIS', 'CE1', 'PHE', 12.93), ('CE1', 'HIS', 'CE2', 'PHE', 14.85), ('CE1', 'HIS', 'CZ', 'PHE', 13.69), ('CE1', 'HIS', 'O', 'PHE', 18.01), ('CE1', 'HIS', 'C', 'PHE', 17.05), ('CE1', 'HIS', 'CA', 'PHE', 15.6), ('CE1', 'HIS', 'N', 'PHE', 14.6)], [('NE2', 'HIS', 'CB', 'PHE', 15.81), ('NE2', 'HIS', 'CG', 'PHE', 15.17), ('NE2', 'HIS', 'CD1', 'PHE', 14.03), ('NE2', 'HIS', 'CD2', 'PHE', 15.85), ('NE2', 'HIS', 'CE1', 'PHE', 13.62), ('NE2', 'HIS', 'CE2', 'PHE', 15.51), ('NE2', 'HIS', 'CZ', 'PHE', 14.4), ('NE2', 'HIS', 'O', 'PHE', 18.46), ('NE2', 'HIS', 'C', 'PHE', 17.47), ('NE2', 'HIS', 'CA', 'PHE', 16.05), ('NE2', 'HIS', 'N', 'PHE', 14.99)], [('O', 'HIS', 'CB', 'PHE', 19.19), ('O', 'HIS', 'CG', 'PHE', 18.66), ('O', 'HIS', 'CD1', 'PHE', 17.42), ('O', 'HIS', 'CD2', 'PHE', 19.51), ('O', 'HIS', 'CE1', 'PHE', 17.09), ('O', 'HIS', 'CE2', 'PHE', 19.23), ('O', 'HIS', 'CZ', 'PHE', 18.04), ('O', 'HIS', 'O', 'PHE', 21.55), ('O', 'HIS', 'C', 'PHE', 20.47), ('O', 'HIS', 'CA', 'PHE', 19.11), ('O', 'HIS', 'N', 'PHE', 17.93)], [('C', 'HIS', 'CB', 'PHE', 18.53), ('C', 'HIS', 'CG', 'PHE', 17.93), ('C', 'HIS', 'CD1', 'PHE', 16.67), ('C', 'HIS', 'CD2', 'PHE', 18.75), ('C', 'HIS', 'CE1', 'PHE', 16.26), ('C', 'HIS', 'CE2', 'PHE', 18.42), ('C', 'HIS', 'CZ', 'PHE', 17.19), ('C', 'HIS', 'O', 'PHE', 20.91), ('C', 'HIS', 'C', 'PHE', 19.85), ('C', 'HIS', 'CA', 'PHE', 18.46), ('C', 'HIS', 'N', 'PHE', 17.33)], [('CA', 'HIS', 'CB', 'PHE', 18.98), ('CA', 'HIS', 'CG', 'PHE', 18.26), ('CA', 'HIS', 'CD1', 'PHE', 16.98), ('CA', 'HIS', 'CD2', 'PHE', 18.98), ('CA', 'HIS', 'CE1', 'PHE', 16.45), ('CA', 'HIS', 'CE2', 'PHE', 18.54), ('CA', 'HIS', 'CZ', 'PHE', 17.28), ('CA', 'HIS', 'O', 'PHE', 21.43), ('CA', 'HIS', 'C', 'PHE', 20.42), ('CA', 'HIS', 'CA', 'PHE', 18.99), ('CA', 'HIS', 'N', 'PHE', 17.93)], [('N', 'HIS', 'CB', 'PHE', 20.38), ('N', 'HIS', 'CG', 'PHE', 19.65), ('N', 'HIS', 'CD1', 'PHE', 18.35), ('N', 'HIS', 'CD2', 'PHE', 20.36), ('N', 'HIS', 'CE1', 'PHE', 17.79), ('N', 'HIS', 'CE2', 'PHE', 19.89), ('N', 'HIS', 'CZ', 'PHE', 18.61), ('N', 'HIS', 'O', 'PHE', 22.8), ('N', 'HIS', 'C', 'PHE', 21.8), ('N', 'HIS', 'CA', 'PHE', 20.37), ('N', 'HIS', 'N', 'PHE', 19.31)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_HIS, d, 'P_1brl_1_14_14_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_PHE, d, 'P_1brl_1_14_14_3')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_HIS' :  match1,
		'HIS_PHE' :  match2}