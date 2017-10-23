'''
FUNC:A_1bs9_3_1_1_6
PDB:1bs9
EC:3.1.1.6
RESI:thr,ser,gln,asp,his
LOCI:a-13,90,91,175,187;
'''
import motifFunctions as cmd
GLN_ASP = { 
	'distances':
		[[15.77, 14.35, 13.68, 13.94], [16.97, 15.58, 14.87, 15.23], [18.01, 16.6, 15.83, 16.29], [19.16, 17.76, 16.98, 17.46], [17.87, 16.43, 15.63, 16.14], [16.62, 15.3, 14.82, 14.79], [15.88, 14.52, 14.05, 13.97], [14.95, 13.56, 12.99, 13.11], [13.75, 12.34, 11.82, 11.81]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'ASP', 15.77), ('CB', 'GLN', 'CG', 'ASP', 14.35), ('CB', 'GLN', 'OD1', 'ASP', 13.68), ('CB', 'GLN', 'OD2', 'ASP', 13.94)], [('CG', 'GLN', 'CB', 'ASP', 16.97), ('CG', 'GLN', 'CG', 'ASP', 15.58), ('CG', 'GLN', 'OD1', 'ASP', 14.87), ('CG', 'GLN', 'OD2', 'ASP', 15.23)], [('CD', 'GLN', 'CB', 'ASP', 18.01), ('CD', 'GLN', 'CG', 'ASP', 16.6), ('CD', 'GLN', 'OD1', 'ASP', 15.83), ('CD', 'GLN', 'OD2', 'ASP', 16.29)], [('OE1', 'GLN', 'CB', 'ASP', 19.16), ('OE1', 'GLN', 'CG', 'ASP', 17.76), ('OE1', 'GLN', 'OD1', 'ASP', 16.98), ('OE1', 'GLN', 'OD2', 'ASP', 17.46)], [('NE2', 'GLN', 'CB', 'ASP', 17.87), ('NE2', 'GLN', 'CG', 'ASP', 16.43), ('NE2', 'GLN', 'OD1', 'ASP', 15.63), ('NE2', 'GLN', 'OD2', 'ASP', 16.14)], [('O', 'GLN', 'CB', 'ASP', 16.62), ('O', 'GLN', 'CG', 'ASP', 15.3), ('O', 'GLN', 'OD1', 'ASP', 14.82), ('O', 'GLN', 'OD2', 'ASP', 14.79)], [('C', 'GLN', 'CB', 'ASP', 15.88), ('C', 'GLN', 'CG', 'ASP', 14.52), ('C', 'GLN', 'OD1', 'ASP', 14.05), ('C', 'GLN', 'OD2', 'ASP', 13.97)], [('CA', 'GLN', 'CB', 'ASP', 14.95), ('CA', 'GLN', 'CG', 'ASP', 13.56), ('CA', 'GLN', 'OD1', 'ASP', 12.99), ('CA', 'GLN', 'OD2', 'ASP', 13.11)], [('N', 'GLN', 'CB', 'ASP', 13.75), ('N', 'GLN', 'CG', 'ASP', 12.34), ('N', 'GLN', 'OD1', 'ASP', 11.82), ('N', 'GLN', 'OD2', 'ASP', 11.81)]]}
GLN_HIS = { 
	'distances':
		[[13.33, 11.88, 11.55, 10.78, 10.28, 9.73], [14.73, 13.28, 12.91, 12.19, 11.63, 11.13], [15.54, 14.12, 13.88, 12.97, 12.62, 12.01], [16.78, 15.36, 15.09, 14.21, 13.83, 13.24], [15.1, 13.73, 13.63, 12.52, 12.43, 11.69], [14.9, 13.42, 12.8, 12.54, 11.5, 11.31], [13.87, 12.4, 11.85, 11.46, 10.57, 10.28], [12.87, 11.39, 10.89, 10.42, 9.59, 9.24], [11.5, 10.02, 9.55, 9.07, 8.26, 7.89]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'HIS', 13.33), ('CB', 'GLN', 'CG', 'HIS', 11.88), ('CB', 'GLN', 'ND1', 'HIS', 11.55), ('CB', 'GLN', 'CD2', 'HIS', 10.78), ('CB', 'GLN', 'CE1', 'HIS', 10.28), ('CB', 'GLN', 'NE2', 'HIS', 9.73)], [('CG', 'GLN', 'CB', 'HIS', 14.73), ('CG', 'GLN', 'CG', 'HIS', 13.28), ('CG', 'GLN', 'ND1', 'HIS', 12.91), ('CG', 'GLN', 'CD2', 'HIS', 12.19), ('CG', 'GLN', 'CE1', 'HIS', 11.63), ('CG', 'GLN', 'NE2', 'HIS', 11.13)], [('CD', 'GLN', 'CB', 'HIS', 15.54), ('CD', 'GLN', 'CG', 'HIS', 14.12), ('CD', 'GLN', 'ND1', 'HIS', 13.88), ('CD', 'GLN', 'CD2', 'HIS', 12.97), ('CD', 'GLN', 'CE1', 'HIS', 12.62), ('CD', 'GLN', 'NE2', 'HIS', 12.01)], [('OE1', 'GLN', 'CB', 'HIS', 16.78), ('OE1', 'GLN', 'CG', 'HIS', 15.36), ('OE1', 'GLN', 'ND1', 'HIS', 15.09), ('OE1', 'GLN', 'CD2', 'HIS', 14.21), ('OE1', 'GLN', 'CE1', 'HIS', 13.83), ('OE1', 'GLN', 'NE2', 'HIS', 13.24)], [('NE2', 'GLN', 'CB', 'HIS', 15.1), ('NE2', 'GLN', 'CG', 'HIS', 13.73), ('NE2', 'GLN', 'ND1', 'HIS', 13.63), ('NE2', 'GLN', 'CD2', 'HIS', 12.52), ('NE2', 'GLN', 'CE1', 'HIS', 12.43), ('NE2', 'GLN', 'NE2', 'HIS', 11.69)], [('O', 'GLN', 'CB', 'HIS', 14.9), ('O', 'GLN', 'CG', 'HIS', 13.42), ('O', 'GLN', 'ND1', 'HIS', 12.8), ('O', 'GLN', 'CD2', 'HIS', 12.54), ('O', 'GLN', 'CE1', 'HIS', 11.5), ('O', 'GLN', 'NE2', 'HIS', 11.31)], [('C', 'GLN', 'CB', 'HIS', 13.87), ('C', 'GLN', 'CG', 'HIS', 12.4), ('C', 'GLN', 'ND1', 'HIS', 11.85), ('C', 'GLN', 'CD2', 'HIS', 11.46), ('C', 'GLN', 'CE1', 'HIS', 10.57), ('C', 'GLN', 'NE2', 'HIS', 10.28)], [('CA', 'GLN', 'CB', 'HIS', 12.87), ('CA', 'GLN', 'CG', 'HIS', 11.39), ('CA', 'GLN', 'ND1', 'HIS', 10.89), ('CA', 'GLN', 'CD2', 'HIS', 10.42), ('CA', 'GLN', 'CE1', 'HIS', 9.59), ('CA', 'GLN', 'NE2', 'HIS', 9.24)], [('N', 'GLN', 'CB', 'HIS', 11.5), ('N', 'GLN', 'CG', 'HIS', 10.02), ('N', 'GLN', 'ND1', 'HIS', 9.55), ('N', 'GLN', 'CD2', 'HIS', 9.07), ('N', 'GLN', 'CE1', 'HIS', 8.26), ('N', 'GLN', 'NE2', 'HIS', 7.89)]]}
ASP_HIS = { 
	'distances':
		[[7.03, 7.43, 6.81, 8.68, 7.81, 8.81], [5.92, 6.06, 5.35, 7.26, 6.33, 7.33], [5.96, 5.88, 5.19, 6.91, 5.98, 6.9], [5.43, 5.5, 4.73, 6.73, 5.77, 6.78]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 7.03), ('CB', 'ASP', 'CG', 'HIS', 7.43), ('CB', 'ASP', 'ND1', 'HIS', 6.81), ('CB', 'ASP', 'CD2', 'HIS', 8.68), ('CB', 'ASP', 'CE1', 'HIS', 7.81), ('CB', 'ASP', 'NE2', 'HIS', 8.81)], [('CG', 'ASP', 'CB', 'HIS', 5.92), ('CG', 'ASP', 'CG', 'HIS', 6.06), ('CG', 'ASP', 'ND1', 'HIS', 5.35), ('CG', 'ASP', 'CD2', 'HIS', 7.26), ('CG', 'ASP', 'CE1', 'HIS', 6.33), ('CG', 'ASP', 'NE2', 'HIS', 7.33)], [('OD1', 'ASP', 'CB', 'HIS', 5.96), ('OD1', 'ASP', 'CG', 'HIS', 5.88), ('OD1', 'ASP', 'ND1', 'HIS', 5.19), ('OD1', 'ASP', 'CD2', 'HIS', 6.91), ('OD1', 'ASP', 'CE1', 'HIS', 5.98), ('OD1', 'ASP', 'NE2', 'HIS', 6.9)], [('OD2', 'ASP', 'CB', 'HIS', 5.43), ('OD2', 'ASP', 'CG', 'HIS', 5.5), ('OD2', 'ASP', 'ND1', 'HIS', 4.73), ('OD2', 'ASP', 'CD2', 'HIS', 6.73), ('OD2', 'ASP', 'CE1', 'HIS', 5.77), ('OD2', 'ASP', 'NE2', 'HIS', 6.78)]]}
THR_HIS = { 
	'distances':
		[[12.67, 11.51, 11.84, 10.18, 10.88, 9.8], [12.52, 11.25, 11.38, 9.97, 10.31, 9.37], [13.84, 12.73, 13.08, 11.43, 12.15, 11.09], [12.5, 11.58, 12.23, 10.25, 11.5, 10.26], [13.39, 12.37, 12.9, 11.03, 12.07, 10.88], [13.13, 11.97, 12.33, 10.63, 11.37, 10.26], [12.33, 11.13, 11.42, 9.81, 10.43, 9.36]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'HIS', 12.67), ('CB', 'THR', 'CG', 'HIS', 11.51), ('CB', 'THR', 'ND1', 'HIS', 11.84), ('CB', 'THR', 'CD2', 'HIS', 10.18), ('CB', 'THR', 'CE1', 'HIS', 10.88), ('CB', 'THR', 'NE2', 'HIS', 9.8)], [('OG1', 'THR', 'CB', 'HIS', 12.52), ('OG1', 'THR', 'CG', 'HIS', 11.25), ('OG1', 'THR', 'ND1', 'HIS', 11.38), ('OG1', 'THR', 'CD2', 'HIS', 9.97), ('OG1', 'THR', 'CE1', 'HIS', 10.31), ('OG1', 'THR', 'NE2', 'HIS', 9.37)], [('CG2', 'THR', 'CB', 'HIS', 13.84), ('CG2', 'THR', 'CG', 'HIS', 12.73), ('CG2', 'THR', 'ND1', 'HIS', 13.08), ('CG2', 'THR', 'CD2', 'HIS', 11.43), ('CG2', 'THR', 'CE1', 'HIS', 12.15), ('CG2', 'THR', 'NE2', 'HIS', 11.09)], [('O', 'THR', 'CB', 'HIS', 12.5), ('O', 'THR', 'CG', 'HIS', 11.58), ('O', 'THR', 'ND1', 'HIS', 12.23), ('O', 'THR', 'CD2', 'HIS', 10.25), ('O', 'THR', 'CE1', 'HIS', 11.5), ('O', 'THR', 'NE2', 'HIS', 10.26)], [('C', 'THR', 'CB', 'HIS', 13.39), ('C', 'THR', 'CG', 'HIS', 12.37), ('C', 'THR', 'ND1', 'HIS', 12.9), ('C', 'THR', 'CD2', 'HIS', 11.03), ('C', 'THR', 'CE1', 'HIS', 12.07), ('C', 'THR', 'NE2', 'HIS', 10.88)], [('CA', 'THR', 'CB', 'HIS', 13.13), ('CA', 'THR', 'CG', 'HIS', 11.97), ('CA', 'THR', 'ND1', 'HIS', 12.33), ('CA', 'THR', 'CD2', 'HIS', 10.63), ('CA', 'THR', 'CE1', 'HIS', 11.37), ('CA', 'THR', 'NE2', 'HIS', 10.26)], [('N', 'THR', 'CB', 'HIS', 12.33), ('N', 'THR', 'CG', 'HIS', 11.13), ('N', 'THR', 'ND1', 'HIS', 11.42), ('N', 'THR', 'CD2', 'HIS', 9.81), ('N', 'THR', 'CE1', 'HIS', 10.43), ('N', 'THR', 'NE2', 'HIS', 9.36)]]}
THR_ASP = { 
	'distances':
		[[16.31, 14.85, 14.07, 14.53], [15.77, 14.31, 13.51, 14.02], [17.41, 15.98, 15.13, 15.74], [16.86, 15.41, 14.81, 14.93], [17.56, 16.1, 15.45, 15.63], [16.98, 15.5, 14.83, 15.04], [16.15, 14.67, 14.09, 14.12]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ASP', 16.31), ('CB', 'THR', 'CG', 'ASP', 14.85), ('CB', 'THR', 'OD1', 'ASP', 14.07), ('CB', 'THR', 'OD2', 'ASP', 14.53)], [('OG1', 'THR', 'CB', 'ASP', 15.77), ('OG1', 'THR', 'CG', 'ASP', 14.31), ('OG1', 'THR', 'OD1', 'ASP', 13.51), ('OG1', 'THR', 'OD2', 'ASP', 14.02)], [('CG2', 'THR', 'CB', 'ASP', 17.41), ('CG2', 'THR', 'CG', 'ASP', 15.98), ('CG2', 'THR', 'OD1', 'ASP', 15.13), ('CG2', 'THR', 'OD2', 'ASP', 15.74)], [('O', 'THR', 'CB', 'ASP', 16.86), ('O', 'THR', 'CG', 'ASP', 15.41), ('O', 'THR', 'OD1', 'ASP', 14.81), ('O', 'THR', 'OD2', 'ASP', 14.93)], [('C', 'THR', 'CB', 'ASP', 17.56), ('C', 'THR', 'CG', 'ASP', 16.1), ('C', 'THR', 'OD1', 'ASP', 15.45), ('C', 'THR', 'OD2', 'ASP', 15.63)], [('CA', 'THR', 'CB', 'ASP', 16.98), ('CA', 'THR', 'CG', 'ASP', 15.5), ('CA', 'THR', 'OD1', 'ASP', 14.83), ('CA', 'THR', 'OD2', 'ASP', 15.04)], [('N', 'THR', 'CB', 'ASP', 16.15), ('N', 'THR', 'CG', 'ASP', 14.67), ('N', 'THR', 'OD1', 'ASP', 14.09), ('N', 'THR', 'OD2', 'ASP', 14.12)]]}
THR_SER = { 
	'distances':
		[[8.44, 8.09], [7.76, 7.32], [9.88, 9.43], [9.17, 9.17], [9.43, 9.44], [8.48, 8.46], [7.26, 7.47]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'SER', 8.44), ('CB', 'THR', 'OG', 'SER', 8.09)], [('OG1', 'THR', 'CB', 'SER', 7.76), ('OG1', 'THR', 'OG', 'SER', 7.32)], [('CG2', 'THR', 'CB', 'SER', 9.88), ('CG2', 'THR', 'OG', 'SER', 9.43)], [('O', 'THR', 'CB', 'SER', 9.17), ('O', 'THR', 'OG', 'SER', 9.17)], [('C', 'THR', 'CB', 'SER', 9.43), ('C', 'THR', 'OG', 'SER', 9.44)], [('CA', 'THR', 'CB', 'SER', 8.48), ('CA', 'THR', 'OG', 'SER', 8.46)], [('N', 'THR', 'CB', 'SER', 7.26), ('N', 'THR', 'OG', 'SER', 7.47)]]}
THR_GLN = { 
	'distances':
		[[6.77, 7.49, 7.06, 8.08, 5.89, 9.95, 9.04, 8.01, 7.9], [5.51, 6.23, 5.99, 7.12, 4.97, 8.75, 7.89, 6.75, 6.77], [7.63, 8.01, 7.25, 8.07, 5.94, 10.81, 10.03, 9.01, 9.11], [8.98, 9.91, 9.58, 10.54, 8.49, 11.83, 10.77, 9.99, 9.53], [8.4, 9.16, 8.67, 9.54, 7.56, 11.25, 10.27, 9.55, 9.32], [6.89, 7.66, 7.25, 8.2, 6.19, 9.8, 8.85, 8.09, 7.97], [6.36, 7.41, 7.36, 8.42, 6.58, 9.03, 7.96, 7.29, 6.96]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'GLN', 6.77), ('CB', 'THR', 'CG', 'GLN', 7.49), ('CB', 'THR', 'CD', 'GLN', 7.06), ('CB', 'THR', 'OE1', 'GLN', 8.08), ('CB', 'THR', 'NE2', 'GLN', 5.89), ('CB', 'THR', 'O', 'GLN', 9.95), ('CB', 'THR', 'C', 'GLN', 9.04), ('CB', 'THR', 'CA', 'GLN', 8.01), ('CB', 'THR', 'N', 'GLN', 7.9)], [('OG1', 'THR', 'CB', 'GLN', 5.51), ('OG1', 'THR', 'CG', 'GLN', 6.23), ('OG1', 'THR', 'CD', 'GLN', 5.99), ('OG1', 'THR', 'OE1', 'GLN', 7.12), ('OG1', 'THR', 'NE2', 'GLN', 4.97), ('OG1', 'THR', 'O', 'GLN', 8.75), ('OG1', 'THR', 'C', 'GLN', 7.89), ('OG1', 'THR', 'CA', 'GLN', 6.75), ('OG1', 'THR', 'N', 'GLN', 6.77)], [('CG2', 'THR', 'CB', 'GLN', 7.63), ('CG2', 'THR', 'CG', 'GLN', 8.01), ('CG2', 'THR', 'CD', 'GLN', 7.25), ('CG2', 'THR', 'OE1', 'GLN', 8.07), ('CG2', 'THR', 'NE2', 'GLN', 5.94), ('CG2', 'THR', 'O', 'GLN', 10.81), ('CG2', 'THR', 'C', 'GLN', 10.03), ('CG2', 'THR', 'CA', 'GLN', 9.01), ('CG2', 'THR', 'N', 'GLN', 9.11)], [('O', 'THR', 'CB', 'GLN', 8.98), ('O', 'THR', 'CG', 'GLN', 9.91), ('O', 'THR', 'CD', 'GLN', 9.58), ('O', 'THR', 'OE1', 'GLN', 10.54), ('O', 'THR', 'NE2', 'GLN', 8.49), ('O', 'THR', 'O', 'GLN', 11.83), ('O', 'THR', 'C', 'GLN', 10.77), ('O', 'THR', 'CA', 'GLN', 9.99), ('O', 'THR', 'N', 'GLN', 9.53)], [('C', 'THR', 'CB', 'GLN', 8.4), ('C', 'THR', 'CG', 'GLN', 9.16), ('C', 'THR', 'CD', 'GLN', 8.67), ('C', 'THR', 'OE1', 'GLN', 9.54), ('C', 'THR', 'NE2', 'GLN', 7.56), ('C', 'THR', 'O', 'GLN', 11.25), ('C', 'THR', 'C', 'GLN', 10.27), ('C', 'THR', 'CA', 'GLN', 9.55), ('C', 'THR', 'N', 'GLN', 9.32)], [('CA', 'THR', 'CB', 'GLN', 6.89), ('CA', 'THR', 'CG', 'GLN', 7.66), ('CA', 'THR', 'CD', 'GLN', 7.25), ('CA', 'THR', 'OE1', 'GLN', 8.2), ('CA', 'THR', 'NE2', 'GLN', 6.19), ('CA', 'THR', 'O', 'GLN', 9.8), ('CA', 'THR', 'C', 'GLN', 8.85), ('CA', 'THR', 'CA', 'GLN', 8.09), ('CA', 'THR', 'N', 'GLN', 7.97)], [('N', 'THR', 'CB', 'GLN', 6.36), ('N', 'THR', 'CG', 'GLN', 7.41), ('N', 'THR', 'CD', 'GLN', 7.36), ('N', 'THR', 'OE1', 'GLN', 8.42), ('N', 'THR', 'NE2', 'GLN', 6.58), ('N', 'THR', 'O', 'GLN', 9.03), ('N', 'THR', 'C', 'GLN', 7.96), ('N', 'THR', 'CA', 'GLN', 7.29), ('N', 'THR', 'N', 'GLN', 6.96)]]}
SER_HIS = { 
	'distances':
		[[8.88, 7.45, 7.13, 6.51, 5.97, 5.45], [8.42, 6.94, 6.6, 5.97, 5.36, 4.79]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 8.88), ('CB', 'SER', 'CG', 'HIS', 7.45), ('CB', 'SER', 'ND1', 'HIS', 7.13), ('CB', 'SER', 'CD2', 'HIS', 6.51), ('CB', 'SER', 'CE1', 'HIS', 5.97), ('CB', 'SER', 'NE2', 'HIS', 5.45)], [('OG', 'SER', 'CB', 'HIS', 8.42), ('OG', 'SER', 'CG', 'HIS', 6.94), ('OG', 'SER', 'ND1', 'HIS', 6.6), ('OG', 'SER', 'CD2', 'HIS', 5.97), ('OG', 'SER', 'CE1', 'HIS', 5.36), ('OG', 'SER', 'NE2', 'HIS', 4.79)]]}
GLN_SER = { 
	'distances':
		[[7.01, 6.99], [8.49, 8.4], [9.52, 9.37], [10.7, 10.58], [9.44, 9.2], [8.22, 8.6], [7.1, 7.55], [6.34, 6.46], [4.89, 5.13]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'SER', 7.01), ('CB', 'GLN', 'OG', 'SER', 6.99)], [('CG', 'GLN', 'CB', 'SER', 8.49), ('CG', 'GLN', 'OG', 'SER', 8.4)], [('CD', 'GLN', 'CB', 'SER', 9.52), ('CD', 'GLN', 'OG', 'SER', 9.37)], [('OE1', 'GLN', 'CB', 'SER', 10.7), ('OE1', 'GLN', 'OG', 'SER', 10.58)], [('NE2', 'GLN', 'CB', 'SER', 9.44), ('NE2', 'GLN', 'OG', 'SER', 9.2)], [('O', 'GLN', 'CB', 'SER', 8.22), ('O', 'GLN', 'OG', 'SER', 8.6)], [('C', 'GLN', 'CB', 'SER', 7.1), ('C', 'GLN', 'OG', 'SER', 7.55)], [('CA', 'GLN', 'CB', 'SER', 6.34), ('CA', 'GLN', 'OG', 'SER', 6.46)], [('N', 'GLN', 'CB', 'SER', 4.89), ('N', 'GLN', 'OG', 'SER', 5.13)]]}
SER_ASP = { 
	'distances':
		[[11.69, 10.24, 9.89, 9.54], [11.08, 9.61, 9.08, 9.1]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 11.69), ('CB', 'SER', 'CG', 'ASP', 10.24), ('CB', 'SER', 'OD1', 'ASP', 9.89), ('CB', 'SER', 'OD2', 'ASP', 9.54)], [('OG', 'SER', 'CB', 'ASP', 11.08), ('OG', 'SER', 'CG', 'ASP', 9.61), ('OG', 'SER', 'OD1', 'ASP', 9.08), ('OG', 'SER', 'OD2', 'ASP', 9.1)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLN_ASP, d, 'A_1bs9_3_1_1_6')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLN_HIS, d, 'A_1bs9_3_1_1_6')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_HIS, d, 'A_1bs9_3_1_1_6')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(THR_HIS, d, 'A_1bs9_3_1_1_6')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(THR_ASP, d, 'A_1bs9_3_1_1_6')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(THR_SER, d, 'A_1bs9_3_1_1_6')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(THR_GLN, d, 'A_1bs9_3_1_1_6')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(SER_HIS, d, 'A_1bs9_3_1_1_6')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(GLN_SER, d, 'A_1bs9_3_1_1_6')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(SER_ASP, d, 'A_1bs9_3_1_1_6')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLN_ASP' :  match1,
		'GLN_HIS' :  match2,
		'ASP_HIS' :  match3,
		'THR_HIS' :  match4,
		'THR_ASP' :  match5,
		'THR_SER' :  match6,
		'THR_GLN' :  match7,
		'SER_HIS' :  match8,
		'GLN_SER' :  match9,
		'SER_ASP' :  match10}