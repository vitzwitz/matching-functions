'''
FUNC:A_1r4z_3_1_1_3
PDB:1r4z
EC:3.1.1.3
RESI:ile,ser,met,asp,his
LOCI:a-12,77,78,133,156;
'''
import motifFunctions as cmd
MET_SER = { 
	'distances':
		[[6.75, 6.8], [8.25, 8.21], [8.9, 8.61], [9.76, 9.22], [8.14, 8.7], [6.92, 7.55], [6.13, 6.42], [4.68, 5.1]],
	'comparisons':
		[[('CB', 'MET', 'CB', 'SER', 6.75), ('CB', 'MET', 'OG', 'SER', 6.8)], [('CG', 'MET', 'CB', 'SER', 8.25), ('CG', 'MET', 'OG', 'SER', 8.21)], [('SD', 'MET', 'CB', 'SER', 8.9), ('SD', 'MET', 'OG', 'SER', 8.61)], [('CE', 'MET', 'CB', 'SER', 9.76), ('CE', 'MET', 'OG', 'SER', 9.22)], [('O', 'MET', 'CB', 'SER', 8.14), ('O', 'MET', 'OG', 'SER', 8.7)], [('C', 'MET', 'CB', 'SER', 6.92), ('C', 'MET', 'OG', 'SER', 7.55)], [('CA', 'MET', 'CB', 'SER', 6.13), ('CA', 'MET', 'OG', 'SER', 6.42)], [('N', 'MET', 'CB', 'SER', 4.68), ('N', 'MET', 'OG', 'SER', 5.1)]]}
ILE_HIS = { 
	'distances':
		[[13.3, 12.09, 12.23, 10.89, 11.18, 10.27], [13.85, 12.56, 12.5, 11.43, 11.38, 10.64], [14.26, 13.15, 13.39, 11.94, 12.42, 11.46], [13.76, 12.51, 12.39, 11.49, 11.34, 10.71], [12.22, 11.18, 11.65, 9.85, 10.75, 9.57], [13.26, 12.15, 12.51, 10.82, 11.52, 10.41], [13.43, 12.2, 12.36, 10.92, 11.27, 10.29], [12.67, 11.35, 11.4, 10.09, 10.24, 9.33]],
	'comparisons':
		[[('CB', 'ILE', 'CB', 'HIS', 13.3), ('CB', 'ILE', 'CG', 'HIS', 12.09), ('CB', 'ILE', 'ND1', 'HIS', 12.23), ('CB', 'ILE', 'CD2', 'HIS', 10.89), ('CB', 'ILE', 'CE1', 'HIS', 11.18), ('CB', 'ILE', 'NE2', 'HIS', 10.27)], [('CG1', 'ILE', 'CB', 'HIS', 13.85), ('CG1', 'ILE', 'CG', 'HIS', 12.56), ('CG1', 'ILE', 'ND1', 'HIS', 12.5), ('CG1', 'ILE', 'CD2', 'HIS', 11.43), ('CG1', 'ILE', 'CE1', 'HIS', 11.38), ('CG1', 'ILE', 'NE2', 'HIS', 10.64)], [('CG2', 'ILE', 'CB', 'HIS', 14.26), ('CG2', 'ILE', 'CG', 'HIS', 13.15), ('CG2', 'ILE', 'ND1', 'HIS', 13.39), ('CG2', 'ILE', 'CD2', 'HIS', 11.94), ('CG2', 'ILE', 'CE1', 'HIS', 12.42), ('CG2', 'ILE', 'NE2', 'HIS', 11.46)], [('CD1', 'ILE', 'CB', 'HIS', 13.76), ('CD1', 'ILE', 'CG', 'HIS', 12.51), ('CD1', 'ILE', 'ND1', 'HIS', 12.39), ('CD1', 'ILE', 'CD2', 'HIS', 11.49), ('CD1', 'ILE', 'CE1', 'HIS', 11.34), ('CD1', 'ILE', 'NE2', 'HIS', 10.71)], [('O', 'ILE', 'CB', 'HIS', 12.22), ('O', 'ILE', 'CG', 'HIS', 11.18), ('O', 'ILE', 'ND1', 'HIS', 11.65), ('O', 'ILE', 'CD2', 'HIS', 9.85), ('O', 'ILE', 'CE1', 'HIS', 10.75), ('O', 'ILE', 'NE2', 'HIS', 9.57)], [('C', 'ILE', 'CB', 'HIS', 13.26), ('C', 'ILE', 'CG', 'HIS', 12.15), ('C', 'ILE', 'ND1', 'HIS', 12.51), ('C', 'ILE', 'CD2', 'HIS', 10.82), ('C', 'ILE', 'CE1', 'HIS', 11.52), ('C', 'ILE', 'NE2', 'HIS', 10.41)], [('CA', 'ILE', 'CB', 'HIS', 13.43), ('CA', 'ILE', 'CG', 'HIS', 12.2), ('CA', 'ILE', 'ND1', 'HIS', 12.36), ('CA', 'ILE', 'CD2', 'HIS', 10.92), ('CA', 'ILE', 'CE1', 'HIS', 11.27), ('CA', 'ILE', 'NE2', 'HIS', 10.29)], [('N', 'ILE', 'CB', 'HIS', 12.67), ('N', 'ILE', 'CG', 'HIS', 11.35), ('N', 'ILE', 'ND1', 'HIS', 11.4), ('N', 'ILE', 'CD2', 'HIS', 10.09), ('N', 'ILE', 'CE1', 'HIS', 10.24), ('N', 'ILE', 'NE2', 'HIS', 9.33)]]}
MET_ILE = { 
	'distances':
		[[6.67, 5.53, 7.99, 5.81, 8.74, 8.3, 6.87, 6.06], [7.28, 5.87, 8.36, 5.95, 9.73, 9.14, 7.63, 7.1], [8.31, 6.86, 9.26, 6.35, 10.91, 10.44, 8.97, 8.52], [7.78, 6.32, 8.41, 5.44, 10.64, 10.15, 8.74, 8.66], [9.54, 8.41, 10.84, 8.78, 11.3, 10.79, 9.39, 8.38], [8.85, 7.88, 10.25, 8.31, 10.38, 9.97, 8.65, 7.52], [7.93, 6.95, 9.34, 7.14, 9.62, 9.34, 8.01, 6.95], [7.87, 7.21, 9.36, 7.45, 9.07, 9.01, 7.87, 6.66]],
	'comparisons':
		[[('CB', 'MET', 'CB', 'ILE', 6.67), ('CB', 'MET', 'CG1', 'ILE', 5.53), ('CB', 'MET', 'CG2', 'ILE', 7.99), ('CB', 'MET', 'CD1', 'ILE', 5.81), ('CB', 'MET', 'O', 'ILE', 8.74), ('CB', 'MET', 'C', 'ILE', 8.3), ('CB', 'MET', 'CA', 'ILE', 6.87), ('CB', 'MET', 'N', 'ILE', 6.06)], [('CG', 'MET', 'CB', 'ILE', 7.28), ('CG', 'MET', 'CG1', 'ILE', 5.87), ('CG', 'MET', 'CG2', 'ILE', 8.36), ('CG', 'MET', 'CD1', 'ILE', 5.95), ('CG', 'MET', 'O', 'ILE', 9.73), ('CG', 'MET', 'C', 'ILE', 9.14), ('CG', 'MET', 'CA', 'ILE', 7.63), ('CG', 'MET', 'N', 'ILE', 7.1)], [('SD', 'MET', 'CB', 'ILE', 8.31), ('SD', 'MET', 'CG1', 'ILE', 6.86), ('SD', 'MET', 'CG2', 'ILE', 9.26), ('SD', 'MET', 'CD1', 'ILE', 6.35), ('SD', 'MET', 'O', 'ILE', 10.91), ('SD', 'MET', 'C', 'ILE', 10.44), ('SD', 'MET', 'CA', 'ILE', 8.97), ('SD', 'MET', 'N', 'ILE', 8.52)], [('CE', 'MET', 'CB', 'ILE', 7.78), ('CE', 'MET', 'CG1', 'ILE', 6.32), ('CE', 'MET', 'CG2', 'ILE', 8.41), ('CE', 'MET', 'CD1', 'ILE', 5.44), ('CE', 'MET', 'O', 'ILE', 10.64), ('CE', 'MET', 'C', 'ILE', 10.15), ('CE', 'MET', 'CA', 'ILE', 8.74), ('CE', 'MET', 'N', 'ILE', 8.66)], [('O', 'MET', 'CB', 'ILE', 9.54), ('O', 'MET', 'CG1', 'ILE', 8.41), ('O', 'MET', 'CG2', 'ILE', 10.84), ('O', 'MET', 'CD1', 'ILE', 8.78), ('O', 'MET', 'O', 'ILE', 11.3), ('O', 'MET', 'C', 'ILE', 10.79), ('O', 'MET', 'CA', 'ILE', 9.39), ('O', 'MET', 'N', 'ILE', 8.38)], [('C', 'MET', 'CB', 'ILE', 8.85), ('C', 'MET', 'CG1', 'ILE', 7.88), ('C', 'MET', 'CG2', 'ILE', 10.25), ('C', 'MET', 'CD1', 'ILE', 8.31), ('C', 'MET', 'O', 'ILE', 10.38), ('C', 'MET', 'C', 'ILE', 9.97), ('C', 'MET', 'CA', 'ILE', 8.65), ('C', 'MET', 'N', 'ILE', 7.52)], [('CA', 'MET', 'CB', 'ILE', 7.93), ('CA', 'MET', 'CG1', 'ILE', 6.95), ('CA', 'MET', 'CG2', 'ILE', 9.34), ('CA', 'MET', 'CD1', 'ILE', 7.14), ('CA', 'MET', 'O', 'ILE', 9.62), ('CA', 'MET', 'C', 'ILE', 9.34), ('CA', 'MET', 'CA', 'ILE', 8.01), ('CA', 'MET', 'N', 'ILE', 6.95)], [('N', 'MET', 'CB', 'ILE', 7.87), ('N', 'MET', 'CG1', 'ILE', 7.21), ('N', 'MET', 'CG2', 'ILE', 9.36), ('N', 'MET', 'CD1', 'ILE', 7.45), ('N', 'MET', 'O', 'ILE', 9.07), ('N', 'MET', 'C', 'ILE', 9.01), ('N', 'MET', 'CA', 'ILE', 7.87), ('N', 'MET', 'N', 'ILE', 6.66)]]}
HIS_ASP = { 
	'distances':
		[[6.74, 5.64, 5.36, 5.6], [7.27, 5.9, 5.63, 5.52], [6.81, 5.37, 5.36, 4.66], [8.57, 7.15, 6.77, 6.72], [7.94, 6.48, 6.42, 5.69], [8.9, 7.42, 7.15, 6.77]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 6.74), ('CB', 'HIS', 'CG', 'ASP', 5.64), ('CB', 'HIS', 'OD1', 'ASP', 5.36), ('CB', 'HIS', 'OD2', 'ASP', 5.6)], [('CG', 'HIS', 'CB', 'ASP', 7.27), ('CG', 'HIS', 'CG', 'ASP', 5.9), ('CG', 'HIS', 'OD1', 'ASP', 5.63), ('CG', 'HIS', 'OD2', 'ASP', 5.52)], [('ND1', 'HIS', 'CB', 'ASP', 6.81), ('ND1', 'HIS', 'CG', 'ASP', 5.37), ('ND1', 'HIS', 'OD1', 'ASP', 5.36), ('ND1', 'HIS', 'OD2', 'ASP', 4.66)], [('CD2', 'HIS', 'CB', 'ASP', 8.57), ('CD2', 'HIS', 'CG', 'ASP', 7.15), ('CD2', 'HIS', 'OD1', 'ASP', 6.77), ('CD2', 'HIS', 'OD2', 'ASP', 6.72)], [('CE1', 'HIS', 'CB', 'ASP', 7.94), ('CE1', 'HIS', 'CG', 'ASP', 6.48), ('CE1', 'HIS', 'OD1', 'ASP', 6.42), ('CE1', 'HIS', 'OD2', 'ASP', 5.69)], [('NE2', 'HIS', 'CB', 'ASP', 8.9), ('NE2', 'HIS', 'CG', 'ASP', 7.42), ('NE2', 'HIS', 'OD1', 'ASP', 7.15), ('NE2', 'HIS', 'OD2', 'ASP', 6.77)]]}
MET_HIS = { 
	'distances':
		[[13.47, 12.02, 11.52, 11.08, 10.26, 9.92], [14.87, 13.42, 12.9, 12.53, 11.65, 11.36], [15.03, 13.63, 13.0, 12.88, 11.83, 11.72], [15.45, 14.12, 13.64, 13.33, 12.54, 12.31], [15.07, 13.58, 12.83, 12.79, 11.54, 11.48], [13.9, 12.41, 11.71, 11.6, 10.4, 10.29], [12.95, 11.47, 10.81, 10.66, 9.52, 9.38], [11.55, 10.06, 9.42, 9.24, 8.12, 7.95]],
	'comparisons':
		[[('CB', 'MET', 'CB', 'HIS', 13.47), ('CB', 'MET', 'CG', 'HIS', 12.02), ('CB', 'MET', 'ND1', 'HIS', 11.52), ('CB', 'MET', 'CD2', 'HIS', 11.08), ('CB', 'MET', 'CE1', 'HIS', 10.26), ('CB', 'MET', 'NE2', 'HIS', 9.92)], [('CG', 'MET', 'CB', 'HIS', 14.87), ('CG', 'MET', 'CG', 'HIS', 13.42), ('CG', 'MET', 'ND1', 'HIS', 12.9), ('CG', 'MET', 'CD2', 'HIS', 12.53), ('CG', 'MET', 'CE1', 'HIS', 11.65), ('CG', 'MET', 'NE2', 'HIS', 11.36)], [('SD', 'MET', 'CB', 'HIS', 15.03), ('SD', 'MET', 'CG', 'HIS', 13.63), ('SD', 'MET', 'ND1', 'HIS', 13.0), ('SD', 'MET', 'CD2', 'HIS', 12.88), ('SD', 'MET', 'CE1', 'HIS', 11.83), ('SD', 'MET', 'NE2', 'HIS', 11.72)], [('CE', 'MET', 'CB', 'HIS', 15.45), ('CE', 'MET', 'CG', 'HIS', 14.12), ('CE', 'MET', 'ND1', 'HIS', 13.64), ('CE', 'MET', 'CD2', 'HIS', 13.33), ('CE', 'MET', 'CE1', 'HIS', 12.54), ('CE', 'MET', 'NE2', 'HIS', 12.31)], [('O', 'MET', 'CB', 'HIS', 15.07), ('O', 'MET', 'CG', 'HIS', 13.58), ('O', 'MET', 'ND1', 'HIS', 12.83), ('O', 'MET', 'CD2', 'HIS', 12.79), ('O', 'MET', 'CE1', 'HIS', 11.54), ('O', 'MET', 'NE2', 'HIS', 11.48)], [('C', 'MET', 'CB', 'HIS', 13.9), ('C', 'MET', 'CG', 'HIS', 12.41), ('C', 'MET', 'ND1', 'HIS', 11.71), ('C', 'MET', 'CD2', 'HIS', 11.6), ('C', 'MET', 'CE1', 'HIS', 10.4), ('C', 'MET', 'NE2', 'HIS', 10.29)], [('CA', 'MET', 'CB', 'HIS', 12.95), ('CA', 'MET', 'CG', 'HIS', 11.47), ('CA', 'MET', 'ND1', 'HIS', 10.81), ('CA', 'MET', 'CD2', 'HIS', 10.66), ('CA', 'MET', 'CE1', 'HIS', 9.52), ('CA', 'MET', 'NE2', 'HIS', 9.38)], [('N', 'MET', 'CB', 'HIS', 11.55), ('N', 'MET', 'CG', 'HIS', 10.06), ('N', 'MET', 'ND1', 'HIS', 9.42), ('N', 'MET', 'CD2', 'HIS', 9.24), ('N', 'MET', 'CE1', 'HIS', 8.12), ('N', 'MET', 'NE2', 'HIS', 7.95)]]}
MET_ASP = { 
	'distances':
		[[15.49, 14.06, 13.7, 13.41], [16.67, 15.27, 14.9, 14.66], [16.31, 14.99, 14.59, 14.47], [16.88, 15.55, 15.0, 15.16], [16.6, 15.28, 15.18, 14.43], [15.63, 14.27, 14.17, 13.42], [14.67, 13.29, 13.07, 12.54], [13.46, 12.05, 11.85, 11.27]],
	'comparisons':
		[[('CB', 'MET', 'CB', 'ASP', 15.49), ('CB', 'MET', 'CG', 'ASP', 14.06), ('CB', 'MET', 'OD1', 'ASP', 13.7), ('CB', 'MET', 'OD2', 'ASP', 13.41)], [('CG', 'MET', 'CB', 'ASP', 16.67), ('CG', 'MET', 'CG', 'ASP', 15.27), ('CG', 'MET', 'OD1', 'ASP', 14.9), ('CG', 'MET', 'OD2', 'ASP', 14.66)], [('SD', 'MET', 'CB', 'ASP', 16.31), ('SD', 'MET', 'CG', 'ASP', 14.99), ('SD', 'MET', 'OD1', 'ASP', 14.59), ('SD', 'MET', 'OD2', 'ASP', 14.47)], [('CE', 'MET', 'CB', 'ASP', 16.88), ('CE', 'MET', 'CG', 'ASP', 15.55), ('CE', 'MET', 'OD1', 'ASP', 15.0), ('CE', 'MET', 'OD2', 'ASP', 15.16)], [('O', 'MET', 'CB', 'ASP', 16.6), ('O', 'MET', 'CG', 'ASP', 15.28), ('O', 'MET', 'OD1', 'ASP', 15.18), ('O', 'MET', 'OD2', 'ASP', 14.43)], [('C', 'MET', 'CB', 'ASP', 15.63), ('C', 'MET', 'CG', 'ASP', 14.27), ('C', 'MET', 'OD1', 'ASP', 14.17), ('C', 'MET', 'OD2', 'ASP', 13.42)], [('CA', 'MET', 'CB', 'ASP', 14.67), ('CA', 'MET', 'CG', 'ASP', 13.29), ('CA', 'MET', 'OD1', 'ASP', 13.07), ('CA', 'MET', 'OD2', 'ASP', 12.54)], [('N', 'MET', 'CB', 'ASP', 13.46), ('N', 'MET', 'CG', 'ASP', 12.05), ('N', 'MET', 'OD1', 'ASP', 11.85), ('N', 'MET', 'OD2', 'ASP', 11.27)]]}
SER_ASP = { 
	'distances':
		[[11.67, 10.2, 10.0, 9.4], [11.15, 9.65, 9.26, 9.03]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 11.67), ('CB', 'SER', 'CG', 'ASP', 10.2), ('CB', 'SER', 'OD1', 'ASP', 10.0), ('CB', 'SER', 'OD2', 'ASP', 9.4)], [('OG', 'SER', 'CB', 'ASP', 11.15), ('OG', 'SER', 'CG', 'ASP', 9.65), ('OG', 'SER', 'OD1', 'ASP', 9.26), ('OG', 'SER', 'OD2', 'ASP', 9.03)]]}
SER_HIS = { 
	'distances':
		[[9.1, 7.62, 7.17, 6.7, 5.86, 5.44], [8.67, 7.22, 6.84, 6.33, 5.63, 5.17]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 9.1), ('CB', 'SER', 'CG', 'HIS', 7.62), ('CB', 'SER', 'ND1', 'HIS', 7.17), ('CB', 'SER', 'CD2', 'HIS', 6.7), ('CB', 'SER', 'CE1', 'HIS', 5.86), ('CB', 'SER', 'NE2', 'HIS', 5.44)], [('OG', 'SER', 'CB', 'HIS', 8.67), ('OG', 'SER', 'CG', 'HIS', 7.22), ('OG', 'SER', 'ND1', 'HIS', 6.84), ('OG', 'SER', 'CD2', 'HIS', 6.33), ('OG', 'SER', 'CE1', 'HIS', 5.63), ('OG', 'SER', 'NE2', 'HIS', 5.17)]]}
ILE_ASP = { 
	'distances':
		[[16.44, 14.94, 14.24, 14.55], [16.58, 15.1, 14.45, 14.67], [17.47, 15.98, 15.19, 15.69], [16.14, 14.69, 13.98, 14.37], [16.1, 14.61, 13.93, 14.21], [17.0, 15.49, 14.84, 15.05], [16.82, 15.3, 14.7, 14.82], [15.96, 14.45, 13.94, 13.86]],
	'comparisons':
		[[('CB', 'ILE', 'CB', 'ASP', 16.44), ('CB', 'ILE', 'CG', 'ASP', 14.94), ('CB', 'ILE', 'OD1', 'ASP', 14.24), ('CB', 'ILE', 'OD2', 'ASP', 14.55)], [('CG1', 'ILE', 'CB', 'ASP', 16.58), ('CG1', 'ILE', 'CG', 'ASP', 15.1), ('CG1', 'ILE', 'OD1', 'ASP', 14.45), ('CG1', 'ILE', 'OD2', 'ASP', 14.67)], [('CG2', 'ILE', 'CB', 'ASP', 17.47), ('CG2', 'ILE', 'CG', 'ASP', 15.98), ('CG2', 'ILE', 'OD1', 'ASP', 15.19), ('CG2', 'ILE', 'OD2', 'ASP', 15.69)], [('CD1', 'ILE', 'CB', 'ASP', 16.14), ('CD1', 'ILE', 'CG', 'ASP', 14.69), ('CD1', 'ILE', 'OD1', 'ASP', 13.98), ('CD1', 'ILE', 'OD2', 'ASP', 14.37)], [('O', 'ILE', 'CB', 'ASP', 16.1), ('O', 'ILE', 'CG', 'ASP', 14.61), ('O', 'ILE', 'OD1', 'ASP', 13.93), ('O', 'ILE', 'OD2', 'ASP', 14.21)], [('C', 'ILE', 'CB', 'ASP', 17.0), ('C', 'ILE', 'CG', 'ASP', 15.49), ('C', 'ILE', 'OD1', 'ASP', 14.84), ('C', 'ILE', 'OD2', 'ASP', 15.05)], [('CA', 'ILE', 'CB', 'ASP', 16.82), ('CA', 'ILE', 'CG', 'ASP', 15.3), ('CA', 'ILE', 'OD1', 'ASP', 14.7), ('CA', 'ILE', 'OD2', 'ASP', 14.82)], [('N', 'ILE', 'CB', 'ASP', 15.96), ('N', 'ILE', 'CG', 'ASP', 14.45), ('N', 'ILE', 'OD1', 'ASP', 13.94), ('N', 'ILE', 'OD2', 'ASP', 13.86)]]}
ILE_SER = { 
	'distances':
		[[8.26, 7.83], [8.23, 7.82], [9.71, 9.18], [8.55, 7.86], [8.35, 8.15], [8.72, 8.62], [8.11, 8.01], [6.85, 6.99]],
	'comparisons':
		[[('CB', 'ILE', 'CB', 'SER', 8.26), ('CB', 'ILE', 'OG', 'SER', 7.83)], [('CG1', 'ILE', 'CB', 'SER', 8.23), ('CG1', 'ILE', 'OG', 'SER', 7.82)], [('CG2', 'ILE', 'CB', 'SER', 9.71), ('CG2', 'ILE', 'OG', 'SER', 9.18)], [('CD1', 'ILE', 'CB', 'SER', 8.55), ('CD1', 'ILE', 'OG', 'SER', 7.86)], [('O', 'ILE', 'CB', 'SER', 8.35), ('O', 'ILE', 'OG', 'SER', 8.15)], [('C', 'ILE', 'CB', 'SER', 8.72), ('C', 'ILE', 'OG', 'SER', 8.62)], [('CA', 'ILE', 'CB', 'SER', 8.11), ('CA', 'ILE', 'OG', 'SER', 8.01)], [('N', 'ILE', 'CB', 'SER', 6.85), ('N', 'ILE', 'OG', 'SER', 6.99)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(MET_SER, d, 'A_1r4z_3_1_1_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ILE_HIS, d, 'A_1r4z_3_1_1_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(MET_ILE, d, 'A_1r4z_3_1_1_3')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_ASP, d, 'A_1r4z_3_1_1_3')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(MET_HIS, d, 'A_1r4z_3_1_1_3')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(MET_ASP, d, 'A_1r4z_3_1_1_3')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(SER_ASP, d, 'A_1r4z_3_1_1_3')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(SER_HIS, d, 'A_1r4z_3_1_1_3')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(ILE_ASP, d, 'A_1r4z_3_1_1_3')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(ILE_SER, d, 'A_1r4z_3_1_1_3')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'MET_SER' :  match1,
		'ILE_HIS' :  match2,
		'MET_ILE' :  match3,
		'HIS_ASP' :  match4,
		'MET_HIS' :  match5,
		'MET_ASP' :  match6,
		'SER_ASP' :  match7,
		'SER_HIS' :  match8,
		'ILE_ASP' :  match9,
		'ILE_SER' :  match10}