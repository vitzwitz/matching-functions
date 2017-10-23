'''
FUNC:A_1kfx_3_4_22_53
PDB:1kfx
EC:3.4.22.53
RESI:gln,cys,his,asn,trp
LOCI:l-99,105,262,286,288;
'''
import motifFunctions as cmd
ASN_GLN = { 
	'distances':
		[[19.03, 19.2, 20.31, 21.42, 20.09], [17.68, 17.91, 19.02, 20.1, 18.83], [16.76, 16.99, 18.15, 19.23, 18.01], [17.63, 17.91, 18.95, 20.02, 18.73]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'GLN', 19.03), ('CB', 'ASN', 'CG', 'GLN', 19.2), ('CB', 'ASN', 'CD', 'GLN', 20.31), ('CB', 'ASN', 'OE1', 'GLN', 21.42), ('CB', 'ASN', 'NE2', 'GLN', 20.09)], [('CG', 'ASN', 'CB', 'GLN', 17.68), ('CG', 'ASN', 'CG', 'GLN', 17.91), ('CG', 'ASN', 'CD', 'GLN', 19.02), ('CG', 'ASN', 'OE1', 'GLN', 20.1), ('CG', 'ASN', 'NE2', 'GLN', 18.83)], [('OD1', 'ASN', 'CB', 'GLN', 16.76), ('OD1', 'ASN', 'CG', 'GLN', 16.99), ('OD1', 'ASN', 'CD', 'GLN', 18.15), ('OD1', 'ASN', 'OE1', 'GLN', 19.23), ('OD1', 'ASN', 'NE2', 'GLN', 18.01)], [('ND2', 'ASN', 'CB', 'GLN', 17.63), ('ND2', 'ASN', 'CG', 'GLN', 17.91), ('ND2', 'ASN', 'CD', 'GLN', 18.95), ('ND2', 'ASN', 'OE1', 'GLN', 20.02), ('ND2', 'ASN', 'NE2', 'GLN', 18.73)]]}
TRP_ASN = { 
	'distances':
		[[7.46, 6.05, 6.03, 5.2], [8.44, 7.0, 6.68, 6.41], [9.79, 8.34, 8.01, 7.7], [8.43, 7.05, 6.51, 6.78], [10.52, 9.09, 8.58, 8.62], [9.81, 8.44, 7.83, 8.19], [7.63, 6.4, 5.74, 6.45], [10.46, 9.19, 8.45, 9.13], [8.49, 7.42, 6.64, 7.67], [9.86, 8.73, 7.93, 8.88]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'ASN', 7.46), ('CB', 'TRP', 'CG', 'ASN', 6.05), ('CB', 'TRP', 'OD1', 'ASN', 6.03), ('CB', 'TRP', 'ND2', 'ASN', 5.2)], [('CG', 'TRP', 'CB', 'ASN', 8.44), ('CG', 'TRP', 'CG', 'ASN', 7.0), ('CG', 'TRP', 'OD1', 'ASN', 6.68), ('CG', 'TRP', 'ND2', 'ASN', 6.41)], [('CD1', 'TRP', 'CB', 'ASN', 9.79), ('CD1', 'TRP', 'CG', 'ASN', 8.34), ('CD1', 'TRP', 'OD1', 'ASN', 8.01), ('CD1', 'TRP', 'ND2', 'ASN', 7.7)], [('CD2', 'TRP', 'CB', 'ASN', 8.43), ('CD2', 'TRP', 'CG', 'ASN', 7.05), ('CD2', 'TRP', 'OD1', 'ASN', 6.51), ('CD2', 'TRP', 'ND2', 'ASN', 6.78)], [('NE1', 'TRP', 'CB', 'ASN', 10.52), ('NE1', 'TRP', 'CG', 'ASN', 9.09), ('NE1', 'TRP', 'OD1', 'ASN', 8.58), ('NE1', 'TRP', 'ND2', 'ASN', 8.62)], [('CE2', 'TRP', 'CB', 'ASN', 9.81), ('CE2', 'TRP', 'CG', 'ASN', 8.44), ('CE2', 'TRP', 'OD1', 'ASN', 7.83), ('CE2', 'TRP', 'ND2', 'ASN', 8.19)], [('CE3', 'TRP', 'CB', 'ASN', 7.63), ('CE3', 'TRP', 'CG', 'ASN', 6.4), ('CE3', 'TRP', 'OD1', 'ASN', 5.74), ('CE3', 'TRP', 'ND2', 'ASN', 6.45)], [('CZ2', 'TRP', 'CB', 'ASN', 10.46), ('CZ2', 'TRP', 'CG', 'ASN', 9.19), ('CZ2', 'TRP', 'OD1', 'ASN', 8.45), ('CZ2', 'TRP', 'ND2', 'ASN', 9.13)], [('CZ3', 'TRP', 'CB', 'ASN', 8.49), ('CZ3', 'TRP', 'CG', 'ASN', 7.42), ('CZ3', 'TRP', 'OD1', 'ASN', 6.64), ('CZ3', 'TRP', 'ND2', 'ASN', 7.67)], [('CH2', 'TRP', 'CB', 'ASN', 9.86), ('CH2', 'TRP', 'CG', 'ASN', 8.73), ('CH2', 'TRP', 'OD1', 'ASN', 7.93), ('CH2', 'TRP', 'ND2', 'ASN', 8.88)]]}
HIS_CYS = { 
	'distances':
		[[12.32, 13.18, 11.61, 12.66, 13.07, 14.49], [12.51, 13.57, 11.57, 12.68, 13.1, 14.55], [11.82, 13.03, 10.97, 12.06, 12.37, 13.81], [13.51, 14.63, 12.3, 13.46, 13.97, 15.43], [12.46, 13.8, 11.38, 12.51, 12.85, 14.29], [13.46, 14.74, 12.17, 13.34, 13.81, 15.26]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYS', 12.32), ('CB', 'HIS', 'SG', 'CYS', 13.18), ('CB', 'HIS', 'O', 'CYS', 11.61), ('CB', 'HIS', 'C', 'CYS', 12.66), ('CB', 'HIS', 'CA', 'CYS', 13.07), ('CB', 'HIS', 'N', 'CYS', 14.49)], [('CG', 'HIS', 'CB', 'CYS', 12.51), ('CG', 'HIS', 'SG', 'CYS', 13.57), ('CG', 'HIS', 'O', 'CYS', 11.57), ('CG', 'HIS', 'C', 'CYS', 12.68), ('CG', 'HIS', 'CA', 'CYS', 13.1), ('CG', 'HIS', 'N', 'CYS', 14.55)], [('ND1', 'HIS', 'CB', 'CYS', 11.82), ('ND1', 'HIS', 'SG', 'CYS', 13.03), ('ND1', 'HIS', 'O', 'CYS', 10.97), ('ND1', 'HIS', 'C', 'CYS', 12.06), ('ND1', 'HIS', 'CA', 'CYS', 12.37), ('ND1', 'HIS', 'N', 'CYS', 13.81)], [('CD2', 'HIS', 'CB', 'CYS', 13.51), ('CD2', 'HIS', 'SG', 'CYS', 14.63), ('CD2', 'HIS', 'O', 'CYS', 12.3), ('CD2', 'HIS', 'C', 'CYS', 13.46), ('CD2', 'HIS', 'CA', 'CYS', 13.97), ('CD2', 'HIS', 'N', 'CYS', 15.43)], [('CE1', 'HIS', 'CB', 'CYS', 12.46), ('CE1', 'HIS', 'SG', 'CYS', 13.8), ('CE1', 'HIS', 'O', 'CYS', 11.38), ('CE1', 'HIS', 'C', 'CYS', 12.51), ('CE1', 'HIS', 'CA', 'CYS', 12.85), ('CE1', 'HIS', 'N', 'CYS', 14.29)], [('NE2', 'HIS', 'CB', 'CYS', 13.46), ('NE2', 'HIS', 'SG', 'CYS', 14.74), ('NE2', 'HIS', 'O', 'CYS', 12.17), ('NE2', 'HIS', 'C', 'CYS', 13.34), ('NE2', 'HIS', 'CA', 'CYS', 13.81), ('NE2', 'HIS', 'N', 'CYS', 15.26)]]}
TRP_GLN = { 
	'distances':
		[[15.02, 15.42, 16.38, 17.39, 16.18], [13.56, 13.92, 14.88, 15.9, 14.67], [12.66, 13.11, 14.0, 14.98, 13.81], [12.98, 13.2, 14.19, 15.27, 13.95], [11.44, 11.81, 12.7, 13.71, 12.5], [11.63, 11.84, 12.8, 13.88, 12.57], [13.61, 13.71, 14.74, 15.86, 14.48], [10.9, 10.95, 11.93, 13.05, 11.65], [13.0, 12.95, 13.99, 15.15, 13.7], [11.67, 11.58, 12.6, 13.76, 12.3]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'GLN', 15.02), ('CB', 'TRP', 'CG', 'GLN', 15.42), ('CB', 'TRP', 'CD', 'GLN', 16.38), ('CB', 'TRP', 'OE1', 'GLN', 17.39), ('CB', 'TRP', 'NE2', 'GLN', 16.18)], [('CG', 'TRP', 'CB', 'GLN', 13.56), ('CG', 'TRP', 'CG', 'GLN', 13.92), ('CG', 'TRP', 'CD', 'GLN', 14.88), ('CG', 'TRP', 'OE1', 'GLN', 15.9), ('CG', 'TRP', 'NE2', 'GLN', 14.67)], [('CD1', 'TRP', 'CB', 'GLN', 12.66), ('CD1', 'TRP', 'CG', 'GLN', 13.11), ('CD1', 'TRP', 'CD', 'GLN', 14.0), ('CD1', 'TRP', 'OE1', 'GLN', 14.98), ('CD1', 'TRP', 'NE2', 'GLN', 13.81)], [('CD2', 'TRP', 'CB', 'GLN', 12.98), ('CD2', 'TRP', 'CG', 'GLN', 13.2), ('CD2', 'TRP', 'CD', 'GLN', 14.19), ('CD2', 'TRP', 'OE1', 'GLN', 15.27), ('CD2', 'TRP', 'NE2', 'GLN', 13.95)], [('NE1', 'TRP', 'CB', 'GLN', 11.44), ('NE1', 'TRP', 'CG', 'GLN', 11.81), ('NE1', 'TRP', 'CD', 'GLN', 12.7), ('NE1', 'TRP', 'OE1', 'GLN', 13.71), ('NE1', 'TRP', 'NE2', 'GLN', 12.5)], [('CE2', 'TRP', 'CB', 'GLN', 11.63), ('CE2', 'TRP', 'CG', 'GLN', 11.84), ('CE2', 'TRP', 'CD', 'GLN', 12.8), ('CE2', 'TRP', 'OE1', 'GLN', 13.88), ('CE2', 'TRP', 'NE2', 'GLN', 12.57)], [('CE3', 'TRP', 'CB', 'GLN', 13.61), ('CE3', 'TRP', 'CG', 'GLN', 13.71), ('CE3', 'TRP', 'CD', 'GLN', 14.74), ('CE3', 'TRP', 'OE1', 'GLN', 15.86), ('CE3', 'TRP', 'NE2', 'GLN', 14.48)], [('CZ2', 'TRP', 'CB', 'GLN', 10.9), ('CZ2', 'TRP', 'CG', 'GLN', 10.95), ('CZ2', 'TRP', 'CD', 'GLN', 11.93), ('CZ2', 'TRP', 'OE1', 'GLN', 13.05), ('CZ2', 'TRP', 'NE2', 'GLN', 11.65)], [('CZ3', 'TRP', 'CB', 'GLN', 13.0), ('CZ3', 'TRP', 'CG', 'GLN', 12.95), ('CZ3', 'TRP', 'CD', 'GLN', 13.99), ('CZ3', 'TRP', 'OE1', 'GLN', 15.15), ('CZ3', 'TRP', 'NE2', 'GLN', 13.7)], [('CH2', 'TRP', 'CB', 'GLN', 11.67), ('CH2', 'TRP', 'CG', 'GLN', 11.58), ('CH2', 'TRP', 'CD', 'GLN', 12.6), ('CH2', 'TRP', 'OE1', 'GLN', 13.76), ('CH2', 'TRP', 'NE2', 'GLN', 12.3)]]}
ASN_CYS = { 
	'distances':
		[[18.07, 19.36, 16.33, 17.55, 18.22, 19.64], [16.99, 18.35, 15.34, 16.55, 17.13, 18.55], [15.86, 17.19, 14.29, 15.49, 16.06, 17.49], [17.39, 18.84, 15.77, 16.96, 17.47, 18.87]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'CYS', 18.07), ('CB', 'ASN', 'SG', 'CYS', 19.36), ('CB', 'ASN', 'O', 'CYS', 16.33), ('CB', 'ASN', 'C', 'CYS', 17.55), ('CB', 'ASN', 'CA', 'CYS', 18.22), ('CB', 'ASN', 'N', 'CYS', 19.64)], [('CG', 'ASN', 'CB', 'CYS', 16.99), ('CG', 'ASN', 'SG', 'CYS', 18.35), ('CG', 'ASN', 'O', 'CYS', 15.34), ('CG', 'ASN', 'C', 'CYS', 16.55), ('CG', 'ASN', 'CA', 'CYS', 17.13), ('CG', 'ASN', 'N', 'CYS', 18.55)], [('OD1', 'ASN', 'CB', 'CYS', 15.86), ('OD1', 'ASN', 'SG', 'CYS', 17.19), ('OD1', 'ASN', 'O', 'CYS', 14.29), ('OD1', 'ASN', 'C', 'CYS', 15.49), ('OD1', 'ASN', 'CA', 'CYS', 16.06), ('OD1', 'ASN', 'N', 'CYS', 17.49)], [('ND2', 'ASN', 'CB', 'CYS', 17.39), ('ND2', 'ASN', 'SG', 'CYS', 18.84), ('ND2', 'ASN', 'O', 'CYS', 15.77), ('ND2', 'ASN', 'C', 'CYS', 16.96), ('ND2', 'ASN', 'CA', 'CYS', 17.47), ('ND2', 'ASN', 'N', 'CYS', 18.87)]]}
CYS_GLN = { 
	'distances':
		[[7.5, 7.02, 8.28, 8.92, 8.9], [8.92, 8.4, 9.5, 9.96, 10.17], [8.56, 7.74, 8.83, 9.82, 8.89], [8.25, 7.3, 8.28, 9.18, 8.43], [7.08, 6.24, 7.32, 8.09, 7.74], [7.24, 6.22, 7.0, 7.56, 7.47]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLN', 7.5), ('CB', 'CYS', 'CG', 'GLN', 7.02), ('CB', 'CYS', 'CD', 'GLN', 8.28), ('CB', 'CYS', 'OE1', 'GLN', 8.92), ('CB', 'CYS', 'NE2', 'GLN', 8.9)], [('SG', 'CYS', 'CB', 'GLN', 8.92), ('SG', 'CYS', 'CG', 'GLN', 8.4), ('SG', 'CYS', 'CD', 'GLN', 9.5), ('SG', 'CYS', 'OE1', 'GLN', 9.96), ('SG', 'CYS', 'NE2', 'GLN', 10.17)], [('O', 'CYS', 'CB', 'GLN', 8.56), ('O', 'CYS', 'CG', 'GLN', 7.74), ('O', 'CYS', 'CD', 'GLN', 8.83), ('O', 'CYS', 'OE1', 'GLN', 9.82), ('O', 'CYS', 'NE2', 'GLN', 8.89)], [('C', 'CYS', 'CB', 'GLN', 8.25), ('C', 'CYS', 'CG', 'GLN', 7.3), ('C', 'CYS', 'CD', 'GLN', 8.28), ('C', 'CYS', 'OE1', 'GLN', 9.18), ('C', 'CYS', 'NE2', 'GLN', 8.43)], [('CA', 'CYS', 'CB', 'GLN', 7.08), ('CA', 'CYS', 'CG', 'GLN', 6.24), ('CA', 'CYS', 'CD', 'GLN', 7.32), ('CA', 'CYS', 'OE1', 'GLN', 8.09), ('CA', 'CYS', 'NE2', 'GLN', 7.74)], [('N', 'CYS', 'CB', 'GLN', 7.24), ('N', 'CYS', 'CG', 'GLN', 6.22), ('N', 'CYS', 'CD', 'GLN', 7.0), ('N', 'CYS', 'OE1', 'GLN', 7.56), ('N', 'CYS', 'NE2', 'GLN', 7.47)]]}
TRP_CYS = { 
	'distances':
		[[15.67, 17.29, 14.26, 15.36, 15.66, 16.99], [14.32, 15.98, 12.91, 13.98, 14.25, 15.56], [13.98, 15.7, 12.75, 13.73, 13.86, 15.11], [13.29, 14.92, 11.69, 12.8, 13.18, 14.51], [12.75, 14.5, 11.48, 12.44, 12.57, 13.8], [12.26, 13.95, 10.73, 11.77, 12.07, 13.36], [13.29, 14.82, 11.48, 12.65, 13.2, 14.57], [11.14, 12.81, 9.41, 10.47, 10.87, 12.16], [12.26, 13.75, 10.27, 11.46, 12.12, 13.48], [11.16, 12.72, 9.17, 10.32, 10.92, 12.25]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'CYS', 15.67), ('CB', 'TRP', 'SG', 'CYS', 17.29), ('CB', 'TRP', 'O', 'CYS', 14.26), ('CB', 'TRP', 'C', 'CYS', 15.36), ('CB', 'TRP', 'CA', 'CYS', 15.66), ('CB', 'TRP', 'N', 'CYS', 16.99)], [('CG', 'TRP', 'CB', 'CYS', 14.32), ('CG', 'TRP', 'SG', 'CYS', 15.98), ('CG', 'TRP', 'O', 'CYS', 12.91), ('CG', 'TRP', 'C', 'CYS', 13.98), ('CG', 'TRP', 'CA', 'CYS', 14.25), ('CG', 'TRP', 'N', 'CYS', 15.56)], [('CD1', 'TRP', 'CB', 'CYS', 13.98), ('CD1', 'TRP', 'SG', 'CYS', 15.7), ('CD1', 'TRP', 'O', 'CYS', 12.75), ('CD1', 'TRP', 'C', 'CYS', 13.73), ('CD1', 'TRP', 'CA', 'CYS', 13.86), ('CD1', 'TRP', 'N', 'CYS', 15.11)], [('CD2', 'TRP', 'CB', 'CYS', 13.29), ('CD2', 'TRP', 'SG', 'CYS', 14.92), ('CD2', 'TRP', 'O', 'CYS', 11.69), ('CD2', 'TRP', 'C', 'CYS', 12.8), ('CD2', 'TRP', 'CA', 'CYS', 13.18), ('CD2', 'TRP', 'N', 'CYS', 14.51)], [('NE1', 'TRP', 'CB', 'CYS', 12.75), ('NE1', 'TRP', 'SG', 'CYS', 14.5), ('NE1', 'TRP', 'O', 'CYS', 11.48), ('NE1', 'TRP', 'C', 'CYS', 12.44), ('NE1', 'TRP', 'CA', 'CYS', 12.57), ('NE1', 'TRP', 'N', 'CYS', 13.8)], [('CE2', 'TRP', 'CB', 'CYS', 12.26), ('CE2', 'TRP', 'SG', 'CYS', 13.95), ('CE2', 'TRP', 'O', 'CYS', 10.73), ('CE2', 'TRP', 'C', 'CYS', 11.77), ('CE2', 'TRP', 'CA', 'CYS', 12.07), ('CE2', 'TRP', 'N', 'CYS', 13.36)], [('CE3', 'TRP', 'CB', 'CYS', 13.29), ('CE3', 'TRP', 'SG', 'CYS', 14.82), ('CE3', 'TRP', 'O', 'CYS', 11.48), ('CE3', 'TRP', 'C', 'CYS', 12.65), ('CE3', 'TRP', 'CA', 'CYS', 13.2), ('CE3', 'TRP', 'N', 'CYS', 14.57)], [('CZ2', 'TRP', 'CB', 'CYS', 11.14), ('CZ2', 'TRP', 'SG', 'CYS', 12.81), ('CZ2', 'TRP', 'O', 'CYS', 9.41), ('CZ2', 'TRP', 'C', 'CYS', 10.47), ('CZ2', 'TRP', 'CA', 'CYS', 10.87), ('CZ2', 'TRP', 'N', 'CYS', 12.16)], [('CZ3', 'TRP', 'CB', 'CYS', 12.26), ('CZ3', 'TRP', 'SG', 'CYS', 13.75), ('CZ3', 'TRP', 'O', 'CYS', 10.27), ('CZ3', 'TRP', 'C', 'CYS', 11.46), ('CZ3', 'TRP', 'CA', 'CYS', 12.12), ('CZ3', 'TRP', 'N', 'CYS', 13.48)], [('CH2', 'TRP', 'CB', 'CYS', 11.16), ('CH2', 'TRP', 'SG', 'CYS', 12.72), ('CH2', 'TRP', 'O', 'CYS', 9.17), ('CH2', 'TRP', 'C', 'CYS', 10.32), ('CH2', 'TRP', 'CA', 'CYS', 10.92), ('CH2', 'TRP', 'N', 'CYS', 12.25)]]}
HIS_GLN = { 
	'distances':
		[[14.84, 15.1, 16.53, 17.47, 16.79], [14.49, 14.77, 16.15, 17.13, 16.32], [13.33, 13.68, 15.05, 16.02, 15.24], [15.29, 15.53, 16.85, 17.88, 16.92], [13.51, 13.85, 15.14, 16.14, 15.22], [14.7, 14.97, 16.24, 17.28, 16.26]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLN', 14.84), ('CB', 'HIS', 'CG', 'GLN', 15.1), ('CB', 'HIS', 'CD', 'GLN', 16.53), ('CB', 'HIS', 'OE1', 'GLN', 17.47), ('CB', 'HIS', 'NE2', 'GLN', 16.79)], [('CG', 'HIS', 'CB', 'GLN', 14.49), ('CG', 'HIS', 'CG', 'GLN', 14.77), ('CG', 'HIS', 'CD', 'GLN', 16.15), ('CG', 'HIS', 'OE1', 'GLN', 17.13), ('CG', 'HIS', 'NE2', 'GLN', 16.32)], [('ND1', 'HIS', 'CB', 'GLN', 13.33), ('ND1', 'HIS', 'CG', 'GLN', 13.68), ('ND1', 'HIS', 'CD', 'GLN', 15.05), ('ND1', 'HIS', 'OE1', 'GLN', 16.02), ('ND1', 'HIS', 'NE2', 'GLN', 15.24)], [('CD2', 'HIS', 'CB', 'GLN', 15.29), ('CD2', 'HIS', 'CG', 'GLN', 15.53), ('CD2', 'HIS', 'CD', 'GLN', 16.85), ('CD2', 'HIS', 'OE1', 'GLN', 17.88), ('CD2', 'HIS', 'NE2', 'GLN', 16.92)], [('CE1', 'HIS', 'CB', 'GLN', 13.51), ('CE1', 'HIS', 'CG', 'GLN', 13.85), ('CE1', 'HIS', 'CD', 'GLN', 15.14), ('CE1', 'HIS', 'OE1', 'GLN', 16.14), ('CE1', 'HIS', 'NE2', 'GLN', 15.22)], [('NE2', 'HIS', 'CB', 'GLN', 14.7), ('NE2', 'HIS', 'CG', 'GLN', 14.97), ('NE2', 'HIS', 'CD', 'GLN', 16.24), ('NE2', 'HIS', 'OE1', 'GLN', 17.28), ('NE2', 'HIS', 'NE2', 'GLN', 16.26)]]}
ASN_HIS = { 
	'distances':
		[[9.8, 8.67, 9.08, 7.33, 8.17, 6.97], [9.12, 7.83, 8.0, 6.57, 6.96, 5.89], [7.95, 6.63, 6.81, 5.37, 5.81, 4.68], [10.06, 8.69, 8.62, 7.52, 7.45, 6.61]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'HIS', 9.8), ('CB', 'ASN', 'CG', 'HIS', 8.67), ('CB', 'ASN', 'ND1', 'HIS', 9.08), ('CB', 'ASN', 'CD2', 'HIS', 7.33), ('CB', 'ASN', 'CE1', 'HIS', 8.17), ('CB', 'ASN', 'NE2', 'HIS', 6.97)], [('CG', 'ASN', 'CB', 'HIS', 9.12), ('CG', 'ASN', 'CG', 'HIS', 7.83), ('CG', 'ASN', 'ND1', 'HIS', 8.0), ('CG', 'ASN', 'CD2', 'HIS', 6.57), ('CG', 'ASN', 'CE1', 'HIS', 6.96), ('CG', 'ASN', 'NE2', 'HIS', 5.89)], [('OD1', 'ASN', 'CB', 'HIS', 7.95), ('OD1', 'ASN', 'CG', 'HIS', 6.63), ('OD1', 'ASN', 'ND1', 'HIS', 6.81), ('OD1', 'ASN', 'CD2', 'HIS', 5.37), ('OD1', 'ASN', 'CE1', 'HIS', 5.81), ('OD1', 'ASN', 'NE2', 'HIS', 4.68)], [('ND2', 'ASN', 'CB', 'HIS', 10.06), ('ND2', 'ASN', 'CG', 'HIS', 8.69), ('ND2', 'ASN', 'ND1', 'HIS', 8.62), ('ND2', 'ASN', 'CD2', 'HIS', 7.52), ('ND2', 'ASN', 'CE1', 'HIS', 7.45), ('ND2', 'ASN', 'NE2', 'HIS', 6.61)]]}
TRP_HIS = { 
	'distances':
		[[10.29, 8.81, 8.1, 8.09, 6.81, 6.76], [10.02, 8.57, 7.66, 8.06, 6.42, 6.69], [10.74, 9.35, 8.27, 9.05, 7.16, 7.7], [9.31, 7.89, 7.01, 7.43, 5.83, 6.12], [10.59, 9.28, 8.12, 9.13, 7.15, 7.85], [9.73, 8.42, 7.37, 8.22, 6.39, 6.99], [8.65, 7.25, 6.64, 6.62, 5.48, 5.44], [9.58, 8.41, 7.41, 8.35, 6.66, 7.3], [8.45, 7.22, 6.66, 6.77, 5.79, 5.85], [8.95, 7.83, 7.05, 7.67, 6.37, 6.78]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'HIS', 10.29), ('CB', 'TRP', 'CG', 'HIS', 8.81), ('CB', 'TRP', 'ND1', 'HIS', 8.1), ('CB', 'TRP', 'CD2', 'HIS', 8.09), ('CB', 'TRP', 'CE1', 'HIS', 6.81), ('CB', 'TRP', 'NE2', 'HIS', 6.76)], [('CG', 'TRP', 'CB', 'HIS', 10.02), ('CG', 'TRP', 'CG', 'HIS', 8.57), ('CG', 'TRP', 'ND1', 'HIS', 7.66), ('CG', 'TRP', 'CD2', 'HIS', 8.06), ('CG', 'TRP', 'CE1', 'HIS', 6.42), ('CG', 'TRP', 'NE2', 'HIS', 6.69)], [('CD1', 'TRP', 'CB', 'HIS', 10.74), ('CD1', 'TRP', 'CG', 'HIS', 9.35), ('CD1', 'TRP', 'ND1', 'HIS', 8.27), ('CD1', 'TRP', 'CD2', 'HIS', 9.05), ('CD1', 'TRP', 'CE1', 'HIS', 7.16), ('CD1', 'TRP', 'NE2', 'HIS', 7.7)], [('CD2', 'TRP', 'CB', 'HIS', 9.31), ('CD2', 'TRP', 'CG', 'HIS', 7.89), ('CD2', 'TRP', 'ND1', 'HIS', 7.01), ('CD2', 'TRP', 'CD2', 'HIS', 7.43), ('CD2', 'TRP', 'CE1', 'HIS', 5.83), ('CD2', 'TRP', 'NE2', 'HIS', 6.12)], [('NE1', 'TRP', 'CB', 'HIS', 10.59), ('NE1', 'TRP', 'CG', 'HIS', 9.28), ('NE1', 'TRP', 'ND1', 'HIS', 8.12), ('NE1', 'TRP', 'CD2', 'HIS', 9.13), ('NE1', 'TRP', 'CE1', 'HIS', 7.15), ('NE1', 'TRP', 'NE2', 'HIS', 7.85)], [('CE2', 'TRP', 'CB', 'HIS', 9.73), ('CE2', 'TRP', 'CG', 'HIS', 8.42), ('CE2', 'TRP', 'ND1', 'HIS', 7.37), ('CE2', 'TRP', 'CD2', 'HIS', 8.22), ('CE2', 'TRP', 'CE1', 'HIS', 6.39), ('CE2', 'TRP', 'NE2', 'HIS', 6.99)], [('CE3', 'TRP', 'CB', 'HIS', 8.65), ('CE3', 'TRP', 'CG', 'HIS', 7.25), ('CE3', 'TRP', 'ND1', 'HIS', 6.64), ('CE3', 'TRP', 'CD2', 'HIS', 6.62), ('CE3', 'TRP', 'CE1', 'HIS', 5.48), ('CE3', 'TRP', 'NE2', 'HIS', 5.44)], [('CZ2', 'TRP', 'CB', 'HIS', 9.58), ('CZ2', 'TRP', 'CG', 'HIS', 8.41), ('CZ2', 'TRP', 'ND1', 'HIS', 7.41), ('CZ2', 'TRP', 'CD2', 'HIS', 8.35), ('CZ2', 'TRP', 'CE1', 'HIS', 6.66), ('CZ2', 'TRP', 'NE2', 'HIS', 7.3)], [('CZ3', 'TRP', 'CB', 'HIS', 8.45), ('CZ3', 'TRP', 'CG', 'HIS', 7.22), ('CZ3', 'TRP', 'ND1', 'HIS', 6.66), ('CZ3', 'TRP', 'CD2', 'HIS', 6.77), ('CZ3', 'TRP', 'CE1', 'HIS', 5.79), ('CZ3', 'TRP', 'NE2', 'HIS', 5.85)], [('CH2', 'TRP', 'CB', 'HIS', 8.95), ('CH2', 'TRP', 'CG', 'HIS', 7.83), ('CH2', 'TRP', 'ND1', 'HIS', 7.05), ('CH2', 'TRP', 'CD2', 'HIS', 7.67), ('CH2', 'TRP', 'CE1', 'HIS', 6.37), ('CH2', 'TRP', 'NE2', 'HIS', 6.78)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASN_GLN, d, 'A_1kfx_3_4_22_53')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TRP_ASN, d, 'A_1kfx_3_4_22_53')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_CYS, d, 'A_1kfx_3_4_22_53')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(TRP_GLN, d, 'A_1kfx_3_4_22_53')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASN_CYS, d, 'A_1kfx_3_4_22_53')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(CYS_GLN, d, 'A_1kfx_3_4_22_53')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(TRP_CYS, d, 'A_1kfx_3_4_22_53')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(HIS_GLN, d, 'A_1kfx_3_4_22_53')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(ASN_HIS, d, 'A_1kfx_3_4_22_53')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(TRP_HIS, d, 'A_1kfx_3_4_22_53')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASN_GLN' :  match1,
		'TRP_ASN' :  match2,
		'HIS_CYS' :  match3,
		'TRP_GLN' :  match4,
		'ASN_CYS' :  match5,
		'CYS_GLN' :  match6,
		'TRP_CYS' :  match7,
		'HIS_GLN' :  match8,
		'ASN_HIS' :  match9,
		'TRP_HIS' :  match10}