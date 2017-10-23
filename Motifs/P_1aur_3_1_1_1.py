'''
FUNC:P_1aur_3_1_1_1
PDB:1aur
EC:3.1.1.1
RESI:leu,ser,gln,asp,his
LOCI:a-23,114,115,168,199;
'''
import motifFunctions as cmd
GLN_HIS = { 
	'distances':
		[[13.24, 11.77, 11.37, 10.72, 10.06, 9.58], [13.95, 12.5, 12.11, 11.47, 10.83, 10.36], [14.85, 13.44, 13.19, 12.32, 11.93, 11.31], [15.62, 14.24, 14.0, 13.14, 12.77, 12.17], [14.95, 13.56, 13.4, 12.37, 12.15, 11.43], [14.9, 13.39, 12.68, 12.58, 11.38, 11.28], [13.86, 12.36, 11.71, 11.5, 10.41, 10.22], [12.86, 11.36, 10.77, 10.46, 9.45, 9.2], [11.53, 10.02, 9.43, 9.15, 8.11, 7.87]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'HIS', 13.24), ('CB', 'GLN', 'CG', 'HIS', 11.77), ('CB', 'GLN', 'ND1', 'HIS', 11.37), ('CB', 'GLN', 'CD2', 'HIS', 10.72), ('CB', 'GLN', 'CE1', 'HIS', 10.06), ('CB', 'GLN', 'NE2', 'HIS', 9.58)], [('CG', 'GLN', 'CB', 'HIS', 13.95), ('CG', 'GLN', 'CG', 'HIS', 12.5), ('CG', 'GLN', 'ND1', 'HIS', 12.11), ('CG', 'GLN', 'CD2', 'HIS', 11.47), ('CG', 'GLN', 'CE1', 'HIS', 10.83), ('CG', 'GLN', 'NE2', 'HIS', 10.36)], [('CD', 'GLN', 'CB', 'HIS', 14.85), ('CD', 'GLN', 'CG', 'HIS', 13.44), ('CD', 'GLN', 'ND1', 'HIS', 13.19), ('CD', 'GLN', 'CD2', 'HIS', 12.32), ('CD', 'GLN', 'CE1', 'HIS', 11.93), ('CD', 'GLN', 'NE2', 'HIS', 11.31)], [('OE1', 'GLN', 'CB', 'HIS', 15.62), ('OE1', 'GLN', 'CG', 'HIS', 14.24), ('OE1', 'GLN', 'ND1', 'HIS', 14.0), ('OE1', 'GLN', 'CD2', 'HIS', 13.14), ('OE1', 'GLN', 'CE1', 'HIS', 12.77), ('OE1', 'GLN', 'NE2', 'HIS', 12.17)], [('NE2', 'GLN', 'CB', 'HIS', 14.95), ('NE2', 'GLN', 'CG', 'HIS', 13.56), ('NE2', 'GLN', 'ND1', 'HIS', 13.4), ('NE2', 'GLN', 'CD2', 'HIS', 12.37), ('NE2', 'GLN', 'CE1', 'HIS', 12.15), ('NE2', 'GLN', 'NE2', 'HIS', 11.43)], [('O', 'GLN', 'CB', 'HIS', 14.9), ('O', 'GLN', 'CG', 'HIS', 13.39), ('O', 'GLN', 'ND1', 'HIS', 12.68), ('O', 'GLN', 'CD2', 'HIS', 12.58), ('O', 'GLN', 'CE1', 'HIS', 11.38), ('O', 'GLN', 'NE2', 'HIS', 11.28)], [('C', 'GLN', 'CB', 'HIS', 13.86), ('C', 'GLN', 'CG', 'HIS', 12.36), ('C', 'GLN', 'ND1', 'HIS', 11.71), ('C', 'GLN', 'CD2', 'HIS', 11.5), ('C', 'GLN', 'CE1', 'HIS', 10.41), ('C', 'GLN', 'NE2', 'HIS', 10.22)], [('CA', 'GLN', 'CB', 'HIS', 12.86), ('CA', 'GLN', 'CG', 'HIS', 11.36), ('CA', 'GLN', 'ND1', 'HIS', 10.77), ('CA', 'GLN', 'CD2', 'HIS', 10.46), ('CA', 'GLN', 'CE1', 'HIS', 9.45), ('CA', 'GLN', 'NE2', 'HIS', 9.2)], [('N', 'GLN', 'CB', 'HIS', 11.53), ('N', 'GLN', 'CG', 'HIS', 10.02), ('N', 'GLN', 'ND1', 'HIS', 9.43), ('N', 'GLN', 'CD2', 'HIS', 9.15), ('N', 'GLN', 'CE1', 'HIS', 8.11), ('N', 'GLN', 'NE2', 'HIS', 7.87)]]}
ASP_HIS = { 
	'distances':
		[[6.85, 7.33, 6.8, 8.62, 7.91, 8.89], [5.73, 5.95, 5.35, 7.2, 6.43, 7.4], [5.62, 5.77, 5.32, 6.88, 6.29, 7.12], [5.55, 5.49, 4.66, 6.7, 5.7, 6.77]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 6.85), ('CB', 'ASP', 'CG', 'HIS', 7.33), ('CB', 'ASP', 'ND1', 'HIS', 6.8), ('CB', 'ASP', 'CD2', 'HIS', 8.62), ('CB', 'ASP', 'CE1', 'HIS', 7.91), ('CB', 'ASP', 'NE2', 'HIS', 8.89)], [('CG', 'ASP', 'CB', 'HIS', 5.73), ('CG', 'ASP', 'CG', 'HIS', 5.95), ('CG', 'ASP', 'ND1', 'HIS', 5.35), ('CG', 'ASP', 'CD2', 'HIS', 7.2), ('CG', 'ASP', 'CE1', 'HIS', 6.43), ('CG', 'ASP', 'NE2', 'HIS', 7.4)], [('OD1', 'ASP', 'CB', 'HIS', 5.62), ('OD1', 'ASP', 'CG', 'HIS', 5.77), ('OD1', 'ASP', 'ND1', 'HIS', 5.32), ('OD1', 'ASP', 'CD2', 'HIS', 6.88), ('OD1', 'ASP', 'CE1', 'HIS', 6.29), ('OD1', 'ASP', 'NE2', 'HIS', 7.12)], [('OD2', 'ASP', 'CB', 'HIS', 5.55), ('OD2', 'ASP', 'CG', 'HIS', 5.49), ('OD2', 'ASP', 'ND1', 'HIS', 4.66), ('OD2', 'ASP', 'CD2', 'HIS', 6.7), ('OD2', 'ASP', 'CE1', 'HIS', 5.7), ('OD2', 'ASP', 'NE2', 'HIS', 6.77)]]}
SER_GLN = { 
	'distances':
		[[6.68, 7.76, 8.88, 9.91, 8.95, 7.98, 6.89, 6.04, 4.61], [6.27, 7.03, 8.22, 9.11, 8.53, 7.87, 6.89, 5.72, 4.55]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLN', 6.68), ('CB', 'SER', 'CG', 'GLN', 7.76), ('CB', 'SER', 'CD', 'GLN', 8.88), ('CB', 'SER', 'OE1', 'GLN', 9.91), ('CB', 'SER', 'NE2', 'GLN', 8.95), ('CB', 'SER', 'O', 'GLN', 7.98), ('CB', 'SER', 'C', 'GLN', 6.89), ('CB', 'SER', 'CA', 'GLN', 6.04), ('CB', 'SER', 'N', 'GLN', 4.61)], [('OG', 'SER', 'CB', 'GLN', 6.27), ('OG', 'SER', 'CG', 'GLN', 7.03), ('OG', 'SER', 'CD', 'GLN', 8.22), ('OG', 'SER', 'OE1', 'GLN', 9.11), ('OG', 'SER', 'NE2', 'GLN', 8.53), ('OG', 'SER', 'O', 'GLN', 7.87), ('OG', 'SER', 'C', 'GLN', 6.89), ('OG', 'SER', 'CA', 'GLN', 5.72), ('OG', 'SER', 'N', 'GLN', 4.55)]]}
LEU_HIS = { 
	'distances':
		[[12.63, 11.44, 11.63, 10.17, 10.59, 9.59], [13.76, 12.63, 12.87, 11.39, 11.87, 10.88], [15.12, 13.93, 14.08, 12.68, 13.0, 12.07], [13.56, 12.46, 12.65, 11.32, 11.69, 10.8], [12.13, 11.14, 11.69, 9.8, 10.84, 9.61], [13.05, 11.98, 12.41, 10.63, 11.46, 10.29], [12.93, 11.72, 11.95, 10.4, 10.88, 9.83], [12.07, 10.8, 10.95, 9.49, 9.84, 8.83]],
	'comparisons':
		[[('CB', 'LEU', 'CB', 'HIS', 12.63), ('CB', 'LEU', 'CG', 'HIS', 11.44), ('CB', 'LEU', 'ND1', 'HIS', 11.63), ('CB', 'LEU', 'CD2', 'HIS', 10.17), ('CB', 'LEU', 'CE1', 'HIS', 10.59), ('CB', 'LEU', 'NE2', 'HIS', 9.59)], [('CG', 'LEU', 'CB', 'HIS', 13.76), ('CG', 'LEU', 'CG', 'HIS', 12.63), ('CG', 'LEU', 'ND1', 'HIS', 12.87), ('CG', 'LEU', 'CD2', 'HIS', 11.39), ('CG', 'LEU', 'CE1', 'HIS', 11.87), ('CG', 'LEU', 'NE2', 'HIS', 10.88)], [('CD1', 'LEU', 'CB', 'HIS', 15.12), ('CD1', 'LEU', 'CG', 'HIS', 13.93), ('CD1', 'LEU', 'ND1', 'HIS', 14.08), ('CD1', 'LEU', 'CD2', 'HIS', 12.68), ('CD1', 'LEU', 'CE1', 'HIS', 13.0), ('CD1', 'LEU', 'NE2', 'HIS', 12.07)], [('CD2', 'LEU', 'CB', 'HIS', 13.56), ('CD2', 'LEU', 'CG', 'HIS', 12.46), ('CD2', 'LEU', 'ND1', 'HIS', 12.65), ('CD2', 'LEU', 'CD2', 'HIS', 11.32), ('CD2', 'LEU', 'CE1', 'HIS', 11.69), ('CD2', 'LEU', 'NE2', 'HIS', 10.8)], [('O', 'LEU', 'CB', 'HIS', 12.13), ('O', 'LEU', 'CG', 'HIS', 11.14), ('O', 'LEU', 'ND1', 'HIS', 11.69), ('O', 'LEU', 'CD2', 'HIS', 9.8), ('O', 'LEU', 'CE1', 'HIS', 10.84), ('O', 'LEU', 'NE2', 'HIS', 9.61)], [('C', 'LEU', 'CB', 'HIS', 13.05), ('C', 'LEU', 'CG', 'HIS', 11.98), ('C', 'LEU', 'ND1', 'HIS', 12.41), ('C', 'LEU', 'CD2', 'HIS', 10.63), ('C', 'LEU', 'CE1', 'HIS', 11.46), ('C', 'LEU', 'NE2', 'HIS', 10.29)], [('CA', 'LEU', 'CB', 'HIS', 12.93), ('CA', 'LEU', 'CG', 'HIS', 11.72), ('CA', 'LEU', 'ND1', 'HIS', 11.95), ('CA', 'LEU', 'CD2', 'HIS', 10.4), ('CA', 'LEU', 'CE1', 'HIS', 10.88), ('CA', 'LEU', 'NE2', 'HIS', 9.83)], [('N', 'LEU', 'CB', 'HIS', 12.07), ('N', 'LEU', 'CG', 'HIS', 10.8), ('N', 'LEU', 'ND1', 'HIS', 10.95), ('N', 'LEU', 'CD2', 'HIS', 9.49), ('N', 'LEU', 'CE1', 'HIS', 9.84), ('N', 'LEU', 'NE2', 'HIS', 8.83)]]}
GLN_ASP = { 
	'distances':
		[[15.66, 14.21, 13.81, 13.55], [16.23, 14.79, 14.27, 14.25], [17.43, 15.96, 15.38, 15.44], [18.11, 16.65, 16.0, 16.22], [17.84, 16.35, 15.83, 15.77], [16.52, 15.21, 15.03, 14.43], [15.75, 14.4, 14.22, 13.59], [14.86, 13.46, 13.17, 12.75], [13.63, 12.23, 12.0, 11.45]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'ASP', 15.66), ('CB', 'GLN', 'CG', 'ASP', 14.21), ('CB', 'GLN', 'OD1', 'ASP', 13.81), ('CB', 'GLN', 'OD2', 'ASP', 13.55)], [('CG', 'GLN', 'CB', 'ASP', 16.23), ('CG', 'GLN', 'CG', 'ASP', 14.79), ('CG', 'GLN', 'OD1', 'ASP', 14.27), ('CG', 'GLN', 'OD2', 'ASP', 14.25)], [('CD', 'GLN', 'CB', 'ASP', 17.43), ('CD', 'GLN', 'CG', 'ASP', 15.96), ('CD', 'GLN', 'OD1', 'ASP', 15.38), ('CD', 'GLN', 'OD2', 'ASP', 15.44)], [('OE1', 'GLN', 'CB', 'ASP', 18.11), ('OE1', 'GLN', 'CG', 'ASP', 16.65), ('OE1', 'GLN', 'OD1', 'ASP', 16.0), ('OE1', 'GLN', 'OD2', 'ASP', 16.22)], [('NE2', 'GLN', 'CB', 'ASP', 17.84), ('NE2', 'GLN', 'CG', 'ASP', 16.35), ('NE2', 'GLN', 'OD1', 'ASP', 15.83), ('NE2', 'GLN', 'OD2', 'ASP', 15.77)], [('O', 'GLN', 'CB', 'ASP', 16.52), ('O', 'GLN', 'CG', 'ASP', 15.21), ('O', 'GLN', 'OD1', 'ASP', 15.03), ('O', 'GLN', 'OD2', 'ASP', 14.43)], [('C', 'GLN', 'CB', 'ASP', 15.75), ('C', 'GLN', 'CG', 'ASP', 14.4), ('C', 'GLN', 'OD1', 'ASP', 14.22), ('C', 'GLN', 'OD2', 'ASP', 13.59)], [('CA', 'GLN', 'CB', 'ASP', 14.86), ('CA', 'GLN', 'CG', 'ASP', 13.46), ('CA', 'GLN', 'OD1', 'ASP', 13.17), ('CA', 'GLN', 'OD2', 'ASP', 12.75)], [('N', 'GLN', 'CB', 'ASP', 13.63), ('N', 'GLN', 'CG', 'ASP', 12.23), ('N', 'GLN', 'OD1', 'ASP', 12.0), ('N', 'GLN', 'OD2', 'ASP', 11.45)]]}
LEU_SER = { 
	'distances':
		[[8.39, 7.81], [9.84, 9.13], [10.61, 9.94], [10.03, 9.09], [9.06, 9.01], [9.29, 9.16], [8.38, 8.12], [7.12, 7.08]],
	'comparisons':
		[[('CB', 'LEU', 'CB', 'SER', 8.39), ('CB', 'LEU', 'OG', 'SER', 7.81)], [('CG', 'LEU', 'CB', 'SER', 9.84), ('CG', 'LEU', 'OG', 'SER', 9.13)], [('CD1', 'LEU', 'CB', 'SER', 10.61), ('CD1', 'LEU', 'OG', 'SER', 9.94)], [('CD2', 'LEU', 'CB', 'SER', 10.03), ('CD2', 'LEU', 'OG', 'SER', 9.09)], [('O', 'LEU', 'CB', 'SER', 9.06), ('O', 'LEU', 'OG', 'SER', 9.01)], [('C', 'LEU', 'CB', 'SER', 9.29), ('C', 'LEU', 'OG', 'SER', 9.16)], [('CA', 'LEU', 'CB', 'SER', 8.38), ('CA', 'LEU', 'OG', 'SER', 8.12)], [('N', 'LEU', 'CB', 'SER', 7.12), ('N', 'LEU', 'OG', 'SER', 7.08)]]}
LEU_GLN = { 
	'distances':
		[[6.51, 6.35, 5.86, 6.3, 5.65, 9.72, 8.9, 7.78, 7.87], [7.57, 7.04, 6.23, 6.25, 6.16, 10.7, 10.01, 8.91, 9.19], [7.51, 6.82, 5.63, 5.42, 5.46, 10.41, 9.88, 8.97, 9.52], [8.0, 7.24, 6.65, 6.44, 6.99, 11.04, 10.42, 9.18, 9.46], [8.53, 8.92, 8.48, 9.11, 7.78, 11.57, 10.54, 9.65, 9.32], [7.94, 8.21, 7.57, 8.15, 6.78, 10.98, 10.04, 9.21, 9.11], [6.48, 6.7, 6.13, 6.81, 5.42, 9.56, 8.66, 7.79, 7.83], [5.81, 6.47, 6.32, 7.27, 5.63, 8.77, 7.74, 6.92, 6.71]],
	'comparisons':
		[[('CB', 'LEU', 'CB', 'GLN', 6.51), ('CB', 'LEU', 'CG', 'GLN', 6.35), ('CB', 'LEU', 'CD', 'GLN', 5.86), ('CB', 'LEU', 'OE1', 'GLN', 6.3), ('CB', 'LEU', 'NE2', 'GLN', 5.65), ('CB', 'LEU', 'O', 'GLN', 9.72), ('CB', 'LEU', 'C', 'GLN', 8.9), ('CB', 'LEU', 'CA', 'GLN', 7.78), ('CB', 'LEU', 'N', 'GLN', 7.87)], [('CG', 'LEU', 'CB', 'GLN', 7.57), ('CG', 'LEU', 'CG', 'GLN', 7.04), ('CG', 'LEU', 'CD', 'GLN', 6.23), ('CG', 'LEU', 'OE1', 'GLN', 6.25), ('CG', 'LEU', 'NE2', 'GLN', 6.16), ('CG', 'LEU', 'O', 'GLN', 10.7), ('CG', 'LEU', 'C', 'GLN', 10.01), ('CG', 'LEU', 'CA', 'GLN', 8.91), ('CG', 'LEU', 'N', 'GLN', 9.19)], [('CD1', 'LEU', 'CB', 'GLN', 7.51), ('CD1', 'LEU', 'CG', 'GLN', 6.82), ('CD1', 'LEU', 'CD', 'GLN', 5.63), ('CD1', 'LEU', 'OE1', 'GLN', 5.42), ('CD1', 'LEU', 'NE2', 'GLN', 5.46), ('CD1', 'LEU', 'O', 'GLN', 10.41), ('CD1', 'LEU', 'C', 'GLN', 9.88), ('CD1', 'LEU', 'CA', 'GLN', 8.97), ('CD1', 'LEU', 'N', 'GLN', 9.52)], [('CD2', 'LEU', 'CB', 'GLN', 8.0), ('CD2', 'LEU', 'CG', 'GLN', 7.24), ('CD2', 'LEU', 'CD', 'GLN', 6.65), ('CD2', 'LEU', 'OE1', 'GLN', 6.44), ('CD2', 'LEU', 'NE2', 'GLN', 6.99), ('CD2', 'LEU', 'O', 'GLN', 11.04), ('CD2', 'LEU', 'C', 'GLN', 10.42), ('CD2', 'LEU', 'CA', 'GLN', 9.18), ('CD2', 'LEU', 'N', 'GLN', 9.46)], [('O', 'LEU', 'CB', 'GLN', 8.53), ('O', 'LEU', 'CG', 'GLN', 8.92), ('O', 'LEU', 'CD', 'GLN', 8.48), ('O', 'LEU', 'OE1', 'GLN', 9.11), ('O', 'LEU', 'NE2', 'GLN', 7.78), ('O', 'LEU', 'O', 'GLN', 11.57), ('O', 'LEU', 'C', 'GLN', 10.54), ('O', 'LEU', 'CA', 'GLN', 9.65), ('O', 'LEU', 'N', 'GLN', 9.32)], [('C', 'LEU', 'CB', 'GLN', 7.94), ('C', 'LEU', 'CG', 'GLN', 8.21), ('C', 'LEU', 'CD', 'GLN', 7.57), ('C', 'LEU', 'OE1', 'GLN', 8.15), ('C', 'LEU', 'NE2', 'GLN', 6.78), ('C', 'LEU', 'O', 'GLN', 10.98), ('C', 'LEU', 'C', 'GLN', 10.04), ('C', 'LEU', 'CA', 'GLN', 9.21), ('C', 'LEU', 'N', 'GLN', 9.11)], [('CA', 'LEU', 'CB', 'GLN', 6.48), ('CA', 'LEU', 'CG', 'GLN', 6.7), ('CA', 'LEU', 'CD', 'GLN', 6.13), ('CA', 'LEU', 'OE1', 'GLN', 6.81), ('CA', 'LEU', 'NE2', 'GLN', 5.42), ('CA', 'LEU', 'O', 'GLN', 9.56), ('CA', 'LEU', 'C', 'GLN', 8.66), ('CA', 'LEU', 'CA', 'GLN', 7.79), ('CA', 'LEU', 'N', 'GLN', 7.83)], [('N', 'LEU', 'CB', 'GLN', 5.81), ('N', 'LEU', 'CG', 'GLN', 6.47), ('N', 'LEU', 'CD', 'GLN', 6.32), ('N', 'LEU', 'OE1', 'GLN', 7.27), ('N', 'LEU', 'NE2', 'GLN', 5.63), ('N', 'LEU', 'O', 'GLN', 8.77), ('N', 'LEU', 'C', 'GLN', 7.74), ('N', 'LEU', 'CA', 'GLN', 6.92), ('N', 'LEU', 'N', 'GLN', 6.71)]]}
LEU_ASP = { 
	'distances':
		[[16.07, 14.55, 13.86, 14.16], [17.15, 15.65, 14.86, 15.35], [18.4, 16.9, 16.15, 16.55], [16.64, 15.18, 14.3, 15.0], [16.3, 14.81, 14.23, 14.34], [17.05, 15.54, 14.95, 15.05], [16.58, 15.06, 14.48, 14.55], [15.66, 14.15, 13.67, 13.54]],
	'comparisons':
		[[('CB', 'LEU', 'CB', 'ASP', 16.07), ('CB', 'LEU', 'CG', 'ASP', 14.55), ('CB', 'LEU', 'OD1', 'ASP', 13.86), ('CB', 'LEU', 'OD2', 'ASP', 14.16)], [('CG', 'LEU', 'CB', 'ASP', 17.15), ('CG', 'LEU', 'CG', 'ASP', 15.65), ('CG', 'LEU', 'OD1', 'ASP', 14.86), ('CG', 'LEU', 'OD2', 'ASP', 15.35)], [('CD1', 'LEU', 'CB', 'ASP', 18.4), ('CD1', 'LEU', 'CG', 'ASP', 16.9), ('CD1', 'LEU', 'OD1', 'ASP', 16.15), ('CD1', 'LEU', 'OD2', 'ASP', 16.55)], [('CD2', 'LEU', 'CB', 'ASP', 16.64), ('CD2', 'LEU', 'CG', 'ASP', 15.18), ('CD2', 'LEU', 'OD1', 'ASP', 14.3), ('CD2', 'LEU', 'OD2', 'ASP', 15.0)], [('O', 'LEU', 'CB', 'ASP', 16.3), ('O', 'LEU', 'CG', 'ASP', 14.81), ('O', 'LEU', 'OD1', 'ASP', 14.23), ('O', 'LEU', 'OD2', 'ASP', 14.34)], [('C', 'LEU', 'CB', 'ASP', 17.05), ('C', 'LEU', 'CG', 'ASP', 15.54), ('C', 'LEU', 'OD1', 'ASP', 14.95), ('C', 'LEU', 'OD2', 'ASP', 15.05)], [('CA', 'LEU', 'CB', 'ASP', 16.58), ('CA', 'LEU', 'CG', 'ASP', 15.06), ('CA', 'LEU', 'OD1', 'ASP', 14.48), ('CA', 'LEU', 'OD2', 'ASP', 14.55)], [('N', 'LEU', 'CB', 'ASP', 15.66), ('N', 'LEU', 'CG', 'ASP', 14.15), ('N', 'LEU', 'OD1', 'ASP', 13.67), ('N', 'LEU', 'OD2', 'ASP', 13.54)]]}
SER_HIS = { 
	'distances':
		[[8.99, 7.49, 6.97, 6.66, 5.68, 5.39], [9.2, 7.7, 7.14, 6.88, 5.84, 5.58]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 8.99), ('CB', 'SER', 'CG', 'HIS', 7.49), ('CB', 'SER', 'ND1', 'HIS', 6.97), ('CB', 'SER', 'CD2', 'HIS', 6.66), ('CB', 'SER', 'CE1', 'HIS', 5.68), ('CB', 'SER', 'NE2', 'HIS', 5.39)], [('OG', 'SER', 'CB', 'HIS', 9.2), ('OG', 'SER', 'CG', 'HIS', 7.7), ('OG', 'SER', 'ND1', 'HIS', 7.14), ('OG', 'SER', 'CD2', 'HIS', 6.88), ('OG', 'SER', 'CE1', 'HIS', 5.84), ('OG', 'SER', 'NE2', 'HIS', 5.58)]]}
SER_ASP = { 
	'distances':
		[[11.42, 9.99, 9.83, 9.17], [11.41, 9.95, 9.6, 9.3]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 11.42), ('CB', 'SER', 'CG', 'ASP', 9.99), ('CB', 'SER', 'OD1', 'ASP', 9.83), ('CB', 'SER', 'OD2', 'ASP', 9.17)], [('OG', 'SER', 'CB', 'ASP', 11.41), ('OG', 'SER', 'CG', 'ASP', 9.95), ('OG', 'SER', 'OD1', 'ASP', 9.6), ('OG', 'SER', 'OD2', 'ASP', 9.3)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLN_HIS, d, 'P_1aur_3_1_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'P_1aur_3_1_1_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_GLN, d, 'P_1aur_3_1_1_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(LEU_HIS, d, 'P_1aur_3_1_1_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLN_ASP, d, 'P_1aur_3_1_1_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(LEU_SER, d, 'P_1aur_3_1_1_1')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(LEU_GLN, d, 'P_1aur_3_1_1_1')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(LEU_ASP, d, 'P_1aur_3_1_1_1')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(SER_HIS, d, 'P_1aur_3_1_1_1')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(SER_ASP, d, 'P_1aur_3_1_1_1')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLN_HIS' :  match1,
		'ASP_HIS' :  match2,
		'SER_GLN' :  match3,
		'LEU_HIS' :  match4,
		'GLN_ASP' :  match5,
		'LEU_SER' :  match6,
		'LEU_GLN' :  match7,
		'LEU_ASP' :  match8,
		'SER_HIS' :  match9,
		'SER_ASP' :  match10}