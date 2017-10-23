'''
FUNC:A_5cox_1_14_99_1
PDB:5cox
EC:1.14.99.1
RESI:gln,his,tyr
LOCI:a-203,207,385;
'''
import motifFunctions as cmd
GLN_HIS = { 
	'distances':
		[[7.79, 7.19, 6.7, 7.6, 6.86, 7.4, 10.63, 10.08, 8.77, 8.34], [7.17, 6.35, 6.05, 6.45, 5.99, 6.24, 10.01, 9.65, 8.34, 8.23], [8.29, 7.42, 7.29, 7.21, 7.03, 6.96, 11.03, 10.81, 9.59, 9.62], [8.4, 7.42, 7.44, 6.91, 6.99, 6.63, 11.01, 10.94, 9.77, 10.01], [9.37, 8.63, 8.45, 8.51, 8.25, 8.28, 12.12, 11.86, 10.65, 10.58], [4.87, 4.85, 4.54, 5.96, 5.59, 6.3, 7.54, 6.8, 5.5, 4.98], [6.01, 5.94, 5.57, 6.89, 6.39, 7.11, 8.67, 7.95, 6.72, 6.1], [7.18, 6.73, 6.03, 7.45, 6.47, 7.3, 9.96, 9.24, 7.88, 7.2], [8.32, 8.02, 7.25, 8.85, 7.74, 8.67, 10.95, 10.11, 8.81, 7.89]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'HIS', 7.79), ('CB', 'GLN', 'CG', 'HIS', 7.19), ('CB', 'GLN', 'ND1', 'HIS', 6.7), ('CB', 'GLN', 'CD2', 'HIS', 7.6), ('CB', 'GLN', 'CE1', 'HIS', 6.86), ('CB', 'GLN', 'NE2', 'HIS', 7.4), ('CB', 'GLN', 'O', 'HIS', 10.63), ('CB', 'GLN', 'C', 'HIS', 10.08), ('CB', 'GLN', 'CA', 'HIS', 8.77), ('CB', 'GLN', 'N', 'HIS', 8.34)], [('CG', 'GLN', 'CB', 'HIS', 7.17), ('CG', 'GLN', 'CG', 'HIS', 6.35), ('CG', 'GLN', 'ND1', 'HIS', 6.05), ('CG', 'GLN', 'CD2', 'HIS', 6.45), ('CG', 'GLN', 'CE1', 'HIS', 5.99), ('CG', 'GLN', 'NE2', 'HIS', 6.24), ('CG', 'GLN', 'O', 'HIS', 10.01), ('CG', 'GLN', 'C', 'HIS', 9.65), ('CG', 'GLN', 'CA', 'HIS', 8.34), ('CG', 'GLN', 'N', 'HIS', 8.23)], [('CD', 'GLN', 'CB', 'HIS', 8.29), ('CD', 'GLN', 'CG', 'HIS', 7.42), ('CD', 'GLN', 'ND1', 'HIS', 7.29), ('CD', 'GLN', 'CD2', 'HIS', 7.21), ('CD', 'GLN', 'CE1', 'HIS', 7.03), ('CD', 'GLN', 'NE2', 'HIS', 6.96), ('CD', 'GLN', 'O', 'HIS', 11.03), ('CD', 'GLN', 'C', 'HIS', 10.81), ('CD', 'GLN', 'CA', 'HIS', 9.59), ('CD', 'GLN', 'N', 'HIS', 9.62)], [('OE1', 'GLN', 'CB', 'HIS', 8.4), ('OE1', 'GLN', 'CG', 'HIS', 7.42), ('OE1', 'GLN', 'ND1', 'HIS', 7.44), ('OE1', 'GLN', 'CD2', 'HIS', 6.91), ('OE1', 'GLN', 'CE1', 'HIS', 6.99), ('OE1', 'GLN', 'NE2', 'HIS', 6.63), ('OE1', 'GLN', 'O', 'HIS', 11.01), ('OE1', 'GLN', 'C', 'HIS', 10.94), ('OE1', 'GLN', 'CA', 'HIS', 9.77), ('OE1', 'GLN', 'N', 'HIS', 10.01)], [('NE2', 'GLN', 'CB', 'HIS', 9.37), ('NE2', 'GLN', 'CG', 'HIS', 8.63), ('NE2', 'GLN', 'ND1', 'HIS', 8.45), ('NE2', 'GLN', 'CD2', 'HIS', 8.51), ('NE2', 'GLN', 'CE1', 'HIS', 8.25), ('NE2', 'GLN', 'NE2', 'HIS', 8.28), ('NE2', 'GLN', 'O', 'HIS', 12.12), ('NE2', 'GLN', 'C', 'HIS', 11.86), ('NE2', 'GLN', 'CA', 'HIS', 10.65), ('NE2', 'GLN', 'N', 'HIS', 10.58)], [('O', 'GLN', 'CB', 'HIS', 4.87), ('O', 'GLN', 'CG', 'HIS', 4.85), ('O', 'GLN', 'ND1', 'HIS', 4.54), ('O', 'GLN', 'CD2', 'HIS', 5.96), ('O', 'GLN', 'CE1', 'HIS', 5.59), ('O', 'GLN', 'NE2', 'HIS', 6.3), ('O', 'GLN', 'O', 'HIS', 7.54), ('O', 'GLN', 'C', 'HIS', 6.8), ('O', 'GLN', 'CA', 'HIS', 5.5), ('O', 'GLN', 'N', 'HIS', 4.98)], [('C', 'GLN', 'CB', 'HIS', 6.01), ('C', 'GLN', 'CG', 'HIS', 5.94), ('C', 'GLN', 'ND1', 'HIS', 5.57), ('C', 'GLN', 'CD2', 'HIS', 6.89), ('C', 'GLN', 'CE1', 'HIS', 6.39), ('C', 'GLN', 'NE2', 'HIS', 7.11), ('C', 'GLN', 'O', 'HIS', 8.67), ('C', 'GLN', 'C', 'HIS', 7.95), ('C', 'GLN', 'CA', 'HIS', 6.72), ('C', 'GLN', 'N', 'HIS', 6.1)], [('CA', 'GLN', 'CB', 'HIS', 7.18), ('CA', 'GLN', 'CG', 'HIS', 6.73), ('CA', 'GLN', 'ND1', 'HIS', 6.03), ('CA', 'GLN', 'CD2', 'HIS', 7.45), ('CA', 'GLN', 'CE1', 'HIS', 6.47), ('CA', 'GLN', 'NE2', 'HIS', 7.3), ('CA', 'GLN', 'O', 'HIS', 9.96), ('CA', 'GLN', 'C', 'HIS', 9.24), ('CA', 'GLN', 'CA', 'HIS', 7.88), ('CA', 'GLN', 'N', 'HIS', 7.2)], [('N', 'GLN', 'CB', 'HIS', 8.32), ('N', 'GLN', 'CG', 'HIS', 8.02), ('N', 'GLN', 'ND1', 'HIS', 7.25), ('N', 'GLN', 'CD2', 'HIS', 8.85), ('N', 'GLN', 'CE1', 'HIS', 7.74), ('N', 'GLN', 'NE2', 'HIS', 8.67), ('N', 'GLN', 'O', 'HIS', 10.95), ('N', 'GLN', 'C', 'HIS', 10.11), ('N', 'GLN', 'CA', 'HIS', 8.81), ('N', 'GLN', 'N', 'HIS', 7.89)]]}
HIS_TYR = { 
	'distances':
		[[11.79, 11.72, 11.08, 12.52, 11.3, 12.73, 12.14, 12.61, 11.5, 12.43, 12.88, 13.91], [11.0, 11.08, 10.44, 12.02, 10.83, 12.37, 11.81, 12.43, 10.42, 11.36, 11.96, 12.98], [9.73, 9.79, 9.11, 10.78, 9.54, 11.15, 10.58, 11.25, 9.1, 10.07, 10.66, 11.74], [11.43, 11.7, 11.12, 12.74, 11.66, 13.21, 12.71, 13.43, 10.6, 11.51, 12.26, 13.22], [9.43, 9.7, 9.08, 10.82, 9.71, 11.35, 10.84, 11.66, 8.45, 9.41, 10.19, 11.22], [10.52, 10.9, 10.34, 12.03, 11.01, 12.61, 12.14, 12.97, 9.46, 10.36, 11.22, 12.17], [13.25, 13.24, 12.84, 13.82, 13.06, 14.03, 13.66, 14.08, 13.5, 14.25, 14.5, 15.34], [12.37, 12.25, 11.83, 12.78, 11.96, 12.92, 12.52, 12.89, 12.74, 13.5, 13.66, 14.55], [11.21, 11.09, 10.58, 11.74, 10.76, 11.91, 11.44, 11.89, 11.37, 12.19, 12.44, 13.4], [10.41, 10.1, 9.5, 10.68, 9.53, 10.72, 10.16, 10.52, 10.7, 11.54, 11.68, 12.72]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'TYR', 11.79), ('CB', 'HIS', 'CG', 'TYR', 11.72), ('CB', 'HIS', 'CD1', 'TYR', 11.08), ('CB', 'HIS', 'CD2', 'TYR', 12.52), ('CB', 'HIS', 'CE1', 'TYR', 11.3), ('CB', 'HIS', 'CE2', 'TYR', 12.73), ('CB', 'HIS', 'CZ', 'TYR', 12.14), ('CB', 'HIS', 'OH', 'TYR', 12.61), ('CB', 'HIS', 'O', 'TYR', 11.5), ('CB', 'HIS', 'C', 'TYR', 12.43), ('CB', 'HIS', 'CA', 'TYR', 12.88), ('CB', 'HIS', 'N', 'TYR', 13.91)], [('CG', 'HIS', 'CB', 'TYR', 11.0), ('CG', 'HIS', 'CG', 'TYR', 11.08), ('CG', 'HIS', 'CD1', 'TYR', 10.44), ('CG', 'HIS', 'CD2', 'TYR', 12.02), ('CG', 'HIS', 'CE1', 'TYR', 10.83), ('CG', 'HIS', 'CE2', 'TYR', 12.37), ('CG', 'HIS', 'CZ', 'TYR', 11.81), ('CG', 'HIS', 'OH', 'TYR', 12.43), ('CG', 'HIS', 'O', 'TYR', 10.42), ('CG', 'HIS', 'C', 'TYR', 11.36), ('CG', 'HIS', 'CA', 'TYR', 11.96), ('CG', 'HIS', 'N', 'TYR', 12.98)], [('ND1', 'HIS', 'CB', 'TYR', 9.73), ('ND1', 'HIS', 'CG', 'TYR', 9.79), ('ND1', 'HIS', 'CD1', 'TYR', 9.11), ('ND1', 'HIS', 'CD2', 'TYR', 10.78), ('ND1', 'HIS', 'CE1', 'TYR', 9.54), ('ND1', 'HIS', 'CE2', 'TYR', 11.15), ('ND1', 'HIS', 'CZ', 'TYR', 10.58), ('ND1', 'HIS', 'OH', 'TYR', 11.25), ('ND1', 'HIS', 'O', 'TYR', 9.1), ('ND1', 'HIS', 'C', 'TYR', 10.07), ('ND1', 'HIS', 'CA', 'TYR', 10.66), ('ND1', 'HIS', 'N', 'TYR', 11.74)], [('CD2', 'HIS', 'CB', 'TYR', 11.43), ('CD2', 'HIS', 'CG', 'TYR', 11.7), ('CD2', 'HIS', 'CD1', 'TYR', 11.12), ('CD2', 'HIS', 'CD2', 'TYR', 12.74), ('CD2', 'HIS', 'CE1', 'TYR', 11.66), ('CD2', 'HIS', 'CE2', 'TYR', 13.21), ('CD2', 'HIS', 'CZ', 'TYR', 12.71), ('CD2', 'HIS', 'OH', 'TYR', 13.43), ('CD2', 'HIS', 'O', 'TYR', 10.6), ('CD2', 'HIS', 'C', 'TYR', 11.51), ('CD2', 'HIS', 'CA', 'TYR', 12.26), ('CD2', 'HIS', 'N', 'TYR', 13.22)], [('CE1', 'HIS', 'CB', 'TYR', 9.43), ('CE1', 'HIS', 'CG', 'TYR', 9.7), ('CE1', 'HIS', 'CD1', 'TYR', 9.08), ('CE1', 'HIS', 'CD2', 'TYR', 10.82), ('CE1', 'HIS', 'CE1', 'TYR', 9.71), ('CE1', 'HIS', 'CE2', 'TYR', 11.35), ('CE1', 'HIS', 'CZ', 'TYR', 10.84), ('CE1', 'HIS', 'OH', 'TYR', 11.66), ('CE1', 'HIS', 'O', 'TYR', 8.45), ('CE1', 'HIS', 'C', 'TYR', 9.41), ('CE1', 'HIS', 'CA', 'TYR', 10.19), ('CE1', 'HIS', 'N', 'TYR', 11.22)], [('NE2', 'HIS', 'CB', 'TYR', 10.52), ('NE2', 'HIS', 'CG', 'TYR', 10.9), ('NE2', 'HIS', 'CD1', 'TYR', 10.34), ('NE2', 'HIS', 'CD2', 'TYR', 12.03), ('NE2', 'HIS', 'CE1', 'TYR', 11.01), ('NE2', 'HIS', 'CE2', 'TYR', 12.61), ('NE2', 'HIS', 'CZ', 'TYR', 12.14), ('NE2', 'HIS', 'OH', 'TYR', 12.97), ('NE2', 'HIS', 'O', 'TYR', 9.46), ('NE2', 'HIS', 'C', 'TYR', 10.36), ('NE2', 'HIS', 'CA', 'TYR', 11.22), ('NE2', 'HIS', 'N', 'TYR', 12.17)], [('O', 'HIS', 'CB', 'TYR', 13.25), ('O', 'HIS', 'CG', 'TYR', 13.24), ('O', 'HIS', 'CD1', 'TYR', 12.84), ('O', 'HIS', 'CD2', 'TYR', 13.82), ('O', 'HIS', 'CE1', 'TYR', 13.06), ('O', 'HIS', 'CE2', 'TYR', 14.03), ('O', 'HIS', 'CZ', 'TYR', 13.66), ('O', 'HIS', 'OH', 'TYR', 14.08), ('O', 'HIS', 'O', 'TYR', 13.5), ('O', 'HIS', 'C', 'TYR', 14.25), ('O', 'HIS', 'CA', 'TYR', 14.5), ('O', 'HIS', 'N', 'TYR', 15.34)], [('C', 'HIS', 'CB', 'TYR', 12.37), ('C', 'HIS', 'CG', 'TYR', 12.25), ('C', 'HIS', 'CD1', 'TYR', 11.83), ('C', 'HIS', 'CD2', 'TYR', 12.78), ('C', 'HIS', 'CE1', 'TYR', 11.96), ('C', 'HIS', 'CE2', 'TYR', 12.92), ('C', 'HIS', 'CZ', 'TYR', 12.52), ('C', 'HIS', 'OH', 'TYR', 12.89), ('C', 'HIS', 'O', 'TYR', 12.74), ('C', 'HIS', 'C', 'TYR', 13.5), ('C', 'HIS', 'CA', 'TYR', 13.66), ('C', 'HIS', 'N', 'TYR', 14.55)], [('CA', 'HIS', 'CB', 'TYR', 11.21), ('CA', 'HIS', 'CG', 'TYR', 11.09), ('CA', 'HIS', 'CD1', 'TYR', 10.58), ('CA', 'HIS', 'CD2', 'TYR', 11.74), ('CA', 'HIS', 'CE1', 'TYR', 10.76), ('CA', 'HIS', 'CE2', 'TYR', 11.91), ('CA', 'HIS', 'CZ', 'TYR', 11.44), ('CA', 'HIS', 'OH', 'TYR', 11.89), ('CA', 'HIS', 'O', 'TYR', 11.37), ('CA', 'HIS', 'C', 'TYR', 12.19), ('CA', 'HIS', 'CA', 'TYR', 12.44), ('CA', 'HIS', 'N', 'TYR', 13.4)], [('N', 'HIS', 'CB', 'TYR', 10.41), ('N', 'HIS', 'CG', 'TYR', 10.1), ('N', 'HIS', 'CD1', 'TYR', 9.5), ('N', 'HIS', 'CD2', 'TYR', 10.68), ('N', 'HIS', 'CE1', 'TYR', 9.53), ('N', 'HIS', 'CE2', 'TYR', 10.72), ('N', 'HIS', 'CZ', 'TYR', 10.16), ('N', 'HIS', 'OH', 'TYR', 10.52), ('N', 'HIS', 'O', 'TYR', 10.7), ('N', 'HIS', 'C', 'TYR', 11.54), ('N', 'HIS', 'CA', 'TYR', 11.68), ('N', 'HIS', 'N', 'TYR', 12.72)]]}
GLN_TYR = { 
	'distances':
		[[11.83, 11.5, 10.32, 12.55, 10.31, 12.57, 11.52, 11.84, 10.33, 11.55, 12.35, 13.71], [11.93, 11.82, 10.75, 12.95, 10.96, 13.13, 12.2, 12.68, 10.34, 11.53, 12.45, 13.72], [13.06, 13.04, 11.99, 14.22, 12.25, 14.46, 13.53, 14.03, 11.22, 12.39, 13.44, 14.68], [13.38, 13.51, 12.55, 14.74, 12.95, 15.09, 14.25, 14.84, 11.49, 12.61, 13.73, 14.89], [13.83, 13.71, 12.58, 14.87, 12.73, 15.02, 14.01, 14.41, 11.9, 13.1, 14.14, 15.42], [10.9, 10.55, 9.58, 11.4, 9.56, 11.4, 10.53, 10.85, 10.3, 11.39, 11.86, 13.11], [11.35, 10.88, 9.78, 11.74, 9.64, 11.65, 10.64, 10.86, 10.54, 11.68, 12.2, 13.52], [10.81, 10.36, 9.17, 11.32, 9.06, 11.26, 10.2, 10.48, 9.66, 10.86, 11.48, 12.85], [10.92, 10.24, 8.96, 11.09, 8.6, 10.84, 9.65, 9.73, 9.89, 11.07, 11.56, 12.98]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'TYR', 11.83), ('CB', 'GLN', 'CG', 'TYR', 11.5), ('CB', 'GLN', 'CD1', 'TYR', 10.32), ('CB', 'GLN', 'CD2', 'TYR', 12.55), ('CB', 'GLN', 'CE1', 'TYR', 10.31), ('CB', 'GLN', 'CE2', 'TYR', 12.57), ('CB', 'GLN', 'CZ', 'TYR', 11.52), ('CB', 'GLN', 'OH', 'TYR', 11.84), ('CB', 'GLN', 'O', 'TYR', 10.33), ('CB', 'GLN', 'C', 'TYR', 11.55), ('CB', 'GLN', 'CA', 'TYR', 12.35), ('CB', 'GLN', 'N', 'TYR', 13.71)], [('CG', 'GLN', 'CB', 'TYR', 11.93), ('CG', 'GLN', 'CG', 'TYR', 11.82), ('CG', 'GLN', 'CD1', 'TYR', 10.75), ('CG', 'GLN', 'CD2', 'TYR', 12.95), ('CG', 'GLN', 'CE1', 'TYR', 10.96), ('CG', 'GLN', 'CE2', 'TYR', 13.13), ('CG', 'GLN', 'CZ', 'TYR', 12.2), ('CG', 'GLN', 'OH', 'TYR', 12.68), ('CG', 'GLN', 'O', 'TYR', 10.34), ('CG', 'GLN', 'C', 'TYR', 11.53), ('CG', 'GLN', 'CA', 'TYR', 12.45), ('CG', 'GLN', 'N', 'TYR', 13.72)], [('CD', 'GLN', 'CB', 'TYR', 13.06), ('CD', 'GLN', 'CG', 'TYR', 13.04), ('CD', 'GLN', 'CD1', 'TYR', 11.99), ('CD', 'GLN', 'CD2', 'TYR', 14.22), ('CD', 'GLN', 'CE1', 'TYR', 12.25), ('CD', 'GLN', 'CE2', 'TYR', 14.46), ('CD', 'GLN', 'CZ', 'TYR', 13.53), ('CD', 'GLN', 'OH', 'TYR', 14.03), ('CD', 'GLN', 'O', 'TYR', 11.22), ('CD', 'GLN', 'C', 'TYR', 12.39), ('CD', 'GLN', 'CA', 'TYR', 13.44), ('CD', 'GLN', 'N', 'TYR', 14.68)], [('OE1', 'GLN', 'CB', 'TYR', 13.38), ('OE1', 'GLN', 'CG', 'TYR', 13.51), ('OE1', 'GLN', 'CD1', 'TYR', 12.55), ('OE1', 'GLN', 'CD2', 'TYR', 14.74), ('OE1', 'GLN', 'CE1', 'TYR', 12.95), ('OE1', 'GLN', 'CE2', 'TYR', 15.09), ('OE1', 'GLN', 'CZ', 'TYR', 14.25), ('OE1', 'GLN', 'OH', 'TYR', 14.84), ('OE1', 'GLN', 'O', 'TYR', 11.49), ('OE1', 'GLN', 'C', 'TYR', 12.61), ('OE1', 'GLN', 'CA', 'TYR', 13.73), ('OE1', 'GLN', 'N', 'TYR', 14.89)], [('NE2', 'GLN', 'CB', 'TYR', 13.83), ('NE2', 'GLN', 'CG', 'TYR', 13.71), ('NE2', 'GLN', 'CD1', 'TYR', 12.58), ('NE2', 'GLN', 'CD2', 'TYR', 14.87), ('NE2', 'GLN', 'CE1', 'TYR', 12.73), ('NE2', 'GLN', 'CE2', 'TYR', 15.02), ('NE2', 'GLN', 'CZ', 'TYR', 14.01), ('NE2', 'GLN', 'OH', 'TYR', 14.41), ('NE2', 'GLN', 'O', 'TYR', 11.9), ('NE2', 'GLN', 'C', 'TYR', 13.1), ('NE2', 'GLN', 'CA', 'TYR', 14.14), ('NE2', 'GLN', 'N', 'TYR', 15.42)], [('O', 'GLN', 'CB', 'TYR', 10.9), ('O', 'GLN', 'CG', 'TYR', 10.55), ('O', 'GLN', 'CD1', 'TYR', 9.58), ('O', 'GLN', 'CD2', 'TYR', 11.4), ('O', 'GLN', 'CE1', 'TYR', 9.56), ('O', 'GLN', 'CE2', 'TYR', 11.4), ('O', 'GLN', 'CZ', 'TYR', 10.53), ('O', 'GLN', 'OH', 'TYR', 10.85), ('O', 'GLN', 'O', 'TYR', 10.3), ('O', 'GLN', 'C', 'TYR', 11.39), ('O', 'GLN', 'CA', 'TYR', 11.86), ('O', 'GLN', 'N', 'TYR', 13.11)], [('C', 'GLN', 'CB', 'TYR', 11.35), ('C', 'GLN', 'CG', 'TYR', 10.88), ('C', 'GLN', 'CD1', 'TYR', 9.78), ('C', 'GLN', 'CD2', 'TYR', 11.74), ('C', 'GLN', 'CE1', 'TYR', 9.64), ('C', 'GLN', 'CE2', 'TYR', 11.65), ('C', 'GLN', 'CZ', 'TYR', 10.64), ('C', 'GLN', 'OH', 'TYR', 10.86), ('C', 'GLN', 'O', 'TYR', 10.54), ('C', 'GLN', 'C', 'TYR', 11.68), ('C', 'GLN', 'CA', 'TYR', 12.2), ('C', 'GLN', 'N', 'TYR', 13.52)], [('CA', 'GLN', 'CB', 'TYR', 10.81), ('CA', 'GLN', 'CG', 'TYR', 10.36), ('CA', 'GLN', 'CD1', 'TYR', 9.17), ('CA', 'GLN', 'CD2', 'TYR', 11.32), ('CA', 'GLN', 'CE1', 'TYR', 9.06), ('CA', 'GLN', 'CE2', 'TYR', 11.26), ('CA', 'GLN', 'CZ', 'TYR', 10.2), ('CA', 'GLN', 'OH', 'TYR', 10.48), ('CA', 'GLN', 'O', 'TYR', 9.66), ('CA', 'GLN', 'C', 'TYR', 10.86), ('CA', 'GLN', 'CA', 'TYR', 11.48), ('CA', 'GLN', 'N', 'TYR', 12.85)], [('N', 'GLN', 'CB', 'TYR', 10.92), ('N', 'GLN', 'CG', 'TYR', 10.24), ('N', 'GLN', 'CD1', 'TYR', 8.96), ('N', 'GLN', 'CD2', 'TYR', 11.09), ('N', 'GLN', 'CE1', 'TYR', 8.6), ('N', 'GLN', 'CE2', 'TYR', 10.84), ('N', 'GLN', 'CZ', 'TYR', 9.65), ('N', 'GLN', 'OH', 'TYR', 9.73), ('N', 'GLN', 'O', 'TYR', 9.89), ('N', 'GLN', 'C', 'TYR', 11.07), ('N', 'GLN', 'CA', 'TYR', 11.56), ('N', 'GLN', 'N', 'TYR', 12.98)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLN_HIS, d, 'A_5cox_1_14_99_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_TYR, d, 'A_5cox_1_14_99_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLN_TYR, d, 'A_5cox_1_14_99_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLN_HIS' :  match1,
		'HIS_TYR' :  match2,
		'GLN_TYR' :  match3}