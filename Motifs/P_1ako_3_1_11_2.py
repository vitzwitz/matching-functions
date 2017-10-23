'''
FUNC:P_1ako_3_1_11_2
PDB:1ako
EC:3.1.11.2
RESI:asn,asp,asn,asp,his
LOCI:a-7,151,153,229,259;
'''
import motifFunctions as cmd
ASP_HIS = { 
	'distances':
		[[8.23, 7.29, 6.35, 7.46, 5.93, 6.66], [7.87, 6.71, 5.67, 6.71, 4.94, 5.68], [8.29, 7.12, 5.91, 7.21, 5.17, 6.09], [7.53, 6.24, 5.42, 5.96, 4.48, 4.87], [7.2, 7.16, 6.17, 8.27, 6.9, 8.11], [6.01, 5.75, 4.7, 6.81, 5.41, 6.61], [6.06, 5.65, 4.64, 6.53, 5.15, 6.25], [5.4, 5.1, 4.03, 6.19, 4.82, 6.03]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 8.23), ('CB', 'ASP', 'CG', 'HIS', 7.29), ('CB', 'ASP', 'ND1', 'HIS', 6.35), ('CB', 'ASP', 'CD2', 'HIS', 7.46), ('CB', 'ASP', 'CE1', 'HIS', 5.93), ('CB', 'ASP', 'NE2', 'HIS', 6.66)], [('CG', 'ASP', 'CB', 'HIS', 7.87), ('CG', 'ASP', 'CG', 'HIS', 6.71), ('CG', 'ASP', 'ND1', 'HIS', 5.67), ('CG', 'ASP', 'CD2', 'HIS', 6.71), ('CG', 'ASP', 'CE1', 'HIS', 4.94), ('CG', 'ASP', 'NE2', 'HIS', 5.68)], [('OD1', 'ASP', 'CB', 'HIS', 8.29), ('OD1', 'ASP', 'CG', 'HIS', 7.12), ('OD1', 'ASP', 'ND1', 'HIS', 5.91), ('OD1', 'ASP', 'CD2', 'HIS', 7.21), ('OD1', 'ASP', 'CE1', 'HIS', 5.17), ('OD1', 'ASP', 'NE2', 'HIS', 6.09)], [('OD2', 'ASP', 'CB', 'HIS', 7.53), ('OD2', 'ASP', 'CG', 'HIS', 6.24), ('OD2', 'ASP', 'ND1', 'HIS', 5.42), ('OD2', 'ASP', 'CD2', 'HIS', 5.96), ('OD2', 'ASP', 'CE1', 'HIS', 4.48), ('OD2', 'ASP', 'NE2', 'HIS', 4.87)], [('CB', 'ASP', 'CB', 'HIS', 7.2), ('CB', 'ASP', 'CG', 'HIS', 7.16), ('CB', 'ASP', 'ND1', 'HIS', 6.17), ('CB', 'ASP', 'CD2', 'HIS', 8.27), ('CB', 'ASP', 'CE1', 'HIS', 6.9), ('CB', 'ASP', 'NE2', 'HIS', 8.11)], [('CG', 'ASP', 'CB', 'HIS', 6.01), ('CG', 'ASP', 'CG', 'HIS', 5.75), ('CG', 'ASP', 'ND1', 'HIS', 4.7), ('CG', 'ASP', 'CD2', 'HIS', 6.81), ('CG', 'ASP', 'CE1', 'HIS', 5.41), ('CG', 'ASP', 'NE2', 'HIS', 6.61)], [('OD1', 'ASP', 'CB', 'HIS', 6.06), ('OD1', 'ASP', 'CG', 'HIS', 5.65), ('OD1', 'ASP', 'ND1', 'HIS', 4.64), ('OD1', 'ASP', 'CD2', 'HIS', 6.53), ('OD1', 'ASP', 'CE1', 'HIS', 5.15), ('OD1', 'ASP', 'NE2', 'HIS', 6.25)], [('OD2', 'ASP', 'CB', 'HIS', 5.4), ('OD2', 'ASP', 'CG', 'HIS', 5.1), ('OD2', 'ASP', 'ND1', 'HIS', 4.03), ('OD2', 'ASP', 'CD2', 'HIS', 6.19), ('OD2', 'ASP', 'CE1', 'HIS', 4.82), ('OD2', 'ASP', 'NE2', 'HIS', 6.03)]]}
HIS_ASPI = { 
	'distances':
		[[7.2, 6.01, 6.06, 5.4], [7.16, 5.75, 5.65, 5.1], [6.17, 4.7, 4.64, 4.03], [8.27, 6.81, 6.53, 6.19], [6.9, 5.41, 5.15, 4.82], [8.11, 6.61, 6.25, 6.03]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASPI', 7.2), ('CB', 'HIS', 'CG', 'ASPI', 6.01), ('CB', 'HIS', 'OD1', 'ASPI', 6.06), ('CB', 'HIS', 'OD2', 'ASPI', 5.4)], [('CG', 'HIS', 'CB', 'ASPI', 7.16), ('CG', 'HIS', 'CG', 'ASPI', 5.75), ('CG', 'HIS', 'OD1', 'ASPI', 5.65), ('CG', 'HIS', 'OD2', 'ASPI', 5.1)], [('ND1', 'HIS', 'CB', 'ASPI', 6.17), ('ND1', 'HIS', 'CG', 'ASPI', 4.7), ('ND1', 'HIS', 'OD1', 'ASPI', 4.64), ('ND1', 'HIS', 'OD2', 'ASPI', 4.03)], [('CD2', 'HIS', 'CB', 'ASPI', 8.27), ('CD2', 'HIS', 'CG', 'ASPI', 6.81), ('CD2', 'HIS', 'OD1', 'ASPI', 6.53), ('CD2', 'HIS', 'OD2', 'ASPI', 6.19)], [('CE1', 'HIS', 'CB', 'ASPI', 6.9), ('CE1', 'HIS', 'CG', 'ASPI', 5.41), ('CE1', 'HIS', 'OD1', 'ASPI', 5.15), ('CE1', 'HIS', 'OD2', 'ASPI', 4.82)], [('NE2', 'HIS', 'CB', 'ASPI', 8.11), ('NE2', 'HIS', 'CG', 'ASPI', 6.61), ('NE2', 'HIS', 'OD1', 'ASPI', 6.25), ('NE2', 'HIS', 'OD2', 'ASPI', 6.03)]]}
ASP_ASNI = { 
	'distances':
		[[10.3, 10.06, 9.89, 10.29], [9.58, 9.12, 8.86, 9.3], [9.16, 8.61, 8.48, 8.6], [9.65, 9.1, 8.65, 9.4]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASNI', 10.3), ('CB', 'ASP', 'CG', 'ASNI', 10.06), ('CB', 'ASP', 'OD1', 'ASNI', 9.89), ('CB', 'ASP', 'ND2', 'ASNI', 10.29)], [('CG', 'ASP', 'CB', 'ASNI', 9.58), ('CG', 'ASP', 'CG', 'ASNI', 9.12), ('CG', 'ASP', 'OD1', 'ASNI', 8.86), ('CG', 'ASP', 'ND2', 'ASNI', 9.3)], [('OD1', 'ASP', 'CB', 'ASNI', 9.16), ('OD1', 'ASP', 'CG', 'ASNI', 8.61), ('OD1', 'ASP', 'OD1', 'ASNI', 8.48), ('OD1', 'ASP', 'ND2', 'ASNI', 8.6)], [('OD2', 'ASP', 'CB', 'ASNI', 9.65), ('OD2', 'ASP', 'CG', 'ASNI', 9.1), ('OD2', 'ASP', 'OD1', 'ASNI', 8.65), ('OD2', 'ASP', 'ND2', 'ASNI', 9.4)]]}
ASN_ASP = { 
	'distances':
		[[5.82, 6.04, 7.05, 5.59], [6.13, 6.1, 7.19, 5.3], [7.34, 7.27, 8.35, 6.38], [5.36, 5.14, 6.26, 4.2], [7.62, 6.4, 5.49, 6.64], [8.83, 7.5, 6.58, 7.61], [9.91, 8.58, 7.72, 8.6], [8.86, 7.5, 6.51, 7.62], [7.11, 6.16, 5.39, 6.54], [6.51, 5.35, 4.79, 5.42], [6.85, 5.48, 4.86, 5.39], [6.02, 5.03, 4.88, 4.95], [10.3, 9.58, 9.16, 9.65], [10.06, 9.12, 8.61, 9.1], [9.89, 8.86, 8.48, 8.65], [10.29, 9.3, 8.6, 9.4]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ASP', 5.82), ('CB', 'ASN', 'CG', 'ASP', 6.04), ('CB', 'ASN', 'OD1', 'ASP', 7.05), ('CB', 'ASN', 'OD2', 'ASP', 5.59)], [('CG', 'ASN', 'CB', 'ASP', 6.13), ('CG', 'ASN', 'CG', 'ASP', 6.1), ('CG', 'ASN', 'OD1', 'ASP', 7.19), ('CG', 'ASN', 'OD2', 'ASP', 5.3)], [('OD1', 'ASN', 'CB', 'ASP', 7.34), ('OD1', 'ASN', 'CG', 'ASP', 7.27), ('OD1', 'ASN', 'OD1', 'ASP', 8.35), ('OD1', 'ASN', 'OD2', 'ASP', 6.38)], [('ND2', 'ASN', 'CB', 'ASP', 5.36), ('ND2', 'ASN', 'CG', 'ASP', 5.14), ('ND2', 'ASN', 'OD1', 'ASP', 6.26), ('ND2', 'ASN', 'OD2', 'ASP', 4.2)], [('CB', 'ASN', 'CB', 'ASP', 7.62), ('CB', 'ASN', 'CG', 'ASP', 6.4), ('CB', 'ASN', 'OD1', 'ASP', 5.49), ('CB', 'ASN', 'OD2', 'ASP', 6.64)], [('CG', 'ASN', 'CB', 'ASP', 8.83), ('CG', 'ASN', 'CG', 'ASP', 7.5), ('CG', 'ASN', 'OD1', 'ASP', 6.58), ('CG', 'ASN', 'OD2', 'ASP', 7.61)], [('OD1', 'ASN', 'CB', 'ASP', 9.91), ('OD1', 'ASN', 'CG', 'ASP', 8.58), ('OD1', 'ASN', 'OD1', 'ASP', 7.72), ('OD1', 'ASN', 'OD2', 'ASP', 8.6)], [('ND2', 'ASN', 'CB', 'ASP', 8.86), ('ND2', 'ASN', 'CG', 'ASP', 7.5), ('ND2', 'ASN', 'OD1', 'ASP', 6.51), ('ND2', 'ASN', 'OD2', 'ASP', 7.62)], [('CB', 'ASN', 'CB', 'ASP', 7.11), ('CB', 'ASN', 'CG', 'ASP', 6.16), ('CB', 'ASN', 'OD1', 'ASP', 5.39), ('CB', 'ASN', 'OD2', 'ASP', 6.54)], [('CG', 'ASN', 'CB', 'ASP', 6.51), ('CG', 'ASN', 'CG', 'ASP', 5.35), ('CG', 'ASN', 'OD1', 'ASP', 4.79), ('CG', 'ASN', 'OD2', 'ASP', 5.42)], [('OD1', 'ASN', 'CB', 'ASP', 6.85), ('OD1', 'ASN', 'CG', 'ASP', 5.48), ('OD1', 'ASN', 'OD1', 'ASP', 4.86), ('OD1', 'ASN', 'OD2', 'ASP', 5.39)], [('ND2', 'ASN', 'CB', 'ASP', 6.02), ('ND2', 'ASN', 'CG', 'ASP', 5.03), ('ND2', 'ASN', 'OD1', 'ASP', 4.88), ('ND2', 'ASN', 'OD2', 'ASP', 4.95)], [('CB', 'ASN', 'CB', 'ASP', 10.3), ('CB', 'ASN', 'CG', 'ASP', 9.58), ('CB', 'ASN', 'OD1', 'ASP', 9.16), ('CB', 'ASN', 'OD2', 'ASP', 9.65)], [('CG', 'ASN', 'CB', 'ASP', 10.06), ('CG', 'ASN', 'CG', 'ASP', 9.12), ('CG', 'ASN', 'OD1', 'ASP', 8.61), ('CG', 'ASN', 'OD2', 'ASP', 9.1)], [('OD1', 'ASN', 'CB', 'ASP', 9.89), ('OD1', 'ASN', 'CG', 'ASP', 8.86), ('OD1', 'ASN', 'OD1', 'ASP', 8.48), ('OD1', 'ASN', 'OD2', 'ASP', 8.65)], [('ND2', 'ASN', 'CB', 'ASP', 10.29), ('ND2', 'ASN', 'CG', 'ASP', 9.3), ('ND2', 'ASN', 'OD1', 'ASP', 8.6), ('ND2', 'ASN', 'OD2', 'ASP', 9.4)]]}
ASN_HIS = { 
	'distances':
		[[5.19, 4.81, 5.06, 4.95, 5.32, 5.26], [5.92, 5.23, 5.57, 4.82, 5.41, 4.95], [6.28, 5.75, 6.37, 5.16, 6.26, 5.53], [6.63, 5.63, 5.63, 5.07, 5.11, 4.71], [12.05, 10.7, 9.56, 10.46, 8.52, 9.11], [11.01, 9.6, 8.56, 9.21, 7.42, 7.85], [10.38, 8.95, 7.95, 8.52, 6.76, 7.15], [10.98, 9.58, 8.65, 9.11, 7.49, 7.79]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'HIS', 5.19), ('CB', 'ASN', 'CG', 'HIS', 4.81), ('CB', 'ASN', 'ND1', 'HIS', 5.06), ('CB', 'ASN', 'CD2', 'HIS', 4.95), ('CB', 'ASN', 'CE1', 'HIS', 5.32), ('CB', 'ASN', 'NE2', 'HIS', 5.26)], [('CG', 'ASN', 'CB', 'HIS', 5.92), ('CG', 'ASN', 'CG', 'HIS', 5.23), ('CG', 'ASN', 'ND1', 'HIS', 5.57), ('CG', 'ASN', 'CD2', 'HIS', 4.82), ('CG', 'ASN', 'CE1', 'HIS', 5.41), ('CG', 'ASN', 'NE2', 'HIS', 4.95)], [('OD1', 'ASN', 'CB', 'HIS', 6.28), ('OD1', 'ASN', 'CG', 'HIS', 5.75), ('OD1', 'ASN', 'ND1', 'HIS', 6.37), ('OD1', 'ASN', 'CD2', 'HIS', 5.16), ('OD1', 'ASN', 'CE1', 'HIS', 6.26), ('OD1', 'ASN', 'NE2', 'HIS', 5.53)], [('ND2', 'ASN', 'CB', 'HIS', 6.63), ('ND2', 'ASN', 'CG', 'HIS', 5.63), ('ND2', 'ASN', 'ND1', 'HIS', 5.63), ('ND2', 'ASN', 'CD2', 'HIS', 5.07), ('ND2', 'ASN', 'CE1', 'HIS', 5.11), ('ND2', 'ASN', 'NE2', 'HIS', 4.71)], [('CB', 'ASN', 'CB', 'HIS', 12.05), ('CB', 'ASN', 'CG', 'HIS', 10.7), ('CB', 'ASN', 'ND1', 'HIS', 9.56), ('CB', 'ASN', 'CD2', 'HIS', 10.46), ('CB', 'ASN', 'CE1', 'HIS', 8.52), ('CB', 'ASN', 'NE2', 'HIS', 9.11)], [('CG', 'ASN', 'CB', 'HIS', 11.01), ('CG', 'ASN', 'CG', 'HIS', 9.6), ('CG', 'ASN', 'ND1', 'HIS', 8.56), ('CG', 'ASN', 'CD2', 'HIS', 9.21), ('CG', 'ASN', 'CE1', 'HIS', 7.42), ('CG', 'ASN', 'NE2', 'HIS', 7.85)], [('OD1', 'ASN', 'CB', 'HIS', 10.38), ('OD1', 'ASN', 'CG', 'HIS', 8.95), ('OD1', 'ASN', 'ND1', 'HIS', 7.95), ('OD1', 'ASN', 'CD2', 'HIS', 8.52), ('OD1', 'ASN', 'CE1', 'HIS', 6.76), ('OD1', 'ASN', 'NE2', 'HIS', 7.15)], [('ND2', 'ASN', 'CB', 'HIS', 10.98), ('ND2', 'ASN', 'CG', 'HIS', 9.58), ('ND2', 'ASN', 'ND1', 'HIS', 8.65), ('ND2', 'ASN', 'CD2', 'HIS', 9.11), ('ND2', 'ASN', 'CE1', 'HIS', 7.49), ('ND2', 'ASN', 'NE2', 'HIS', 7.79)]]}
ASN_ASN = { 
	'distances':
		[[10.84, 9.75, 9.58, 9.23], [10.56, 9.33, 9.14, 8.68], [11.56, 10.26, 10.03, 9.58], [9.35, 8.1, 7.98, 7.39], [10.84, 10.56, 11.56, 9.35], [9.75, 9.33, 10.26, 8.1], [9.58, 9.14, 10.03, 7.98], [9.23, 8.68, 9.58, 7.39]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ASN', 10.84), ('CB', 'ASN', 'CG', 'ASN', 9.75), ('CB', 'ASN', 'OD1', 'ASN', 9.58), ('CB', 'ASN', 'ND2', 'ASN', 9.23)], [('CG', 'ASN', 'CB', 'ASN', 10.56), ('CG', 'ASN', 'CG', 'ASN', 9.33), ('CG', 'ASN', 'OD1', 'ASN', 9.14), ('CG', 'ASN', 'ND2', 'ASN', 8.68)], [('OD1', 'ASN', 'CB', 'ASN', 11.56), ('OD1', 'ASN', 'CG', 'ASN', 10.26), ('OD1', 'ASN', 'OD1', 'ASN', 10.03), ('OD1', 'ASN', 'ND2', 'ASN', 9.58)], [('ND2', 'ASN', 'CB', 'ASN', 9.35), ('ND2', 'ASN', 'CG', 'ASN', 8.1), ('ND2', 'ASN', 'OD1', 'ASN', 7.98), ('ND2', 'ASN', 'ND2', 'ASN', 7.39)], [('CB', 'ASN', 'CB', 'ASN', 10.84), ('CB', 'ASN', 'CG', 'ASN', 10.56), ('CB', 'ASN', 'OD1', 'ASN', 11.56), ('CB', 'ASN', 'ND2', 'ASN', 9.35)], [('CG', 'ASN', 'CB', 'ASN', 9.75), ('CG', 'ASN', 'CG', 'ASN', 9.33), ('CG', 'ASN', 'OD1', 'ASN', 10.26), ('CG', 'ASN', 'ND2', 'ASN', 8.1)], [('OD1', 'ASN', 'CB', 'ASN', 9.58), ('OD1', 'ASN', 'CG', 'ASN', 9.14), ('OD1', 'ASN', 'OD1', 'ASN', 10.03), ('OD1', 'ASN', 'ND2', 'ASN', 7.98)], [('ND2', 'ASN', 'CB', 'ASN', 9.23), ('ND2', 'ASN', 'CG', 'ASN', 8.68), ('ND2', 'ASN', 'OD1', 'ASN', 9.58), ('ND2', 'ASN', 'ND2', 'ASN', 7.39)]]}
HIS_ASNI = { 
	'distances':
		[[12.05, 11.01, 10.38, 10.98], [10.7, 9.6, 8.95, 9.58], [9.56, 8.56, 7.95, 8.65], [10.46, 9.21, 8.52, 9.11], [8.52, 7.42, 6.76, 7.49], [9.11, 7.85, 7.15, 7.79]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASNI', 12.05), ('CB', 'HIS', 'CG', 'ASNI', 11.01), ('CB', 'HIS', 'OD1', 'ASNI', 10.38), ('CB', 'HIS', 'ND2', 'ASNI', 10.98)], [('CG', 'HIS', 'CB', 'ASNI', 10.7), ('CG', 'HIS', 'CG', 'ASNI', 9.6), ('CG', 'HIS', 'OD1', 'ASNI', 8.95), ('CG', 'HIS', 'ND2', 'ASNI', 9.58)], [('ND1', 'HIS', 'CB', 'ASNI', 9.56), ('ND1', 'HIS', 'CG', 'ASNI', 8.56), ('ND1', 'HIS', 'OD1', 'ASNI', 7.95), ('ND1', 'HIS', 'ND2', 'ASNI', 8.65)], [('CD2', 'HIS', 'CB', 'ASNI', 10.46), ('CD2', 'HIS', 'CG', 'ASNI', 9.21), ('CD2', 'HIS', 'OD1', 'ASNI', 8.52), ('CD2', 'HIS', 'ND2', 'ASNI', 9.11)], [('CE1', 'HIS', 'CB', 'ASNI', 8.52), ('CE1', 'HIS', 'CG', 'ASNI', 7.42), ('CE1', 'HIS', 'OD1', 'ASNI', 6.76), ('CE1', 'HIS', 'ND2', 'ASNI', 7.49)], [('NE2', 'HIS', 'CB', 'ASNI', 9.11), ('NE2', 'HIS', 'CG', 'ASNI', 7.85), ('NE2', 'HIS', 'OD1', 'ASNI', 7.15), ('NE2', 'HIS', 'ND2', 'ASNI', 7.79)]]}
ASP_ASP = { 
	'distances':
		[[6.63, 5.76, 4.66, 6.44], [6.89, 5.8, 4.91, 6.13], [6.67, 5.7, 5.09, 5.93], [7.71, 6.44, 5.56, 6.58], [6.63, 6.89, 6.67, 7.71], [5.76, 5.8, 5.7, 6.44], [4.66, 4.91, 5.09, 5.56], [6.44, 6.13, 5.93, 6.58]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 6.63), ('CB', 'ASP', 'CG', 'ASP', 5.76), ('CB', 'ASP', 'OD1', 'ASP', 4.66), ('CB', 'ASP', 'OD2', 'ASP', 6.44)], [('CG', 'ASP', 'CB', 'ASP', 6.89), ('CG', 'ASP', 'CG', 'ASP', 5.8), ('CG', 'ASP', 'OD1', 'ASP', 4.91), ('CG', 'ASP', 'OD2', 'ASP', 6.13)], [('OD1', 'ASP', 'CB', 'ASP', 6.67), ('OD1', 'ASP', 'CG', 'ASP', 5.7), ('OD1', 'ASP', 'OD1', 'ASP', 5.09), ('OD1', 'ASP', 'OD2', 'ASP', 5.93)], [('OD2', 'ASP', 'CB', 'ASP', 7.71), ('OD2', 'ASP', 'CG', 'ASP', 6.44), ('OD2', 'ASP', 'OD1', 'ASP', 5.56), ('OD2', 'ASP', 'OD2', 'ASP', 6.58)], [('CB', 'ASP', 'CB', 'ASP', 6.63), ('CB', 'ASP', 'CG', 'ASP', 6.89), ('CB', 'ASP', 'OD1', 'ASP', 6.67), ('CB', 'ASP', 'OD2', 'ASP', 7.71)], [('CG', 'ASP', 'CB', 'ASP', 5.76), ('CG', 'ASP', 'CG', 'ASP', 5.8), ('CG', 'ASP', 'OD1', 'ASP', 5.7), ('CG', 'ASP', 'OD2', 'ASP', 6.44)], [('OD1', 'ASP', 'CB', 'ASP', 4.66), ('OD1', 'ASP', 'CG', 'ASP', 4.91), ('OD1', 'ASP', 'OD1', 'ASP', 5.09), ('OD1', 'ASP', 'OD2', 'ASP', 5.56)], [('OD2', 'ASP', 'CB', 'ASP', 6.44), ('OD2', 'ASP', 'CG', 'ASP', 6.13), ('OD2', 'ASP', 'OD1', 'ASP', 5.93), ('OD2', 'ASP', 'OD2', 'ASP', 6.58)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HIS, d, 'P_1ako_3_1_11_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASPI, d, 'P_1ako_3_1_11_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_ASNI, d, 'P_1ako_3_1_11_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASN_ASP, d, 'P_1ako_3_1_11_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASN_HIS, d, 'P_1ako_3_1_11_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ASN_ASN, d, 'P_1ako_3_1_11_2')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(HIS_ASNI, d, 'P_1ako_3_1_11_2')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ASP_ASP, d, 'P_1ako_3_1_11_2')
	if match8 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HIS' :  match1,
		'HIS_ASPI' :  match2,
		'ASP_ASNI' :  match3,
		'ASN_ASP' :  match4,
		'ASN_HIS' :  match5,
		'ASN_ASN' :  match6,
		'HIS_ASNI' :  match7,
		'ASP_ASP' :  match8}