'''
FUNC:A_1auo_3_1_1_1
PDB:1auo
EC:3.1.1.1
RESI:leu,ser,gln,asp,his
LOCI:a-23,114,115,168,199;
'''
import motifFunctions as cmd
GLN_ASP = { 
	'distances':
		[[15.3, 13.81, 13.47, 13.03], [16.6, 15.11, 14.73, 14.36], [17.61, 16.1, 15.64, 15.41], [18.11, 16.59, 16.05, 15.99], [18.12, 16.6, 16.19, 15.87], [16.37, 15.0, 14.91, 14.04], [15.62, 14.23, 14.14, 13.26], [14.59, 13.14, 12.95, 12.27], [13.3, 11.86, 11.73, 10.95]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'ASP', 15.3), ('CB', 'GLN', 'CG', 'ASP', 13.81), ('CB', 'GLN', 'OD1', 'ASP', 13.47), ('CB', 'GLN', 'OD2', 'ASP', 13.03)], [('CG', 'GLN', 'CB', 'ASP', 16.6), ('CG', 'GLN', 'CG', 'ASP', 15.11), ('CG', 'GLN', 'OD1', 'ASP', 14.73), ('CG', 'GLN', 'OD2', 'ASP', 14.36)], [('CD', 'GLN', 'CB', 'ASP', 17.61), ('CD', 'GLN', 'CG', 'ASP', 16.1), ('CD', 'GLN', 'OD1', 'ASP', 15.64), ('CD', 'GLN', 'OD2', 'ASP', 15.41)], [('OE1', 'GLN', 'CB', 'ASP', 18.11), ('OE1', 'GLN', 'CG', 'ASP', 16.59), ('OE1', 'GLN', 'OD1', 'ASP', 16.05), ('OE1', 'GLN', 'OD2', 'ASP', 15.99)], [('NE2', 'GLN', 'CB', 'ASP', 18.12), ('NE2', 'GLN', 'CG', 'ASP', 16.6), ('NE2', 'GLN', 'OD1', 'ASP', 16.19), ('NE2', 'GLN', 'OD2', 'ASP', 15.87)], [('O', 'GLN', 'CB', 'ASP', 16.37), ('O', 'GLN', 'CG', 'ASP', 15.0), ('O', 'GLN', 'OD1', 'ASP', 14.91), ('O', 'GLN', 'OD2', 'ASP', 14.04)], [('C', 'GLN', 'CB', 'ASP', 15.62), ('C', 'GLN', 'CG', 'ASP', 14.23), ('C', 'GLN', 'OD1', 'ASP', 14.14), ('C', 'GLN', 'OD2', 'ASP', 13.26)], [('CA', 'GLN', 'CB', 'ASP', 14.59), ('CA', 'GLN', 'CG', 'ASP', 13.14), ('CA', 'GLN', 'OD1', 'ASP', 12.95), ('CA', 'GLN', 'OD2', 'ASP', 12.27)], [('N', 'GLN', 'CB', 'ASP', 13.3), ('N', 'GLN', 'CG', 'ASP', 11.86), ('N', 'GLN', 'OD1', 'ASP', 11.73), ('N', 'GLN', 'OD2', 'ASP', 10.95)]]}
HIS_ASP = { 
	'distances':
		[[6.62, 5.63, 5.55, 5.64], [7.15, 5.84, 5.71, 5.49], [6.69, 5.27, 5.34, 4.58], [8.43, 7.05, 6.75, 6.65], [7.79, 6.31, 6.23, 5.54], [8.73, 7.25, 6.98, 6.65]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 6.62), ('CB', 'HIS', 'CG', 'ASP', 5.63), ('CB', 'HIS', 'OD1', 'ASP', 5.55), ('CB', 'HIS', 'OD2', 'ASP', 5.64)], [('CG', 'HIS', 'CB', 'ASP', 7.15), ('CG', 'HIS', 'CG', 'ASP', 5.84), ('CG', 'HIS', 'OD1', 'ASP', 5.71), ('CG', 'HIS', 'OD2', 'ASP', 5.49)], [('ND1', 'HIS', 'CB', 'ASP', 6.69), ('ND1', 'HIS', 'CG', 'ASP', 5.27), ('ND1', 'HIS', 'OD1', 'ASP', 5.34), ('ND1', 'HIS', 'OD2', 'ASP', 4.58)], [('CD2', 'HIS', 'CB', 'ASP', 8.43), ('CD2', 'HIS', 'CG', 'ASP', 7.05), ('CD2', 'HIS', 'OD1', 'ASP', 6.75), ('CD2', 'HIS', 'OD2', 'ASP', 6.65)], [('CE1', 'HIS', 'CB', 'ASP', 7.79), ('CE1', 'HIS', 'CG', 'ASP', 6.31), ('CE1', 'HIS', 'OD1', 'ASP', 6.23), ('CE1', 'HIS', 'OD2', 'ASP', 5.54)], [('NE2', 'HIS', 'CB', 'ASP', 8.73), ('NE2', 'HIS', 'CG', 'ASP', 7.25), ('NE2', 'HIS', 'OD1', 'ASP', 6.98), ('NE2', 'HIS', 'OD2', 'ASP', 6.65)]]}
GLN_LEU = { 
	'distances':
		[[6.26, 7.44, 7.5, 7.92, 8.45, 7.81, 6.31, 5.71], [6.76, 7.61, 7.28, 8.05, 9.2, 8.36, 6.86, 6.62], [6.1, 6.65, 6.01, 7.22, 8.56, 7.59, 6.18, 6.38], [6.37, 6.54, 5.74, 6.87, 9.03, 8.06, 6.75, 7.22], [5.94, 6.53, 5.79, 7.46, 7.93, 6.84, 5.56, 5.79], [9.48, 10.61, 10.39, 11.13, 11.4, 10.67, 9.25, 8.46], [8.64, 9.89, 9.82, 10.47, 10.37, 9.72, 8.33, 7.41], [7.64, 8.91, 9.05, 9.31, 9.59, 9.06, 7.63, 6.75], [7.77, 9.18, 9.6, 9.56, 9.37, 9.06, 7.76, 6.67]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'LEU', 6.26), ('CB', 'GLN', 'CG', 'LEU', 7.44), ('CB', 'GLN', 'CD1', 'LEU', 7.5), ('CB', 'GLN', 'CD2', 'LEU', 7.92), ('CB', 'GLN', 'O', 'LEU', 8.45), ('CB', 'GLN', 'C', 'LEU', 7.81), ('CB', 'GLN', 'CA', 'LEU', 6.31), ('CB', 'GLN', 'N', 'LEU', 5.71)], [('CG', 'GLN', 'CB', 'LEU', 6.76), ('CG', 'GLN', 'CG', 'LEU', 7.61), ('CG', 'GLN', 'CD1', 'LEU', 7.28), ('CG', 'GLN', 'CD2', 'LEU', 8.05), ('CG', 'GLN', 'O', 'LEU', 9.2), ('CG', 'GLN', 'C', 'LEU', 8.36), ('CG', 'GLN', 'CA', 'LEU', 6.86), ('CG', 'GLN', 'N', 'LEU', 6.62)], [('CD', 'GLN', 'CB', 'LEU', 6.1), ('CD', 'GLN', 'CG', 'LEU', 6.65), ('CD', 'GLN', 'CD1', 'LEU', 6.01), ('CD', 'GLN', 'CD2', 'LEU', 7.22), ('CD', 'GLN', 'O', 'LEU', 8.56), ('CD', 'GLN', 'C', 'LEU', 7.59), ('CD', 'GLN', 'CA', 'LEU', 6.18), ('CD', 'GLN', 'N', 'LEU', 6.38)], [('OE1', 'GLN', 'CB', 'LEU', 6.37), ('OE1', 'GLN', 'CG', 'LEU', 6.54), ('OE1', 'GLN', 'CD1', 'LEU', 5.74), ('OE1', 'GLN', 'CD2', 'LEU', 6.87), ('OE1', 'GLN', 'O', 'LEU', 9.03), ('OE1', 'GLN', 'C', 'LEU', 8.06), ('OE1', 'GLN', 'CA', 'LEU', 6.75), ('OE1', 'GLN', 'N', 'LEU', 7.22)], [('NE2', 'GLN', 'CB', 'LEU', 5.94), ('NE2', 'GLN', 'CG', 'LEU', 6.53), ('NE2', 'GLN', 'CD1', 'LEU', 5.79), ('NE2', 'GLN', 'CD2', 'LEU', 7.46), ('NE2', 'GLN', 'O', 'LEU', 7.93), ('NE2', 'GLN', 'C', 'LEU', 6.84), ('NE2', 'GLN', 'CA', 'LEU', 5.56), ('NE2', 'GLN', 'N', 'LEU', 5.79)], [('O', 'GLN', 'CB', 'LEU', 9.48), ('O', 'GLN', 'CG', 'LEU', 10.61), ('O', 'GLN', 'CD1', 'LEU', 10.39), ('O', 'GLN', 'CD2', 'LEU', 11.13), ('O', 'GLN', 'O', 'LEU', 11.4), ('O', 'GLN', 'C', 'LEU', 10.67), ('O', 'GLN', 'CA', 'LEU', 9.25), ('O', 'GLN', 'N', 'LEU', 8.46)], [('C', 'GLN', 'CB', 'LEU', 8.64), ('C', 'GLN', 'CG', 'LEU', 9.89), ('C', 'GLN', 'CD1', 'LEU', 9.82), ('C', 'GLN', 'CD2', 'LEU', 10.47), ('C', 'GLN', 'O', 'LEU', 10.37), ('C', 'GLN', 'C', 'LEU', 9.72), ('C', 'GLN', 'CA', 'LEU', 8.33), ('C', 'GLN', 'N', 'LEU', 7.41)], [('CA', 'GLN', 'CB', 'LEU', 7.64), ('CA', 'GLN', 'CG', 'LEU', 8.91), ('CA', 'GLN', 'CD1', 'LEU', 9.05), ('CA', 'GLN', 'CD2', 'LEU', 9.31), ('CA', 'GLN', 'O', 'LEU', 9.59), ('CA', 'GLN', 'C', 'LEU', 9.06), ('CA', 'GLN', 'CA', 'LEU', 7.63), ('CA', 'GLN', 'N', 'LEU', 6.75)], [('N', 'GLN', 'CB', 'LEU', 7.77), ('N', 'GLN', 'CG', 'LEU', 9.18), ('N', 'GLN', 'CD1', 'LEU', 9.6), ('N', 'GLN', 'CD2', 'LEU', 9.56), ('N', 'GLN', 'O', 'LEU', 9.37), ('N', 'GLN', 'C', 'LEU', 9.06), ('N', 'GLN', 'CA', 'LEU', 7.76), ('N', 'GLN', 'N', 'LEU', 6.67)]]}
LEU_HIS = { 
	'distances':
		[[12.69, 11.46, 11.67, 10.15, 10.57, 9.54], [13.72, 12.58, 12.86, 11.26, 11.81, 10.75], [15.09, 13.88, 14.07, 12.58, 12.96, 11.96], [13.51, 12.41, 12.69, 11.15, 11.68, 10.66], [12.55, 11.54, 12.05, 10.2, 11.18, 9.97], [13.39, 12.27, 12.66, 10.93, 11.68, 10.54], [13.12, 11.88, 12.08, 10.56, 10.99, 9.96], [12.3, 11.01, 11.12, 9.74, 10.01, 9.05]],
	'comparisons':
		[[('CB', 'LEU', 'CB', 'HIS', 12.69), ('CB', 'LEU', 'CG', 'HIS', 11.46), ('CB', 'LEU', 'ND1', 'HIS', 11.67), ('CB', 'LEU', 'CD2', 'HIS', 10.15), ('CB', 'LEU', 'CE1', 'HIS', 10.57), ('CB', 'LEU', 'NE2', 'HIS', 9.54)], [('CG', 'LEU', 'CB', 'HIS', 13.72), ('CG', 'LEU', 'CG', 'HIS', 12.58), ('CG', 'LEU', 'ND1', 'HIS', 12.86), ('CG', 'LEU', 'CD2', 'HIS', 11.26), ('CG', 'LEU', 'CE1', 'HIS', 11.81), ('CG', 'LEU', 'NE2', 'HIS', 10.75)], [('CD1', 'LEU', 'CB', 'HIS', 15.09), ('CD1', 'LEU', 'CG', 'HIS', 13.88), ('CD1', 'LEU', 'ND1', 'HIS', 14.07), ('CD1', 'LEU', 'CD2', 'HIS', 12.58), ('CD1', 'LEU', 'CE1', 'HIS', 12.96), ('CD1', 'LEU', 'NE2', 'HIS', 11.96)], [('CD2', 'LEU', 'CB', 'HIS', 13.51), ('CD2', 'LEU', 'CG', 'HIS', 12.41), ('CD2', 'LEU', 'ND1', 'HIS', 12.69), ('CD2', 'LEU', 'CD2', 'HIS', 11.15), ('CD2', 'LEU', 'CE1', 'HIS', 11.68), ('CD2', 'LEU', 'NE2', 'HIS', 10.66)], [('O', 'LEU', 'CB', 'HIS', 12.55), ('O', 'LEU', 'CG', 'HIS', 11.54), ('O', 'LEU', 'ND1', 'HIS', 12.05), ('O', 'LEU', 'CD2', 'HIS', 10.2), ('O', 'LEU', 'CE1', 'HIS', 11.18), ('O', 'LEU', 'NE2', 'HIS', 9.97)], [('C', 'LEU', 'CB', 'HIS', 13.39), ('C', 'LEU', 'CG', 'HIS', 12.27), ('C', 'LEU', 'ND1', 'HIS', 12.66), ('C', 'LEU', 'CD2', 'HIS', 10.93), ('C', 'LEU', 'CE1', 'HIS', 11.68), ('C', 'LEU', 'NE2', 'HIS', 10.54)], [('CA', 'LEU', 'CB', 'HIS', 13.12), ('CA', 'LEU', 'CG', 'HIS', 11.88), ('CA', 'LEU', 'ND1', 'HIS', 12.08), ('CA', 'LEU', 'CD2', 'HIS', 10.56), ('CA', 'LEU', 'CE1', 'HIS', 10.99), ('CA', 'LEU', 'NE2', 'HIS', 9.96)], [('N', 'LEU', 'CB', 'HIS', 12.3), ('N', 'LEU', 'CG', 'HIS', 11.01), ('N', 'LEU', 'ND1', 'HIS', 11.12), ('N', 'LEU', 'CD2', 'HIS', 9.74), ('N', 'LEU', 'CE1', 'HIS', 10.01), ('N', 'LEU', 'NE2', 'HIS', 9.05)]]}
GLN_HIS = { 
	'distances':
		[[12.94, 11.47, 11.06, 10.43, 9.75, 9.27], [14.37, 12.9, 12.48, 11.86, 11.16, 10.71], [15.08, 13.65, 13.39, 12.51, 12.09, 11.48], [15.64, 14.24, 14.0, 13.1, 12.72, 12.09], [15.31, 13.9, 13.72, 12.71, 12.45, 11.75], [14.75, 13.25, 12.53, 12.46, 11.24, 11.17], [13.74, 12.24, 11.59, 11.4, 10.31, 10.15], [12.62, 11.11, 10.51, 10.23, 9.2, 8.96], [11.25, 9.75, 9.14, 8.91, 7.84, 7.63]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'HIS', 12.94), ('CB', 'GLN', 'CG', 'HIS', 11.47), ('CB', 'GLN', 'ND1', 'HIS', 11.06), ('CB', 'GLN', 'CD2', 'HIS', 10.43), ('CB', 'GLN', 'CE1', 'HIS', 9.75), ('CB', 'GLN', 'NE2', 'HIS', 9.27)], [('CG', 'GLN', 'CB', 'HIS', 14.37), ('CG', 'GLN', 'CG', 'HIS', 12.9), ('CG', 'GLN', 'ND1', 'HIS', 12.48), ('CG', 'GLN', 'CD2', 'HIS', 11.86), ('CG', 'GLN', 'CE1', 'HIS', 11.16), ('CG', 'GLN', 'NE2', 'HIS', 10.71)], [('CD', 'GLN', 'CB', 'HIS', 15.08), ('CD', 'GLN', 'CG', 'HIS', 13.65), ('CD', 'GLN', 'ND1', 'HIS', 13.39), ('CD', 'GLN', 'CD2', 'HIS', 12.51), ('CD', 'GLN', 'CE1', 'HIS', 12.09), ('CD', 'GLN', 'NE2', 'HIS', 11.48)], [('OE1', 'GLN', 'CB', 'HIS', 15.64), ('OE1', 'GLN', 'CG', 'HIS', 14.24), ('OE1', 'GLN', 'ND1', 'HIS', 14.0), ('OE1', 'GLN', 'CD2', 'HIS', 13.1), ('OE1', 'GLN', 'CE1', 'HIS', 12.72), ('OE1', 'GLN', 'NE2', 'HIS', 12.09)], [('NE2', 'GLN', 'CB', 'HIS', 15.31), ('NE2', 'GLN', 'CG', 'HIS', 13.9), ('NE2', 'GLN', 'ND1', 'HIS', 13.72), ('NE2', 'GLN', 'CD2', 'HIS', 12.71), ('NE2', 'GLN', 'CE1', 'HIS', 12.45), ('NE2', 'GLN', 'NE2', 'HIS', 11.75)], [('O', 'GLN', 'CB', 'HIS', 14.75), ('O', 'GLN', 'CG', 'HIS', 13.25), ('O', 'GLN', 'ND1', 'HIS', 12.53), ('O', 'GLN', 'CD2', 'HIS', 12.46), ('O', 'GLN', 'CE1', 'HIS', 11.24), ('O', 'GLN', 'NE2', 'HIS', 11.17)], [('C', 'GLN', 'CB', 'HIS', 13.74), ('C', 'GLN', 'CG', 'HIS', 12.24), ('C', 'GLN', 'ND1', 'HIS', 11.59), ('C', 'GLN', 'CD2', 'HIS', 11.4), ('C', 'GLN', 'CE1', 'HIS', 10.31), ('C', 'GLN', 'NE2', 'HIS', 10.15)], [('CA', 'GLN', 'CB', 'HIS', 12.62), ('CA', 'GLN', 'CG', 'HIS', 11.11), ('CA', 'GLN', 'ND1', 'HIS', 10.51), ('CA', 'GLN', 'CD2', 'HIS', 10.23), ('CA', 'GLN', 'CE1', 'HIS', 9.2), ('CA', 'GLN', 'NE2', 'HIS', 8.96)], [('N', 'GLN', 'CB', 'HIS', 11.25), ('N', 'GLN', 'CG', 'HIS', 9.75), ('N', 'GLN', 'ND1', 'HIS', 9.14), ('N', 'GLN', 'CD2', 'HIS', 8.91), ('N', 'GLN', 'CE1', 'HIS', 7.84), ('N', 'GLN', 'NE2', 'HIS', 7.63)]]}
LEU_SER = { 
	'distances':
		[[8.49, 7.92], [9.97, 9.3], [10.79, 10.23], [10.31, 9.42], [9.24, 8.98], [9.37, 9.16], [8.45, 8.21], [7.2, 7.16]],
	'comparisons':
		[[('CB', 'LEU', 'CB', 'SER', 8.49), ('CB', 'LEU', 'OG', 'SER', 7.92)], [('CG', 'LEU', 'CB', 'SER', 9.97), ('CG', 'LEU', 'OG', 'SER', 9.3)], [('CD1', 'LEU', 'CB', 'SER', 10.79), ('CD1', 'LEU', 'OG', 'SER', 10.23)], [('CD2', 'LEU', 'CB', 'SER', 10.31), ('CD2', 'LEU', 'OG', 'SER', 9.42)], [('O', 'LEU', 'CB', 'SER', 9.24), ('O', 'LEU', 'OG', 'SER', 8.98)], [('C', 'LEU', 'CB', 'SER', 9.37), ('C', 'LEU', 'OG', 'SER', 9.16)], [('CA', 'LEU', 'CB', 'SER', 8.45), ('CA', 'LEU', 'OG', 'SER', 8.21)], [('N', 'LEU', 'CB', 'SER', 7.2), ('N', 'LEU', 'OG', 'SER', 7.16)]]}
SER_ASP = { 
	'distances':
		[[11.31, 9.89, 9.88, 8.93], [10.91, 9.41, 9.19, 8.61]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 11.31), ('CB', 'SER', 'CG', 'ASP', 9.89), ('CB', 'SER', 'OD1', 'ASP', 9.88), ('CB', 'SER', 'OD2', 'ASP', 8.93)], [('OG', 'SER', 'CB', 'ASP', 10.91), ('OG', 'SER', 'CG', 'ASP', 9.41), ('OG', 'SER', 'OD1', 'ASP', 9.19), ('OG', 'SER', 'OD2', 'ASP', 8.61)]]}
LEU_ASP = { 
	'distances':
		[[16.08, 14.55, 13.96, 14.05], [17.14, 15.62, 14.93, 15.21], [18.38, 16.85, 16.19, 16.39], [16.71, 15.21, 14.41, 14.92], [16.58, 15.12, 14.62, 14.61], [17.23, 15.74, 15.26, 15.18], [16.65, 15.14, 14.67, 14.53], [15.76, 14.26, 13.9, 13.55]],
	'comparisons':
		[[('CB', 'LEU', 'CB', 'ASP', 16.08), ('CB', 'LEU', 'CG', 'ASP', 14.55), ('CB', 'LEU', 'OD1', 'ASP', 13.96), ('CB', 'LEU', 'OD2', 'ASP', 14.05)], [('CG', 'LEU', 'CB', 'ASP', 17.14), ('CG', 'LEU', 'CG', 'ASP', 15.62), ('CG', 'LEU', 'OD1', 'ASP', 14.93), ('CG', 'LEU', 'OD2', 'ASP', 15.21)], [('CD1', 'LEU', 'CB', 'ASP', 18.38), ('CD1', 'LEU', 'CG', 'ASP', 16.85), ('CD1', 'LEU', 'OD1', 'ASP', 16.19), ('CD1', 'LEU', 'OD2', 'ASP', 16.39)], [('CD2', 'LEU', 'CB', 'ASP', 16.71), ('CD2', 'LEU', 'CG', 'ASP', 15.21), ('CD2', 'LEU', 'OD1', 'ASP', 14.41), ('CD2', 'LEU', 'OD2', 'ASP', 14.92)], [('O', 'LEU', 'CB', 'ASP', 16.58), ('O', 'LEU', 'CG', 'ASP', 15.12), ('O', 'LEU', 'OD1', 'ASP', 14.62), ('O', 'LEU', 'OD2', 'ASP', 14.61)], [('C', 'LEU', 'CB', 'ASP', 17.23), ('C', 'LEU', 'CG', 'ASP', 15.74), ('C', 'LEU', 'OD1', 'ASP', 15.26), ('C', 'LEU', 'OD2', 'ASP', 15.18)], [('CA', 'LEU', 'CB', 'ASP', 16.65), ('CA', 'LEU', 'CG', 'ASP', 15.14), ('CA', 'LEU', 'OD1', 'ASP', 14.67), ('CA', 'LEU', 'OD2', 'ASP', 14.53)], [('N', 'LEU', 'CB', 'ASP', 15.76), ('N', 'LEU', 'CG', 'ASP', 14.26), ('N', 'LEU', 'OD1', 'ASP', 13.9), ('N', 'LEU', 'OD2', 'ASP', 13.55)]]}
GLN_SER = { 
	'distances':
		[[6.77, 6.61], [8.28, 8.07], [9.26, 8.99], [10.16, 9.72], [9.4, 9.3], [8.08, 8.44], [6.98, 7.41], [6.12, 6.21], [4.67, 4.89]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'SER', 6.77), ('CB', 'GLN', 'OG', 'SER', 6.61)], [('CG', 'GLN', 'CB', 'SER', 8.28), ('CG', 'GLN', 'OG', 'SER', 8.07)], [('CD', 'GLN', 'CB', 'SER', 9.26), ('CD', 'GLN', 'OG', 'SER', 8.99)], [('OE1', 'GLN', 'CB', 'SER', 10.16), ('OE1', 'GLN', 'OG', 'SER', 9.72)], [('NE2', 'GLN', 'CB', 'SER', 9.4), ('NE2', 'GLN', 'OG', 'SER', 9.3)], [('O', 'GLN', 'CB', 'SER', 8.08), ('O', 'GLN', 'OG', 'SER', 8.44)], [('C', 'GLN', 'CB', 'SER', 6.98), ('C', 'GLN', 'OG', 'SER', 7.41)], [('CA', 'GLN', 'CB', 'SER', 6.12), ('CA', 'GLN', 'OG', 'SER', 6.21)], [('N', 'GLN', 'CB', 'SER', 4.67), ('N', 'GLN', 'OG', 'SER', 4.89)]]}
SER_HIS = { 
	'distances':
		[[8.85, 7.38, 6.88, 6.61, 5.69, 5.44], [8.42, 6.92, 6.47, 6.03, 5.18, 4.76]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 8.85), ('CB', 'SER', 'CG', 'HIS', 7.38), ('CB', 'SER', 'ND1', 'HIS', 6.88), ('CB', 'SER', 'CD2', 'HIS', 6.61), ('CB', 'SER', 'CE1', 'HIS', 5.69), ('CB', 'SER', 'NE2', 'HIS', 5.44)], [('OG', 'SER', 'CB', 'HIS', 8.42), ('OG', 'SER', 'CG', 'HIS', 6.92), ('OG', 'SER', 'ND1', 'HIS', 6.47), ('OG', 'SER', 'CD2', 'HIS', 6.03), ('OG', 'SER', 'CE1', 'HIS', 5.18), ('OG', 'SER', 'NE2', 'HIS', 4.76)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLN_ASP, d, 'A_1auo_3_1_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'A_1auo_3_1_1_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLN_LEU, d, 'A_1auo_3_1_1_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(LEU_HIS, d, 'A_1auo_3_1_1_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLN_HIS, d, 'A_1auo_3_1_1_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(LEU_SER, d, 'A_1auo_3_1_1_1')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(SER_ASP, d, 'A_1auo_3_1_1_1')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(LEU_ASP, d, 'A_1auo_3_1_1_1')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(GLN_SER, d, 'A_1auo_3_1_1_1')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(SER_HIS, d, 'A_1auo_3_1_1_1')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLN_ASP' :  match1,
		'HIS_ASP' :  match2,
		'GLN_LEU' :  match3,
		'LEU_HIS' :  match4,
		'GLN_HIS' :  match5,
		'LEU_SER' :  match6,
		'SER_ASP' :  match7,
		'LEU_ASP' :  match8,
		'GLN_SER' :  match9,
		'SER_HIS' :  match10}