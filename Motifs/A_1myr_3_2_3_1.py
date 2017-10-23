'''
FUNC:A_1myr_3_2_3_1
PDB:1myr
EC:3.2.3.1
RESI:arg,gln,ser,asn,tyr,glu
LOCI:a-95,187,190,328,330,409;
'''
import motifFunctions as cmd
GLU_GLN = { 
	'distances':
		[[10.31, 8.8, 8.46, 7.37, 9.57], [9.81, 8.33, 8.18, 7.25, 9.31], [8.85, 7.41, 7.12, 6.25, 8.13], [8.8, 7.36, 6.72, 5.72, 7.58], [8.45, 7.11, 7.07, 6.45, 8.06]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLN', 10.31), ('CB', 'GLU', 'CG', 'GLN', 8.8), ('CB', 'GLU', 'CD', 'GLN', 8.46), ('CB', 'GLU', 'OE1', 'GLN', 7.37), ('CB', 'GLU', 'NE2', 'GLN', 9.57)], [('CG', 'GLU', 'CB', 'GLN', 9.81), ('CG', 'GLU', 'CG', 'GLN', 8.33), ('CG', 'GLU', 'CD', 'GLN', 8.18), ('CG', 'GLU', 'OE1', 'GLN', 7.25), ('CG', 'GLU', 'NE2', 'GLN', 9.31)], [('CD', 'GLU', 'CB', 'GLN', 8.85), ('CD', 'GLU', 'CG', 'GLN', 7.41), ('CD', 'GLU', 'CD', 'GLN', 7.12), ('CD', 'GLU', 'OE1', 'GLN', 6.25), ('CD', 'GLU', 'NE2', 'GLN', 8.13)], [('OE1', 'GLU', 'CB', 'GLN', 8.8), ('OE1', 'GLU', 'CG', 'GLN', 7.36), ('OE1', 'GLU', 'CD', 'GLN', 6.72), ('OE1', 'GLU', 'OE1', 'GLN', 5.72), ('OE1', 'GLU', 'NE2', 'GLN', 7.58)], [('OE2', 'GLU', 'CB', 'GLN', 8.45), ('OE2', 'GLU', 'CG', 'GLN', 7.11), ('OE2', 'GLU', 'CD', 'GLN', 7.07), ('OE2', 'GLU', 'OE1', 'GLN', 6.45), ('OE2', 'GLU', 'NE2', 'GLN', 8.06)]]}
ASN_GLN = { 
	'distances':
		[[7.86, 6.56, 6.55, 5.78, 7.77], [7.61, 6.23, 6.49, 5.79, 7.81], [8.5, 7.19, 7.62, 6.98, 8.96], [6.66, 5.2, 5.45, 4.85, 6.77]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'GLN', 7.86), ('CB', 'ASN', 'CG', 'GLN', 6.56), ('CB', 'ASN', 'CD', 'GLN', 6.55), ('CB', 'ASN', 'OE1', 'GLN', 5.78), ('CB', 'ASN', 'NE2', 'GLN', 7.77)], [('CG', 'ASN', 'CB', 'GLN', 7.61), ('CG', 'ASN', 'CG', 'GLN', 6.23), ('CG', 'ASN', 'CD', 'GLN', 6.49), ('CG', 'ASN', 'OE1', 'GLN', 5.79), ('CG', 'ASN', 'NE2', 'GLN', 7.81)], [('OD1', 'ASN', 'CB', 'GLN', 8.5), ('OD1', 'ASN', 'CG', 'GLN', 7.19), ('OD1', 'ASN', 'CD', 'GLN', 7.62), ('OD1', 'ASN', 'OE1', 'GLN', 6.98), ('OD1', 'ASN', 'NE2', 'GLN', 8.96)], [('ND2', 'ASN', 'CB', 'GLN', 6.66), ('ND2', 'ASN', 'CG', 'GLN', 5.2), ('ND2', 'ASN', 'CD', 'GLN', 5.45), ('ND2', 'ASN', 'OE1', 'GLN', 4.85), ('ND2', 'ASN', 'NE2', 'GLN', 6.77)]]}
GLU_ASN = { 
	'distances':
		[[5.94, 5.44, 5.5, 5.81], [6.39, 5.4, 5.34, 5.38], [6.55, 5.56, 5.91, 4.97], [6.61, 5.98, 6.61, 5.34], [7.14, 5.93, 6.18, 5.08]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASN', 5.94), ('CB', 'GLU', 'CG', 'ASN', 5.44), ('CB', 'GLU', 'OD1', 'ASN', 5.5), ('CB', 'GLU', 'ND2', 'ASN', 5.81)], [('CG', 'GLU', 'CB', 'ASN', 6.39), ('CG', 'GLU', 'CG', 'ASN', 5.4), ('CG', 'GLU', 'OD1', 'ASN', 5.34), ('CG', 'GLU', 'ND2', 'ASN', 5.38)], [('CD', 'GLU', 'CB', 'ASN', 6.55), ('CD', 'GLU', 'CG', 'ASN', 5.56), ('CD', 'GLU', 'OD1', 'ASN', 5.91), ('CD', 'GLU', 'ND2', 'ASN', 4.97)], [('OE1', 'GLU', 'CB', 'ASN', 6.61), ('OE1', 'GLU', 'CG', 'ASN', 5.98), ('OE1', 'GLU', 'OD1', 'ASN', 6.61), ('OE1', 'GLU', 'ND2', 'ASN', 5.34)], [('OE2', 'GLU', 'CB', 'ASN', 7.14), ('OE2', 'GLU', 'CG', 'ASN', 5.93), ('OE2', 'GLU', 'OD1', 'ASN', 6.18), ('OE2', 'GLU', 'ND2', 'ASN', 5.08)]]}
GLU_TYR = { 
	'distances':
		[[9.28, 7.92, 7.77, 7.12, 6.84, 6.01, 5.85, 5.33], [10.46, 9.06, 8.92, 8.13, 7.88, 6.89, 6.76, 5.92], [10.33, 8.9, 8.83, 7.85, 7.77, 6.54, 6.51, 5.56], [9.34, 7.9, 7.83, 6.87, 6.78, 5.53, 5.48, 4.57], [11.4, 10.0, 9.99, 8.88, 8.93, 7.6, 7.64, 6.66]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'TYR', 9.28), ('CB', 'GLU', 'CG', 'TYR', 7.92), ('CB', 'GLU', 'CD1', 'TYR', 7.77), ('CB', 'GLU', 'CD2', 'TYR', 7.12), ('CB', 'GLU', 'CE1', 'TYR', 6.84), ('CB', 'GLU', 'CE2', 'TYR', 6.01), ('CB', 'GLU', 'CZ', 'TYR', 5.85), ('CB', 'GLU', 'OH', 'TYR', 5.33)], [('CG', 'GLU', 'CB', 'TYR', 10.46), ('CG', 'GLU', 'CG', 'TYR', 9.06), ('CG', 'GLU', 'CD1', 'TYR', 8.92), ('CG', 'GLU', 'CD2', 'TYR', 8.13), ('CG', 'GLU', 'CE1', 'TYR', 7.88), ('CG', 'GLU', 'CE2', 'TYR', 6.89), ('CG', 'GLU', 'CZ', 'TYR', 6.76), ('CG', 'GLU', 'OH', 'TYR', 5.92)], [('CD', 'GLU', 'CB', 'TYR', 10.33), ('CD', 'GLU', 'CG', 'TYR', 8.9), ('CD', 'GLU', 'CD1', 'TYR', 8.83), ('CD', 'GLU', 'CD2', 'TYR', 7.85), ('CD', 'GLU', 'CE1', 'TYR', 7.77), ('CD', 'GLU', 'CE2', 'TYR', 6.54), ('CD', 'GLU', 'CZ', 'TYR', 6.51), ('CD', 'GLU', 'OH', 'TYR', 5.56)], [('OE1', 'GLU', 'CB', 'TYR', 9.34), ('OE1', 'GLU', 'CG', 'TYR', 7.9), ('OE1', 'GLU', 'CD1', 'TYR', 7.83), ('OE1', 'GLU', 'CD2', 'TYR', 6.87), ('OE1', 'GLU', 'CE1', 'TYR', 6.78), ('OE1', 'GLU', 'CE2', 'TYR', 5.53), ('OE1', 'GLU', 'CZ', 'TYR', 5.48), ('OE1', 'GLU', 'OH', 'TYR', 4.57)], [('OE2', 'GLU', 'CB', 'TYR', 11.4), ('OE2', 'GLU', 'CG', 'TYR', 10.0), ('OE2', 'GLU', 'CD1', 'TYR', 9.99), ('OE2', 'GLU', 'CD2', 'TYR', 8.88), ('OE2', 'GLU', 'CE1', 'TYR', 8.93), ('OE2', 'GLU', 'CE2', 'TYR', 7.6), ('OE2', 'GLU', 'CZ', 'TYR', 7.64), ('OE2', 'GLU', 'OH', 'TYR', 6.66)]]}
TYR_ARG = { 
	'distances':
		[[16.99, 16.74, 15.66, 15.54, 14.49, 13.31, 14.81], [15.61, 15.35, 14.32, 14.22, 13.17, 11.95, 13.51], [15.26, 15.11, 14.2, 14.22, 13.21, 11.93, 13.64], [14.8, 14.42, 13.35, 13.14, 12.04, 10.88, 12.3], [14.12, 13.98, 13.15, 13.19, 12.2, 10.89, 12.65], [13.6, 13.2, 12.18, 11.97, 10.86, 9.67, 11.14], [13.24, 12.97, 12.1, 12.03, 10.97, 9.7, 11.36], [12.2, 11.92, 11.16, 11.11, 10.06, 8.78, 10.46]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ARG', 16.99), ('CB', 'TYR', 'CG', 'ARG', 16.74), ('CB', 'TYR', 'CD', 'ARG', 15.66), ('CB', 'TYR', 'NE', 'ARG', 15.54), ('CB', 'TYR', 'CZ', 'ARG', 14.49), ('CB', 'TYR', 'NH1', 'ARG', 13.31), ('CB', 'TYR', 'NH2', 'ARG', 14.81)], [('CG', 'TYR', 'CB', 'ARG', 15.61), ('CG', 'TYR', 'CG', 'ARG', 15.35), ('CG', 'TYR', 'CD', 'ARG', 14.32), ('CG', 'TYR', 'NE', 'ARG', 14.22), ('CG', 'TYR', 'CZ', 'ARG', 13.17), ('CG', 'TYR', 'NH1', 'ARG', 11.95), ('CG', 'TYR', 'NH2', 'ARG', 13.51)], [('CD1', 'TYR', 'CB', 'ARG', 15.26), ('CD1', 'TYR', 'CG', 'ARG', 15.11), ('CD1', 'TYR', 'CD', 'ARG', 14.2), ('CD1', 'TYR', 'NE', 'ARG', 14.22), ('CD1', 'TYR', 'CZ', 'ARG', 13.21), ('CD1', 'TYR', 'NH1', 'ARG', 11.93), ('CD1', 'TYR', 'NH2', 'ARG', 13.64)], [('CD2', 'TYR', 'CB', 'ARG', 14.8), ('CD2', 'TYR', 'CG', 'ARG', 14.42), ('CD2', 'TYR', 'CD', 'ARG', 13.35), ('CD2', 'TYR', 'NE', 'ARG', 13.14), ('CD2', 'TYR', 'CZ', 'ARG', 12.04), ('CD2', 'TYR', 'NH1', 'ARG', 10.88), ('CD2', 'TYR', 'NH2', 'ARG', 12.3)], [('CE1', 'TYR', 'CB', 'ARG', 14.12), ('CE1', 'TYR', 'CG', 'ARG', 13.98), ('CE1', 'TYR', 'CD', 'ARG', 13.15), ('CE1', 'TYR', 'NE', 'ARG', 13.19), ('CE1', 'TYR', 'CZ', 'ARG', 12.2), ('CE1', 'TYR', 'NH1', 'ARG', 10.89), ('CE1', 'TYR', 'NH2', 'ARG', 12.65)], [('CE2', 'TYR', 'CB', 'ARG', 13.6), ('CE2', 'TYR', 'CG', 'ARG', 13.2), ('CE2', 'TYR', 'CD', 'ARG', 12.18), ('CE2', 'TYR', 'NE', 'ARG', 11.97), ('CE2', 'TYR', 'CZ', 'ARG', 10.86), ('CE2', 'TYR', 'NH1', 'ARG', 9.67), ('CE2', 'TYR', 'NH2', 'ARG', 11.14)], [('CZ', 'TYR', 'CB', 'ARG', 13.24), ('CZ', 'TYR', 'CG', 'ARG', 12.97), ('CZ', 'TYR', 'CD', 'ARG', 12.1), ('CZ', 'TYR', 'NE', 'ARG', 12.03), ('CZ', 'TYR', 'CZ', 'ARG', 10.97), ('CZ', 'TYR', 'NH1', 'ARG', 9.7), ('CZ', 'TYR', 'NH2', 'ARG', 11.36)], [('OH', 'TYR', 'CB', 'ARG', 12.2), ('OH', 'TYR', 'CG', 'ARG', 11.92), ('OH', 'TYR', 'CD', 'ARG', 11.16), ('OH', 'TYR', 'NE', 'ARG', 11.11), ('OH', 'TYR', 'CZ', 'ARG', 10.06), ('OH', 'TYR', 'NH1', 'ARG', 8.78), ('OH', 'TYR', 'NH2', 'ARG', 10.46)]]}
ASN_SER = { 
	'distances':
		[[11.5, 10.26], [11.45, 10.35], [12.47, 11.42], [10.37, 9.34]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'SER', 11.5), ('CB', 'ASN', 'OG', 'SER', 10.26)], [('CG', 'ASN', 'CB', 'SER', 11.45), ('CG', 'ASN', 'OG', 'SER', 10.35)], [('OD1', 'ASN', 'CB', 'SER', 12.47), ('OD1', 'ASN', 'OG', 'SER', 11.42)], [('ND2', 'ASN', 'CB', 'SER', 10.37), ('ND2', 'ASN', 'OG', 'SER', 9.34)]]}
ASN_TYR = { 
	'distances':
		[[8.92, 8.07, 8.8, 6.86, 8.53, 6.46, 7.43, 7.69], [10.02, 8.99, 9.51, 7.74, 8.97, 7.0, 7.75, 7.63], [10.9, 9.84, 10.25, 8.69, 9.65, 7.91, 8.49, 8.25], [10.24, 9.13, 9.63, 7.8, 9.0, 6.93, 7.67, 7.39]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'TYR', 8.92), ('CB', 'ASN', 'CG', 'TYR', 8.07), ('CB', 'ASN', 'CD1', 'TYR', 8.8), ('CB', 'ASN', 'CD2', 'TYR', 6.86), ('CB', 'ASN', 'CE1', 'TYR', 8.53), ('CB', 'ASN', 'CE2', 'TYR', 6.46), ('CB', 'ASN', 'CZ', 'TYR', 7.43), ('CB', 'ASN', 'OH', 'TYR', 7.69)], [('CG', 'ASN', 'CB', 'TYR', 10.02), ('CG', 'ASN', 'CG', 'TYR', 8.99), ('CG', 'ASN', 'CD1', 'TYR', 9.51), ('CG', 'ASN', 'CD2', 'TYR', 7.74), ('CG', 'ASN', 'CE1', 'TYR', 8.97), ('CG', 'ASN', 'CE2', 'TYR', 7.0), ('CG', 'ASN', 'CZ', 'TYR', 7.75), ('CG', 'ASN', 'OH', 'TYR', 7.63)], [('OD1', 'ASN', 'CB', 'TYR', 10.9), ('OD1', 'ASN', 'CG', 'TYR', 9.84), ('OD1', 'ASN', 'CD1', 'TYR', 10.25), ('OD1', 'ASN', 'CD2', 'TYR', 8.69), ('OD1', 'ASN', 'CE1', 'TYR', 9.65), ('OD1', 'ASN', 'CE2', 'TYR', 7.91), ('OD1', 'ASN', 'CZ', 'TYR', 8.49), ('OD1', 'ASN', 'OH', 'TYR', 8.25)], [('ND2', 'ASN', 'CB', 'TYR', 10.24), ('ND2', 'ASN', 'CG', 'TYR', 9.13), ('ND2', 'ASN', 'CD1', 'TYR', 9.63), ('ND2', 'ASN', 'CD2', 'TYR', 7.8), ('ND2', 'ASN', 'CE1', 'TYR', 9.0), ('ND2', 'ASN', 'CE2', 'TYR', 6.93), ('ND2', 'ASN', 'CZ', 'TYR', 7.67), ('ND2', 'ASN', 'OH', 'TYR', 7.39)]]}
GLU_ARG = { 
	'distances':
		[[9.72, 9.49, 8.46, 8.57, 7.74, 6.42, 8.48], [8.74, 8.31, 7.35, 7.31, 6.39, 5.06, 7.1], [9.58, 8.94, 8.07, 7.73, 6.58, 5.39, 6.9], [10.75, 10.15, 9.32, 8.97, 7.79, 6.64, 8.01], [9.23, 8.38, 7.59, 7.02, 5.77, 4.8, 5.87]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 9.72), ('CB', 'GLU', 'CG', 'ARG', 9.49), ('CB', 'GLU', 'CD', 'ARG', 8.46), ('CB', 'GLU', 'NE', 'ARG', 8.57), ('CB', 'GLU', 'CZ', 'ARG', 7.74), ('CB', 'GLU', 'NH1', 'ARG', 6.42), ('CB', 'GLU', 'NH2', 'ARG', 8.48)], [('CG', 'GLU', 'CB', 'ARG', 8.74), ('CG', 'GLU', 'CG', 'ARG', 8.31), ('CG', 'GLU', 'CD', 'ARG', 7.35), ('CG', 'GLU', 'NE', 'ARG', 7.31), ('CG', 'GLU', 'CZ', 'ARG', 6.39), ('CG', 'GLU', 'NH1', 'ARG', 5.06), ('CG', 'GLU', 'NH2', 'ARG', 7.1)], [('CD', 'GLU', 'CB', 'ARG', 9.58), ('CD', 'GLU', 'CG', 'ARG', 8.94), ('CD', 'GLU', 'CD', 'ARG', 8.07), ('CD', 'GLU', 'NE', 'ARG', 7.73), ('CD', 'GLU', 'CZ', 'ARG', 6.58), ('CD', 'GLU', 'NH1', 'ARG', 5.39), ('CD', 'GLU', 'NH2', 'ARG', 6.9)], [('OE1', 'GLU', 'CB', 'ARG', 10.75), ('OE1', 'GLU', 'CG', 'ARG', 10.15), ('OE1', 'GLU', 'CD', 'ARG', 9.32), ('OE1', 'GLU', 'NE', 'ARG', 8.97), ('OE1', 'GLU', 'CZ', 'ARG', 7.79), ('OE1', 'GLU', 'NH1', 'ARG', 6.64), ('OE1', 'GLU', 'NH2', 'ARG', 8.01)], [('OE2', 'GLU', 'CB', 'ARG', 9.23), ('OE2', 'GLU', 'CG', 'ARG', 8.38), ('OE2', 'GLU', 'CD', 'ARG', 7.59), ('OE2', 'GLU', 'NE', 'ARG', 7.02), ('OE2', 'GLU', 'CZ', 'ARG', 5.77), ('OE2', 'GLU', 'NH1', 'ARG', 4.8), ('OE2', 'GLU', 'NH2', 'ARG', 5.87)]]}
GLN_ARG = { 
	'distances':
		[[14.52, 13.32, 12.22, 11.06, 9.88, 9.79, 9.08], [13.38, 12.27, 11.14, 10.09, 8.86, 8.58, 8.24], [13.89, 12.89, 11.8, 10.88, 9.59, 9.07, 9.09], [13.33, 12.44, 11.34, 10.57, 9.28, 8.57, 8.98], [15.04, 14.01, 12.99, 12.03, 10.71, 10.23, 10.11]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'ARG', 14.52), ('CB', 'GLN', 'CG', 'ARG', 13.32), ('CB', 'GLN', 'CD', 'ARG', 12.22), ('CB', 'GLN', 'NE', 'ARG', 11.06), ('CB', 'GLN', 'CZ', 'ARG', 9.88), ('CB', 'GLN', 'NH1', 'ARG', 9.79), ('CB', 'GLN', 'NH2', 'ARG', 9.08)], [('CG', 'GLN', 'CB', 'ARG', 13.38), ('CG', 'GLN', 'CG', 'ARG', 12.27), ('CG', 'GLN', 'CD', 'ARG', 11.14), ('CG', 'GLN', 'NE', 'ARG', 10.09), ('CG', 'GLN', 'CZ', 'ARG', 8.86), ('CG', 'GLN', 'NH1', 'ARG', 8.58), ('CG', 'GLN', 'NH2', 'ARG', 8.24)], [('CD', 'GLN', 'CB', 'ARG', 13.89), ('CD', 'GLN', 'CG', 'ARG', 12.89), ('CD', 'GLN', 'CD', 'ARG', 11.8), ('CD', 'GLN', 'NE', 'ARG', 10.88), ('CD', 'GLN', 'CZ', 'ARG', 9.59), ('CD', 'GLN', 'NH1', 'ARG', 9.07), ('CD', 'GLN', 'NH2', 'ARG', 9.09)], [('OE1', 'GLN', 'CB', 'ARG', 13.33), ('OE1', 'GLN', 'CG', 'ARG', 12.44), ('OE1', 'GLN', 'CD', 'ARG', 11.34), ('OE1', 'GLN', 'NE', 'ARG', 10.57), ('OE1', 'GLN', 'CZ', 'ARG', 9.28), ('OE1', 'GLN', 'NH1', 'ARG', 8.57), ('OE1', 'GLN', 'NH2', 'ARG', 8.98)], [('NE2', 'GLN', 'CB', 'ARG', 15.04), ('NE2', 'GLN', 'CG', 'ARG', 14.01), ('NE2', 'GLN', 'CD', 'ARG', 12.99), ('NE2', 'GLN', 'NE', 'ARG', 12.03), ('NE2', 'GLN', 'CZ', 'ARG', 10.71), ('NE2', 'GLN', 'NH1', 'ARG', 10.23), ('NE2', 'GLN', 'NH2', 'ARG', 10.11)]]}
TYR_SER = { 
	'distances':
		[[13.81, 12.48], [13.32, 12.02], [14.18, 12.94], [12.15, 10.84], [13.98, 12.8], [11.91, 10.67], [12.9, 11.73], [12.92, 11.85]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'SER', 13.81), ('CB', 'TYR', 'OG', 'SER', 12.48)], [('CG', 'TYR', 'CB', 'SER', 13.32), ('CG', 'TYR', 'OG', 'SER', 12.02)], [('CD1', 'TYR', 'CB', 'SER', 14.18), ('CD1', 'TYR', 'OG', 'SER', 12.94)], [('CD2', 'TYR', 'CB', 'SER', 12.15), ('CD2', 'TYR', 'OG', 'SER', 10.84)], [('CE1', 'TYR', 'CB', 'SER', 13.98), ('CE1', 'TYR', 'OG', 'SER', 12.8)], [('CE2', 'TYR', 'CB', 'SER', 11.91), ('CE2', 'TYR', 'OG', 'SER', 10.67)], [('CZ', 'TYR', 'CB', 'SER', 12.9), ('CZ', 'TYR', 'OG', 'SER', 11.73)], [('OH', 'TYR', 'CB', 'SER', 12.92), ('OH', 'TYR', 'OG', 'SER', 11.85)]]}
ASN_ARG = { 
	'distances':
		[[12.04, 11.44, 10.05, 9.65, 8.7, 7.88, 8.98], [10.71, 10.01, 8.65, 8.17, 7.18, 6.4, 7.47], [9.78, 9.14, 7.71, 7.36, 6.57, 5.85, 7.08], [10.85, 9.99, 8.74, 8.06, 6.88, 6.17, 6.89]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ARG', 12.04), ('CB', 'ASN', 'CG', 'ARG', 11.44), ('CB', 'ASN', 'CD', 'ARG', 10.05), ('CB', 'ASN', 'NE', 'ARG', 9.65), ('CB', 'ASN', 'CZ', 'ARG', 8.7), ('CB', 'ASN', 'NH1', 'ARG', 7.88), ('CB', 'ASN', 'NH2', 'ARG', 8.98)], [('CG', 'ASN', 'CB', 'ARG', 10.71), ('CG', 'ASN', 'CG', 'ARG', 10.01), ('CG', 'ASN', 'CD', 'ARG', 8.65), ('CG', 'ASN', 'NE', 'ARG', 8.17), ('CG', 'ASN', 'CZ', 'ARG', 7.18), ('CG', 'ASN', 'NH1', 'ARG', 6.4), ('CG', 'ASN', 'NH2', 'ARG', 7.47)], [('OD1', 'ASN', 'CB', 'ARG', 9.78), ('OD1', 'ASN', 'CG', 'ARG', 9.14), ('OD1', 'ASN', 'CD', 'ARG', 7.71), ('OD1', 'ASN', 'NE', 'ARG', 7.36), ('OD1', 'ASN', 'CZ', 'ARG', 6.57), ('OD1', 'ASN', 'NH1', 'ARG', 5.85), ('OD1', 'ASN', 'NH2', 'ARG', 7.08)], [('ND2', 'ASN', 'CB', 'ARG', 10.85), ('ND2', 'ASN', 'CG', 'ARG', 9.99), ('ND2', 'ASN', 'CD', 'ARG', 8.74), ('ND2', 'ASN', 'NE', 'ARG', 8.06), ('ND2', 'ASN', 'CZ', 'ARG', 6.88), ('ND2', 'ASN', 'NH1', 'ARG', 6.17), ('ND2', 'ASN', 'NH2', 'ARG', 6.89)]]}
SER_ARG = { 
	'distances':
		[[18.01, 16.76, 15.86, 14.65, 13.42, 13.32, 12.45], [17.39, 16.22, 15.23, 14.1, 12.84, 12.61, 11.99]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ARG', 18.01), ('CB', 'SER', 'CG', 'ARG', 16.76), ('CB', 'SER', 'CD', 'ARG', 15.86), ('CB', 'SER', 'NE', 'ARG', 14.65), ('CB', 'SER', 'CZ', 'ARG', 13.42), ('CB', 'SER', 'NH1', 'ARG', 13.32), ('CB', 'SER', 'NH2', 'ARG', 12.45)], [('OG', 'SER', 'CB', 'ARG', 17.39), ('OG', 'SER', 'CG', 'ARG', 16.22), ('OG', 'SER', 'CD', 'ARG', 15.23), ('OG', 'SER', 'NE', 'ARG', 14.1), ('OG', 'SER', 'CZ', 'ARG', 12.84), ('OG', 'SER', 'NH1', 'ARG', 12.61), ('OG', 'SER', 'NH2', 'ARG', 11.99)]]}
GLU_SER = { 
	'distances':
		[[13.56, 12.48], [13.1, 12.14], [11.85, 10.95], [11.44, 10.48], [11.44, 10.68]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'SER', 13.56), ('CB', 'GLU', 'OG', 'SER', 12.48)], [('CG', 'GLU', 'CB', 'SER', 13.1), ('CG', 'GLU', 'OG', 'SER', 12.14)], [('CD', 'GLU', 'CB', 'SER', 11.85), ('CD', 'GLU', 'OG', 'SER', 10.95)], [('OE1', 'GLU', 'CB', 'SER', 11.44), ('OE1', 'GLU', 'OG', 'SER', 10.48)], [('OE2', 'GLU', 'CB', 'SER', 11.44), ('OE2', 'GLU', 'OG', 'SER', 10.68)]]}
GLN_SER = { 
	'distances':
		[[6.19, 5.39], [7.28, 6.32], [7.18, 6.04], [8.31, 7.13], [6.13, 4.96]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'SER', 6.19), ('CB', 'GLN', 'OG', 'SER', 5.39)], [('CG', 'GLN', 'CB', 'SER', 7.28), ('CG', 'GLN', 'OG', 'SER', 6.32)], [('CD', 'GLN', 'CB', 'SER', 7.18), ('CD', 'GLN', 'OG', 'SER', 6.04)], [('OE1', 'GLN', 'CB', 'SER', 8.31), ('OE1', 'GLN', 'OG', 'SER', 7.13)], [('NE2', 'GLN', 'CB', 'SER', 6.13), ('NE2', 'GLN', 'OG', 'SER', 4.96)]]}
TYR_GLN = { 
	'distances':
		[[12.25, 11.2, 9.98, 9.04, 10.23], [11.54, 10.36, 9.14, 8.09, 9.5], [12.39, 11.13, 9.92, 8.81, 10.31], [10.16, 8.96, 7.77, 6.72, 8.23], [12.06, 10.72, 9.56, 8.41, 10.03], [9.72, 8.4, 7.27, 6.1, 7.85], [10.78, 9.42, 8.31, 7.14, 8.87], [10.73, 9.32, 8.32, 7.18, 8.95]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'GLN', 12.25), ('CB', 'TYR', 'CG', 'GLN', 11.2), ('CB', 'TYR', 'CD', 'GLN', 9.98), ('CB', 'TYR', 'OE1', 'GLN', 9.04), ('CB', 'TYR', 'NE2', 'GLN', 10.23)], [('CG', 'TYR', 'CB', 'GLN', 11.54), ('CG', 'TYR', 'CG', 'GLN', 10.36), ('CG', 'TYR', 'CD', 'GLN', 9.14), ('CG', 'TYR', 'OE1', 'GLN', 8.09), ('CG', 'TYR', 'NE2', 'GLN', 9.5)], [('CD1', 'TYR', 'CB', 'GLN', 12.39), ('CD1', 'TYR', 'CG', 'GLN', 11.13), ('CD1', 'TYR', 'CD', 'GLN', 9.92), ('CD1', 'TYR', 'OE1', 'GLN', 8.81), ('CD1', 'TYR', 'NE2', 'GLN', 10.31)], [('CD2', 'TYR', 'CB', 'GLN', 10.16), ('CD2', 'TYR', 'CG', 'GLN', 8.96), ('CD2', 'TYR', 'CD', 'GLN', 7.77), ('CD2', 'TYR', 'OE1', 'GLN', 6.72), ('CD2', 'TYR', 'NE2', 'GLN', 8.23)], [('CE1', 'TYR', 'CB', 'GLN', 12.06), ('CE1', 'TYR', 'CG', 'GLN', 10.72), ('CE1', 'TYR', 'CD', 'GLN', 9.56), ('CE1', 'TYR', 'OE1', 'GLN', 8.41), ('CE1', 'TYR', 'NE2', 'GLN', 10.03)], [('CE2', 'TYR', 'CB', 'GLN', 9.72), ('CE2', 'TYR', 'CG', 'GLN', 8.4), ('CE2', 'TYR', 'CD', 'GLN', 7.27), ('CE2', 'TYR', 'OE1', 'GLN', 6.1), ('CE2', 'TYR', 'NE2', 'GLN', 7.85)], [('CZ', 'TYR', 'CB', 'GLN', 10.78), ('CZ', 'TYR', 'CG', 'GLN', 9.42), ('CZ', 'TYR', 'CD', 'GLN', 8.31), ('CZ', 'TYR', 'OE1', 'GLN', 7.14), ('CZ', 'TYR', 'NE2', 'GLN', 8.87)], [('OH', 'TYR', 'CB', 'GLN', 10.73), ('OH', 'TYR', 'CG', 'GLN', 9.32), ('OH', 'TYR', 'CD', 'GLN', 8.32), ('OH', 'TYR', 'OE1', 'GLN', 7.18), ('OH', 'TYR', 'NE2', 'GLN', 8.95)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_GLN, d, 'A_1myr_3_2_3_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASN_GLN, d, 'A_1myr_3_2_3_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_ASN, d, 'A_1myr_3_2_3_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_TYR, d, 'A_1myr_3_2_3_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(TYR_ARG, d, 'A_1myr_3_2_3_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ASN_SER, d, 'A_1myr_3_2_3_1')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(ASN_TYR, d, 'A_1myr_3_2_3_1')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(GLU_ARG, d, 'A_1myr_3_2_3_1')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(GLN_ARG, d, 'A_1myr_3_2_3_1')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(TYR_SER, d, 'A_1myr_3_2_3_1')
	if match10 == []:
		 flag = True
		 break
	match11 , totTime11 = cmd.detect(ASN_ARG, d, 'A_1myr_3_2_3_1')
	if match11 == []:
		 flag = True
		 break
	match12 , totTime12 = cmd.detect(SER_ARG, d, 'A_1myr_3_2_3_1')
	if match12 == []:
		 flag = True
		 break
	match13 , totTime13 = cmd.detect(GLU_SER, d, 'A_1myr_3_2_3_1')
	if match13 == []:
		 flag = True
		 break
	match14 , totTime14 = cmd.detect(GLN_SER, d, 'A_1myr_3_2_3_1')
	if match14 == []:
		 flag = True
		 break
	match15 , totTime15 = cmd.detect(TYR_GLN, d, 'A_1myr_3_2_3_1')
	if match15 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_GLN' :  match1,
		'ASN_GLN' :  match2,
		'GLU_ASN' :  match3,
		'GLU_TYR' :  match4,
		'TYR_ARG' :  match5,
		'ASN_SER' :  match6,
		'ASN_TYR' :  match7,
		'GLU_ARG' :  match8,
		'GLN_ARG' :  match9,
		'TYR_SER' :  match10,
		'ASN_ARG' :  match11,
		'SER_ARG' :  match12,
		'GLU_SER' :  match13,
		'GLN_SER' :  match14,
		'TYR_GLN' :  match15}