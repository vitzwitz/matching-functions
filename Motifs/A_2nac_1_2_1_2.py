'''
FUNC:A_2nac_1_2_1_2
PDB:2nac
EC:1.2.1.2
RESI:asn,arg,gln,his
LOCI:a-146,284,313,332;
'''
import motifFunctions as cmd
GLN_ASN = { 
	'distances':
		[[18.55, 17.51, 17.7, 16.64, 19.17, 19.84, 19.85, 20.45], [17.97, 16.95, 17.09, 16.17, 18.37, 19.11, 19.22, 19.89], [16.48, 15.47, 15.6, 14.7, 16.87, 17.61, 17.72, 18.4], [16.21, 15.22, 15.29, 14.55, 16.38, 17.17, 17.39, 18.12], [15.63, 14.61, 14.81, 13.76, 16.23, 16.91, 16.92, 17.55], [20.75, 19.66, 19.89, 18.69, 21.63, 22.21, 22.09, 22.57], [20.51, 19.49, 19.75, 18.53, 21.32, 21.96, 21.86, 22.42], [20.03, 19.0, 19.2, 18.12, 20.63, 21.33, 21.33, 21.95], [20.83, 19.75, 19.85, 18.91, 21.32, 22.01, 22.08, 22.67]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'ASN', 18.55), ('CB', 'GLN', 'CG', 'ASN', 17.51), ('CB', 'GLN', 'OD1', 'ASN', 17.7), ('CB', 'GLN', 'ND2', 'ASN', 16.64), ('CB', 'GLN', 'O', 'ASN', 19.17), ('CB', 'GLN', 'C', 'ASN', 19.84), ('CB', 'GLN', 'CA', 'ASN', 19.85), ('CB', 'GLN', 'N', 'ASN', 20.45)], [('CG', 'GLN', 'CB', 'ASN', 17.97), ('CG', 'GLN', 'CG', 'ASN', 16.95), ('CG', 'GLN', 'OD1', 'ASN', 17.09), ('CG', 'GLN', 'ND2', 'ASN', 16.17), ('CG', 'GLN', 'O', 'ASN', 18.37), ('CG', 'GLN', 'C', 'ASN', 19.11), ('CG', 'GLN', 'CA', 'ASN', 19.22), ('CG', 'GLN', 'N', 'ASN', 19.89)], [('CD', 'GLN', 'CB', 'ASN', 16.48), ('CD', 'GLN', 'CG', 'ASN', 15.47), ('CD', 'GLN', 'OD1', 'ASN', 15.6), ('CD', 'GLN', 'ND2', 'ASN', 14.7), ('CD', 'GLN', 'O', 'ASN', 16.87), ('CD', 'GLN', 'C', 'ASN', 17.61), ('CD', 'GLN', 'CA', 'ASN', 17.72), ('CD', 'GLN', 'N', 'ASN', 18.4)], [('OE1', 'GLN', 'CB', 'ASN', 16.21), ('OE1', 'GLN', 'CG', 'ASN', 15.22), ('OE1', 'GLN', 'OD1', 'ASN', 15.29), ('OE1', 'GLN', 'ND2', 'ASN', 14.55), ('OE1', 'GLN', 'O', 'ASN', 16.38), ('OE1', 'GLN', 'C', 'ASN', 17.17), ('OE1', 'GLN', 'CA', 'ASN', 17.39), ('OE1', 'GLN', 'N', 'ASN', 18.12)], [('NE2', 'GLN', 'CB', 'ASN', 15.63), ('NE2', 'GLN', 'CG', 'ASN', 14.61), ('NE2', 'GLN', 'OD1', 'ASN', 14.81), ('NE2', 'GLN', 'ND2', 'ASN', 13.76), ('NE2', 'GLN', 'O', 'ASN', 16.23), ('NE2', 'GLN', 'C', 'ASN', 16.91), ('NE2', 'GLN', 'CA', 'ASN', 16.92), ('NE2', 'GLN', 'N', 'ASN', 17.55)], [('O', 'GLN', 'CB', 'ASN', 20.75), ('O', 'GLN', 'CG', 'ASN', 19.66), ('O', 'GLN', 'OD1', 'ASN', 19.89), ('O', 'GLN', 'ND2', 'ASN', 18.69), ('O', 'GLN', 'O', 'ASN', 21.63), ('O', 'GLN', 'C', 'ASN', 22.21), ('O', 'GLN', 'CA', 'ASN', 22.09), ('O', 'GLN', 'N', 'ASN', 22.57)], [('C', 'GLN', 'CB', 'ASN', 20.51), ('C', 'GLN', 'CG', 'ASN', 19.49), ('C', 'GLN', 'OD1', 'ASN', 19.75), ('C', 'GLN', 'ND2', 'ASN', 18.53), ('C', 'GLN', 'O', 'ASN', 21.32), ('C', 'GLN', 'C', 'ASN', 21.96), ('C', 'GLN', 'CA', 'ASN', 21.86), ('C', 'GLN', 'N', 'ASN', 22.42)], [('CA', 'GLN', 'CB', 'ASN', 20.03), ('CA', 'GLN', 'CG', 'ASN', 19.0), ('CA', 'GLN', 'OD1', 'ASN', 19.2), ('CA', 'GLN', 'ND2', 'ASN', 18.12), ('CA', 'GLN', 'O', 'ASN', 20.63), ('CA', 'GLN', 'C', 'ASN', 21.33), ('CA', 'GLN', 'CA', 'ASN', 21.33), ('CA', 'GLN', 'N', 'ASN', 21.95)], [('N', 'GLN', 'CB', 'ASN', 20.83), ('N', 'GLN', 'CG', 'ASN', 19.75), ('N', 'GLN', 'OD1', 'ASN', 19.85), ('N', 'GLN', 'ND2', 'ASN', 18.91), ('N', 'GLN', 'O', 'ASN', 21.32), ('N', 'GLN', 'C', 'ASN', 22.01), ('N', 'GLN', 'CA', 'ASN', 22.08), ('N', 'GLN', 'N', 'ASN', 22.67)]]}
HIS_ARG = { 
	'distances':
		[[11.98, 11.94, 10.89, 10.79, 10.23, 9.3, 10.74, 12.32, 11.28, 10.94, 11.28], [11.03, 10.83, 9.79, 9.56, 8.88, 7.92, 9.35, 11.67, 10.61, 10.06, 10.32], [10.57, 10.22, 9.03, 8.66, 7.98, 7.2, 8.34, 11.61, 10.48, 9.8, 10.2], [10.78, 10.52, 9.64, 9.37, 8.58, 7.46, 9.06, 11.38, 10.4, 9.74, 9.79], [9.97, 9.47, 8.36, 7.84, 7.0, 6.13, 7.31, 11.22, 10.12, 9.25, 9.51], [10.07, 9.62, 8.71, 8.26, 7.36, 6.26, 7.74, 11.07, 10.06, 9.19, 9.22], [14.4, 14.16, 13.12, 12.76, 11.94, 10.98, 12.17, 14.86, 13.86, 13.37, 13.52], [13.86, 13.72, 12.78, 12.53, 11.75, 10.7, 12.11, 14.1, 13.16, 12.73, 12.81], [12.9, 12.91, 12.0, 11.92, 11.29, 10.24, 11.82, 12.95, 12.01, 11.72, 11.89], [13.7, 13.85, 12.93, 12.98, 12.46, 11.45, 13.04, 13.5, 12.59, 12.49, 12.74]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 11.98), ('CB', 'HIS', 'CG', 'ARG', 11.94), ('CB', 'HIS', 'CD', 'ARG', 10.89), ('CB', 'HIS', 'NE', 'ARG', 10.79), ('CB', 'HIS', 'CZ', 'ARG', 10.23), ('CB', 'HIS', 'NH1', 'ARG', 9.3), ('CB', 'HIS', 'NH2', 'ARG', 10.74), ('CB', 'HIS', 'O', 'ARG', 12.32), ('CB', 'HIS', 'C', 'ARG', 11.28), ('CB', 'HIS', 'CA', 'ARG', 10.94), ('CB', 'HIS', 'N', 'ARG', 11.28)], [('CG', 'HIS', 'CB', 'ARG', 11.03), ('CG', 'HIS', 'CG', 'ARG', 10.83), ('CG', 'HIS', 'CD', 'ARG', 9.79), ('CG', 'HIS', 'NE', 'ARG', 9.56), ('CG', 'HIS', 'CZ', 'ARG', 8.88), ('CG', 'HIS', 'NH1', 'ARG', 7.92), ('CG', 'HIS', 'NH2', 'ARG', 9.35), ('CG', 'HIS', 'O', 'ARG', 11.67), ('CG', 'HIS', 'C', 'ARG', 10.61), ('CG', 'HIS', 'CA', 'ARG', 10.06), ('CG', 'HIS', 'N', 'ARG', 10.32)], [('ND1', 'HIS', 'CB', 'ARG', 10.57), ('ND1', 'HIS', 'CG', 'ARG', 10.22), ('ND1', 'HIS', 'CD', 'ARG', 9.03), ('ND1', 'HIS', 'NE', 'ARG', 8.66), ('ND1', 'HIS', 'CZ', 'ARG', 7.98), ('ND1', 'HIS', 'NH1', 'ARG', 7.2), ('ND1', 'HIS', 'NH2', 'ARG', 8.34), ('ND1', 'HIS', 'O', 'ARG', 11.61), ('ND1', 'HIS', 'C', 'ARG', 10.48), ('ND1', 'HIS', 'CA', 'ARG', 9.8), ('ND1', 'HIS', 'N', 'ARG', 10.2)], [('CD2', 'HIS', 'CB', 'ARG', 10.78), ('CD2', 'HIS', 'CG', 'ARG', 10.52), ('CD2', 'HIS', 'CD', 'ARG', 9.64), ('CD2', 'HIS', 'NE', 'ARG', 9.37), ('CD2', 'HIS', 'CZ', 'ARG', 8.58), ('CD2', 'HIS', 'NH1', 'ARG', 7.46), ('CD2', 'HIS', 'NH2', 'ARG', 9.06), ('CD2', 'HIS', 'O', 'ARG', 11.38), ('CD2', 'HIS', 'C', 'ARG', 10.4), ('CD2', 'HIS', 'CA', 'ARG', 9.74), ('CD2', 'HIS', 'N', 'ARG', 9.79)], [('CE1', 'HIS', 'CB', 'ARG', 9.97), ('CE1', 'HIS', 'CG', 'ARG', 9.47), ('CE1', 'HIS', 'CD', 'ARG', 8.36), ('CE1', 'HIS', 'NE', 'ARG', 7.84), ('CE1', 'HIS', 'CZ', 'ARG', 7.0), ('CE1', 'HIS', 'NH1', 'ARG', 6.13), ('CE1', 'HIS', 'NH2', 'ARG', 7.31), ('CE1', 'HIS', 'O', 'ARG', 11.22), ('CE1', 'HIS', 'C', 'ARG', 10.12), ('CE1', 'HIS', 'CA', 'ARG', 9.25), ('CE1', 'HIS', 'N', 'ARG', 9.51)], [('NE2', 'HIS', 'CB', 'ARG', 10.07), ('NE2', 'HIS', 'CG', 'ARG', 9.62), ('NE2', 'HIS', 'CD', 'ARG', 8.71), ('NE2', 'HIS', 'NE', 'ARG', 8.26), ('NE2', 'HIS', 'CZ', 'ARG', 7.36), ('NE2', 'HIS', 'NH1', 'ARG', 6.26), ('NE2', 'HIS', 'NH2', 'ARG', 7.74), ('NE2', 'HIS', 'O', 'ARG', 11.07), ('NE2', 'HIS', 'C', 'ARG', 10.06), ('NE2', 'HIS', 'CA', 'ARG', 9.19), ('NE2', 'HIS', 'N', 'ARG', 9.22)], [('O', 'HIS', 'CB', 'ARG', 14.4), ('O', 'HIS', 'CG', 'ARG', 14.16), ('O', 'HIS', 'CD', 'ARG', 13.12), ('O', 'HIS', 'NE', 'ARG', 12.76), ('O', 'HIS', 'CZ', 'ARG', 11.94), ('O', 'HIS', 'NH1', 'ARG', 10.98), ('O', 'HIS', 'NH2', 'ARG', 12.17), ('O', 'HIS', 'O', 'ARG', 14.86), ('O', 'HIS', 'C', 'ARG', 13.86), ('O', 'HIS', 'CA', 'ARG', 13.37), ('O', 'HIS', 'N', 'ARG', 13.52)], [('C', 'HIS', 'CB', 'ARG', 13.86), ('C', 'HIS', 'CG', 'ARG', 13.72), ('C', 'HIS', 'CD', 'ARG', 12.78), ('C', 'HIS', 'NE', 'ARG', 12.53), ('C', 'HIS', 'CZ', 'ARG', 11.75), ('C', 'HIS', 'NH1', 'ARG', 10.7), ('C', 'HIS', 'NH2', 'ARG', 12.11), ('C', 'HIS', 'O', 'ARG', 14.1), ('C', 'HIS', 'C', 'ARG', 13.16), ('C', 'HIS', 'CA', 'ARG', 12.73), ('C', 'HIS', 'N', 'ARG', 12.81)], [('CA', 'HIS', 'CB', 'ARG', 12.9), ('CA', 'HIS', 'CG', 'ARG', 12.91), ('CA', 'HIS', 'CD', 'ARG', 12.0), ('CA', 'HIS', 'NE', 'ARG', 11.92), ('CA', 'HIS', 'CZ', 'ARG', 11.29), ('CA', 'HIS', 'NH1', 'ARG', 10.24), ('CA', 'HIS', 'NH2', 'ARG', 11.82), ('CA', 'HIS', 'O', 'ARG', 12.95), ('CA', 'HIS', 'C', 'ARG', 12.01), ('CA', 'HIS', 'CA', 'ARG', 11.72), ('CA', 'HIS', 'N', 'ARG', 11.89)], [('N', 'HIS', 'CB', 'ARG', 13.7), ('N', 'HIS', 'CG', 'ARG', 13.85), ('N', 'HIS', 'CD', 'ARG', 12.93), ('N', 'HIS', 'NE', 'ARG', 12.98), ('N', 'HIS', 'CZ', 'ARG', 12.46), ('N', 'HIS', 'NH1', 'ARG', 11.45), ('N', 'HIS', 'NH2', 'ARG', 13.04), ('N', 'HIS', 'O', 'ARG', 13.5), ('N', 'HIS', 'C', 'ARG', 12.59), ('N', 'HIS', 'CA', 'ARG', 12.49), ('N', 'HIS', 'N', 'ARG', 12.74)]]}
ARG_ASN = { 
	'distances':
		[[17.02, 15.79, 15.22, 15.61, 16.35, 16.99, 17.68, 18.13], [16.08, 14.79, 14.18, 14.59, 15.55, 16.09, 16.73, 17.08], [15.71, 14.38, 13.88, 14.04, 15.46, 15.98, 16.49, 16.82], [14.72, 13.34, 12.84, 12.96, 14.66, 15.09, 15.52, 15.76], [13.43, 12.04, 11.56, 11.64, 13.47, 13.88, 14.25, 14.49], [12.63, 11.31, 10.89, 10.95, 12.56, 13.07, 13.48, 13.86], [12.92, 11.47, 10.99, 11.03, 13.2, 13.48, 13.74, 13.85], [18.28, 17.23, 16.72, 17.14, 17.28, 18.09, 18.91, 19.58], [17.63, 16.55, 16.1, 16.37, 16.82, 17.61, 18.34, 19.0], [16.41, 15.27, 14.78, 15.1, 15.66, 16.39, 17.11, 17.69], [15.71, 14.64, 14.08, 14.59, 14.74, 15.5, 16.31, 16.93]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASN', 17.02), ('CB', 'ARG', 'CG', 'ASN', 15.79), ('CB', 'ARG', 'OD1', 'ASN', 15.22), ('CB', 'ARG', 'ND2', 'ASN', 15.61), ('CB', 'ARG', 'O', 'ASN', 16.35), ('CB', 'ARG', 'C', 'ASN', 16.99), ('CB', 'ARG', 'CA', 'ASN', 17.68), ('CB', 'ARG', 'N', 'ASN', 18.13)], [('CG', 'ARG', 'CB', 'ASN', 16.08), ('CG', 'ARG', 'CG', 'ASN', 14.79), ('CG', 'ARG', 'OD1', 'ASN', 14.18), ('CG', 'ARG', 'ND2', 'ASN', 14.59), ('CG', 'ARG', 'O', 'ASN', 15.55), ('CG', 'ARG', 'C', 'ASN', 16.09), ('CG', 'ARG', 'CA', 'ASN', 16.73), ('CG', 'ARG', 'N', 'ASN', 17.08)], [('CD', 'ARG', 'CB', 'ASN', 15.71), ('CD', 'ARG', 'CG', 'ASN', 14.38), ('CD', 'ARG', 'OD1', 'ASN', 13.88), ('CD', 'ARG', 'ND2', 'ASN', 14.04), ('CD', 'ARG', 'O', 'ASN', 15.46), ('CD', 'ARG', 'C', 'ASN', 15.98), ('CD', 'ARG', 'CA', 'ASN', 16.49), ('CD', 'ARG', 'N', 'ASN', 16.82)], [('NE', 'ARG', 'CB', 'ASN', 14.72), ('NE', 'ARG', 'CG', 'ASN', 13.34), ('NE', 'ARG', 'OD1', 'ASN', 12.84), ('NE', 'ARG', 'ND2', 'ASN', 12.96), ('NE', 'ARG', 'O', 'ASN', 14.66), ('NE', 'ARG', 'C', 'ASN', 15.09), ('NE', 'ARG', 'CA', 'ASN', 15.52), ('NE', 'ARG', 'N', 'ASN', 15.76)], [('CZ', 'ARG', 'CB', 'ASN', 13.43), ('CZ', 'ARG', 'CG', 'ASN', 12.04), ('CZ', 'ARG', 'OD1', 'ASN', 11.56), ('CZ', 'ARG', 'ND2', 'ASN', 11.64), ('CZ', 'ARG', 'O', 'ASN', 13.47), ('CZ', 'ARG', 'C', 'ASN', 13.88), ('CZ', 'ARG', 'CA', 'ASN', 14.25), ('CZ', 'ARG', 'N', 'ASN', 14.49)], [('NH1', 'ARG', 'CB', 'ASN', 12.63), ('NH1', 'ARG', 'CG', 'ASN', 11.31), ('NH1', 'ARG', 'OD1', 'ASN', 10.89), ('NH1', 'ARG', 'ND2', 'ASN', 10.95), ('NH1', 'ARG', 'O', 'ASN', 12.56), ('NH1', 'ARG', 'C', 'ASN', 13.07), ('NH1', 'ARG', 'CA', 'ASN', 13.48), ('NH1', 'ARG', 'N', 'ASN', 13.86)], [('NH2', 'ARG', 'CB', 'ASN', 12.92), ('NH2', 'ARG', 'CG', 'ASN', 11.47), ('NH2', 'ARG', 'OD1', 'ASN', 10.99), ('NH2', 'ARG', 'ND2', 'ASN', 11.03), ('NH2', 'ARG', 'O', 'ASN', 13.2), ('NH2', 'ARG', 'C', 'ASN', 13.48), ('NH2', 'ARG', 'CA', 'ASN', 13.74), ('NH2', 'ARG', 'N', 'ASN', 13.85)], [('O', 'ARG', 'CB', 'ASN', 18.28), ('O', 'ARG', 'CG', 'ASN', 17.23), ('O', 'ARG', 'OD1', 'ASN', 16.72), ('O', 'ARG', 'ND2', 'ASN', 17.14), ('O', 'ARG', 'O', 'ASN', 17.28), ('O', 'ARG', 'C', 'ASN', 18.09), ('O', 'ARG', 'CA', 'ASN', 18.91), ('O', 'ARG', 'N', 'ASN', 19.58)], [('C', 'ARG', 'CB', 'ASN', 17.63), ('C', 'ARG', 'CG', 'ASN', 16.55), ('C', 'ARG', 'OD1', 'ASN', 16.1), ('C', 'ARG', 'ND2', 'ASN', 16.37), ('C', 'ARG', 'O', 'ASN', 16.82), ('C', 'ARG', 'C', 'ASN', 17.61), ('C', 'ARG', 'CA', 'ASN', 18.34), ('C', 'ARG', 'N', 'ASN', 19.0)], [('CA', 'ARG', 'CB', 'ASN', 16.41), ('CA', 'ARG', 'CG', 'ASN', 15.27), ('CA', 'ARG', 'OD1', 'ASN', 14.78), ('CA', 'ARG', 'ND2', 'ASN', 15.1), ('CA', 'ARG', 'O', 'ASN', 15.66), ('CA', 'ARG', 'C', 'ASN', 16.39), ('CA', 'ARG', 'CA', 'ASN', 17.11), ('CA', 'ARG', 'N', 'ASN', 17.69)], [('N', 'ARG', 'CB', 'ASN', 15.71), ('N', 'ARG', 'CG', 'ASN', 14.64), ('N', 'ARG', 'OD1', 'ASN', 14.08), ('N', 'ARG', 'ND2', 'ASN', 14.59), ('N', 'ARG', 'O', 'ASN', 14.74), ('N', 'ARG', 'C', 'ASN', 15.5), ('N', 'ARG', 'CA', 'ASN', 16.31), ('N', 'ARG', 'N', 'ASN', 16.93)]]}
GLN_HIS = { 
	'distances':
		[[7.7, 8.12, 7.61, 9.29, 8.61, 9.55, 9.98, 10.06, 9.03, 8.92], [7.02, 7.39, 7.06, 8.45, 7.98, 8.76, 9.61, 9.48, 8.29, 8.23], [5.83, 5.97, 5.61, 6.99, 6.5, 7.26, 8.5, 8.33, 7.19, 7.41], [5.82, 5.84, 5.72, 6.61, 6.4, 6.92, 8.65, 8.27, 7.01, 7.3], [5.29, 5.3, 4.68, 6.45, 5.7, 6.64, 7.67, 7.7, 6.8, 7.2], [10.32, 10.77, 10.08, 12.0, 11.07, 12.16, 12.17, 12.49, 11.65, 11.43], [9.61, 10.22, 9.7, 11.47, 10.78, 11.78, 11.5, 11.76, 10.84, 10.5], [8.93, 9.5, 9.08, 10.68, 10.1, 11.01, 11.14, 11.22, 10.15, 9.83], [9.96, 10.39, 9.9, 11.48, 10.8, 11.7, 12.34, 12.35, 11.2, 10.94]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'HIS', 7.7), ('CB', 'GLN', 'CG', 'HIS', 8.12), ('CB', 'GLN', 'ND1', 'HIS', 7.61), ('CB', 'GLN', 'CD2', 'HIS', 9.29), ('CB', 'GLN', 'CE1', 'HIS', 8.61), ('CB', 'GLN', 'NE2', 'HIS', 9.55), ('CB', 'GLN', 'O', 'HIS', 9.98), ('CB', 'GLN', 'C', 'HIS', 10.06), ('CB', 'GLN', 'CA', 'HIS', 9.03), ('CB', 'GLN', 'N', 'HIS', 8.92)], [('CG', 'GLN', 'CB', 'HIS', 7.02), ('CG', 'GLN', 'CG', 'HIS', 7.39), ('CG', 'GLN', 'ND1', 'HIS', 7.06), ('CG', 'GLN', 'CD2', 'HIS', 8.45), ('CG', 'GLN', 'CE1', 'HIS', 7.98), ('CG', 'GLN', 'NE2', 'HIS', 8.76), ('CG', 'GLN', 'O', 'HIS', 9.61), ('CG', 'GLN', 'C', 'HIS', 9.48), ('CG', 'GLN', 'CA', 'HIS', 8.29), ('CG', 'GLN', 'N', 'HIS', 8.23)], [('CD', 'GLN', 'CB', 'HIS', 5.83), ('CD', 'GLN', 'CG', 'HIS', 5.97), ('CD', 'GLN', 'ND1', 'HIS', 5.61), ('CD', 'GLN', 'CD2', 'HIS', 6.99), ('CD', 'GLN', 'CE1', 'HIS', 6.5), ('CD', 'GLN', 'NE2', 'HIS', 7.26), ('CD', 'GLN', 'O', 'HIS', 8.5), ('CD', 'GLN', 'C', 'HIS', 8.33), ('CD', 'GLN', 'CA', 'HIS', 7.19), ('CD', 'GLN', 'N', 'HIS', 7.41)], [('OE1', 'GLN', 'CB', 'HIS', 5.82), ('OE1', 'GLN', 'CG', 'HIS', 5.84), ('OE1', 'GLN', 'ND1', 'HIS', 5.72), ('OE1', 'GLN', 'CD2', 'HIS', 6.61), ('OE1', 'GLN', 'CE1', 'HIS', 6.4), ('OE1', 'GLN', 'NE2', 'HIS', 6.92), ('OE1', 'GLN', 'O', 'HIS', 8.65), ('OE1', 'GLN', 'C', 'HIS', 8.27), ('OE1', 'GLN', 'CA', 'HIS', 7.01), ('OE1', 'GLN', 'N', 'HIS', 7.3)], [('NE2', 'GLN', 'CB', 'HIS', 5.29), ('NE2', 'GLN', 'CG', 'HIS', 5.3), ('NE2', 'GLN', 'ND1', 'HIS', 4.68), ('NE2', 'GLN', 'CD2', 'HIS', 6.45), ('NE2', 'GLN', 'CE1', 'HIS', 5.7), ('NE2', 'GLN', 'NE2', 'HIS', 6.64), ('NE2', 'GLN', 'O', 'HIS', 7.67), ('NE2', 'GLN', 'C', 'HIS', 7.7), ('NE2', 'GLN', 'CA', 'HIS', 6.8), ('NE2', 'GLN', 'N', 'HIS', 7.2)], [('O', 'GLN', 'CB', 'HIS', 10.32), ('O', 'GLN', 'CG', 'HIS', 10.77), ('O', 'GLN', 'ND1', 'HIS', 10.08), ('O', 'GLN', 'CD2', 'HIS', 12.0), ('O', 'GLN', 'CE1', 'HIS', 11.07), ('O', 'GLN', 'NE2', 'HIS', 12.16), ('O', 'GLN', 'O', 'HIS', 12.17), ('O', 'GLN', 'C', 'HIS', 12.49), ('O', 'GLN', 'CA', 'HIS', 11.65), ('O', 'GLN', 'N', 'HIS', 11.43)], [('C', 'GLN', 'CB', 'HIS', 9.61), ('C', 'GLN', 'CG', 'HIS', 10.22), ('C', 'GLN', 'ND1', 'HIS', 9.7), ('C', 'GLN', 'CD2', 'HIS', 11.47), ('C', 'GLN', 'CE1', 'HIS', 10.78), ('C', 'GLN', 'NE2', 'HIS', 11.78), ('C', 'GLN', 'O', 'HIS', 11.5), ('C', 'GLN', 'C', 'HIS', 11.76), ('C', 'GLN', 'CA', 'HIS', 10.84), ('C', 'GLN', 'N', 'HIS', 10.5)], [('CA', 'GLN', 'CB', 'HIS', 8.93), ('CA', 'GLN', 'CG', 'HIS', 9.5), ('CA', 'GLN', 'ND1', 'HIS', 9.08), ('CA', 'GLN', 'CD2', 'HIS', 10.68), ('CA', 'GLN', 'CE1', 'HIS', 10.1), ('CA', 'GLN', 'NE2', 'HIS', 11.01), ('CA', 'GLN', 'O', 'HIS', 11.14), ('CA', 'GLN', 'C', 'HIS', 11.22), ('CA', 'GLN', 'CA', 'HIS', 10.15), ('CA', 'GLN', 'N', 'HIS', 9.83)], [('N', 'GLN', 'CB', 'HIS', 9.96), ('N', 'GLN', 'CG', 'HIS', 10.39), ('N', 'GLN', 'ND1', 'HIS', 9.9), ('N', 'GLN', 'CD2', 'HIS', 11.48), ('N', 'GLN', 'CE1', 'HIS', 10.8), ('N', 'GLN', 'NE2', 'HIS', 11.7), ('N', 'GLN', 'O', 'HIS', 12.34), ('N', 'GLN', 'C', 'HIS', 12.35), ('N', 'GLN', 'CA', 'HIS', 11.2), ('N', 'GLN', 'N', 'HIS', 10.94)]]}
GLN_ARG = { 
	'distances':
		[[11.53, 11.73, 10.44, 10.72, 10.88, 10.71, 11.5, 12.13, 11.01, 11.07, 12.15], [10.49, 10.81, 9.64, 10.04, 10.23, 9.91, 11.0, 10.85, 9.74, 9.87, 10.91], [9.89, 10.06, 8.86, 9.13, 9.14, 8.69, 9.89, 10.42, 9.27, 9.18, 10.08], [9.11, 9.41, 8.36, 8.77, 8.8, 8.22, 9.71, 9.38, 8.27, 8.24, 9.07], [10.46, 10.4, 9.1, 9.1, 8.91, 8.46, 9.47, 11.29, 10.11, 9.8, 10.62], [13.72, 13.83, 12.48, 12.65, 12.91, 13.0, 13.32, 14.56, 13.46, 13.53, 14.72], [13.67, 13.87, 12.57, 12.81, 13.03, 12.98, 13.53, 14.26, 13.18, 13.32, 14.48], [12.46, 12.79, 11.56, 11.94, 12.22, 12.09, 12.86, 12.86, 11.8, 12.03, 13.18], [11.96, 12.38, 11.23, 11.75, 12.21, 12.2, 12.93, 12.33, 11.33, 11.67, 12.91]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'ARG', 11.53), ('CB', 'GLN', 'CG', 'ARG', 11.73), ('CB', 'GLN', 'CD', 'ARG', 10.44), ('CB', 'GLN', 'NE', 'ARG', 10.72), ('CB', 'GLN', 'CZ', 'ARG', 10.88), ('CB', 'GLN', 'NH1', 'ARG', 10.71), ('CB', 'GLN', 'NH2', 'ARG', 11.5), ('CB', 'GLN', 'O', 'ARG', 12.13), ('CB', 'GLN', 'C', 'ARG', 11.01), ('CB', 'GLN', 'CA', 'ARG', 11.07), ('CB', 'GLN', 'N', 'ARG', 12.15)], [('CG', 'GLN', 'CB', 'ARG', 10.49), ('CG', 'GLN', 'CG', 'ARG', 10.81), ('CG', 'GLN', 'CD', 'ARG', 9.64), ('CG', 'GLN', 'NE', 'ARG', 10.04), ('CG', 'GLN', 'CZ', 'ARG', 10.23), ('CG', 'GLN', 'NH1', 'ARG', 9.91), ('CG', 'GLN', 'NH2', 'ARG', 11.0), ('CG', 'GLN', 'O', 'ARG', 10.85), ('CG', 'GLN', 'C', 'ARG', 9.74), ('CG', 'GLN', 'CA', 'ARG', 9.87), ('CG', 'GLN', 'N', 'ARG', 10.91)], [('CD', 'GLN', 'CB', 'ARG', 9.89), ('CD', 'GLN', 'CG', 'ARG', 10.06), ('CD', 'GLN', 'CD', 'ARG', 8.86), ('CD', 'GLN', 'NE', 'ARG', 9.13), ('CD', 'GLN', 'CZ', 'ARG', 9.14), ('CD', 'GLN', 'NH1', 'ARG', 8.69), ('CD', 'GLN', 'NH2', 'ARG', 9.89), ('CD', 'GLN', 'O', 'ARG', 10.42), ('CD', 'GLN', 'C', 'ARG', 9.27), ('CD', 'GLN', 'CA', 'ARG', 9.18), ('CD', 'GLN', 'N', 'ARG', 10.08)], [('OE1', 'GLN', 'CB', 'ARG', 9.11), ('OE1', 'GLN', 'CG', 'ARG', 9.41), ('OE1', 'GLN', 'CD', 'ARG', 8.36), ('OE1', 'GLN', 'NE', 'ARG', 8.77), ('OE1', 'GLN', 'CZ', 'ARG', 8.8), ('OE1', 'GLN', 'NH1', 'ARG', 8.22), ('OE1', 'GLN', 'NH2', 'ARG', 9.71), ('OE1', 'GLN', 'O', 'ARG', 9.38), ('OE1', 'GLN', 'C', 'ARG', 8.27), ('OE1', 'GLN', 'CA', 'ARG', 8.24), ('OE1', 'GLN', 'N', 'ARG', 9.07)], [('NE2', 'GLN', 'CB', 'ARG', 10.46), ('NE2', 'GLN', 'CG', 'ARG', 10.4), ('NE2', 'GLN', 'CD', 'ARG', 9.1), ('NE2', 'GLN', 'NE', 'ARG', 9.1), ('NE2', 'GLN', 'CZ', 'ARG', 8.91), ('NE2', 'GLN', 'NH1', 'ARG', 8.46), ('NE2', 'GLN', 'NH2', 'ARG', 9.47), ('NE2', 'GLN', 'O', 'ARG', 11.29), ('NE2', 'GLN', 'C', 'ARG', 10.11), ('NE2', 'GLN', 'CA', 'ARG', 9.8), ('NE2', 'GLN', 'N', 'ARG', 10.62)], [('O', 'GLN', 'CB', 'ARG', 13.72), ('O', 'GLN', 'CG', 'ARG', 13.83), ('O', 'GLN', 'CD', 'ARG', 12.48), ('O', 'GLN', 'NE', 'ARG', 12.65), ('O', 'GLN', 'CZ', 'ARG', 12.91), ('O', 'GLN', 'NH1', 'ARG', 13.0), ('O', 'GLN', 'NH2', 'ARG', 13.32), ('O', 'GLN', 'O', 'ARG', 14.56), ('O', 'GLN', 'C', 'ARG', 13.46), ('O', 'GLN', 'CA', 'ARG', 13.53), ('O', 'GLN', 'N', 'ARG', 14.72)], [('C', 'GLN', 'CB', 'ARG', 13.67), ('C', 'GLN', 'CG', 'ARG', 13.87), ('C', 'GLN', 'CD', 'ARG', 12.57), ('C', 'GLN', 'NE', 'ARG', 12.81), ('C', 'GLN', 'CZ', 'ARG', 13.03), ('C', 'GLN', 'NH1', 'ARG', 12.98), ('C', 'GLN', 'NH2', 'ARG', 13.53), ('C', 'GLN', 'O', 'ARG', 14.26), ('C', 'GLN', 'C', 'ARG', 13.18), ('C', 'GLN', 'CA', 'ARG', 13.32), ('C', 'GLN', 'N', 'ARG', 14.48)], [('CA', 'GLN', 'CB', 'ARG', 12.46), ('CA', 'GLN', 'CG', 'ARG', 12.79), ('CA', 'GLN', 'CD', 'ARG', 11.56), ('CA', 'GLN', 'NE', 'ARG', 11.94), ('CA', 'GLN', 'CZ', 'ARG', 12.22), ('CA', 'GLN', 'NH1', 'ARG', 12.09), ('CA', 'GLN', 'NH2', 'ARG', 12.86), ('CA', 'GLN', 'O', 'ARG', 12.86), ('CA', 'GLN', 'C', 'ARG', 11.8), ('CA', 'GLN', 'CA', 'ARG', 12.03), ('CA', 'GLN', 'N', 'ARG', 13.18)], [('N', 'GLN', 'CB', 'ARG', 11.96), ('N', 'GLN', 'CG', 'ARG', 12.38), ('N', 'GLN', 'CD', 'ARG', 11.23), ('N', 'GLN', 'NE', 'ARG', 11.75), ('N', 'GLN', 'CZ', 'ARG', 12.21), ('N', 'GLN', 'NH1', 'ARG', 12.2), ('N', 'GLN', 'NH2', 'ARG', 12.93), ('N', 'GLN', 'O', 'ARG', 12.33), ('N', 'GLN', 'C', 'ARG', 11.33), ('N', 'GLN', 'CA', 'ARG', 11.67), ('N', 'GLN', 'N', 'ARG', 12.91)]]}
HIS_ASN = { 
	'distances':
		[[13.68, 12.95, 13.34, 12.17, 14.19, 15.0, 14.99, 15.86], [12.62, 11.78, 12.08, 11.02, 13.1, 13.87, 13.9, 14.71], [12.76, 11.77, 12.02, 10.95, 13.41, 14.08, 14.06, 14.72], [11.62, 10.8, 11.05, 10.16, 11.91, 12.72, 12.84, 13.7], [11.85, 10.78, 10.92, 10.02, 12.41, 13.04, 13.09, 13.71], [11.1, 10.12, 10.25, 9.48, 11.43, 12.16, 12.29, 13.03], [12.4, 11.92, 12.58, 11.04, 13.31, 14.06, 13.8, 14.71], [12.39, 11.94, 12.53, 11.18, 13.01, 13.85, 13.73, 14.72], [13.38, 12.84, 13.3, 12.13, 13.78, 14.67, 14.67, 15.67], [14.71, 14.23, 14.72, 13.51, 15.09, 16.01, 16.0, 17.03]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 13.68), ('CB', 'HIS', 'CG', 'ASN', 12.95), ('CB', 'HIS', 'OD1', 'ASN', 13.34), ('CB', 'HIS', 'ND2', 'ASN', 12.17), ('CB', 'HIS', 'O', 'ASN', 14.19), ('CB', 'HIS', 'C', 'ASN', 15.0), ('CB', 'HIS', 'CA', 'ASN', 14.99), ('CB', 'HIS', 'N', 'ASN', 15.86)], [('CG', 'HIS', 'CB', 'ASN', 12.62), ('CG', 'HIS', 'CG', 'ASN', 11.78), ('CG', 'HIS', 'OD1', 'ASN', 12.08), ('CG', 'HIS', 'ND2', 'ASN', 11.02), ('CG', 'HIS', 'O', 'ASN', 13.1), ('CG', 'HIS', 'C', 'ASN', 13.87), ('CG', 'HIS', 'CA', 'ASN', 13.9), ('CG', 'HIS', 'N', 'ASN', 14.71)], [('ND1', 'HIS', 'CB', 'ASN', 12.76), ('ND1', 'HIS', 'CG', 'ASN', 11.77), ('ND1', 'HIS', 'OD1', 'ASN', 12.02), ('ND1', 'HIS', 'ND2', 'ASN', 10.95), ('ND1', 'HIS', 'O', 'ASN', 13.41), ('ND1', 'HIS', 'C', 'ASN', 14.08), ('ND1', 'HIS', 'CA', 'ASN', 14.06), ('ND1', 'HIS', 'N', 'ASN', 14.72)], [('CD2', 'HIS', 'CB', 'ASN', 11.62), ('CD2', 'HIS', 'CG', 'ASN', 10.8), ('CD2', 'HIS', 'OD1', 'ASN', 11.05), ('CD2', 'HIS', 'ND2', 'ASN', 10.16), ('CD2', 'HIS', 'O', 'ASN', 11.91), ('CD2', 'HIS', 'C', 'ASN', 12.72), ('CD2', 'HIS', 'CA', 'ASN', 12.84), ('CD2', 'HIS', 'N', 'ASN', 13.7)], [('CE1', 'HIS', 'CB', 'ASN', 11.85), ('CE1', 'HIS', 'CG', 'ASN', 10.78), ('CE1', 'HIS', 'OD1', 'ASN', 10.92), ('CE1', 'HIS', 'ND2', 'ASN', 10.02), ('CE1', 'HIS', 'O', 'ASN', 12.41), ('CE1', 'HIS', 'C', 'ASN', 13.04), ('CE1', 'HIS', 'CA', 'ASN', 13.09), ('CE1', 'HIS', 'N', 'ASN', 13.71)], [('NE2', 'HIS', 'CB', 'ASN', 11.1), ('NE2', 'HIS', 'CG', 'ASN', 10.12), ('NE2', 'HIS', 'OD1', 'ASN', 10.25), ('NE2', 'HIS', 'ND2', 'ASN', 9.48), ('NE2', 'HIS', 'O', 'ASN', 11.43), ('NE2', 'HIS', 'C', 'ASN', 12.16), ('NE2', 'HIS', 'CA', 'ASN', 12.29), ('NE2', 'HIS', 'N', 'ASN', 13.03)], [('O', 'HIS', 'CB', 'ASN', 12.4), ('O', 'HIS', 'CG', 'ASN', 11.92), ('O', 'HIS', 'OD1', 'ASN', 12.58), ('O', 'HIS', 'ND2', 'ASN', 11.04), ('O', 'HIS', 'O', 'ASN', 13.31), ('O', 'HIS', 'C', 'ASN', 14.06), ('O', 'HIS', 'CA', 'ASN', 13.8), ('O', 'HIS', 'N', 'ASN', 14.71)], [('C', 'HIS', 'CB', 'ASN', 12.39), ('C', 'HIS', 'CG', 'ASN', 11.94), ('C', 'HIS', 'OD1', 'ASN', 12.53), ('C', 'HIS', 'ND2', 'ASN', 11.18), ('C', 'HIS', 'O', 'ASN', 13.01), ('C', 'HIS', 'C', 'ASN', 13.85), ('C', 'HIS', 'CA', 'ASN', 13.73), ('C', 'HIS', 'N', 'ASN', 14.72)], [('CA', 'HIS', 'CB', 'ASN', 13.38), ('CA', 'HIS', 'CG', 'ASN', 12.84), ('CA', 'HIS', 'OD1', 'ASN', 13.3), ('CA', 'HIS', 'ND2', 'ASN', 12.13), ('CA', 'HIS', 'O', 'ASN', 13.78), ('CA', 'HIS', 'C', 'ASN', 14.67), ('CA', 'HIS', 'CA', 'ASN', 14.67), ('CA', 'HIS', 'N', 'ASN', 15.67)], [('N', 'HIS', 'CB', 'ASN', 14.71), ('N', 'HIS', 'CG', 'ASN', 14.23), ('N', 'HIS', 'OD1', 'ASN', 14.72), ('N', 'HIS', 'ND2', 'ASN', 13.51), ('N', 'HIS', 'O', 'ASN', 15.09), ('N', 'HIS', 'C', 'ASN', 16.01), ('N', 'HIS', 'CA', 'ASN', 16.0), ('N', 'HIS', 'N', 'ASN', 17.03)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLN_ASN, d, 'A_2nac_1_2_1_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ARG, d, 'A_2nac_1_2_1_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_ASN, d, 'A_2nac_1_2_1_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLN_HIS, d, 'A_2nac_1_2_1_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLN_ARG, d, 'A_2nac_1_2_1_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(HIS_ASN, d, 'A_2nac_1_2_1_2')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLN_ASN' :  match1,
		'HIS_ARG' :  match2,
		'ARG_ASN' :  match3,
		'GLN_HIS' :  match4,
		'GLN_ARG' :  match5,
		'HIS_ASN' :  match6}