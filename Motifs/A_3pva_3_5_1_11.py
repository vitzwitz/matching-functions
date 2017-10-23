'''
FUNC:A_3pva_3_5_1_11
PDB:3pva
EC:3.5.1.11
RESI:cys,tyr,asn,arg
LOCI:a-1,82,175,228;
'''
import motifFunctions as cmd
TYR_CYS = { 
	'distances':
		[[8.24, 6.94, 9.13, 9.36, 8.61, 7.64], [9.26, 7.76, 10.46, 10.6, 9.68, 8.68], [9.44, 7.76, 11.14, 11.12, 10.08, 9.24], [10.32, 8.9, 11.23, 11.45, 10.56, 9.4], [10.61, 8.89, 12.42, 12.36, 11.25, 10.37], [11.38, 9.87, 12.49, 12.65, 11.67, 10.51], [11.5, 9.85, 13.02, 13.05, 11.97, 10.93], [12.71, 11.02, 14.33, 14.32, 13.19, 12.15], [8.84, 8.23, 8.5, 9.15, 9.06, 8.36], [9.22, 8.32, 9.35, 9.87, 9.57, 8.79], [8.47, 7.28, 9.29, 9.58, 9.02, 8.28], [7.38, 6.26, 8.49, 8.66, 8.12, 7.66]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'CYS', 8.24), ('CB', 'TYR', 'SG', 'CYS', 6.94), ('CB', 'TYR', 'O', 'CYS', 9.13), ('CB', 'TYR', 'C', 'CYS', 9.36), ('CB', 'TYR', 'CA', 'CYS', 8.61), ('CB', 'TYR', 'N', 'CYS', 7.64)], [('CG', 'TYR', 'CB', 'CYS', 9.26), ('CG', 'TYR', 'SG', 'CYS', 7.76), ('CG', 'TYR', 'O', 'CYS', 10.46), ('CG', 'TYR', 'C', 'CYS', 10.6), ('CG', 'TYR', 'CA', 'CYS', 9.68), ('CG', 'TYR', 'N', 'CYS', 8.68)], [('CD1', 'TYR', 'CB', 'CYS', 9.44), ('CD1', 'TYR', 'SG', 'CYS', 7.76), ('CD1', 'TYR', 'O', 'CYS', 11.14), ('CD1', 'TYR', 'C', 'CYS', 11.12), ('CD1', 'TYR', 'CA', 'CYS', 10.08), ('CD1', 'TYR', 'N', 'CYS', 9.24)], [('CD2', 'TYR', 'CB', 'CYS', 10.32), ('CD2', 'TYR', 'SG', 'CYS', 8.9), ('CD2', 'TYR', 'O', 'CYS', 11.23), ('CD2', 'TYR', 'C', 'CYS', 11.45), ('CD2', 'TYR', 'CA', 'CYS', 10.56), ('CD2', 'TYR', 'N', 'CYS', 9.4)], [('CE1', 'TYR', 'CB', 'CYS', 10.61), ('CE1', 'TYR', 'SG', 'CYS', 8.89), ('CE1', 'TYR', 'O', 'CYS', 12.42), ('CE1', 'TYR', 'C', 'CYS', 12.36), ('CE1', 'TYR', 'CA', 'CYS', 11.25), ('CE1', 'TYR', 'N', 'CYS', 10.37)], [('CE2', 'TYR', 'CB', 'CYS', 11.38), ('CE2', 'TYR', 'SG', 'CYS', 9.87), ('CE2', 'TYR', 'O', 'CYS', 12.49), ('CE2', 'TYR', 'C', 'CYS', 12.65), ('CE2', 'TYR', 'CA', 'CYS', 11.67), ('CE2', 'TYR', 'N', 'CYS', 10.51)], [('CZ', 'TYR', 'CB', 'CYS', 11.5), ('CZ', 'TYR', 'SG', 'CYS', 9.85), ('CZ', 'TYR', 'O', 'CYS', 13.02), ('CZ', 'TYR', 'C', 'CYS', 13.05), ('CZ', 'TYR', 'CA', 'CYS', 11.97), ('CZ', 'TYR', 'N', 'CYS', 10.93)], [('OH', 'TYR', 'CB', 'CYS', 12.71), ('OH', 'TYR', 'SG', 'CYS', 11.02), ('OH', 'TYR', 'O', 'CYS', 14.33), ('OH', 'TYR', 'C', 'CYS', 14.32), ('OH', 'TYR', 'CA', 'CYS', 13.19), ('OH', 'TYR', 'N', 'CYS', 12.15)], [('O', 'TYR', 'CB', 'CYS', 8.84), ('O', 'TYR', 'SG', 'CYS', 8.23), ('O', 'TYR', 'O', 'CYS', 8.5), ('O', 'TYR', 'C', 'CYS', 9.15), ('O', 'TYR', 'CA', 'CYS', 9.06), ('O', 'TYR', 'N', 'CYS', 8.36)], [('C', 'TYR', 'CB', 'CYS', 9.22), ('C', 'TYR', 'SG', 'CYS', 8.32), ('C', 'TYR', 'O', 'CYS', 9.35), ('C', 'TYR', 'C', 'CYS', 9.87), ('C', 'TYR', 'CA', 'CYS', 9.57), ('C', 'TYR', 'N', 'CYS', 8.79)], [('CA', 'TYR', 'CB', 'CYS', 8.47), ('CA', 'TYR', 'SG', 'CYS', 7.28), ('CA', 'TYR', 'O', 'CYS', 9.29), ('CA', 'TYR', 'C', 'CYS', 9.58), ('CA', 'TYR', 'CA', 'CYS', 9.02), ('CA', 'TYR', 'N', 'CYS', 8.28)], [('N', 'TYR', 'CB', 'CYS', 7.38), ('N', 'TYR', 'SG', 'CYS', 6.26), ('N', 'TYR', 'O', 'CYS', 8.49), ('N', 'TYR', 'C', 'CYS', 8.66), ('N', 'TYR', 'CA', 'CYS', 8.12), ('N', 'TYR', 'N', 'CYS', 7.66)]]}
TYR_ARG = { 
	'distances':
		[[13.69, 13.83, 12.83, 11.65, 10.53, 10.49, 9.62], [14.91, 14.93, 13.87, 12.66, 11.62, 11.7, 10.65], [15.87, 15.88, 14.74, 13.6, 12.59, 12.61, 11.7], [15.22, 15.15, 14.13, 12.84, 11.87, 12.11, 10.78], [17.01, 16.93, 15.76, 14.59, 13.65, 13.76, 12.72], [16.4, 16.25, 15.19, 13.89, 12.99, 13.31, 11.89], [17.25, 17.1, 15.96, 14.72, 13.82, 14.07, 12.79], [18.46, 18.25, 17.09, 15.84, 15.0, 15.31, 13.96], [12.85, 13.38, 12.71, 11.62, 10.33, 10.0, 9.53], [13.8, 14.22, 13.46, 12.32, 11.07, 10.84, 10.19], [14.12, 14.44, 13.52, 12.41, 11.21, 10.98, 10.38], [13.72, 14.11, 13.15, 12.18, 10.96, 10.55, 10.31]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ARG', 13.69), ('CB', 'TYR', 'CG', 'ARG', 13.83), ('CB', 'TYR', 'CD', 'ARG', 12.83), ('CB', 'TYR', 'NE', 'ARG', 11.65), ('CB', 'TYR', 'CZ', 'ARG', 10.53), ('CB', 'TYR', 'NH1', 'ARG', 10.49), ('CB', 'TYR', 'NH2', 'ARG', 9.62)], [('CG', 'TYR', 'CB', 'ARG', 14.91), ('CG', 'TYR', 'CG', 'ARG', 14.93), ('CG', 'TYR', 'CD', 'ARG', 13.87), ('CG', 'TYR', 'NE', 'ARG', 12.66), ('CG', 'TYR', 'CZ', 'ARG', 11.62), ('CG', 'TYR', 'NH1', 'ARG', 11.7), ('CG', 'TYR', 'NH2', 'ARG', 10.65)], [('CD1', 'TYR', 'CB', 'ARG', 15.87), ('CD1', 'TYR', 'CG', 'ARG', 15.88), ('CD1', 'TYR', 'CD', 'ARG', 14.74), ('CD1', 'TYR', 'NE', 'ARG', 13.6), ('CD1', 'TYR', 'CZ', 'ARG', 12.59), ('CD1', 'TYR', 'NH1', 'ARG', 12.61), ('CD1', 'TYR', 'NH2', 'ARG', 11.7)], [('CD2', 'TYR', 'CB', 'ARG', 15.22), ('CD2', 'TYR', 'CG', 'ARG', 15.15), ('CD2', 'TYR', 'CD', 'ARG', 14.13), ('CD2', 'TYR', 'NE', 'ARG', 12.84), ('CD2', 'TYR', 'CZ', 'ARG', 11.87), ('CD2', 'TYR', 'NH1', 'ARG', 12.11), ('CD2', 'TYR', 'NH2', 'ARG', 10.78)], [('CE1', 'TYR', 'CB', 'ARG', 17.01), ('CE1', 'TYR', 'CG', 'ARG', 16.93), ('CE1', 'TYR', 'CD', 'ARG', 15.76), ('CE1', 'TYR', 'NE', 'ARG', 14.59), ('CE1', 'TYR', 'CZ', 'ARG', 13.65), ('CE1', 'TYR', 'NH1', 'ARG', 13.76), ('CE1', 'TYR', 'NH2', 'ARG', 12.72)], [('CE2', 'TYR', 'CB', 'ARG', 16.4), ('CE2', 'TYR', 'CG', 'ARG', 16.25), ('CE2', 'TYR', 'CD', 'ARG', 15.19), ('CE2', 'TYR', 'NE', 'ARG', 13.89), ('CE2', 'TYR', 'CZ', 'ARG', 12.99), ('CE2', 'TYR', 'NH1', 'ARG', 13.31), ('CE2', 'TYR', 'NH2', 'ARG', 11.89)], [('CZ', 'TYR', 'CB', 'ARG', 17.25), ('CZ', 'TYR', 'CG', 'ARG', 17.1), ('CZ', 'TYR', 'CD', 'ARG', 15.96), ('CZ', 'TYR', 'NE', 'ARG', 14.72), ('CZ', 'TYR', 'CZ', 'ARG', 13.82), ('CZ', 'TYR', 'NH1', 'ARG', 14.07), ('CZ', 'TYR', 'NH2', 'ARG', 12.79)], [('OH', 'TYR', 'CB', 'ARG', 18.46), ('OH', 'TYR', 'CG', 'ARG', 18.25), ('OH', 'TYR', 'CD', 'ARG', 17.09), ('OH', 'TYR', 'NE', 'ARG', 15.84), ('OH', 'TYR', 'CZ', 'ARG', 15.0), ('OH', 'TYR', 'NH1', 'ARG', 15.31), ('OH', 'TYR', 'NH2', 'ARG', 13.96)], [('O', 'TYR', 'CB', 'ARG', 12.85), ('O', 'TYR', 'CG', 'ARG', 13.38), ('O', 'TYR', 'CD', 'ARG', 12.71), ('O', 'TYR', 'NE', 'ARG', 11.62), ('O', 'TYR', 'CZ', 'ARG', 10.33), ('O', 'TYR', 'NH1', 'ARG', 10.0), ('O', 'TYR', 'NH2', 'ARG', 9.53)], [('C', 'TYR', 'CB', 'ARG', 13.8), ('C', 'TYR', 'CG', 'ARG', 14.22), ('C', 'TYR', 'CD', 'ARG', 13.46), ('C', 'TYR', 'NE', 'ARG', 12.32), ('C', 'TYR', 'CZ', 'ARG', 11.07), ('C', 'TYR', 'NH1', 'ARG', 10.84), ('C', 'TYR', 'NH2', 'ARG', 10.19)], [('CA', 'TYR', 'CB', 'ARG', 14.12), ('CA', 'TYR', 'CG', 'ARG', 14.44), ('CA', 'TYR', 'CD', 'ARG', 13.52), ('CA', 'TYR', 'NE', 'ARG', 12.41), ('CA', 'TYR', 'CZ', 'ARG', 11.21), ('CA', 'TYR', 'NH1', 'ARG', 10.98), ('CA', 'TYR', 'NH2', 'ARG', 10.38)], [('N', 'TYR', 'CB', 'ARG', 13.72), ('N', 'TYR', 'CG', 'ARG', 14.11), ('N', 'TYR', 'CD', 'ARG', 13.15), ('N', 'TYR', 'NE', 'ARG', 12.18), ('N', 'TYR', 'CZ', 'ARG', 10.96), ('N', 'TYR', 'NH1', 'ARG', 10.55), ('N', 'TYR', 'NH2', 'ARG', 10.31)]]}
ASN_CYS = { 
	'distances':
		[[8.67, 8.71, 6.87, 7.87, 8.1, 7.12], [7.18, 7.23, 5.77, 6.59, 6.64, 5.64], [6.83, 7.14, 5.11, 5.91, 5.98, 4.9], [6.66, 6.43, 6.03, 6.65, 6.52, 5.69]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'CYS', 8.67), ('CB', 'ASN', 'SG', 'CYS', 8.71), ('CB', 'ASN', 'O', 'CYS', 6.87), ('CB', 'ASN', 'C', 'CYS', 7.87), ('CB', 'ASN', 'CA', 'CYS', 8.1), ('CB', 'ASN', 'N', 'CYS', 7.12)], [('CG', 'ASN', 'CB', 'CYS', 7.18), ('CG', 'ASN', 'SG', 'CYS', 7.23), ('CG', 'ASN', 'O', 'CYS', 5.77), ('CG', 'ASN', 'C', 'CYS', 6.59), ('CG', 'ASN', 'CA', 'CYS', 6.64), ('CG', 'ASN', 'N', 'CYS', 5.64)], [('OD1', 'ASN', 'CB', 'CYS', 6.83), ('OD1', 'ASN', 'SG', 'CYS', 7.14), ('OD1', 'ASN', 'O', 'CYS', 5.11), ('OD1', 'ASN', 'C', 'CYS', 5.91), ('OD1', 'ASN', 'CA', 'CYS', 5.98), ('OD1', 'ASN', 'N', 'CYS', 4.9)], [('ND2', 'ASN', 'CB', 'CYS', 6.66), ('ND2', 'ASN', 'SG', 'CYS', 6.43), ('ND2', 'ASN', 'O', 'CYS', 6.03), ('ND2', 'ASN', 'C', 'CYS', 6.65), ('ND2', 'ASN', 'CA', 'CYS', 6.52), ('ND2', 'ASN', 'N', 'CYS', 5.69)]]}
ASN_ARG = { 
	'distances':
		[[9.72, 10.16, 9.66, 8.5, 7.25, 7.15, 6.36], [9.51, 9.86, 9.11, 8.0, 6.72, 6.52, 5.95], [8.54, 8.78, 7.95, 6.84, 5.58, 5.43, 4.87], [10.56, 10.95, 10.13, 9.09, 7.82, 7.47, 7.14]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ARG', 9.72), ('CB', 'ASN', 'CG', 'ARG', 10.16), ('CB', 'ASN', 'CD', 'ARG', 9.66), ('CB', 'ASN', 'NE', 'ARG', 8.5), ('CB', 'ASN', 'CZ', 'ARG', 7.25), ('CB', 'ASN', 'NH1', 'ARG', 7.15), ('CB', 'ASN', 'NH2', 'ARG', 6.36)], [('CG', 'ASN', 'CB', 'ARG', 9.51), ('CG', 'ASN', 'CG', 'ARG', 9.86), ('CG', 'ASN', 'CD', 'ARG', 9.11), ('CG', 'ASN', 'NE', 'ARG', 8.0), ('CG', 'ASN', 'CZ', 'ARG', 6.72), ('CG', 'ASN', 'NH1', 'ARG', 6.52), ('CG', 'ASN', 'NH2', 'ARG', 5.95)], [('OD1', 'ASN', 'CB', 'ARG', 8.54), ('OD1', 'ASN', 'CG', 'ARG', 8.78), ('OD1', 'ASN', 'CD', 'ARG', 7.95), ('OD1', 'ASN', 'NE', 'ARG', 6.84), ('OD1', 'ASN', 'CZ', 'ARG', 5.58), ('OD1', 'ASN', 'NH1', 'ARG', 5.43), ('OD1', 'ASN', 'NH2', 'ARG', 4.87)], [('ND2', 'ASN', 'CB', 'ARG', 10.56), ('ND2', 'ASN', 'CG', 'ARG', 10.95), ('ND2', 'ASN', 'CD', 'ARG', 10.13), ('ND2', 'ASN', 'NE', 'ARG', 9.09), ('ND2', 'ASN', 'CZ', 'ARG', 7.82), ('ND2', 'ASN', 'NH1', 'ARG', 7.47), ('ND2', 'ASN', 'NH2', 'ARG', 7.14)]]}
TYR_ASN = { 
	'distances':
		[[7.0, 6.37, 7.16, 5.48], [8.3, 7.73, 8.42, 6.94], [9.51, 8.81, 9.44, 7.89], [8.52, 8.18, 8.84, 7.63], [10.69, 10.04, 10.63, 9.19], [9.84, 9.51, 10.11, 8.99], [10.82, 10.33, 10.91, 9.66], [12.12, 11.66, 12.21, 11.02], [5.56, 5.63, 6.82, 4.76], [6.41, 6.37, 7.51, 5.43], [7.18, 6.7, 7.67, 5.57], [7.41, 6.64, 7.5, 5.34]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASN', 7.0), ('CB', 'TYR', 'CG', 'ASN', 6.37), ('CB', 'TYR', 'OD1', 'ASN', 7.16), ('CB', 'TYR', 'ND2', 'ASN', 5.48)], [('CG', 'TYR', 'CB', 'ASN', 8.3), ('CG', 'TYR', 'CG', 'ASN', 7.73), ('CG', 'TYR', 'OD1', 'ASN', 8.42), ('CG', 'TYR', 'ND2', 'ASN', 6.94)], [('CD1', 'TYR', 'CB', 'ASN', 9.51), ('CD1', 'TYR', 'CG', 'ASN', 8.81), ('CD1', 'TYR', 'OD1', 'ASN', 9.44), ('CD1', 'TYR', 'ND2', 'ASN', 7.89)], [('CD2', 'TYR', 'CB', 'ASN', 8.52), ('CD2', 'TYR', 'CG', 'ASN', 8.18), ('CD2', 'TYR', 'OD1', 'ASN', 8.84), ('CD2', 'TYR', 'ND2', 'ASN', 7.63)], [('CE1', 'TYR', 'CB', 'ASN', 10.69), ('CE1', 'TYR', 'CG', 'ASN', 10.04), ('CE1', 'TYR', 'OD1', 'ASN', 10.63), ('CE1', 'TYR', 'ND2', 'ASN', 9.19)], [('CE2', 'TYR', 'CB', 'ASN', 9.84), ('CE2', 'TYR', 'CG', 'ASN', 9.51), ('CE2', 'TYR', 'OD1', 'ASN', 10.11), ('CE2', 'TYR', 'ND2', 'ASN', 8.99)], [('CZ', 'TYR', 'CB', 'ASN', 10.82), ('CZ', 'TYR', 'CG', 'ASN', 10.33), ('CZ', 'TYR', 'OD1', 'ASN', 10.91), ('CZ', 'TYR', 'ND2', 'ASN', 9.66)], [('OH', 'TYR', 'CB', 'ASN', 12.12), ('OH', 'TYR', 'CG', 'ASN', 11.66), ('OH', 'TYR', 'OD1', 'ASN', 12.21), ('OH', 'TYR', 'ND2', 'ASN', 11.02)], [('O', 'TYR', 'CB', 'ASN', 5.56), ('O', 'TYR', 'CG', 'ASN', 5.63), ('O', 'TYR', 'OD1', 'ASN', 6.82), ('O', 'TYR', 'ND2', 'ASN', 4.76)], [('C', 'TYR', 'CB', 'ASN', 6.41), ('C', 'TYR', 'CG', 'ASN', 6.37), ('C', 'TYR', 'OD1', 'ASN', 7.51), ('C', 'TYR', 'ND2', 'ASN', 5.43)], [('CA', 'TYR', 'CB', 'ASN', 7.18), ('CA', 'TYR', 'CG', 'ASN', 6.7), ('CA', 'TYR', 'OD1', 'ASN', 7.67), ('CA', 'TYR', 'ND2', 'ASN', 5.57)], [('N', 'TYR', 'CB', 'ASN', 7.41), ('N', 'TYR', 'CG', 'ASN', 6.64), ('N', 'TYR', 'OD1', 'ASN', 7.5), ('N', 'TYR', 'ND2', 'ASN', 5.34)]]}
CYS_ARG = { 
	'distances':
		[[10.73, 10.95, 9.74, 9.32, 8.43, 7.76, 8.54], [12.09, 12.21, 10.95, 10.3, 9.37, 8.91, 9.17], [7.71, 8.27, 7.42, 7.02, 5.95, 4.88, 6.31], [8.31, 8.71, 7.69, 7.43, 6.54, 5.56, 6.98], [9.32, 9.46, 8.23, 7.82, 6.98, 6.34, 7.2], [9.25, 9.26, 8.0, 7.26, 6.34, 6.02, 6.22]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ARG', 10.73), ('CB', 'CYS', 'CG', 'ARG', 10.95), ('CB', 'CYS', 'CD', 'ARG', 9.74), ('CB', 'CYS', 'NE', 'ARG', 9.32), ('CB', 'CYS', 'CZ', 'ARG', 8.43), ('CB', 'CYS', 'NH1', 'ARG', 7.76), ('CB', 'CYS', 'NH2', 'ARG', 8.54)], [('SG', 'CYS', 'CB', 'ARG', 12.09), ('SG', 'CYS', 'CG', 'ARG', 12.21), ('SG', 'CYS', 'CD', 'ARG', 10.95), ('SG', 'CYS', 'NE', 'ARG', 10.3), ('SG', 'CYS', 'CZ', 'ARG', 9.37), ('SG', 'CYS', 'NH1', 'ARG', 8.91), ('SG', 'CYS', 'NH2', 'ARG', 9.17)], [('O', 'CYS', 'CB', 'ARG', 7.71), ('O', 'CYS', 'CG', 'ARG', 8.27), ('O', 'CYS', 'CD', 'ARG', 7.42), ('O', 'CYS', 'NE', 'ARG', 7.02), ('O', 'CYS', 'CZ', 'ARG', 5.95), ('O', 'CYS', 'NH1', 'ARG', 4.88), ('O', 'CYS', 'NH2', 'ARG', 6.31)], [('C', 'CYS', 'CB', 'ARG', 8.31), ('C', 'CYS', 'CG', 'ARG', 8.71), ('C', 'CYS', 'CD', 'ARG', 7.69), ('C', 'CYS', 'NE', 'ARG', 7.43), ('C', 'CYS', 'CZ', 'ARG', 6.54), ('C', 'CYS', 'NH1', 'ARG', 5.56), ('C', 'CYS', 'NH2', 'ARG', 6.98)], [('CA', 'CYS', 'CB', 'ARG', 9.32), ('CA', 'CYS', 'CG', 'ARG', 9.46), ('CA', 'CYS', 'CD', 'ARG', 8.23), ('CA', 'CYS', 'NE', 'ARG', 7.82), ('CA', 'CYS', 'CZ', 'ARG', 6.98), ('CA', 'CYS', 'NH1', 'ARG', 6.34), ('CA', 'CYS', 'NH2', 'ARG', 7.2)], [('N', 'CYS', 'CB', 'ARG', 9.25), ('N', 'CYS', 'CG', 'ARG', 9.26), ('N', 'CYS', 'CD', 'ARG', 8.0), ('N', 'CYS', 'NE', 'ARG', 7.26), ('N', 'CYS', 'CZ', 'ARG', 6.34), ('N', 'CYS', 'NH1', 'ARG', 6.02), ('N', 'CYS', 'NH2', 'ARG', 6.22)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TYR_CYS, d, 'A_3pva_3_5_1_11')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TYR_ARG, d, 'A_3pva_3_5_1_11')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASN_CYS, d, 'A_3pva_3_5_1_11')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASN_ARG, d, 'A_3pva_3_5_1_11')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(TYR_ASN, d, 'A_3pva_3_5_1_11')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(CYS_ARG, d, 'A_3pva_3_5_1_11')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TYR_CYS' :  match1,
		'TYR_ARG' :  match2,
		'ASN_CYS' :  match3,
		'ASN_ARG' :  match4,
		'TYR_ASN' :  match5,
		'CYS_ARG' :  match6}