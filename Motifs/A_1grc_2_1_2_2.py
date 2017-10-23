'''
FUNC:A_1grc_2_1_2_2
PDB:1grc
EC:2.1.2.2
RESI:asn,his,ser,asp
LOCI:a-106,108,135,144;
'''
import motifFunctions as cmd
HIS_ASP = { 
	'distances':
		[[10.24, 9.13, 8.51, 9.09, 9.79, 10.88, 11.31, 12.62], [8.73, 7.63, 7.06, 7.64, 8.42, 9.47, 9.83, 11.13], [8.11, 6.9, 6.52, 6.66, 8.31, 9.22, 9.32, 10.6], [7.97, 7.05, 6.39, 7.34, 7.27, 8.4, 8.93, 10.21], [6.79, 5.64, 5.32, 5.53, 7.11, 7.97, 8.02, 9.29], [6.68, 5.76, 5.22, 6.06, 6.33, 7.37, 7.73, 9.01], [13.15, 11.9, 11.22, 11.74, 12.68, 13.75, 14.18, 15.54], [12.44, 11.21, 10.65, 10.96, 12.2, 13.24, 13.56, 14.89], [10.98, 9.71, 9.15, 9.47, 10.81, 11.82, 12.09, 13.43], [11.01, 9.63, 8.94, 9.4, 10.75, 11.7, 11.99, 13.39]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 10.24), ('CB', 'HIS', 'CG', 'ASP', 9.13), ('CB', 'HIS', 'OD1', 'ASP', 8.51), ('CB', 'HIS', 'OD2', 'ASP', 9.09), ('CB', 'HIS', 'O', 'ASP', 9.79), ('CB', 'HIS', 'C', 'ASP', 10.88), ('CB', 'HIS', 'CA', 'ASP', 11.31), ('CB', 'HIS', 'N', 'ASP', 12.62)], [('CG', 'HIS', 'CB', 'ASP', 8.73), ('CG', 'HIS', 'CG', 'ASP', 7.63), ('CG', 'HIS', 'OD1', 'ASP', 7.06), ('CG', 'HIS', 'OD2', 'ASP', 7.64), ('CG', 'HIS', 'O', 'ASP', 8.42), ('CG', 'HIS', 'C', 'ASP', 9.47), ('CG', 'HIS', 'CA', 'ASP', 9.83), ('CG', 'HIS', 'N', 'ASP', 11.13)], [('ND1', 'HIS', 'CB', 'ASP', 8.11), ('ND1', 'HIS', 'CG', 'ASP', 6.9), ('ND1', 'HIS', 'OD1', 'ASP', 6.52), ('ND1', 'HIS', 'OD2', 'ASP', 6.66), ('ND1', 'HIS', 'O', 'ASP', 8.31), ('ND1', 'HIS', 'C', 'ASP', 9.22), ('ND1', 'HIS', 'CA', 'ASP', 9.32), ('ND1', 'HIS', 'N', 'ASP', 10.6)], [('CD2', 'HIS', 'CB', 'ASP', 7.97), ('CD2', 'HIS', 'CG', 'ASP', 7.05), ('CD2', 'HIS', 'OD1', 'ASP', 6.39), ('CD2', 'HIS', 'OD2', 'ASP', 7.34), ('CD2', 'HIS', 'O', 'ASP', 7.27), ('CD2', 'HIS', 'C', 'ASP', 8.4), ('CD2', 'HIS', 'CA', 'ASP', 8.93), ('CD2', 'HIS', 'N', 'ASP', 10.21)], [('CE1', 'HIS', 'CB', 'ASP', 6.79), ('CE1', 'HIS', 'CG', 'ASP', 5.64), ('CE1', 'HIS', 'OD1', 'ASP', 5.32), ('CE1', 'HIS', 'OD2', 'ASP', 5.53), ('CE1', 'HIS', 'O', 'ASP', 7.11), ('CE1', 'HIS', 'C', 'ASP', 7.97), ('CE1', 'HIS', 'CA', 'ASP', 8.02), ('CE1', 'HIS', 'N', 'ASP', 9.29)], [('NE2', 'HIS', 'CB', 'ASP', 6.68), ('NE2', 'HIS', 'CG', 'ASP', 5.76), ('NE2', 'HIS', 'OD1', 'ASP', 5.22), ('NE2', 'HIS', 'OD2', 'ASP', 6.06), ('NE2', 'HIS', 'O', 'ASP', 6.33), ('NE2', 'HIS', 'C', 'ASP', 7.37), ('NE2', 'HIS', 'CA', 'ASP', 7.73), ('NE2', 'HIS', 'N', 'ASP', 9.01)], [('O', 'HIS', 'CB', 'ASP', 13.15), ('O', 'HIS', 'CG', 'ASP', 11.9), ('O', 'HIS', 'OD1', 'ASP', 11.22), ('O', 'HIS', 'OD2', 'ASP', 11.74), ('O', 'HIS', 'O', 'ASP', 12.68), ('O', 'HIS', 'C', 'ASP', 13.75), ('O', 'HIS', 'CA', 'ASP', 14.18), ('O', 'HIS', 'N', 'ASP', 15.54)], [('C', 'HIS', 'CB', 'ASP', 12.44), ('C', 'HIS', 'CG', 'ASP', 11.21), ('C', 'HIS', 'OD1', 'ASP', 10.65), ('C', 'HIS', 'OD2', 'ASP', 10.96), ('C', 'HIS', 'O', 'ASP', 12.2), ('C', 'HIS', 'C', 'ASP', 13.24), ('C', 'HIS', 'CA', 'ASP', 13.56), ('C', 'HIS', 'N', 'ASP', 14.89)], [('CA', 'HIS', 'CB', 'ASP', 10.98), ('CA', 'HIS', 'CG', 'ASP', 9.71), ('CA', 'HIS', 'OD1', 'ASP', 9.15), ('CA', 'HIS', 'OD2', 'ASP', 9.47), ('CA', 'HIS', 'O', 'ASP', 10.81), ('CA', 'HIS', 'C', 'ASP', 11.82), ('CA', 'HIS', 'CA', 'ASP', 12.09), ('CA', 'HIS', 'N', 'ASP', 13.43)], [('N', 'HIS', 'CB', 'ASP', 11.01), ('N', 'HIS', 'CG', 'ASP', 9.63), ('N', 'HIS', 'OD1', 'ASP', 8.94), ('N', 'HIS', 'OD2', 'ASP', 9.4), ('N', 'HIS', 'O', 'ASP', 10.75), ('N', 'HIS', 'C', 'ASP', 11.7), ('N', 'HIS', 'CA', 'ASP', 11.99), ('N', 'HIS', 'N', 'ASP', 13.39)]]}
ASN_ASP = { 
	'distances':
		[[8.63, 7.2, 6.76, 6.78, 9.25, 9.44, 9.13, 10.4], [8.44, 6.94, 6.67, 6.28, 9.33, 9.64, 9.25, 10.52], [7.45, 5.93, 5.71, 5.26, 8.39, 8.77, 8.4, 9.68], [9.54, 8.05, 7.86, 7.25, 10.54, 10.89, 10.46, 11.68], [10.33, 8.9, 7.98, 8.85, 9.93, 10.46, 10.71, 12.14], [10.17, 8.67, 7.92, 8.41, 10.18, 10.66, 10.71, 12.11], [9.99, 8.53, 7.95, 8.17, 10.32, 10.59, 10.43, 11.74], [10.53, 9.18, 8.51, 8.99, 10.62, 10.79, 10.72, 12.0]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ASP', 8.63), ('CB', 'ASN', 'CG', 'ASP', 7.2), ('CB', 'ASN', 'OD1', 'ASP', 6.76), ('CB', 'ASN', 'OD2', 'ASP', 6.78), ('CB', 'ASN', 'O', 'ASP', 9.25), ('CB', 'ASN', 'C', 'ASP', 9.44), ('CB', 'ASN', 'CA', 'ASP', 9.13), ('CB', 'ASN', 'N', 'ASP', 10.4)], [('CG', 'ASN', 'CB', 'ASP', 8.44), ('CG', 'ASN', 'CG', 'ASP', 6.94), ('CG', 'ASN', 'OD1', 'ASP', 6.67), ('CG', 'ASN', 'OD2', 'ASP', 6.28), ('CG', 'ASN', 'O', 'ASP', 9.33), ('CG', 'ASN', 'C', 'ASP', 9.64), ('CG', 'ASN', 'CA', 'ASP', 9.25), ('CG', 'ASN', 'N', 'ASP', 10.52)], [('OD1', 'ASN', 'CB', 'ASP', 7.45), ('OD1', 'ASN', 'CG', 'ASP', 5.93), ('OD1', 'ASN', 'OD1', 'ASP', 5.71), ('OD1', 'ASN', 'OD2', 'ASP', 5.26), ('OD1', 'ASN', 'O', 'ASP', 8.39), ('OD1', 'ASN', 'C', 'ASP', 8.77), ('OD1', 'ASN', 'CA', 'ASP', 8.4), ('OD1', 'ASN', 'N', 'ASP', 9.68)], [('ND2', 'ASN', 'CB', 'ASP', 9.54), ('ND2', 'ASN', 'CG', 'ASP', 8.05), ('ND2', 'ASN', 'OD1', 'ASP', 7.86), ('ND2', 'ASN', 'OD2', 'ASP', 7.25), ('ND2', 'ASN', 'O', 'ASP', 10.54), ('ND2', 'ASN', 'C', 'ASP', 10.89), ('ND2', 'ASN', 'CA', 'ASP', 10.46), ('ND2', 'ASN', 'N', 'ASP', 11.68)], [('O', 'ASN', 'CB', 'ASP', 10.33), ('O', 'ASN', 'CG', 'ASP', 8.9), ('O', 'ASN', 'OD1', 'ASP', 7.98), ('O', 'ASN', 'OD2', 'ASP', 8.85), ('O', 'ASN', 'O', 'ASP', 9.93), ('O', 'ASN', 'C', 'ASP', 10.46), ('O', 'ASN', 'CA', 'ASP', 10.71), ('O', 'ASN', 'N', 'ASP', 12.14)], [('C', 'ASN', 'CB', 'ASP', 10.17), ('C', 'ASN', 'CG', 'ASP', 8.67), ('C', 'ASN', 'OD1', 'ASP', 7.92), ('C', 'ASN', 'OD2', 'ASP', 8.41), ('C', 'ASN', 'O', 'ASP', 10.18), ('C', 'ASN', 'C', 'ASP', 10.66), ('C', 'ASN', 'CA', 'ASP', 10.71), ('C', 'ASN', 'N', 'ASP', 12.11)], [('CA', 'ASN', 'CB', 'ASP', 9.99), ('CA', 'ASN', 'CG', 'ASP', 8.53), ('CA', 'ASN', 'OD1', 'ASP', 7.95), ('CA', 'ASN', 'OD2', 'ASP', 8.17), ('CA', 'ASN', 'O', 'ASP', 10.32), ('CA', 'ASN', 'C', 'ASP', 10.59), ('CA', 'ASN', 'CA', 'ASP', 10.43), ('CA', 'ASN', 'N', 'ASP', 11.74)], [('N', 'ASN', 'CB', 'ASP', 10.53), ('N', 'ASN', 'CG', 'ASP', 9.18), ('N', 'ASN', 'OD1', 'ASP', 8.51), ('N', 'ASN', 'OD2', 'ASP', 8.99), ('N', 'ASN', 'O', 'ASP', 10.62), ('N', 'ASN', 'C', 'ASP', 10.79), ('N', 'ASN', 'CA', 'ASP', 10.72), ('N', 'ASN', 'N', 'ASP', 12.0)]]}
HIS_ASN = { 
	'distances':
		[[9.36, 8.48, 7.81, 8.63, 8.33, 8.31, 9.52, 10.56], [8.47, 7.6, 6.75, 7.97, 7.94, 7.87, 8.89, 9.93], [7.66, 6.61, 5.68, 6.95, 7.74, 7.43, 8.24, 9.4], [8.74, 8.08, 7.12, 8.7, 8.26, 8.36, 9.3, 10.18], [7.41, 6.51, 5.39, 7.13, 7.92, 7.66, 8.25, 9.31], [8.12, 7.46, 6.37, 8.22, 8.23, 8.22, 8.91, 9.79], [10.74, 9.93, 9.67, 9.68, 9.01, 9.01, 10.4, 11.38], [10.36, 9.39, 9.03, 9.1, 9.07, 8.9, 10.19, 11.3], [9.01, 8.03, 7.58, 7.9, 7.97, 7.76, 8.99, 10.13], [8.08, 7.29, 7.07, 7.17, 6.66, 6.51, 7.84, 8.9]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 9.36), ('CB', 'HIS', 'CG', 'ASN', 8.48), ('CB', 'HIS', 'OD1', 'ASN', 7.81), ('CB', 'HIS', 'ND2', 'ASN', 8.63), ('CB', 'HIS', 'O', 'ASN', 8.33), ('CB', 'HIS', 'C', 'ASN', 8.31), ('CB', 'HIS', 'CA', 'ASN', 9.52), ('CB', 'HIS', 'N', 'ASN', 10.56)], [('CG', 'HIS', 'CB', 'ASN', 8.47), ('CG', 'HIS', 'CG', 'ASN', 7.6), ('CG', 'HIS', 'OD1', 'ASN', 6.75), ('CG', 'HIS', 'ND2', 'ASN', 7.97), ('CG', 'HIS', 'O', 'ASN', 7.94), ('CG', 'HIS', 'C', 'ASN', 7.87), ('CG', 'HIS', 'CA', 'ASN', 8.89), ('CG', 'HIS', 'N', 'ASN', 9.93)], [('ND1', 'HIS', 'CB', 'ASN', 7.66), ('ND1', 'HIS', 'CG', 'ASN', 6.61), ('ND1', 'HIS', 'OD1', 'ASN', 5.68), ('ND1', 'HIS', 'ND2', 'ASN', 6.95), ('ND1', 'HIS', 'O', 'ASN', 7.74), ('ND1', 'HIS', 'C', 'ASN', 7.43), ('ND1', 'HIS', 'CA', 'ASN', 8.24), ('ND1', 'HIS', 'N', 'ASN', 9.4)], [('CD2', 'HIS', 'CB', 'ASN', 8.74), ('CD2', 'HIS', 'CG', 'ASN', 8.08), ('CD2', 'HIS', 'OD1', 'ASN', 7.12), ('CD2', 'HIS', 'ND2', 'ASN', 8.7), ('CD2', 'HIS', 'O', 'ASN', 8.26), ('CD2', 'HIS', 'C', 'ASN', 8.36), ('CD2', 'HIS', 'CA', 'ASN', 9.3), ('CD2', 'HIS', 'N', 'ASN', 10.18)], [('CE1', 'HIS', 'CB', 'ASN', 7.41), ('CE1', 'HIS', 'CG', 'ASN', 6.51), ('CE1', 'HIS', 'OD1', 'ASN', 5.39), ('CE1', 'HIS', 'ND2', 'ASN', 7.13), ('CE1', 'HIS', 'O', 'ASN', 7.92), ('CE1', 'HIS', 'C', 'ASN', 7.66), ('CE1', 'HIS', 'CA', 'ASN', 8.25), ('CE1', 'HIS', 'N', 'ASN', 9.31)], [('NE2', 'HIS', 'CB', 'ASN', 8.12), ('NE2', 'HIS', 'CG', 'ASN', 7.46), ('NE2', 'HIS', 'OD1', 'ASN', 6.37), ('NE2', 'HIS', 'ND2', 'ASN', 8.22), ('NE2', 'HIS', 'O', 'ASN', 8.23), ('NE2', 'HIS', 'C', 'ASN', 8.22), ('NE2', 'HIS', 'CA', 'ASN', 8.91), ('NE2', 'HIS', 'N', 'ASN', 9.79)], [('O', 'HIS', 'CB', 'ASN', 10.74), ('O', 'HIS', 'CG', 'ASN', 9.93), ('O', 'HIS', 'OD1', 'ASN', 9.67), ('O', 'HIS', 'ND2', 'ASN', 9.68), ('O', 'HIS', 'O', 'ASN', 9.01), ('O', 'HIS', 'C', 'ASN', 9.01), ('O', 'HIS', 'CA', 'ASN', 10.4), ('O', 'HIS', 'N', 'ASN', 11.38)], [('C', 'HIS', 'CB', 'ASN', 10.36), ('C', 'HIS', 'CG', 'ASN', 9.39), ('C', 'HIS', 'OD1', 'ASN', 9.03), ('C', 'HIS', 'ND2', 'ASN', 9.1), ('C', 'HIS', 'O', 'ASN', 9.07), ('C', 'HIS', 'C', 'ASN', 8.9), ('C', 'HIS', 'CA', 'ASN', 10.19), ('C', 'HIS', 'N', 'ASN', 11.3)], [('CA', 'HIS', 'CB', 'ASN', 9.01), ('CA', 'HIS', 'CG', 'ASN', 8.03), ('CA', 'HIS', 'OD1', 'ASN', 7.58), ('CA', 'HIS', 'ND2', 'ASN', 7.9), ('CA', 'HIS', 'O', 'ASN', 7.97), ('CA', 'HIS', 'C', 'ASN', 7.76), ('CA', 'HIS', 'CA', 'ASN', 8.99), ('CA', 'HIS', 'N', 'ASN', 10.13)], [('N', 'HIS', 'CB', 'ASN', 8.08), ('N', 'HIS', 'CG', 'ASN', 7.29), ('N', 'HIS', 'OD1', 'ASN', 7.07), ('N', 'HIS', 'ND2', 'ASN', 7.17), ('N', 'HIS', 'O', 'ASN', 6.66), ('N', 'HIS', 'C', 'ASN', 6.51), ('N', 'HIS', 'CA', 'ASN', 7.84), ('N', 'HIS', 'N', 'ASN', 8.9)]]}
SER_HIS = { 
	'distances':
		[[6.77, 7.48, 8.62, 7.45, 9.21, 8.58, 6.82, 7.53, 7.4, 7.07], [5.89, 6.3, 7.42, 6.09, 7.87, 7.18, 6.82, 7.24, 6.74, 6.47], [6.06, 6.61, 7.28, 7.07, 8.02, 7.9, 5.86, 6.43, 5.94, 4.9], [7.0, 7.66, 8.45, 8.0, 9.15, 8.91, 6.4, 7.21, 6.97, 6.04], [7.1, 7.99, 8.99, 8.27, 9.75, 9.36, 6.26, 7.2, 7.27, 6.7], [6.68, 7.85, 8.83, 8.39, 9.78, 9.55, 5.09, 6.18, 6.62, 6.26]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 6.77), ('CB', 'SER', 'CG', 'HIS', 7.48), ('CB', 'SER', 'ND1', 'HIS', 8.62), ('CB', 'SER', 'CD2', 'HIS', 7.45), ('CB', 'SER', 'CE1', 'HIS', 9.21), ('CB', 'SER', 'NE2', 'HIS', 8.58), ('CB', 'SER', 'O', 'HIS', 6.82), ('CB', 'SER', 'C', 'HIS', 7.53), ('CB', 'SER', 'CA', 'HIS', 7.4), ('CB', 'SER', 'N', 'HIS', 7.07)], [('OG', 'SER', 'CB', 'HIS', 5.89), ('OG', 'SER', 'CG', 'HIS', 6.3), ('OG', 'SER', 'ND1', 'HIS', 7.42), ('OG', 'SER', 'CD2', 'HIS', 6.09), ('OG', 'SER', 'CE1', 'HIS', 7.87), ('OG', 'SER', 'NE2', 'HIS', 7.18), ('OG', 'SER', 'O', 'HIS', 6.82), ('OG', 'SER', 'C', 'HIS', 7.24), ('OG', 'SER', 'CA', 'HIS', 6.74), ('OG', 'SER', 'N', 'HIS', 6.47)], [('O', 'SER', 'CB', 'HIS', 6.06), ('O', 'SER', 'CG', 'HIS', 6.61), ('O', 'SER', 'ND1', 'HIS', 7.28), ('O', 'SER', 'CD2', 'HIS', 7.07), ('O', 'SER', 'CE1', 'HIS', 8.02), ('O', 'SER', 'NE2', 'HIS', 7.9), ('O', 'SER', 'O', 'HIS', 5.86), ('O', 'SER', 'C', 'HIS', 6.43), ('O', 'SER', 'CA', 'HIS', 5.94), ('O', 'SER', 'N', 'HIS', 4.9)], [('C', 'SER', 'CB', 'HIS', 7.0), ('C', 'SER', 'CG', 'HIS', 7.66), ('C', 'SER', 'ND1', 'HIS', 8.45), ('C', 'SER', 'CD2', 'HIS', 8.0), ('C', 'SER', 'CE1', 'HIS', 9.15), ('C', 'SER', 'NE2', 'HIS', 8.91), ('C', 'SER', 'O', 'HIS', 6.4), ('C', 'SER', 'C', 'HIS', 7.21), ('C', 'SER', 'CA', 'HIS', 6.97), ('C', 'SER', 'N', 'HIS', 6.04)], [('CA', 'SER', 'CB', 'HIS', 7.1), ('CA', 'SER', 'CG', 'HIS', 7.99), ('CA', 'SER', 'ND1', 'HIS', 8.99), ('CA', 'SER', 'CD2', 'HIS', 8.27), ('CA', 'SER', 'CE1', 'HIS', 9.75), ('CA', 'SER', 'NE2', 'HIS', 9.36), ('CA', 'SER', 'O', 'HIS', 6.26), ('CA', 'SER', 'C', 'HIS', 7.2), ('CA', 'SER', 'CA', 'HIS', 7.27), ('CA', 'SER', 'N', 'HIS', 6.7)], [('N', 'SER', 'CB', 'HIS', 6.68), ('N', 'SER', 'CG', 'HIS', 7.85), ('N', 'SER', 'ND1', 'HIS', 8.83), ('N', 'SER', 'CD2', 'HIS', 8.39), ('N', 'SER', 'CE1', 'HIS', 9.78), ('N', 'SER', 'NE2', 'HIS', 9.55), ('N', 'SER', 'O', 'HIS', 5.09), ('N', 'SER', 'C', 'HIS', 6.18), ('N', 'SER', 'CA', 'HIS', 6.62), ('N', 'SER', 'N', 'HIS', 6.26)]]}
SER_ASN = { 
	'distances':
		[[11.21, 11.06, 10.72, 11.48, 8.7, 9.47, 10.88, 11.26], [10.2, 10.02, 9.55, 10.54, 8.01, 8.72, 10.06, 10.51], [8.74, 8.58, 8.5, 8.82, 6.11, 6.72, 8.2, 8.71], [9.76, 9.73, 9.69, 9.98, 6.9, 7.66, 9.12, 9.45], [11.1, 10.95, 10.79, 11.19, 8.35, 9.07, 10.54, 10.92], [11.45, 11.09, 10.92, 11.15, 8.89, 9.4, 10.9, 11.47]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASN', 11.21), ('CB', 'SER', 'CG', 'ASN', 11.06), ('CB', 'SER', 'OD1', 'ASN', 10.72), ('CB', 'SER', 'ND2', 'ASN', 11.48), ('CB', 'SER', 'O', 'ASN', 8.7), ('CB', 'SER', 'C', 'ASN', 9.47), ('CB', 'SER', 'CA', 'ASN', 10.88), ('CB', 'SER', 'N', 'ASN', 11.26)], [('OG', 'SER', 'CB', 'ASN', 10.2), ('OG', 'SER', 'CG', 'ASN', 10.02), ('OG', 'SER', 'OD1', 'ASN', 9.55), ('OG', 'SER', 'ND2', 'ASN', 10.54), ('OG', 'SER', 'O', 'ASN', 8.01), ('OG', 'SER', 'C', 'ASN', 8.72), ('OG', 'SER', 'CA', 'ASN', 10.06), ('OG', 'SER', 'N', 'ASN', 10.51)], [('O', 'SER', 'CB', 'ASN', 8.74), ('O', 'SER', 'CG', 'ASN', 8.58), ('O', 'SER', 'OD1', 'ASN', 8.5), ('O', 'SER', 'ND2', 'ASN', 8.82), ('O', 'SER', 'O', 'ASN', 6.11), ('O', 'SER', 'C', 'ASN', 6.72), ('O', 'SER', 'CA', 'ASN', 8.2), ('O', 'SER', 'N', 'ASN', 8.71)], [('C', 'SER', 'CB', 'ASN', 9.76), ('C', 'SER', 'CG', 'ASN', 9.73), ('C', 'SER', 'OD1', 'ASN', 9.69), ('C', 'SER', 'ND2', 'ASN', 9.98), ('C', 'SER', 'O', 'ASN', 6.9), ('C', 'SER', 'C', 'ASN', 7.66), ('C', 'SER', 'CA', 'ASN', 9.12), ('C', 'SER', 'N', 'ASN', 9.45)], [('CA', 'SER', 'CB', 'ASN', 11.1), ('CA', 'SER', 'CG', 'ASN', 10.95), ('CA', 'SER', 'OD1', 'ASN', 10.79), ('CA', 'SER', 'ND2', 'ASN', 11.19), ('CA', 'SER', 'O', 'ASN', 8.35), ('CA', 'SER', 'C', 'ASN', 9.07), ('CA', 'SER', 'CA', 'ASN', 10.54), ('CA', 'SER', 'N', 'ASN', 10.92)], [('N', 'SER', 'CB', 'ASN', 11.45), ('N', 'SER', 'CG', 'ASN', 11.09), ('N', 'SER', 'OD1', 'ASN', 10.92), ('N', 'SER', 'ND2', 'ASN', 11.15), ('N', 'SER', 'O', 'ASN', 8.89), ('N', 'SER', 'C', 'ASN', 9.4), ('N', 'SER', 'CA', 'ASN', 10.9), ('N', 'SER', 'N', 'ASN', 11.47)]]}
SER_ASP = { 
	'distances':
		[[12.71, 11.71, 10.65, 12.12, 11.11, 12.23, 13.19, 14.57], [11.27, 10.29, 9.25, 10.73, 9.71, 10.84, 11.78, 13.15], [11.82, 10.53, 9.52, 10.66, 10.81, 11.78, 12.42, 13.88], [12.8, 11.56, 10.5, 11.78, 11.57, 12.55, 13.31, 14.76], [13.52, 12.38, 11.33, 12.65, 12.13, 13.21, 14.06, 15.48], [13.96, 12.77, 11.82, 12.91, 12.81, 13.91, 14.65, 16.07]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 12.71), ('CB', 'SER', 'CG', 'ASP', 11.71), ('CB', 'SER', 'OD1', 'ASP', 10.65), ('CB', 'SER', 'OD2', 'ASP', 12.12), ('CB', 'SER', 'O', 'ASP', 11.11), ('CB', 'SER', 'C', 'ASP', 12.23), ('CB', 'SER', 'CA', 'ASP', 13.19), ('CB', 'SER', 'N', 'ASP', 14.57)], [('OG', 'SER', 'CB', 'ASP', 11.27), ('OG', 'SER', 'CG', 'ASP', 10.29), ('OG', 'SER', 'OD1', 'ASP', 9.25), ('OG', 'SER', 'OD2', 'ASP', 10.73), ('OG', 'SER', 'O', 'ASP', 9.71), ('OG', 'SER', 'C', 'ASP', 10.84), ('OG', 'SER', 'CA', 'ASP', 11.78), ('OG', 'SER', 'N', 'ASP', 13.15)], [('O', 'SER', 'CB', 'ASP', 11.82), ('O', 'SER', 'CG', 'ASP', 10.53), ('O', 'SER', 'OD1', 'ASP', 9.52), ('O', 'SER', 'OD2', 'ASP', 10.66), ('O', 'SER', 'O', 'ASP', 10.81), ('O', 'SER', 'C', 'ASP', 11.78), ('O', 'SER', 'CA', 'ASP', 12.42), ('O', 'SER', 'N', 'ASP', 13.88)], [('C', 'SER', 'CB', 'ASP', 12.8), ('C', 'SER', 'CG', 'ASP', 11.56), ('C', 'SER', 'OD1', 'ASP', 10.5), ('C', 'SER', 'OD2', 'ASP', 11.78), ('C', 'SER', 'O', 'ASP', 11.57), ('C', 'SER', 'C', 'ASP', 12.55), ('C', 'SER', 'CA', 'ASP', 13.31), ('C', 'SER', 'N', 'ASP', 14.76)], [('CA', 'SER', 'CB', 'ASP', 13.52), ('CA', 'SER', 'CG', 'ASP', 12.38), ('CA', 'SER', 'OD1', 'ASP', 11.33), ('CA', 'SER', 'OD2', 'ASP', 12.65), ('CA', 'SER', 'O', 'ASP', 12.13), ('CA', 'SER', 'C', 'ASP', 13.21), ('CA', 'SER', 'CA', 'ASP', 14.06), ('CA', 'SER', 'N', 'ASP', 15.48)], [('N', 'SER', 'CB', 'ASP', 13.96), ('N', 'SER', 'CG', 'ASP', 12.77), ('N', 'SER', 'OD1', 'ASP', 11.82), ('N', 'SER', 'OD2', 'ASP', 12.91), ('N', 'SER', 'O', 'ASP', 12.81), ('N', 'SER', 'C', 'ASP', 13.91), ('N', 'SER', 'CA', 'ASP', 14.65), ('N', 'SER', 'N', 'ASP', 16.07)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASP, d, 'A_1grc_2_1_2_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASN_ASP, d, 'A_1grc_2_1_2_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASN, d, 'A_1grc_2_1_2_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(SER_HIS, d, 'A_1grc_2_1_2_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(SER_ASN, d, 'A_1grc_2_1_2_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(SER_ASP, d, 'A_1grc_2_1_2_2')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASP' :  match1,
		'ASN_ASP' :  match2,
		'HIS_ASN' :  match3,
		'SER_HIS' :  match4,
		'SER_ASN' :  match5,
		'SER_ASP' :  match6}