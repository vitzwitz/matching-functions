'''
FUNC:A_1ci8_3_1_1_1
PDB:1ci8
EC:3.1.1.1
RESI:ser,lys,tyr,trp,val
LOCI:a-75,78,181,348,351;
'''
import motifFunctions as cmd
SER_TYR = { 
	'distances':
		[[10.87, 9.35, 8.79, 8.7, 7.44, 7.32, 6.57, 5.21], [10.11, 8.62, 8.19, 7.89, 6.92, 6.54, 5.93, 4.67], [12.79, 11.31, 10.42, 10.96, 9.03, 9.68, 8.61, 7.36], [13.11, 11.61, 10.85, 11.09, 9.46, 9.75, 8.83, 7.5], [12.29, 10.78, 10.17, 10.15, 8.8, 8.78, 8.0, 6.65], [13.03, 11.54, 11.09, 10.74, 9.78, 9.36, 8.81, 7.49]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'TYR', 10.87), ('CB', 'SER', 'CG', 'TYR', 9.35), ('CB', 'SER', 'CD1', 'TYR', 8.79), ('CB', 'SER', 'CD2', 'TYR', 8.7), ('CB', 'SER', 'CE1', 'TYR', 7.44), ('CB', 'SER', 'CE2', 'TYR', 7.32), ('CB', 'SER', 'CZ', 'TYR', 6.57), ('CB', 'SER', 'OH', 'TYR', 5.21)], [('OG', 'SER', 'CB', 'TYR', 10.11), ('OG', 'SER', 'CG', 'TYR', 8.62), ('OG', 'SER', 'CD1', 'TYR', 8.19), ('OG', 'SER', 'CD2', 'TYR', 7.89), ('OG', 'SER', 'CE1', 'TYR', 6.92), ('OG', 'SER', 'CE2', 'TYR', 6.54), ('OG', 'SER', 'CZ', 'TYR', 5.93), ('OG', 'SER', 'OH', 'TYR', 4.67)], [('O', 'SER', 'CB', 'TYR', 12.79), ('O', 'SER', 'CG', 'TYR', 11.31), ('O', 'SER', 'CD1', 'TYR', 10.42), ('O', 'SER', 'CD2', 'TYR', 10.96), ('O', 'SER', 'CE1', 'TYR', 9.03), ('O', 'SER', 'CE2', 'TYR', 9.68), ('O', 'SER', 'CZ', 'TYR', 8.61), ('O', 'SER', 'OH', 'TYR', 7.36)], [('C', 'SER', 'CB', 'TYR', 13.11), ('C', 'SER', 'CG', 'TYR', 11.61), ('C', 'SER', 'CD1', 'TYR', 10.85), ('C', 'SER', 'CD2', 'TYR', 11.09), ('C', 'SER', 'CE1', 'TYR', 9.46), ('C', 'SER', 'CE2', 'TYR', 9.75), ('C', 'SER', 'CZ', 'TYR', 8.83), ('C', 'SER', 'OH', 'TYR', 7.5)], [('CA', 'SER', 'CB', 'TYR', 12.29), ('CA', 'SER', 'CG', 'TYR', 10.78), ('CA', 'SER', 'CD1', 'TYR', 10.17), ('CA', 'SER', 'CD2', 'TYR', 10.15), ('CA', 'SER', 'CE1', 'TYR', 8.8), ('CA', 'SER', 'CE2', 'TYR', 8.78), ('CA', 'SER', 'CZ', 'TYR', 8.0), ('CA', 'SER', 'OH', 'TYR', 6.65)], [('N', 'SER', 'CB', 'TYR', 13.03), ('N', 'SER', 'CG', 'TYR', 11.54), ('N', 'SER', 'CD1', 'TYR', 11.09), ('N', 'SER', 'CD2', 'TYR', 10.74), ('N', 'SER', 'CE1', 'TYR', 9.78), ('N', 'SER', 'CE2', 'TYR', 9.36), ('N', 'SER', 'CZ', 'TYR', 8.81), ('N', 'SER', 'OH', 'TYR', 7.49)]]}
TRP_TYR = { 
	'distances':
		[[12.12, 10.95, 10.15, 10.88, 9.2, 10.02, 9.14, 8.56], [10.66, 9.47, 8.68, 9.4, 7.73, 8.56, 7.68, 7.19], [10.19, 8.86, 8.05, 8.69, 6.92, 7.7, 6.72, 6.03], [9.66, 8.6, 7.92, 8.61, 7.2, 7.99, 7.26, 7.11], [8.84, 7.5, 6.76, 7.33, 5.67, 6.39, 5.45, 4.98], [8.43, 7.27, 6.63, 7.24, 5.88, 6.59, 5.87, 5.84], [9.88, 9.04, 8.47, 9.17, 8.02, 8.78, 8.2, 8.26], [7.25, 6.27, 5.84, 6.34, 5.48, 6.03, 5.59, 6.04], [8.96, 8.31, 7.91, 8.53, 7.75, 8.4, 8.01, 8.37], [7.6, 6.93, 6.65, 7.15, 6.59, 7.12, 6.85, 7.4]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'TYR', 12.12), ('CB', 'TRP', 'CG', 'TYR', 10.95), ('CB', 'TRP', 'CD1', 'TYR', 10.15), ('CB', 'TRP', 'CD2', 'TYR', 10.88), ('CB', 'TRP', 'CE1', 'TYR', 9.2), ('CB', 'TRP', 'CE2', 'TYR', 10.02), ('CB', 'TRP', 'CZ', 'TYR', 9.14), ('CB', 'TRP', 'OH', 'TYR', 8.56)], [('CG', 'TRP', 'CB', 'TYR', 10.66), ('CG', 'TRP', 'CG', 'TYR', 9.47), ('CG', 'TRP', 'CD1', 'TYR', 8.68), ('CG', 'TRP', 'CD2', 'TYR', 9.4), ('CG', 'TRP', 'CE1', 'TYR', 7.73), ('CG', 'TRP', 'CE2', 'TYR', 8.56), ('CG', 'TRP', 'CZ', 'TYR', 7.68), ('CG', 'TRP', 'OH', 'TYR', 7.19)], [('CD1', 'TRP', 'CB', 'TYR', 10.19), ('CD1', 'TRP', 'CG', 'TYR', 8.86), ('CD1', 'TRP', 'CD1', 'TYR', 8.05), ('CD1', 'TRP', 'CD2', 'TYR', 8.69), ('CD1', 'TRP', 'CE1', 'TYR', 6.92), ('CD1', 'TRP', 'CE2', 'TYR', 7.7), ('CD1', 'TRP', 'CZ', 'TYR', 6.72), ('CD1', 'TRP', 'OH', 'TYR', 6.03)], [('CD2', 'TRP', 'CB', 'TYR', 9.66), ('CD2', 'TRP', 'CG', 'TYR', 8.6), ('CD2', 'TRP', 'CD1', 'TYR', 7.92), ('CD2', 'TRP', 'CD2', 'TYR', 8.61), ('CD2', 'TRP', 'CE1', 'TYR', 7.2), ('CD2', 'TRP', 'CE2', 'TYR', 7.99), ('CD2', 'TRP', 'CZ', 'TYR', 7.26), ('CD2', 'TRP', 'OH', 'TYR', 7.11)], [('NE1', 'TRP', 'CB', 'TYR', 8.84), ('NE1', 'TRP', 'CG', 'TYR', 7.5), ('NE1', 'TRP', 'CD1', 'TYR', 6.76), ('NE1', 'TRP', 'CD2', 'TYR', 7.33), ('NE1', 'TRP', 'CE1', 'TYR', 5.67), ('NE1', 'TRP', 'CE2', 'TYR', 6.39), ('NE1', 'TRP', 'CZ', 'TYR', 5.45), ('NE1', 'TRP', 'OH', 'TYR', 4.98)], [('CE2', 'TRP', 'CB', 'TYR', 8.43), ('CE2', 'TRP', 'CG', 'TYR', 7.27), ('CE2', 'TRP', 'CD1', 'TYR', 6.63), ('CE2', 'TRP', 'CD2', 'TYR', 7.24), ('CE2', 'TRP', 'CE1', 'TYR', 5.88), ('CE2', 'TRP', 'CE2', 'TYR', 6.59), ('CE2', 'TRP', 'CZ', 'TYR', 5.87), ('CE2', 'TRP', 'OH', 'TYR', 5.84)], [('CE3', 'TRP', 'CB', 'TYR', 9.88), ('CE3', 'TRP', 'CG', 'TYR', 9.04), ('CE3', 'TRP', 'CD1', 'TYR', 8.47), ('CE3', 'TRP', 'CD2', 'TYR', 9.17), ('CE3', 'TRP', 'CE1', 'TYR', 8.02), ('CE3', 'TRP', 'CE2', 'TYR', 8.78), ('CE3', 'TRP', 'CZ', 'TYR', 8.2), ('CE3', 'TRP', 'OH', 'TYR', 8.26)], [('CZ2', 'TRP', 'CB', 'TYR', 7.25), ('CZ2', 'TRP', 'CG', 'TYR', 6.27), ('CZ2', 'TRP', 'CD1', 'TYR', 5.84), ('CZ2', 'TRP', 'CD2', 'TYR', 6.34), ('CZ2', 'TRP', 'CE1', 'TYR', 5.48), ('CZ2', 'TRP', 'CE2', 'TYR', 6.03), ('CZ2', 'TRP', 'CZ', 'TYR', 5.59), ('CZ2', 'TRP', 'OH', 'TYR', 6.04)], [('CZ3', 'TRP', 'CB', 'TYR', 8.96), ('CZ3', 'TRP', 'CG', 'TYR', 8.31), ('CZ3', 'TRP', 'CD1', 'TYR', 7.91), ('CZ3', 'TRP', 'CD2', 'TYR', 8.53), ('CZ3', 'TRP', 'CE1', 'TYR', 7.75), ('CZ3', 'TRP', 'CE2', 'TYR', 8.4), ('CZ3', 'TRP', 'CZ', 'TYR', 8.01), ('CZ3', 'TRP', 'OH', 'TYR', 8.37)], [('CH2', 'TRP', 'CB', 'TYR', 7.6), ('CH2', 'TRP', 'CG', 'TYR', 6.93), ('CH2', 'TRP', 'CD1', 'TYR', 6.65), ('CH2', 'TRP', 'CD2', 'TYR', 7.15), ('CH2', 'TRP', 'CE1', 'TYR', 6.59), ('CH2', 'TRP', 'CE2', 'TYR', 7.12), ('CH2', 'TRP', 'CZ', 'TYR', 6.85), ('CH2', 'TRP', 'OH', 'TYR', 7.4)]]}
SER_VAL = { 
	'distances':
		[[8.88, 8.39, 8.56, 11.03, 9.87, 8.74, 7.44], [8.52, 7.89, 8.08, 11.01, 9.91, 8.7, 7.59], [11.34, 11.06, 10.97, 13.0, 11.78, 10.9, 9.47], [10.39, 10.26, 9.95, 11.95, 10.72, 9.93, 8.5], [9.26, 9.07, 8.71, 11.13, 9.9, 9.01, 7.67], [8.25, 8.31, 7.57, 9.95, 8.72, 7.98, 6.7]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'VAL', 8.88), ('CB', 'SER', 'CG1', 'VAL', 8.39), ('CB', 'SER', 'CG2', 'VAL', 8.56), ('CB', 'SER', 'O', 'VAL', 11.03), ('CB', 'SER', 'C', 'VAL', 9.87), ('CB', 'SER', 'CA', 'VAL', 8.74), ('CB', 'SER', 'N', 'VAL', 7.44)], [('OG', 'SER', 'CB', 'VAL', 8.52), ('OG', 'SER', 'CG1', 'VAL', 7.89), ('OG', 'SER', 'CG2', 'VAL', 8.08), ('OG', 'SER', 'O', 'VAL', 11.01), ('OG', 'SER', 'C', 'VAL', 9.91), ('OG', 'SER', 'CA', 'VAL', 8.7), ('OG', 'SER', 'N', 'VAL', 7.59)], [('O', 'SER', 'CB', 'VAL', 11.34), ('O', 'SER', 'CG1', 'VAL', 11.06), ('O', 'SER', 'CG2', 'VAL', 10.97), ('O', 'SER', 'O', 'VAL', 13.0), ('O', 'SER', 'C', 'VAL', 11.78), ('O', 'SER', 'CA', 'VAL', 10.9), ('O', 'SER', 'N', 'VAL', 9.47)], [('C', 'SER', 'CB', 'VAL', 10.39), ('C', 'SER', 'CG1', 'VAL', 10.26), ('C', 'SER', 'CG2', 'VAL', 9.95), ('C', 'SER', 'O', 'VAL', 11.95), ('C', 'SER', 'C', 'VAL', 10.72), ('C', 'SER', 'CA', 'VAL', 9.93), ('C', 'SER', 'N', 'VAL', 8.5)], [('CA', 'SER', 'CB', 'VAL', 9.26), ('CA', 'SER', 'CG1', 'VAL', 9.07), ('CA', 'SER', 'CG2', 'VAL', 8.71), ('CA', 'SER', 'O', 'VAL', 11.13), ('CA', 'SER', 'C', 'VAL', 9.9), ('CA', 'SER', 'CA', 'VAL', 9.01), ('CA', 'SER', 'N', 'VAL', 7.67)], [('N', 'SER', 'CB', 'VAL', 8.25), ('N', 'SER', 'CG1', 'VAL', 8.31), ('N', 'SER', 'CG2', 'VAL', 7.57), ('N', 'SER', 'O', 'VAL', 9.95), ('N', 'SER', 'C', 'VAL', 8.72), ('N', 'SER', 'CA', 'VAL', 7.98), ('N', 'SER', 'N', 'VAL', 6.7)]]}
LYS_VAL = { 
	'distances':
		[[13.89, 13.36, 13.39, 15.99, 14.78, 13.76, 12.41], [13.04, 12.46, 12.47, 15.35, 14.17, 13.09, 11.83], [12.77, 11.99, 12.34, 15.24, 14.11, 12.9, 11.69], [12.3, 11.46, 11.81, 14.97, 13.89, 12.64, 11.57], [10.86, 10.06, 10.33, 13.57, 12.51, 11.27, 10.26]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'VAL', 13.89), ('CB', 'LYS', 'CG1', 'VAL', 13.36), ('CB', 'LYS', 'CG2', 'VAL', 13.39), ('CB', 'LYS', 'O', 'VAL', 15.99), ('CB', 'LYS', 'C', 'VAL', 14.78), ('CB', 'LYS', 'CA', 'VAL', 13.76), ('CB', 'LYS', 'N', 'VAL', 12.41)], [('CG', 'LYS', 'CB', 'VAL', 13.04), ('CG', 'LYS', 'CG1', 'VAL', 12.46), ('CG', 'LYS', 'CG2', 'VAL', 12.47), ('CG', 'LYS', 'O', 'VAL', 15.35), ('CG', 'LYS', 'C', 'VAL', 14.17), ('CG', 'LYS', 'CA', 'VAL', 13.09), ('CG', 'LYS', 'N', 'VAL', 11.83)], [('CD', 'LYS', 'CB', 'VAL', 12.77), ('CD', 'LYS', 'CG1', 'VAL', 11.99), ('CD', 'LYS', 'CG2', 'VAL', 12.34), ('CD', 'LYS', 'O', 'VAL', 15.24), ('CD', 'LYS', 'C', 'VAL', 14.11), ('CD', 'LYS', 'CA', 'VAL', 12.9), ('CD', 'LYS', 'N', 'VAL', 11.69)], [('CE', 'LYS', 'CB', 'VAL', 12.3), ('CE', 'LYS', 'CG1', 'VAL', 11.46), ('CE', 'LYS', 'CG2', 'VAL', 11.81), ('CE', 'LYS', 'O', 'VAL', 14.97), ('CE', 'LYS', 'C', 'VAL', 13.89), ('CE', 'LYS', 'CA', 'VAL', 12.64), ('CE', 'LYS', 'N', 'VAL', 11.57)], [('NZ', 'LYS', 'CB', 'VAL', 10.86), ('NZ', 'LYS', 'CG1', 'VAL', 10.06), ('NZ', 'LYS', 'CG2', 'VAL', 10.33), ('NZ', 'LYS', 'O', 'VAL', 13.57), ('NZ', 'LYS', 'C', 'VAL', 12.51), ('NZ', 'LYS', 'CA', 'VAL', 11.27), ('NZ', 'LYS', 'N', 'VAL', 10.26)]]}
TRP_VAL = { 
	'distances':
		[[13.29, 12.6, 13.65, 14.68, 13.68, 12.6, 11.33], [12.5, 11.67, 12.84, 14.19, 13.19, 11.98, 10.75], [11.59, 10.78, 11.8, 13.46, 12.41, 11.17, 9.91], [12.69, 11.7, 13.14, 14.51, 13.59, 12.28, 11.18], [11.18, 10.2, 11.42, 13.3, 12.3, 10.95, 9.81], [11.88, 10.79, 12.27, 13.96, 13.04, 11.65, 10.61], [13.64, 12.6, 14.21, 15.39, 14.53, 13.22, 12.21], [12.09, 10.86, 12.56, 14.32, 13.48, 12.03, 11.13], [13.81, 12.64, 14.44, 15.69, 14.91, 13.53, 12.64], [13.08, 11.82, 13.67, 15.18, 14.41, 12.97, 12.13]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'VAL', 13.29), ('CB', 'TRP', 'CG1', 'VAL', 12.6), ('CB', 'TRP', 'CG2', 'VAL', 13.65), ('CB', 'TRP', 'O', 'VAL', 14.68), ('CB', 'TRP', 'C', 'VAL', 13.68), ('CB', 'TRP', 'CA', 'VAL', 12.6), ('CB', 'TRP', 'N', 'VAL', 11.33)], [('CG', 'TRP', 'CB', 'VAL', 12.5), ('CG', 'TRP', 'CG1', 'VAL', 11.67), ('CG', 'TRP', 'CG2', 'VAL', 12.84), ('CG', 'TRP', 'O', 'VAL', 14.19), ('CG', 'TRP', 'C', 'VAL', 13.19), ('CG', 'TRP', 'CA', 'VAL', 11.98), ('CG', 'TRP', 'N', 'VAL', 10.75)], [('CD1', 'TRP', 'CB', 'VAL', 11.59), ('CD1', 'TRP', 'CG1', 'VAL', 10.78), ('CD1', 'TRP', 'CG2', 'VAL', 11.8), ('CD1', 'TRP', 'O', 'VAL', 13.46), ('CD1', 'TRP', 'C', 'VAL', 12.41), ('CD1', 'TRP', 'CA', 'VAL', 11.17), ('CD1', 'TRP', 'N', 'VAL', 9.91)], [('CD2', 'TRP', 'CB', 'VAL', 12.69), ('CD2', 'TRP', 'CG1', 'VAL', 11.7), ('CD2', 'TRP', 'CG2', 'VAL', 13.14), ('CD2', 'TRP', 'O', 'VAL', 14.51), ('CD2', 'TRP', 'C', 'VAL', 13.59), ('CD2', 'TRP', 'CA', 'VAL', 12.28), ('CD2', 'TRP', 'N', 'VAL', 11.18)], [('NE1', 'TRP', 'CB', 'VAL', 11.18), ('NE1', 'TRP', 'CG1', 'VAL', 10.2), ('NE1', 'TRP', 'CG2', 'VAL', 11.42), ('NE1', 'TRP', 'O', 'VAL', 13.3), ('NE1', 'TRP', 'C', 'VAL', 12.3), ('NE1', 'TRP', 'CA', 'VAL', 10.95), ('NE1', 'TRP', 'N', 'VAL', 9.81)], [('CE2', 'TRP', 'CB', 'VAL', 11.88), ('CE2', 'TRP', 'CG1', 'VAL', 10.79), ('CE2', 'TRP', 'CG2', 'VAL', 12.27), ('CE2', 'TRP', 'O', 'VAL', 13.96), ('CE2', 'TRP', 'C', 'VAL', 13.04), ('CE2', 'TRP', 'CA', 'VAL', 11.65), ('CE2', 'TRP', 'N', 'VAL', 10.61)], [('CE3', 'TRP', 'CB', 'VAL', 13.64), ('CE3', 'TRP', 'CG1', 'VAL', 12.6), ('CE3', 'TRP', 'CG2', 'VAL', 14.21), ('CE3', 'TRP', 'O', 'VAL', 15.39), ('CE3', 'TRP', 'C', 'VAL', 14.53), ('CE3', 'TRP', 'CA', 'VAL', 13.22), ('CE3', 'TRP', 'N', 'VAL', 12.21)], [('CZ2', 'TRP', 'CB', 'VAL', 12.09), ('CZ2', 'TRP', 'CG1', 'VAL', 10.86), ('CZ2', 'TRP', 'CG2', 'VAL', 12.56), ('CZ2', 'TRP', 'O', 'VAL', 14.32), ('CZ2', 'TRP', 'C', 'VAL', 13.48), ('CZ2', 'TRP', 'CA', 'VAL', 12.03), ('CZ2', 'TRP', 'N', 'VAL', 11.13)], [('CZ3', 'TRP', 'CB', 'VAL', 13.81), ('CZ3', 'TRP', 'CG1', 'VAL', 12.64), ('CZ3', 'TRP', 'CG2', 'VAL', 14.44), ('CZ3', 'TRP', 'O', 'VAL', 15.69), ('CZ3', 'TRP', 'C', 'VAL', 14.91), ('CZ3', 'TRP', 'CA', 'VAL', 13.53), ('CZ3', 'TRP', 'N', 'VAL', 12.64)], [('CH2', 'TRP', 'CB', 'VAL', 13.08), ('CH2', 'TRP', 'CG1', 'VAL', 11.82), ('CH2', 'TRP', 'CG2', 'VAL', 13.67), ('CH2', 'TRP', 'O', 'VAL', 15.18), ('CH2', 'TRP', 'C', 'VAL', 14.41), ('CH2', 'TRP', 'CA', 'VAL', 12.97), ('CH2', 'TRP', 'N', 'VAL', 12.13)]]}
LYS_TRP = { 
	'distances':
		[[8.79, 8.29, 7.35, 9.14, 7.74, 8.82, 10.36, 9.79, 11.15, 10.89], [9.43, 8.66, 7.54, 9.34, 7.59, 8.73, 10.6, 9.53, 11.22, 10.74], [8.98, 7.98, 6.87, 8.4, 6.61, 7.63, 9.6, 8.24, 10.05, 9.45], [10.09, 8.93, 7.76, 9.14, 7.19, 8.13, 10.31, 8.47, 10.55, 9.72], [10.23, 9.04, 7.75, 9.28, 7.11, 8.17, 10.51, 8.51, 10.75, 9.85]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'TRP', 8.79), ('CB', 'LYS', 'CG', 'TRP', 8.29), ('CB', 'LYS', 'CD1', 'TRP', 7.35), ('CB', 'LYS', 'CD2', 'TRP', 9.14), ('CB', 'LYS', 'NE1', 'TRP', 7.74), ('CB', 'LYS', 'CE2', 'TRP', 8.82), ('CB', 'LYS', 'CE3', 'TRP', 10.36), ('CB', 'LYS', 'CZ2', 'TRP', 9.79), ('CB', 'LYS', 'CZ3', 'TRP', 11.15), ('CB', 'LYS', 'CH2', 'TRP', 10.89)], [('CG', 'LYS', 'CB', 'TRP', 9.43), ('CG', 'LYS', 'CG', 'TRP', 8.66), ('CG', 'LYS', 'CD1', 'TRP', 7.54), ('CG', 'LYS', 'CD2', 'TRP', 9.34), ('CG', 'LYS', 'NE1', 'TRP', 7.59), ('CG', 'LYS', 'CE2', 'TRP', 8.73), ('CG', 'LYS', 'CE3', 'TRP', 10.6), ('CG', 'LYS', 'CZ2', 'TRP', 9.53), ('CG', 'LYS', 'CZ3', 'TRP', 11.22), ('CG', 'LYS', 'CH2', 'TRP', 10.74)], [('CD', 'LYS', 'CB', 'TRP', 8.98), ('CD', 'LYS', 'CG', 'TRP', 7.98), ('CD', 'LYS', 'CD1', 'TRP', 6.87), ('CD', 'LYS', 'CD2', 'TRP', 8.4), ('CD', 'LYS', 'NE1', 'TRP', 6.61), ('CD', 'LYS', 'CE2', 'TRP', 7.63), ('CD', 'LYS', 'CE3', 'TRP', 9.6), ('CD', 'LYS', 'CZ2', 'TRP', 8.24), ('CD', 'LYS', 'CZ3', 'TRP', 10.05), ('CD', 'LYS', 'CH2', 'TRP', 9.45)], [('CE', 'LYS', 'CB', 'TRP', 10.09), ('CE', 'LYS', 'CG', 'TRP', 8.93), ('CE', 'LYS', 'CD1', 'TRP', 7.76), ('CE', 'LYS', 'CD2', 'TRP', 9.14), ('CE', 'LYS', 'NE1', 'TRP', 7.19), ('CE', 'LYS', 'CE2', 'TRP', 8.13), ('CE', 'LYS', 'CE3', 'TRP', 10.31), ('CE', 'LYS', 'CZ2', 'TRP', 8.47), ('CE', 'LYS', 'CZ3', 'TRP', 10.55), ('CE', 'LYS', 'CH2', 'TRP', 9.72)], [('NZ', 'LYS', 'CB', 'TRP', 10.23), ('NZ', 'LYS', 'CG', 'TRP', 9.04), ('NZ', 'LYS', 'CD1', 'TRP', 7.75), ('NZ', 'LYS', 'CD2', 'TRP', 9.28), ('NZ', 'LYS', 'NE1', 'TRP', 7.11), ('NZ', 'LYS', 'CE2', 'TRP', 8.17), ('NZ', 'LYS', 'CE3', 'TRP', 10.51), ('NZ', 'LYS', 'CZ2', 'TRP', 8.51), ('NZ', 'LYS', 'CZ3', 'TRP', 10.75), ('NZ', 'LYS', 'CH2', 'TRP', 9.85)]]}
SER_TRP = { 
	'distances':
		[[8.29, 7.43, 6.11, 8.12, 6.08, 7.39, 9.49, 8.25, 10.11, 9.57], [9.38, 8.34, 7.0, 8.78, 6.59, 7.81, 10.1, 8.39, 10.51, 9.75], [7.53, 7.24, 6.19, 8.41, 6.92, 8.22, 9.77, 9.43, 10.75, 10.6], [8.26, 7.94, 6.83, 9.06, 7.45, 8.77, 10.43, 9.92, 11.36, 11.13], [9.0, 8.39, 7.13, 9.28, 7.38, 8.72, 10.67, 9.68, 11.42, 10.98], [10.04, 9.48, 8.27, 10.33, 8.45, 9.74, 11.69, 10.63, 12.39, 11.91]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'TRP', 8.29), ('CB', 'SER', 'CG', 'TRP', 7.43), ('CB', 'SER', 'CD1', 'TRP', 6.11), ('CB', 'SER', 'CD2', 'TRP', 8.12), ('CB', 'SER', 'NE1', 'TRP', 6.08), ('CB', 'SER', 'CE2', 'TRP', 7.39), ('CB', 'SER', 'CE3', 'TRP', 9.49), ('CB', 'SER', 'CZ2', 'TRP', 8.25), ('CB', 'SER', 'CZ3', 'TRP', 10.11), ('CB', 'SER', 'CH2', 'TRP', 9.57)], [('OG', 'SER', 'CB', 'TRP', 9.38), ('OG', 'SER', 'CG', 'TRP', 8.34), ('OG', 'SER', 'CD1', 'TRP', 7.0), ('OG', 'SER', 'CD2', 'TRP', 8.78), ('OG', 'SER', 'NE1', 'TRP', 6.59), ('OG', 'SER', 'CE2', 'TRP', 7.81), ('OG', 'SER', 'CE3', 'TRP', 10.1), ('OG', 'SER', 'CZ2', 'TRP', 8.39), ('OG', 'SER', 'CZ3', 'TRP', 10.51), ('OG', 'SER', 'CH2', 'TRP', 9.75)], [('O', 'SER', 'CB', 'TRP', 7.53), ('O', 'SER', 'CG', 'TRP', 7.24), ('O', 'SER', 'CD1', 'TRP', 6.19), ('O', 'SER', 'CD2', 'TRP', 8.41), ('O', 'SER', 'NE1', 'TRP', 6.92), ('O', 'SER', 'CE2', 'TRP', 8.22), ('O', 'SER', 'CE3', 'TRP', 9.77), ('O', 'SER', 'CZ2', 'TRP', 9.43), ('O', 'SER', 'CZ3', 'TRP', 10.75), ('O', 'SER', 'CH2', 'TRP', 10.6)], [('C', 'SER', 'CB', 'TRP', 8.26), ('C', 'SER', 'CG', 'TRP', 7.94), ('C', 'SER', 'CD1', 'TRP', 6.83), ('C', 'SER', 'CD2', 'TRP', 9.06), ('C', 'SER', 'NE1', 'TRP', 7.45), ('C', 'SER', 'CE2', 'TRP', 8.77), ('C', 'SER', 'CE3', 'TRP', 10.43), ('C', 'SER', 'CZ2', 'TRP', 9.92), ('C', 'SER', 'CZ3', 'TRP', 11.36), ('C', 'SER', 'CH2', 'TRP', 11.13)], [('CA', 'SER', 'CB', 'TRP', 9.0), ('CA', 'SER', 'CG', 'TRP', 8.39), ('CA', 'SER', 'CD1', 'TRP', 7.13), ('CA', 'SER', 'CD2', 'TRP', 9.28), ('CA', 'SER', 'NE1', 'TRP', 7.38), ('CA', 'SER', 'CE2', 'TRP', 8.72), ('CA', 'SER', 'CE3', 'TRP', 10.67), ('CA', 'SER', 'CZ2', 'TRP', 9.68), ('CA', 'SER', 'CZ3', 'TRP', 11.42), ('CA', 'SER', 'CH2', 'TRP', 10.98)], [('N', 'SER', 'CB', 'TRP', 10.04), ('N', 'SER', 'CG', 'TRP', 9.48), ('N', 'SER', 'CD1', 'TRP', 8.27), ('N', 'SER', 'CD2', 'TRP', 10.33), ('N', 'SER', 'NE1', 'TRP', 8.45), ('N', 'SER', 'CE2', 'TRP', 9.74), ('N', 'SER', 'CE3', 'TRP', 11.69), ('N', 'SER', 'CZ2', 'TRP', 10.63), ('N', 'SER', 'CZ3', 'TRP', 12.39), ('N', 'SER', 'CH2', 'TRP', 11.91)]]}
LYS_TYR = { 
	'distances':
		[[12.2, 10.89, 9.69, 11.03, 8.49, 10.04, 8.72, 7.88], [11.29, 9.97, 8.84, 10.05, 7.64, 9.06, 7.79, 6.97], [9.8, 8.5, 7.33, 8.68, 6.16, 7.79, 6.48, 5.88], [9.01, 7.74, 6.72, 7.88, 5.68, 7.07, 5.91, 5.52], [9.05, 7.69, 6.95, 7.46, 5.81, 6.45, 5.5, 4.84]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'TYR', 12.2), ('CB', 'LYS', 'CG', 'TYR', 10.89), ('CB', 'LYS', 'CD1', 'TYR', 9.69), ('CB', 'LYS', 'CD2', 'TYR', 11.03), ('CB', 'LYS', 'CE1', 'TYR', 8.49), ('CB', 'LYS', 'CE2', 'TYR', 10.04), ('CB', 'LYS', 'CZ', 'TYR', 8.72), ('CB', 'LYS', 'OH', 'TYR', 7.88)], [('CG', 'LYS', 'CB', 'TYR', 11.29), ('CG', 'LYS', 'CG', 'TYR', 9.97), ('CG', 'LYS', 'CD1', 'TYR', 8.84), ('CG', 'LYS', 'CD2', 'TYR', 10.05), ('CG', 'LYS', 'CE1', 'TYR', 7.64), ('CG', 'LYS', 'CE2', 'TYR', 9.06), ('CG', 'LYS', 'CZ', 'TYR', 7.79), ('CG', 'LYS', 'OH', 'TYR', 6.97)], [('CD', 'LYS', 'CB', 'TYR', 9.8), ('CD', 'LYS', 'CG', 'TYR', 8.5), ('CD', 'LYS', 'CD1', 'TYR', 7.33), ('CD', 'LYS', 'CD2', 'TYR', 8.68), ('CD', 'LYS', 'CE1', 'TYR', 6.16), ('CD', 'LYS', 'CE2', 'TYR', 7.79), ('CD', 'LYS', 'CZ', 'TYR', 6.48), ('CD', 'LYS', 'OH', 'TYR', 5.88)], [('CE', 'LYS', 'CB', 'TYR', 9.01), ('CE', 'LYS', 'CG', 'TYR', 7.74), ('CE', 'LYS', 'CD1', 'TYR', 6.72), ('CE', 'LYS', 'CD2', 'TYR', 7.88), ('CE', 'LYS', 'CE1', 'TYR', 5.68), ('CE', 'LYS', 'CE2', 'TYR', 7.07), ('CE', 'LYS', 'CZ', 'TYR', 5.91), ('CE', 'LYS', 'OH', 'TYR', 5.52)], [('NZ', 'LYS', 'CB', 'TYR', 9.05), ('NZ', 'LYS', 'CG', 'TYR', 7.69), ('NZ', 'LYS', 'CD1', 'TYR', 6.95), ('NZ', 'LYS', 'CD2', 'TYR', 7.46), ('NZ', 'LYS', 'CE1', 'TYR', 5.81), ('NZ', 'LYS', 'CE2', 'TYR', 6.45), ('NZ', 'LYS', 'CZ', 'TYR', 5.5), ('NZ', 'LYS', 'OH', 'TYR', 4.84)]]}
LYS_SER = { 
	'distances':
		[[7.05, 7.55, 5.49, 6.48, 6.95, 8.34], [6.44, 6.57, 5.78, 6.5, 6.48, 7.79], [6.35, 6.28, 6.4, 7.12, 6.89, 8.22], [6.57, 6.01, 7.4, 7.86, 7.24, 8.36], [5.62, 4.73, 7.15, 7.3, 6.35, 7.25]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'SER', 7.05), ('CB', 'LYS', 'OG', 'SER', 7.55), ('CB', 'LYS', 'O', 'SER', 5.49), ('CB', 'LYS', 'C', 'SER', 6.48), ('CB', 'LYS', 'CA', 'SER', 6.95), ('CB', 'LYS', 'N', 'SER', 8.34)], [('CG', 'LYS', 'CB', 'SER', 6.44), ('CG', 'LYS', 'OG', 'SER', 6.57), ('CG', 'LYS', 'O', 'SER', 5.78), ('CG', 'LYS', 'C', 'SER', 6.5), ('CG', 'LYS', 'CA', 'SER', 6.48), ('CG', 'LYS', 'N', 'SER', 7.79)], [('CD', 'LYS', 'CB', 'SER', 6.35), ('CD', 'LYS', 'OG', 'SER', 6.28), ('CD', 'LYS', 'O', 'SER', 6.4), ('CD', 'LYS', 'C', 'SER', 7.12), ('CD', 'LYS', 'CA', 'SER', 6.89), ('CD', 'LYS', 'N', 'SER', 8.22)], [('CE', 'LYS', 'CB', 'SER', 6.57), ('CE', 'LYS', 'OG', 'SER', 6.01), ('CE', 'LYS', 'O', 'SER', 7.4), ('CE', 'LYS', 'C', 'SER', 7.86), ('CE', 'LYS', 'CA', 'SER', 7.24), ('CE', 'LYS', 'N', 'SER', 8.36)], [('NZ', 'LYS', 'CB', 'SER', 5.62), ('NZ', 'LYS', 'OG', 'SER', 4.73), ('NZ', 'LYS', 'O', 'SER', 7.15), ('NZ', 'LYS', 'C', 'SER', 7.3), ('NZ', 'LYS', 'CA', 'SER', 6.35), ('NZ', 'LYS', 'N', 'SER', 7.25)]]}
VAL_TYR = { 
	'distances':
		[[13.31, 12.18, 12.6, 10.84, 11.81, 9.87, 10.43, 9.76], [11.85, 10.77, 11.27, 9.41, 10.58, 8.51, 9.2, 8.68], [13.57, 12.39, 12.7, 11.1, 11.84, 10.06, 10.49, 9.72], [16.13, 15.0, 15.39, 13.67, 14.54, 12.69, 13.18, 12.41], [15.47, 14.27, 14.56, 12.98, 13.64, 11.9, 12.28, 11.43], [13.95, 12.75, 13.05, 11.45, 12.17, 10.39, 10.8, 10.01], [13.46, 12.16, 12.3, 10.95, 11.29, 9.76, 9.97, 9.03]],
	'comparisons':
		[[('CB', 'VAL', 'CB', 'TYR', 13.31), ('CB', 'VAL', 'CG', 'TYR', 12.18), ('CB', 'VAL', 'CD1', 'TYR', 12.6), ('CB', 'VAL', 'CD2', 'TYR', 10.84), ('CB', 'VAL', 'CE1', 'TYR', 11.81), ('CB', 'VAL', 'CE2', 'TYR', 9.87), ('CB', 'VAL', 'CZ', 'TYR', 10.43), ('CB', 'VAL', 'OH', 'TYR', 9.76)], [('CG1', 'VAL', 'CB', 'TYR', 11.85), ('CG1', 'VAL', 'CG', 'TYR', 10.77), ('CG1', 'VAL', 'CD1', 'TYR', 11.27), ('CG1', 'VAL', 'CD2', 'TYR', 9.41), ('CG1', 'VAL', 'CE1', 'TYR', 10.58), ('CG1', 'VAL', 'CE2', 'TYR', 8.51), ('CG1', 'VAL', 'CZ', 'TYR', 9.2), ('CG1', 'VAL', 'OH', 'TYR', 8.68)], [('CG2', 'VAL', 'CB', 'TYR', 13.57), ('CG2', 'VAL', 'CG', 'TYR', 12.39), ('CG2', 'VAL', 'CD1', 'TYR', 12.7), ('CG2', 'VAL', 'CD2', 'TYR', 11.1), ('CG2', 'VAL', 'CE1', 'TYR', 11.84), ('CG2', 'VAL', 'CE2', 'TYR', 10.06), ('CG2', 'VAL', 'CZ', 'TYR', 10.49), ('CG2', 'VAL', 'OH', 'TYR', 9.72)], [('O', 'VAL', 'CB', 'TYR', 16.13), ('O', 'VAL', 'CG', 'TYR', 15.0), ('O', 'VAL', 'CD1', 'TYR', 15.39), ('O', 'VAL', 'CD2', 'TYR', 13.67), ('O', 'VAL', 'CE1', 'TYR', 14.54), ('O', 'VAL', 'CE2', 'TYR', 12.69), ('O', 'VAL', 'CZ', 'TYR', 13.18), ('O', 'VAL', 'OH', 'TYR', 12.41)], [('C', 'VAL', 'CB', 'TYR', 15.47), ('C', 'VAL', 'CG', 'TYR', 14.27), ('C', 'VAL', 'CD1', 'TYR', 14.56), ('C', 'VAL', 'CD2', 'TYR', 12.98), ('C', 'VAL', 'CE1', 'TYR', 13.64), ('C', 'VAL', 'CE2', 'TYR', 11.9), ('C', 'VAL', 'CZ', 'TYR', 12.28), ('C', 'VAL', 'OH', 'TYR', 11.43)], [('CA', 'VAL', 'CB', 'TYR', 13.95), ('CA', 'VAL', 'CG', 'TYR', 12.75), ('CA', 'VAL', 'CD1', 'TYR', 13.05), ('CA', 'VAL', 'CD2', 'TYR', 11.45), ('CA', 'VAL', 'CE1', 'TYR', 12.17), ('CA', 'VAL', 'CE2', 'TYR', 10.39), ('CA', 'VAL', 'CZ', 'TYR', 10.8), ('CA', 'VAL', 'OH', 'TYR', 10.01)], [('N', 'VAL', 'CB', 'TYR', 13.46), ('N', 'VAL', 'CG', 'TYR', 12.16), ('N', 'VAL', 'CD1', 'TYR', 12.3), ('N', 'VAL', 'CD2', 'TYR', 10.95), ('N', 'VAL', 'CE1', 'TYR', 11.29), ('N', 'VAL', 'CE2', 'TYR', 9.76), ('N', 'VAL', 'CZ', 'TYR', 9.97), ('N', 'VAL', 'OH', 'TYR', 9.03)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_TYR, d, 'A_1ci8_3_1_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TRP_TYR, d, 'A_1ci8_3_1_1_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_VAL, d, 'A_1ci8_3_1_1_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(LYS_VAL, d, 'A_1ci8_3_1_1_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(TRP_VAL, d, 'A_1ci8_3_1_1_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(LYS_TRP, d, 'A_1ci8_3_1_1_1')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(SER_TRP, d, 'A_1ci8_3_1_1_1')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(LYS_TYR, d, 'A_1ci8_3_1_1_1')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(LYS_SER, d, 'A_1ci8_3_1_1_1')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(VAL_TYR, d, 'A_1ci8_3_1_1_1')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_TYR' :  match1,
		'TRP_TYR' :  match2,
		'SER_VAL' :  match3,
		'LYS_VAL' :  match4,
		'TRP_VAL' :  match5,
		'LYS_TRP' :  match6,
		'SER_TRP' :  match7,
		'LYS_TYR' :  match8,
		'LYS_SER' :  match9,
		'VAL_TYR' :  match10}