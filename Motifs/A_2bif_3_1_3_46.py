'''
FUNC:A_2bif_3_1_3_46
PDB:2bif
EC:3.1.3.46
RESI:arg,ala,asn,arg,glu,his
LOCI:a-255,256,262,305,325,390;
'''
import motifFunctions as cmd
HIS_ALA = { 
	'distances':
		[[8.54], [7.96], [7.09], [8.44], [7.13], [7.97]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ALA', 8.54)], [('CG', 'HIS', 'CB', 'ALA', 7.96)], [('ND1', 'HIS', 'CB', 'ALA', 7.09)], [('CD2', 'HIS', 'CB', 'ALA', 8.44)], [('CE1', 'HIS', 'CB', 'ALA', 7.13)], [('NE2', 'HIS', 'CB', 'ALA', 7.97)]]}
ARG_ASN = { 
	'distances':
		[[10.42, 9.53, 8.82, 9.87], [10.52, 9.45, 8.83, 9.54], [9.3, 8.22, 7.75, 8.18], [9.62, 8.4, 8.07, 8.06], [10.44, 9.28, 9.12, 8.78], [11.01, 10.0, 9.87, 9.57], [10.8, 9.59, 9.53, 8.87], [11.3, 10.0, 9.03, 10.12], [11.79, 10.47, 9.65, 10.41], [10.95, 9.71, 9.0, 9.63], [9.82, 8.53, 7.94, 8.31], [9.02, 7.83, 7.41, 7.56], [9.33, 8.34, 7.97, 8.2], [8.19, 6.95, 6.75, 6.46]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASN', 10.42), ('CB', 'ARG', 'CG', 'ASN', 9.53), ('CB', 'ARG', 'OD1', 'ASN', 8.82), ('CB', 'ARG', 'ND2', 'ASN', 9.87)], [('CG', 'ARG', 'CB', 'ASN', 10.52), ('CG', 'ARG', 'CG', 'ASN', 9.45), ('CG', 'ARG', 'OD1', 'ASN', 8.83), ('CG', 'ARG', 'ND2', 'ASN', 9.54)], [('CD', 'ARG', 'CB', 'ASN', 9.3), ('CD', 'ARG', 'CG', 'ASN', 8.22), ('CD', 'ARG', 'OD1', 'ASN', 7.75), ('CD', 'ARG', 'ND2', 'ASN', 8.18)], [('NE', 'ARG', 'CB', 'ASN', 9.62), ('NE', 'ARG', 'CG', 'ASN', 8.4), ('NE', 'ARG', 'OD1', 'ASN', 8.07), ('NE', 'ARG', 'ND2', 'ASN', 8.06)], [('CZ', 'ARG', 'CB', 'ASN', 10.44), ('CZ', 'ARG', 'CG', 'ASN', 9.28), ('CZ', 'ARG', 'OD1', 'ASN', 9.12), ('CZ', 'ARG', 'ND2', 'ASN', 8.78)], [('NH1', 'ARG', 'CB', 'ASN', 11.01), ('NH1', 'ARG', 'CG', 'ASN', 10.0), ('NH1', 'ARG', 'OD1', 'ASN', 9.87), ('NH1', 'ARG', 'ND2', 'ASN', 9.57)], [('NH2', 'ARG', 'CB', 'ASN', 10.8), ('NH2', 'ARG', 'CG', 'ASN', 9.59), ('NH2', 'ARG', 'OD1', 'ASN', 9.53), ('NH2', 'ARG', 'ND2', 'ASN', 8.87)], [('CB', 'ARG', 'CB', 'ASN', 11.3), ('CB', 'ARG', 'CG', 'ASN', 10.0), ('CB', 'ARG', 'OD1', 'ASN', 9.03), ('CB', 'ARG', 'ND2', 'ASN', 10.12)], [('CG', 'ARG', 'CB', 'ASN', 11.79), ('CG', 'ARG', 'CG', 'ASN', 10.47), ('CG', 'ARG', 'OD1', 'ASN', 9.65), ('CG', 'ARG', 'ND2', 'ASN', 10.41)], [('CD', 'ARG', 'CB', 'ASN', 10.95), ('CD', 'ARG', 'CG', 'ASN', 9.71), ('CD', 'ARG', 'OD1', 'ASN', 9.0), ('CD', 'ARG', 'ND2', 'ASN', 9.63)], [('NE', 'ARG', 'CB', 'ASN', 9.82), ('NE', 'ARG', 'CG', 'ASN', 8.53), ('NE', 'ARG', 'OD1', 'ASN', 7.94), ('NE', 'ARG', 'ND2', 'ASN', 8.31)], [('CZ', 'ARG', 'CB', 'ASN', 9.02), ('CZ', 'ARG', 'CG', 'ASN', 7.83), ('CZ', 'ARG', 'OD1', 'ASN', 7.41), ('CZ', 'ARG', 'ND2', 'ASN', 7.56)], [('NH1', 'ARG', 'CB', 'ASN', 9.33), ('NH1', 'ARG', 'CG', 'ASN', 8.34), ('NH1', 'ARG', 'OD1', 'ASN', 7.97), ('NH1', 'ARG', 'ND2', 'ASN', 8.2)], [('NH2', 'ARG', 'CB', 'ASN', 8.19), ('NH2', 'ARG', 'CG', 'ASN', 6.95), ('NH2', 'ARG', 'OD1', 'ASN', 6.75), ('NH2', 'ARG', 'ND2', 'ASN', 6.46)]]}
GLU_ASN = { 
	'distances':
		[[13.6, 12.23, 12.13, 11.33], [13.15, 11.8, 11.82, 10.78], [13.3, 11.9, 11.84, 10.91], [14.29, 12.85, 12.69, 11.93], [12.58, 11.2, 11.19, 10.17]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASN', 13.6), ('CB', 'GLU', 'CG', 'ASN', 12.23), ('CB', 'GLU', 'OD1', 'ASN', 12.13), ('CB', 'GLU', 'ND2', 'ASN', 11.33)], [('CG', 'GLU', 'CB', 'ASN', 13.15), ('CG', 'GLU', 'CG', 'ASN', 11.8), ('CG', 'GLU', 'OD1', 'ASN', 11.82), ('CG', 'GLU', 'ND2', 'ASN', 10.78)], [('CD', 'GLU', 'CB', 'ASN', 13.3), ('CD', 'GLU', 'CG', 'ASN', 11.9), ('CD', 'GLU', 'OD1', 'ASN', 11.84), ('CD', 'GLU', 'ND2', 'ASN', 10.91)], [('OE1', 'GLU', 'CB', 'ASN', 14.29), ('OE1', 'GLU', 'CG', 'ASN', 12.85), ('OE1', 'GLU', 'OD1', 'ASN', 12.69), ('OE1', 'GLU', 'ND2', 'ASN', 11.93)], [('OE2', 'GLU', 'CB', 'ASN', 12.58), ('OE2', 'GLU', 'CG', 'ASN', 11.2), ('OE2', 'GLU', 'OD1', 'ASN', 11.19), ('OE2', 'GLU', 'ND2', 'ASN', 10.17)]]}
ASN_ARGI = { 
	'distances':
		[[11.3, 11.79, 10.95, 9.82, 9.02, 9.33, 8.19], [10.0, 10.47, 9.71, 8.53, 7.83, 8.34, 6.95], [9.03, 9.65, 9.0, 7.94, 7.41, 7.97, 6.75], [10.12, 10.41, 9.63, 8.31, 7.56, 8.2, 6.46]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ARGI', 11.3), ('CB', 'ASN', 'CG', 'ARGI', 11.79), ('CB', 'ASN', 'CD', 'ARGI', 10.95), ('CB', 'ASN', 'NE', 'ARGI', 9.82), ('CB', 'ASN', 'CZ', 'ARGI', 9.02), ('CB', 'ASN', 'NH1', 'ARGI', 9.33), ('CB', 'ASN', 'NH2', 'ARGI', 8.19)], [('CG', 'ASN', 'CB', 'ARGI', 10.0), ('CG', 'ASN', 'CG', 'ARGI', 10.47), ('CG', 'ASN', 'CD', 'ARGI', 9.71), ('CG', 'ASN', 'NE', 'ARGI', 8.53), ('CG', 'ASN', 'CZ', 'ARGI', 7.83), ('CG', 'ASN', 'NH1', 'ARGI', 8.34), ('CG', 'ASN', 'NH2', 'ARGI', 6.95)], [('OD1', 'ASN', 'CB', 'ARGI', 9.03), ('OD1', 'ASN', 'CG', 'ARGI', 9.65), ('OD1', 'ASN', 'CD', 'ARGI', 9.0), ('OD1', 'ASN', 'NE', 'ARGI', 7.94), ('OD1', 'ASN', 'CZ', 'ARGI', 7.41), ('OD1', 'ASN', 'NH1', 'ARGI', 7.97), ('OD1', 'ASN', 'NH2', 'ARGI', 6.75)], [('ND2', 'ASN', 'CB', 'ARGI', 10.12), ('ND2', 'ASN', 'CG', 'ARGI', 10.41), ('ND2', 'ASN', 'CD', 'ARGI', 9.63), ('ND2', 'ASN', 'NE', 'ARGI', 8.31), ('ND2', 'ASN', 'CZ', 'ARGI', 7.56), ('ND2', 'ASN', 'NH1', 'ARGI', 8.2), ('ND2', 'ASN', 'NH2', 'ARGI', 6.46)]]}
HIS_ARG = { 
	'distances':
		[[9.95, 8.64, 8.39, 7.3, 7.57, 8.78, 7.03], [9.03, 7.67, 7.66, 6.63, 6.81, 7.88, 6.47], [7.69, 6.3, 6.29, 5.33, 5.63, 6.67, 5.58], [9.45, 8.1, 8.35, 7.41, 7.43, 8.3, 7.15], [7.37, 5.98, 6.35, 5.61, 5.73, 6.46, 5.92], [8.52, 7.2, 7.66, 6.9, 6.87, 7.52, 6.86], [7.66, 7.57, 8.27, 7.68, 8.57, 9.84, 8.4], [8.28, 8.5, 9.33, 8.76, 9.66, 10.95, 9.44], [8.38, 8.85, 9.59, 8.9, 9.69, 11.01, 9.36], [9.17, 9.42, 10.4, 9.96, 10.92, 12.2, 10.76], [9.25, 9.86, 10.7, 10.09, 10.92, 12.22, 10.6], [9.72, 10.2, 11.18, 10.7, 11.62, 12.91, 11.4]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 9.95), ('CB', 'HIS', 'CG', 'ARG', 8.64), ('CB', 'HIS', 'CD', 'ARG', 8.39), ('CB', 'HIS', 'NE', 'ARG', 7.3), ('CB', 'HIS', 'CZ', 'ARG', 7.57), ('CB', 'HIS', 'NH1', 'ARG', 8.78), ('CB', 'HIS', 'NH2', 'ARG', 7.03)], [('CG', 'HIS', 'CB', 'ARG', 9.03), ('CG', 'HIS', 'CG', 'ARG', 7.67), ('CG', 'HIS', 'CD', 'ARG', 7.66), ('CG', 'HIS', 'NE', 'ARG', 6.63), ('CG', 'HIS', 'CZ', 'ARG', 6.81), ('CG', 'HIS', 'NH1', 'ARG', 7.88), ('CG', 'HIS', 'NH2', 'ARG', 6.47)], [('ND1', 'HIS', 'CB', 'ARG', 7.69), ('ND1', 'HIS', 'CG', 'ARG', 6.3), ('ND1', 'HIS', 'CD', 'ARG', 6.29), ('ND1', 'HIS', 'NE', 'ARG', 5.33), ('ND1', 'HIS', 'CZ', 'ARG', 5.63), ('ND1', 'HIS', 'NH1', 'ARG', 6.67), ('ND1', 'HIS', 'NH2', 'ARG', 5.58)], [('CD2', 'HIS', 'CB', 'ARG', 9.45), ('CD2', 'HIS', 'CG', 'ARG', 8.1), ('CD2', 'HIS', 'CD', 'ARG', 8.35), ('CD2', 'HIS', 'NE', 'ARG', 7.41), ('CD2', 'HIS', 'CZ', 'ARG', 7.43), ('CD2', 'HIS', 'NH1', 'ARG', 8.3), ('CD2', 'HIS', 'NH2', 'ARG', 7.15)], [('CE1', 'HIS', 'CB', 'ARG', 7.37), ('CE1', 'HIS', 'CG', 'ARG', 5.98), ('CE1', 'HIS', 'CD', 'ARG', 6.35), ('CE1', 'HIS', 'NE', 'ARG', 5.61), ('CE1', 'HIS', 'CZ', 'ARG', 5.73), ('CE1', 'HIS', 'NH1', 'ARG', 6.46), ('CE1', 'HIS', 'NH2', 'ARG', 5.92)], [('NE2', 'HIS', 'CB', 'ARG', 8.52), ('NE2', 'HIS', 'CG', 'ARG', 7.2), ('NE2', 'HIS', 'CD', 'ARG', 7.66), ('NE2', 'HIS', 'NE', 'ARG', 6.9), ('NE2', 'HIS', 'CZ', 'ARG', 6.87), ('NE2', 'HIS', 'NH1', 'ARG', 7.52), ('NE2', 'HIS', 'NH2', 'ARG', 6.86)], [('CB', 'HIS', 'CB', 'ARG', 7.66), ('CB', 'HIS', 'CG', 'ARG', 7.57), ('CB', 'HIS', 'CD', 'ARG', 8.27), ('CB', 'HIS', 'NE', 'ARG', 7.68), ('CB', 'HIS', 'CZ', 'ARG', 8.57), ('CB', 'HIS', 'NH1', 'ARG', 9.84), ('CB', 'HIS', 'NH2', 'ARG', 8.4)], [('CG', 'HIS', 'CB', 'ARG', 8.28), ('CG', 'HIS', 'CG', 'ARG', 8.5), ('CG', 'HIS', 'CD', 'ARG', 9.33), ('CG', 'HIS', 'NE', 'ARG', 8.76), ('CG', 'HIS', 'CZ', 'ARG', 9.66), ('CG', 'HIS', 'NH1', 'ARG', 10.95), ('CG', 'HIS', 'NH2', 'ARG', 9.44)], [('ND1', 'HIS', 'CB', 'ARG', 8.38), ('ND1', 'HIS', 'CG', 'ARG', 8.85), ('ND1', 'HIS', 'CD', 'ARG', 9.59), ('ND1', 'HIS', 'NE', 'ARG', 8.9), ('ND1', 'HIS', 'CZ', 'ARG', 9.69), ('ND1', 'HIS', 'NH1', 'ARG', 11.01), ('ND1', 'HIS', 'NH2', 'ARG', 9.36)], [('CD2', 'HIS', 'CB', 'ARG', 9.17), ('CD2', 'HIS', 'CG', 'ARG', 9.42), ('CD2', 'HIS', 'CD', 'ARG', 10.4), ('CD2', 'HIS', 'NE', 'ARG', 9.96), ('CD2', 'HIS', 'CZ', 'ARG', 10.92), ('CD2', 'HIS', 'NH1', 'ARG', 12.2), ('CD2', 'HIS', 'NH2', 'ARG', 10.76)], [('CE1', 'HIS', 'CB', 'ARG', 9.25), ('CE1', 'HIS', 'CG', 'ARG', 9.86), ('CE1', 'HIS', 'CD', 'ARG', 10.7), ('CE1', 'HIS', 'NE', 'ARG', 10.09), ('CE1', 'HIS', 'CZ', 'ARG', 10.92), ('CE1', 'HIS', 'NH1', 'ARG', 12.22), ('CE1', 'HIS', 'NH2', 'ARG', 10.6)], [('NE2', 'HIS', 'CB', 'ARG', 9.72), ('NE2', 'HIS', 'CG', 'ARG', 10.2), ('NE2', 'HIS', 'CD', 'ARG', 11.18), ('NE2', 'HIS', 'NE', 'ARG', 10.7), ('NE2', 'HIS', 'CZ', 'ARG', 11.62), ('NE2', 'HIS', 'NH1', 'ARG', 12.91), ('NE2', 'HIS', 'NH2', 'ARG', 11.4)]]}
ALA_ASN = { 
	'distances':
		[11.05, 9.9, 8.83, 10.29],
	'comparisons':
		[('CB', 'ALA', 'CB', 'ASN', 11.05), ('CB', 'ALA', 'CG', 'ASN', 9.9), ('CB', 'ALA', 'OD1', 'ASN', 8.83), ('CB', 'ALA', 'ND2', 'ASN', 10.29)]}
HIS_ASN = { 
	'distances':
		[[12.52, 11.02, 10.55, 10.41], [12.83, 11.35, 10.84, 10.83], [11.95, 10.52, 9.99, 10.09], [14.04, 12.59, 12.04, 12.1], [12.76, 11.38, 10.82, 11.02], [14.0, 12.6, 12.03, 12.2]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 12.52), ('CB', 'HIS', 'CG', 'ASN', 11.02), ('CB', 'HIS', 'OD1', 'ASN', 10.55), ('CB', 'HIS', 'ND2', 'ASN', 10.41)], [('CG', 'HIS', 'CB', 'ASN', 12.83), ('CG', 'HIS', 'CG', 'ASN', 11.35), ('CG', 'HIS', 'OD1', 'ASN', 10.84), ('CG', 'HIS', 'ND2', 'ASN', 10.83)], [('ND1', 'HIS', 'CB', 'ASN', 11.95), ('ND1', 'HIS', 'CG', 'ASN', 10.52), ('ND1', 'HIS', 'OD1', 'ASN', 9.99), ('ND1', 'HIS', 'ND2', 'ASN', 10.09)], [('CD2', 'HIS', 'CB', 'ASN', 14.04), ('CD2', 'HIS', 'CG', 'ASN', 12.59), ('CD2', 'HIS', 'OD1', 'ASN', 12.04), ('CD2', 'HIS', 'ND2', 'ASN', 12.1)], [('CE1', 'HIS', 'CB', 'ASN', 12.76), ('CE1', 'HIS', 'CG', 'ASN', 11.38), ('CE1', 'HIS', 'OD1', 'ASN', 10.82), ('CE1', 'HIS', 'ND2', 'ASN', 11.02)], [('NE2', 'HIS', 'CB', 'ASN', 14.0), ('NE2', 'HIS', 'CG', 'ASN', 12.6), ('NE2', 'HIS', 'OD1', 'ASN', 12.03), ('NE2', 'HIS', 'ND2', 'ASN', 12.2)]]}
ARG_ARG = { 
	'distances':
		[[10.36, 11.57, 12.05, 11.38, 11.83, 12.89, 11.44], [9.92, 10.98, 11.5, 10.75, 11.25, 12.41, 10.79], [9.83, 10.75, 11.05, 10.11, 10.44, 11.6, 9.81], [9.68, 10.39, 10.68, 9.65, 9.99, 11.24, 9.28], [10.77, 11.36, 11.66, 10.59, 10.9, 12.18, 10.1], [11.93, 12.6, 12.92, 11.86, 12.15, 13.4, 11.33], [10.9, 11.28, 11.53, 10.4, 10.68, 11.98, 9.82], [10.36, 9.92, 9.83, 9.68, 10.77, 11.93, 10.9], [11.57, 10.98, 10.75, 10.39, 11.36, 12.6, 11.28], [12.05, 11.5, 11.05, 10.68, 11.66, 12.92, 11.53], [11.38, 10.75, 10.11, 9.65, 10.59, 11.86, 10.4], [11.83, 11.25, 10.44, 9.99, 10.9, 12.15, 10.68], [12.89, 12.41, 11.6, 11.24, 12.18, 13.4, 11.98], [11.44, 10.79, 9.81, 9.28, 10.1, 11.33, 9.82]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ARG', 10.36), ('CB', 'ARG', 'CG', 'ARG', 11.57), ('CB', 'ARG', 'CD', 'ARG', 12.05), ('CB', 'ARG', 'NE', 'ARG', 11.38), ('CB', 'ARG', 'CZ', 'ARG', 11.83), ('CB', 'ARG', 'NH1', 'ARG', 12.89), ('CB', 'ARG', 'NH2', 'ARG', 11.44)], [('CG', 'ARG', 'CB', 'ARG', 9.92), ('CG', 'ARG', 'CG', 'ARG', 10.98), ('CG', 'ARG', 'CD', 'ARG', 11.5), ('CG', 'ARG', 'NE', 'ARG', 10.75), ('CG', 'ARG', 'CZ', 'ARG', 11.25), ('CG', 'ARG', 'NH1', 'ARG', 12.41), ('CG', 'ARG', 'NH2', 'ARG', 10.79)], [('CD', 'ARG', 'CB', 'ARG', 9.83), ('CD', 'ARG', 'CG', 'ARG', 10.75), ('CD', 'ARG', 'CD', 'ARG', 11.05), ('CD', 'ARG', 'NE', 'ARG', 10.11), ('CD', 'ARG', 'CZ', 'ARG', 10.44), ('CD', 'ARG', 'NH1', 'ARG', 11.6), ('CD', 'ARG', 'NH2', 'ARG', 9.81)], [('NE', 'ARG', 'CB', 'ARG', 9.68), ('NE', 'ARG', 'CG', 'ARG', 10.39), ('NE', 'ARG', 'CD', 'ARG', 10.68), ('NE', 'ARG', 'NE', 'ARG', 9.65), ('NE', 'ARG', 'CZ', 'ARG', 9.99), ('NE', 'ARG', 'NH1', 'ARG', 11.24), ('NE', 'ARG', 'NH2', 'ARG', 9.28)], [('CZ', 'ARG', 'CB', 'ARG', 10.77), ('CZ', 'ARG', 'CG', 'ARG', 11.36), ('CZ', 'ARG', 'CD', 'ARG', 11.66), ('CZ', 'ARG', 'NE', 'ARG', 10.59), ('CZ', 'ARG', 'CZ', 'ARG', 10.9), ('CZ', 'ARG', 'NH1', 'ARG', 12.18), ('CZ', 'ARG', 'NH2', 'ARG', 10.1)], [('NH1', 'ARG', 'CB', 'ARG', 11.93), ('NH1', 'ARG', 'CG', 'ARG', 12.6), ('NH1', 'ARG', 'CD', 'ARG', 12.92), ('NH1', 'ARG', 'NE', 'ARG', 11.86), ('NH1', 'ARG', 'CZ', 'ARG', 12.15), ('NH1', 'ARG', 'NH1', 'ARG', 13.4), ('NH1', 'ARG', 'NH2', 'ARG', 11.33)], [('NH2', 'ARG', 'CB', 'ARG', 10.9), ('NH2', 'ARG', 'CG', 'ARG', 11.28), ('NH2', 'ARG', 'CD', 'ARG', 11.53), ('NH2', 'ARG', 'NE', 'ARG', 10.4), ('NH2', 'ARG', 'CZ', 'ARG', 10.68), ('NH2', 'ARG', 'NH1', 'ARG', 11.98), ('NH2', 'ARG', 'NH2', 'ARG', 9.82)], [('CB', 'ARG', 'CB', 'ARG', 10.36), ('CB', 'ARG', 'CG', 'ARG', 9.92), ('CB', 'ARG', 'CD', 'ARG', 9.83), ('CB', 'ARG', 'NE', 'ARG', 9.68), ('CB', 'ARG', 'CZ', 'ARG', 10.77), ('CB', 'ARG', 'NH1', 'ARG', 11.93), ('CB', 'ARG', 'NH2', 'ARG', 10.9)], [('CG', 'ARG', 'CB', 'ARG', 11.57), ('CG', 'ARG', 'CG', 'ARG', 10.98), ('CG', 'ARG', 'CD', 'ARG', 10.75), ('CG', 'ARG', 'NE', 'ARG', 10.39), ('CG', 'ARG', 'CZ', 'ARG', 11.36), ('CG', 'ARG', 'NH1', 'ARG', 12.6), ('CG', 'ARG', 'NH2', 'ARG', 11.28)], [('CD', 'ARG', 'CB', 'ARG', 12.05), ('CD', 'ARG', 'CG', 'ARG', 11.5), ('CD', 'ARG', 'CD', 'ARG', 11.05), ('CD', 'ARG', 'NE', 'ARG', 10.68), ('CD', 'ARG', 'CZ', 'ARG', 11.66), ('CD', 'ARG', 'NH1', 'ARG', 12.92), ('CD', 'ARG', 'NH2', 'ARG', 11.53)], [('NE', 'ARG', 'CB', 'ARG', 11.38), ('NE', 'ARG', 'CG', 'ARG', 10.75), ('NE', 'ARG', 'CD', 'ARG', 10.11), ('NE', 'ARG', 'NE', 'ARG', 9.65), ('NE', 'ARG', 'CZ', 'ARG', 10.59), ('NE', 'ARG', 'NH1', 'ARG', 11.86), ('NE', 'ARG', 'NH2', 'ARG', 10.4)], [('CZ', 'ARG', 'CB', 'ARG', 11.83), ('CZ', 'ARG', 'CG', 'ARG', 11.25), ('CZ', 'ARG', 'CD', 'ARG', 10.44), ('CZ', 'ARG', 'NE', 'ARG', 9.99), ('CZ', 'ARG', 'CZ', 'ARG', 10.9), ('CZ', 'ARG', 'NH1', 'ARG', 12.15), ('CZ', 'ARG', 'NH2', 'ARG', 10.68)], [('NH1', 'ARG', 'CB', 'ARG', 12.89), ('NH1', 'ARG', 'CG', 'ARG', 12.41), ('NH1', 'ARG', 'CD', 'ARG', 11.6), ('NH1', 'ARG', 'NE', 'ARG', 11.24), ('NH1', 'ARG', 'CZ', 'ARG', 12.18), ('NH1', 'ARG', 'NH1', 'ARG', 13.4), ('NH1', 'ARG', 'NH2', 'ARG', 11.98)], [('NH2', 'ARG', 'CB', 'ARG', 11.44), ('NH2', 'ARG', 'CG', 'ARG', 10.79), ('NH2', 'ARG', 'CD', 'ARG', 9.81), ('NH2', 'ARG', 'NE', 'ARG', 9.28), ('NH2', 'ARG', 'CZ', 'ARG', 10.1), ('NH2', 'ARG', 'NH1', 'ARG', 11.33), ('NH2', 'ARG', 'NH2', 'ARG', 9.82)]]}
GLU_ARG = { 
	'distances':
		[[10.94, 9.43, 8.96, 7.54, 6.91, 7.78, 5.8], [11.7, 10.23, 9.53, 8.07, 7.55, 8.53, 6.3], [12.23, 10.81, 10.15, 8.75, 8.5, 9.62, 7.36], [12.7, 11.27, 10.79, 9.43, 9.21, 10.31, 8.16], [12.42, 11.06, 10.27, 8.92, 8.82, 10.02, 7.72], [11.21, 11.11, 11.55, 10.65, 11.17, 12.46, 10.55], [11.17, 10.87, 11.1, 10.11, 10.47, 11.71, 9.77], [10.35, 9.85, 10.09, 9.21, 9.65, 10.83, 9.11], [10.38, 9.82, 10.24, 9.56, 10.16, 11.31, 9.8], [9.94, 9.32, 9.34, 8.39, 8.69, 9.82, 8.12]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 10.94), ('CB', 'GLU', 'CG', 'ARG', 9.43), ('CB', 'GLU', 'CD', 'ARG', 8.96), ('CB', 'GLU', 'NE', 'ARG', 7.54), ('CB', 'GLU', 'CZ', 'ARG', 6.91), ('CB', 'GLU', 'NH1', 'ARG', 7.78), ('CB', 'GLU', 'NH2', 'ARG', 5.8)], [('CG', 'GLU', 'CB', 'ARG', 11.7), ('CG', 'GLU', 'CG', 'ARG', 10.23), ('CG', 'GLU', 'CD', 'ARG', 9.53), ('CG', 'GLU', 'NE', 'ARG', 8.07), ('CG', 'GLU', 'CZ', 'ARG', 7.55), ('CG', 'GLU', 'NH1', 'ARG', 8.53), ('CG', 'GLU', 'NH2', 'ARG', 6.3)], [('CD', 'GLU', 'CB', 'ARG', 12.23), ('CD', 'GLU', 'CG', 'ARG', 10.81), ('CD', 'GLU', 'CD', 'ARG', 10.15), ('CD', 'GLU', 'NE', 'ARG', 8.75), ('CD', 'GLU', 'CZ', 'ARG', 8.5), ('CD', 'GLU', 'NH1', 'ARG', 9.62), ('CD', 'GLU', 'NH2', 'ARG', 7.36)], [('OE1', 'GLU', 'CB', 'ARG', 12.7), ('OE1', 'GLU', 'CG', 'ARG', 11.27), ('OE1', 'GLU', 'CD', 'ARG', 10.79), ('OE1', 'GLU', 'NE', 'ARG', 9.43), ('OE1', 'GLU', 'CZ', 'ARG', 9.21), ('OE1', 'GLU', 'NH1', 'ARG', 10.31), ('OE1', 'GLU', 'NH2', 'ARG', 8.16)], [('OE2', 'GLU', 'CB', 'ARG', 12.42), ('OE2', 'GLU', 'CG', 'ARG', 11.06), ('OE2', 'GLU', 'CD', 'ARG', 10.27), ('OE2', 'GLU', 'NE', 'ARG', 8.92), ('OE2', 'GLU', 'CZ', 'ARG', 8.82), ('OE2', 'GLU', 'NH1', 'ARG', 10.02), ('OE2', 'GLU', 'NH2', 'ARG', 7.72)], [('CB', 'GLU', 'CB', 'ARG', 11.21), ('CB', 'GLU', 'CG', 'ARG', 11.11), ('CB', 'GLU', 'CD', 'ARG', 11.55), ('CB', 'GLU', 'NE', 'ARG', 10.65), ('CB', 'GLU', 'CZ', 'ARG', 11.17), ('CB', 'GLU', 'NH1', 'ARG', 12.46), ('CB', 'GLU', 'NH2', 'ARG', 10.55)], [('CG', 'GLU', 'CB', 'ARG', 11.17), ('CG', 'GLU', 'CG', 'ARG', 10.87), ('CG', 'GLU', 'CD', 'ARG', 11.1), ('CG', 'GLU', 'NE', 'ARG', 10.11), ('CG', 'GLU', 'CZ', 'ARG', 10.47), ('CG', 'GLU', 'NH1', 'ARG', 11.71), ('CG', 'GLU', 'NH2', 'ARG', 9.77)], [('CD', 'GLU', 'CB', 'ARG', 10.35), ('CD', 'GLU', 'CG', 'ARG', 9.85), ('CD', 'GLU', 'CD', 'ARG', 10.09), ('CD', 'GLU', 'NE', 'ARG', 9.21), ('CD', 'GLU', 'CZ', 'ARG', 9.65), ('CD', 'GLU', 'NH1', 'ARG', 10.83), ('CD', 'GLU', 'NH2', 'ARG', 9.11)], [('OE1', 'GLU', 'CB', 'ARG', 10.38), ('OE1', 'GLU', 'CG', 'ARG', 9.82), ('OE1', 'GLU', 'CD', 'ARG', 10.24), ('OE1', 'GLU', 'NE', 'ARG', 9.56), ('OE1', 'GLU', 'CZ', 'ARG', 10.16), ('OE1', 'GLU', 'NH1', 'ARG', 11.31), ('OE1', 'GLU', 'NH2', 'ARG', 9.8)], [('OE2', 'GLU', 'CB', 'ARG', 9.94), ('OE2', 'GLU', 'CG', 'ARG', 9.32), ('OE2', 'GLU', 'CD', 'ARG', 9.34), ('OE2', 'GLU', 'NE', 'ARG', 8.39), ('OE2', 'GLU', 'CZ', 'ARG', 8.69), ('OE2', 'GLU', 'NH1', 'ARG', 9.82), ('OE2', 'GLU', 'NH2', 'ARG', 8.12)]]}
GLU_HIS = { 
	'distances':
		[[5.69, 5.53, 5.95, 5.83, 6.43, 6.38], [5.94, 6.31, 6.79, 6.92, 7.56, 7.65], [5.36, 6.22, 7.01, 6.92, 7.96, 7.94], [5.27, 6.11, 7.18, 6.57, 8.02, 7.75], [5.69, 6.8, 7.49, 7.72, 8.59, 8.74]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 5.69), ('CB', 'GLU', 'CG', 'HIS', 5.53), ('CB', 'GLU', 'ND1', 'HIS', 5.95), ('CB', 'GLU', 'CD2', 'HIS', 5.83), ('CB', 'GLU', 'CE1', 'HIS', 6.43), ('CB', 'GLU', 'NE2', 'HIS', 6.38)], [('CG', 'GLU', 'CB', 'HIS', 5.94), ('CG', 'GLU', 'CG', 'HIS', 6.31), ('CG', 'GLU', 'ND1', 'HIS', 6.79), ('CG', 'GLU', 'CD2', 'HIS', 6.92), ('CG', 'GLU', 'CE1', 'HIS', 7.56), ('CG', 'GLU', 'NE2', 'HIS', 7.65)], [('CD', 'GLU', 'CB', 'HIS', 5.36), ('CD', 'GLU', 'CG', 'HIS', 6.22), ('CD', 'GLU', 'ND1', 'HIS', 7.01), ('CD', 'GLU', 'CD2', 'HIS', 6.92), ('CD', 'GLU', 'CE1', 'HIS', 7.96), ('CD', 'GLU', 'NE2', 'HIS', 7.94)], [('OE1', 'GLU', 'CB', 'HIS', 5.27), ('OE1', 'GLU', 'CG', 'HIS', 6.11), ('OE1', 'GLU', 'ND1', 'HIS', 7.18), ('OE1', 'GLU', 'CD2', 'HIS', 6.57), ('OE1', 'GLU', 'CE1', 'HIS', 8.02), ('OE1', 'GLU', 'NE2', 'HIS', 7.75)], [('OE2', 'GLU', 'CB', 'HIS', 5.69), ('OE2', 'GLU', 'CG', 'HIS', 6.8), ('OE2', 'GLU', 'ND1', 'HIS', 7.49), ('OE2', 'GLU', 'CD2', 'HIS', 7.72), ('OE2', 'GLU', 'CE1', 'HIS', 8.59), ('OE2', 'GLU', 'NE2', 'HIS', 8.74)]]}
GLU_ALA = { 
	'distances':
		[[11.0], [11.63], [11.6], [11.78], [11.65]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ALA', 11.0)], [('CG', 'GLU', 'CB', 'ALA', 11.63)], [('CD', 'GLU', 'CB', 'ALA', 11.6)], [('OE1', 'GLU', 'CB', 'ALA', 11.78)], [('OE2', 'GLU', 'CB', 'ALA', 11.65)]]}
ALA_ARG = { 
	'distances':
		[5.78, 5.85, 6.58, 7.23, 8.4, 9.01, 9.25, 7.15, 8.54, 9.33, 9.12, 9.93, 10.88, 10.04],
	'comparisons':
		[('CB', 'ALA', 'CB', 'ARG', 5.78), ('CB', 'ALA', 'CG', 'ARG', 5.85), ('CB', 'ALA', 'CD', 'ARG', 6.58), ('CB', 'ALA', 'NE', 'ARG', 7.23), ('CB', 'ALA', 'CZ', 'ARG', 8.4), ('CB', 'ALA', 'NH1', 'ARG', 9.01), ('CB', 'ALA', 'NH2', 'ARG', 9.25), ('CB', 'ALA', 'CB', 'ARG', 7.15), ('CB', 'ALA', 'CG', 'ARG', 8.54), ('CB', 'ALA', 'CD', 'ARG', 9.33), ('CB', 'ALA', 'NE', 'ARG', 9.12), ('CB', 'ALA', 'CZ', 'ARG', 9.93), ('CB', 'ALA', 'NH1', 'ARG', 10.88), ('CB', 'ALA', 'NH2', 'ARG', 10.04)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ALA, d, 'A_2bif_3_1_3_46')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_ASN, d, 'A_2bif_3_1_3_46')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_ASN, d, 'A_2bif_3_1_3_46')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASN_ARGI, d, 'A_2bif_3_1_3_46')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_ARG, d, 'A_2bif_3_1_3_46')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ALA_ASN, d, 'A_2bif_3_1_3_46')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(HIS_ASN, d, 'A_2bif_3_1_3_46')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ARG_ARG, d, 'A_2bif_3_1_3_46')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(GLU_ARG, d, 'A_2bif_3_1_3_46')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(GLU_HIS, d, 'A_2bif_3_1_3_46')
	if match10 == []:
		 flag = True
		 break
	match11 , totTime11 = cmd.detect(GLU_ALA, d, 'A_2bif_3_1_3_46')
	if match11 == []:
		 flag = True
		 break
	match12 , totTime12 = cmd.detect(ALA_ARG, d, 'A_2bif_3_1_3_46')
	if match12 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ALA' :  match1,
		'ARG_ASN' :  match2,
		'GLU_ASN' :  match3,
		'ASN_ARGI' :  match4,
		'HIS_ARG' :  match5,
		'ALA_ASN' :  match6,
		'HIS_ASN' :  match7,
		'ARG_ARG' :  match8,
		'GLU_ARG' :  match9,
		'GLU_HIS' :  match10,
		'GLU_ALA' :  match11,
		'ALA_ARG' :  match12}