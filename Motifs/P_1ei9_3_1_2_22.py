'''
FUNC:P_1ei9_3_1_2_22
PDB:1ei9
EC:3.1.2.22
RESI:met,ser,gln,asp,his
LOCI:a-41,115,116,233,289;
'''
import motifFunctions as cmd
MET_SER = { 
	'distances':
		[[8.1, 7.89], [9.54, 9.21], [10.04, 9.43], [10.53, 10.02], [8.37, 8.4], [8.77, 8.86], [8.06, 8.18], [6.84, 7.19]],
	'comparisons':
		[[('CB', 'MET', 'CB', 'SER', 8.1), ('CB', 'MET', 'OG', 'SER', 7.89)], [('CG', 'MET', 'CB', 'SER', 9.54), ('CG', 'MET', 'OG', 'SER', 9.21)], [('SD', 'MET', 'CB', 'SER', 10.04), ('SD', 'MET', 'OG', 'SER', 9.43)], [('CE', 'MET', 'CB', 'SER', 10.53), ('CE', 'MET', 'OG', 'SER', 10.02)], [('O', 'MET', 'CB', 'SER', 8.37), ('O', 'MET', 'OG', 'SER', 8.4)], [('C', 'MET', 'CB', 'SER', 8.77), ('C', 'MET', 'OG', 'SER', 8.86)], [('CA', 'MET', 'CB', 'SER', 8.06), ('CA', 'MET', 'OG', 'SER', 8.18)], [('N', 'MET', 'CB', 'SER', 6.84), ('N', 'MET', 'OG', 'SER', 7.19)]]}
GLN_HIS = { 
	'distances':
		[[13.24, 11.78, 11.34, 10.78, 10.04, 9.62], [13.52, 12.09, 11.83, 10.96, 10.55, 9.92], [14.19, 12.82, 12.67, 11.64, 11.44, 10.72], [14.1, 12.76, 12.6, 11.63, 11.41, 10.72], [15.03, 13.69, 13.64, 12.46, 12.43, 11.62], [14.89, 13.39, 12.7, 12.55, 11.39, 11.25], [13.81, 12.31, 11.7, 11.43, 10.38, 10.16], [12.73, 11.23, 10.64, 10.34, 9.32, 9.08], [11.39, 9.89, 9.36, 8.98, 8.03, 7.72]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'HIS', 13.24), ('CB', 'GLN', 'CG', 'HIS', 11.78), ('CB', 'GLN', 'ND1', 'HIS', 11.34), ('CB', 'GLN', 'CD2', 'HIS', 10.78), ('CB', 'GLN', 'CE1', 'HIS', 10.04), ('CB', 'GLN', 'NE2', 'HIS', 9.62)], [('CG', 'GLN', 'CB', 'HIS', 13.52), ('CG', 'GLN', 'CG', 'HIS', 12.09), ('CG', 'GLN', 'ND1', 'HIS', 11.83), ('CG', 'GLN', 'CD2', 'HIS', 10.96), ('CG', 'GLN', 'CE1', 'HIS', 10.55), ('CG', 'GLN', 'NE2', 'HIS', 9.92)], [('CD', 'GLN', 'CB', 'HIS', 14.19), ('CD', 'GLN', 'CG', 'HIS', 12.82), ('CD', 'GLN', 'ND1', 'HIS', 12.67), ('CD', 'GLN', 'CD2', 'HIS', 11.64), ('CD', 'GLN', 'CE1', 'HIS', 11.44), ('CD', 'GLN', 'NE2', 'HIS', 10.72)], [('OE1', 'GLN', 'CB', 'HIS', 14.1), ('OE1', 'GLN', 'CG', 'HIS', 12.76), ('OE1', 'GLN', 'ND1', 'HIS', 12.6), ('OE1', 'GLN', 'CD2', 'HIS', 11.63), ('OE1', 'GLN', 'CE1', 'HIS', 11.41), ('OE1', 'GLN', 'NE2', 'HIS', 10.72)], [('NE2', 'GLN', 'CB', 'HIS', 15.03), ('NE2', 'GLN', 'CG', 'HIS', 13.69), ('NE2', 'GLN', 'ND1', 'HIS', 13.64), ('NE2', 'GLN', 'CD2', 'HIS', 12.46), ('NE2', 'GLN', 'CE1', 'HIS', 12.43), ('NE2', 'GLN', 'NE2', 'HIS', 11.62)], [('O', 'GLN', 'CB', 'HIS', 14.89), ('O', 'GLN', 'CG', 'HIS', 13.39), ('O', 'GLN', 'ND1', 'HIS', 12.7), ('O', 'GLN', 'CD2', 'HIS', 12.55), ('O', 'GLN', 'CE1', 'HIS', 11.39), ('O', 'GLN', 'NE2', 'HIS', 11.25)], [('C', 'GLN', 'CB', 'HIS', 13.81), ('C', 'GLN', 'CG', 'HIS', 12.31), ('C', 'GLN', 'ND1', 'HIS', 11.7), ('C', 'GLN', 'CD2', 'HIS', 11.43), ('C', 'GLN', 'CE1', 'HIS', 10.38), ('C', 'GLN', 'NE2', 'HIS', 10.16)], [('CA', 'GLN', 'CB', 'HIS', 12.73), ('CA', 'GLN', 'CG', 'HIS', 11.23), ('CA', 'GLN', 'ND1', 'HIS', 10.64), ('CA', 'GLN', 'CD2', 'HIS', 10.34), ('CA', 'GLN', 'CE1', 'HIS', 9.32), ('CA', 'GLN', 'NE2', 'HIS', 9.08)], [('N', 'GLN', 'CB', 'HIS', 11.39), ('N', 'GLN', 'CG', 'HIS', 9.89), ('N', 'GLN', 'ND1', 'HIS', 9.36), ('N', 'GLN', 'CD2', 'HIS', 8.98), ('N', 'GLN', 'CE1', 'HIS', 8.03), ('N', 'GLN', 'NE2', 'HIS', 7.72)]]}
MET_GLN = { 
	'distances':
		[[7.27, 6.26, 5.57, 5.67, 5.56, 10.04, 9.18, 8.32, 8.01], [8.44, 7.48, 6.48, 6.33, 6.29, 11.28, 10.51, 9.63, 9.42], [8.62, 8.02, 6.94, 6.33, 7.09, 11.65, 10.95, 9.87, 9.75], [7.91, 7.41, 6.08, 5.25, 6.24, 10.82, 10.33, 9.35, 9.59], [9.54, 8.42, 8.2, 8.61, 7.96, 11.88, 10.83, 10.16, 9.41], [9.1, 7.85, 7.45, 7.91, 7.01, 11.44, 10.48, 9.89, 9.35], [7.64, 6.36, 5.92, 6.45, 5.55, 10.02, 9.11, 8.52, 8.15], [6.91, 5.65, 5.75, 6.49, 5.62, 9.02, 8.02, 7.52, 7.0]],
	'comparisons':
		[[('CB', 'MET', 'CB', 'GLN', 7.27), ('CB', 'MET', 'CG', 'GLN', 6.26), ('CB', 'MET', 'CD', 'GLN', 5.57), ('CB', 'MET', 'OE1', 'GLN', 5.67), ('CB', 'MET', 'NE2', 'GLN', 5.56), ('CB', 'MET', 'O', 'GLN', 10.04), ('CB', 'MET', 'C', 'GLN', 9.18), ('CB', 'MET', 'CA', 'GLN', 8.32), ('CB', 'MET', 'N', 'GLN', 8.01)], [('CG', 'MET', 'CB', 'GLN', 8.44), ('CG', 'MET', 'CG', 'GLN', 7.48), ('CG', 'MET', 'CD', 'GLN', 6.48), ('CG', 'MET', 'OE1', 'GLN', 6.33), ('CG', 'MET', 'NE2', 'GLN', 6.29), ('CG', 'MET', 'O', 'GLN', 11.28), ('CG', 'MET', 'C', 'GLN', 10.51), ('CG', 'MET', 'CA', 'GLN', 9.63), ('CG', 'MET', 'N', 'GLN', 9.42)], [('SD', 'MET', 'CB', 'GLN', 8.62), ('SD', 'MET', 'CG', 'GLN', 8.02), ('SD', 'MET', 'CD', 'GLN', 6.94), ('SD', 'MET', 'OE1', 'GLN', 6.33), ('SD', 'MET', 'NE2', 'GLN', 7.09), ('SD', 'MET', 'O', 'GLN', 11.65), ('SD', 'MET', 'C', 'GLN', 10.95), ('SD', 'MET', 'CA', 'GLN', 9.87), ('SD', 'MET', 'N', 'GLN', 9.75)], [('CE', 'MET', 'CB', 'GLN', 7.91), ('CE', 'MET', 'CG', 'GLN', 7.41), ('CE', 'MET', 'CD', 'GLN', 6.08), ('CE', 'MET', 'OE1', 'GLN', 5.25), ('CE', 'MET', 'NE2', 'GLN', 6.24), ('CE', 'MET', 'O', 'GLN', 10.82), ('CE', 'MET', 'C', 'GLN', 10.33), ('CE', 'MET', 'CA', 'GLN', 9.35), ('CE', 'MET', 'N', 'GLN', 9.59)], [('O', 'MET', 'CB', 'GLN', 9.54), ('O', 'MET', 'CG', 'GLN', 8.42), ('O', 'MET', 'CD', 'GLN', 8.2), ('O', 'MET', 'OE1', 'GLN', 8.61), ('O', 'MET', 'NE2', 'GLN', 7.96), ('O', 'MET', 'O', 'GLN', 11.88), ('O', 'MET', 'C', 'GLN', 10.83), ('O', 'MET', 'CA', 'GLN', 10.16), ('O', 'MET', 'N', 'GLN', 9.41)], [('C', 'MET', 'CB', 'GLN', 9.1), ('C', 'MET', 'CG', 'GLN', 7.85), ('C', 'MET', 'CD', 'GLN', 7.45), ('C', 'MET', 'OE1', 'GLN', 7.91), ('C', 'MET', 'NE2', 'GLN', 7.01), ('C', 'MET', 'O', 'GLN', 11.44), ('C', 'MET', 'C', 'GLN', 10.48), ('C', 'MET', 'CA', 'GLN', 9.89), ('C', 'MET', 'N', 'GLN', 9.35)], [('CA', 'MET', 'CB', 'GLN', 7.64), ('CA', 'MET', 'CG', 'GLN', 6.36), ('CA', 'MET', 'CD', 'GLN', 5.92), ('CA', 'MET', 'OE1', 'GLN', 6.45), ('CA', 'MET', 'NE2', 'GLN', 5.55), ('CA', 'MET', 'O', 'GLN', 10.02), ('CA', 'MET', 'C', 'GLN', 9.11), ('CA', 'MET', 'CA', 'GLN', 8.52), ('CA', 'MET', 'N', 'GLN', 8.15)], [('N', 'MET', 'CB', 'GLN', 6.91), ('N', 'MET', 'CG', 'GLN', 5.65), ('N', 'MET', 'CD', 'GLN', 5.75), ('N', 'MET', 'OE1', 'GLN', 6.49), ('N', 'MET', 'NE2', 'GLN', 5.62), ('N', 'MET', 'O', 'GLN', 9.02), ('N', 'MET', 'C', 'GLN', 8.02), ('N', 'MET', 'CA', 'GLN', 7.52), ('N', 'MET', 'N', 'GLN', 7.0)]]}
ASP_HIS = { 
	'distances':
		[[7.06, 7.59, 7.14, 8.86, 8.24, 9.17], [5.84, 6.18, 5.72, 7.39, 6.8, 7.69], [5.56, 5.96, 5.79, 7.05, 6.82, 7.47], [5.64, 5.65, 4.89, 6.86, 5.92, 6.96]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 7.06), ('CB', 'ASP', 'CG', 'HIS', 7.59), ('CB', 'ASP', 'ND1', 'HIS', 7.14), ('CB', 'ASP', 'CD2', 'HIS', 8.86), ('CB', 'ASP', 'CE1', 'HIS', 8.24), ('CB', 'ASP', 'NE2', 'HIS', 9.17)], [('CG', 'ASP', 'CB', 'HIS', 5.84), ('CG', 'ASP', 'CG', 'HIS', 6.18), ('CG', 'ASP', 'ND1', 'HIS', 5.72), ('CG', 'ASP', 'CD2', 'HIS', 7.39), ('CG', 'ASP', 'CE1', 'HIS', 6.8), ('CG', 'ASP', 'NE2', 'HIS', 7.69)], [('OD1', 'ASP', 'CB', 'HIS', 5.56), ('OD1', 'ASP', 'CG', 'HIS', 5.96), ('OD1', 'ASP', 'ND1', 'HIS', 5.79), ('OD1', 'ASP', 'CD2', 'HIS', 7.05), ('OD1', 'ASP', 'CE1', 'HIS', 6.82), ('OD1', 'ASP', 'NE2', 'HIS', 7.47)], [('OD2', 'ASP', 'CB', 'HIS', 5.64), ('OD2', 'ASP', 'CG', 'HIS', 5.65), ('OD2', 'ASP', 'ND1', 'HIS', 4.89), ('OD2', 'ASP', 'CD2', 'HIS', 6.86), ('OD2', 'ASP', 'CE1', 'HIS', 5.92), ('OD2', 'ASP', 'NE2', 'HIS', 6.96)]]}
SER_GLN = { 
	'distances':
		[[6.94, 7.02, 8.15, 8.55, 8.95, 8.21, 7.01, 6.24, 4.78], [7.08, 7.32, 8.24, 8.38, 9.16, 8.81, 7.68, 6.58, 5.22]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLN', 6.94), ('CB', 'SER', 'CG', 'GLN', 7.02), ('CB', 'SER', 'CD', 'GLN', 8.15), ('CB', 'SER', 'OE1', 'GLN', 8.55), ('CB', 'SER', 'NE2', 'GLN', 8.95), ('CB', 'SER', 'O', 'GLN', 8.21), ('CB', 'SER', 'C', 'GLN', 7.01), ('CB', 'SER', 'CA', 'GLN', 6.24), ('CB', 'SER', 'N', 'GLN', 4.78)], [('OG', 'SER', 'CB', 'GLN', 7.08), ('OG', 'SER', 'CG', 'GLN', 7.32), ('OG', 'SER', 'CD', 'GLN', 8.24), ('OG', 'SER', 'OE1', 'GLN', 8.38), ('OG', 'SER', 'NE2', 'GLN', 9.16), ('OG', 'SER', 'O', 'GLN', 8.81), ('OG', 'SER', 'C', 'GLN', 7.68), ('OG', 'SER', 'CA', 'GLN', 6.58), ('OG', 'SER', 'N', 'GLN', 5.22)]]}
GLN_ASP = { 
	'distances':
		[[15.63, 14.25, 14.0, 13.51], [16.4, 14.96, 14.65, 14.23], [17.13, 15.68, 15.25, 15.05], [16.81, 15.37, 14.88, 14.84], [18.23, 16.75, 16.3, 16.13], [16.88, 15.61, 15.63, 14.69], [16.07, 14.75, 14.74, 13.83], [14.95, 13.6, 13.5, 12.76], [13.88, 12.51, 12.42, 11.63]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'ASP', 15.63), ('CB', 'GLN', 'CG', 'ASP', 14.25), ('CB', 'GLN', 'OD1', 'ASP', 14.0), ('CB', 'GLN', 'OD2', 'ASP', 13.51)], [('CG', 'GLN', 'CB', 'ASP', 16.4), ('CG', 'GLN', 'CG', 'ASP', 14.96), ('CG', 'GLN', 'OD1', 'ASP', 14.65), ('CG', 'GLN', 'OD2', 'ASP', 14.23)], [('CD', 'GLN', 'CB', 'ASP', 17.13), ('CD', 'GLN', 'CG', 'ASP', 15.68), ('CD', 'GLN', 'OD1', 'ASP', 15.25), ('CD', 'GLN', 'OD2', 'ASP', 15.05)], [('OE1', 'GLN', 'CB', 'ASP', 16.81), ('OE1', 'GLN', 'CG', 'ASP', 15.37), ('OE1', 'GLN', 'OD1', 'ASP', 14.88), ('OE1', 'GLN', 'OD2', 'ASP', 14.84)], [('NE2', 'GLN', 'CB', 'ASP', 18.23), ('NE2', 'GLN', 'CG', 'ASP', 16.75), ('NE2', 'GLN', 'OD1', 'ASP', 16.3), ('NE2', 'GLN', 'OD2', 'ASP', 16.13)], [('O', 'GLN', 'CB', 'ASP', 16.88), ('O', 'GLN', 'CG', 'ASP', 15.61), ('O', 'GLN', 'OD1', 'ASP', 15.63), ('O', 'GLN', 'OD2', 'ASP', 14.69)], [('C', 'GLN', 'CB', 'ASP', 16.07), ('C', 'GLN', 'CG', 'ASP', 14.75), ('C', 'GLN', 'OD1', 'ASP', 14.74), ('C', 'GLN', 'OD2', 'ASP', 13.83)], [('CA', 'GLN', 'CB', 'ASP', 14.95), ('CA', 'GLN', 'CG', 'ASP', 13.6), ('CA', 'GLN', 'OD1', 'ASP', 13.5), ('CA', 'GLN', 'OD2', 'ASP', 12.76)], [('N', 'GLN', 'CB', 'ASP', 13.88), ('N', 'GLN', 'CG', 'ASP', 12.51), ('N', 'GLN', 'OD1', 'ASP', 12.42), ('N', 'GLN', 'OD2', 'ASP', 11.63)]]}
MET_HIS = { 
	'distances':
		[[12.63, 11.5, 11.81, 10.19, 10.81, 9.73], [13.48, 12.46, 12.86, 11.18, 11.94, 10.84], [13.39, 12.4, 12.75, 11.22, 11.88, 10.89], [14.63, 13.52, 13.67, 12.37, 12.69, 11.82], [11.95, 11.04, 11.68, 9.7, 10.9, 9.63], [12.96, 11.97, 12.5, 10.62, 11.62, 10.4], [13.02, 11.88, 12.23, 10.54, 11.21, 10.09], [12.4, 11.18, 11.41, 9.86, 10.33, 9.27]],
	'comparisons':
		[[('CB', 'MET', 'CB', 'HIS', 12.63), ('CB', 'MET', 'CG', 'HIS', 11.5), ('CB', 'MET', 'ND1', 'HIS', 11.81), ('CB', 'MET', 'CD2', 'HIS', 10.19), ('CB', 'MET', 'CE1', 'HIS', 10.81), ('CB', 'MET', 'NE2', 'HIS', 9.73)], [('CG', 'MET', 'CB', 'HIS', 13.48), ('CG', 'MET', 'CG', 'HIS', 12.46), ('CG', 'MET', 'ND1', 'HIS', 12.86), ('CG', 'MET', 'CD2', 'HIS', 11.18), ('CG', 'MET', 'CE1', 'HIS', 11.94), ('CG', 'MET', 'NE2', 'HIS', 10.84)], [('SD', 'MET', 'CB', 'HIS', 13.39), ('SD', 'MET', 'CG', 'HIS', 12.4), ('SD', 'MET', 'ND1', 'HIS', 12.75), ('SD', 'MET', 'CD2', 'HIS', 11.22), ('SD', 'MET', 'CE1', 'HIS', 11.88), ('SD', 'MET', 'NE2', 'HIS', 10.89)], [('CE', 'MET', 'CB', 'HIS', 14.63), ('CE', 'MET', 'CG', 'HIS', 13.52), ('CE', 'MET', 'ND1', 'HIS', 13.67), ('CE', 'MET', 'CD2', 'HIS', 12.37), ('CE', 'MET', 'CE1', 'HIS', 12.69), ('CE', 'MET', 'NE2', 'HIS', 11.82)], [('O', 'MET', 'CB', 'HIS', 11.95), ('O', 'MET', 'CG', 'HIS', 11.04), ('O', 'MET', 'ND1', 'HIS', 11.68), ('O', 'MET', 'CD2', 'HIS', 9.7), ('O', 'MET', 'CE1', 'HIS', 10.9), ('O', 'MET', 'NE2', 'HIS', 9.63)], [('C', 'MET', 'CB', 'HIS', 12.96), ('C', 'MET', 'CG', 'HIS', 11.97), ('C', 'MET', 'ND1', 'HIS', 12.5), ('C', 'MET', 'CD2', 'HIS', 10.62), ('C', 'MET', 'CE1', 'HIS', 11.62), ('C', 'MET', 'NE2', 'HIS', 10.4)], [('CA', 'MET', 'CB', 'HIS', 13.02), ('CA', 'MET', 'CG', 'HIS', 11.88), ('CA', 'MET', 'ND1', 'HIS', 12.23), ('CA', 'MET', 'CD2', 'HIS', 10.54), ('CA', 'MET', 'CE1', 'HIS', 11.21), ('CA', 'MET', 'NE2', 'HIS', 10.09)], [('N', 'MET', 'CB', 'HIS', 12.4), ('N', 'MET', 'CG', 'HIS', 11.18), ('N', 'MET', 'ND1', 'HIS', 11.41), ('N', 'MET', 'CD2', 'HIS', 9.86), ('N', 'MET', 'CE1', 'HIS', 10.33), ('N', 'MET', 'NE2', 'HIS', 9.27)]]}
MET_ASP = { 
	'distances':
		[[16.34, 14.83, 14.18, 14.38], [17.16, 15.66, 14.92, 15.33], [16.63, 15.18, 14.36, 14.97], [17.53, 16.1, 15.35, 15.82], [16.41, 14.9, 14.29, 14.44], [17.25, 15.74, 15.13, 15.26], [17.0, 15.48, 14.92, 14.94], [16.34, 14.83, 14.38, 14.18]],
	'comparisons':
		[[('CB', 'MET', 'CB', 'ASP', 16.34), ('CB', 'MET', 'CG', 'ASP', 14.83), ('CB', 'MET', 'OD1', 'ASP', 14.18), ('CB', 'MET', 'OD2', 'ASP', 14.38)], [('CG', 'MET', 'CB', 'ASP', 17.16), ('CG', 'MET', 'CG', 'ASP', 15.66), ('CG', 'MET', 'OD1', 'ASP', 14.92), ('CG', 'MET', 'OD2', 'ASP', 15.33)], [('SD', 'MET', 'CB', 'ASP', 16.63), ('SD', 'MET', 'CG', 'ASP', 15.18), ('SD', 'MET', 'OD1', 'ASP', 14.36), ('SD', 'MET', 'OD2', 'ASP', 14.97)], [('CE', 'MET', 'CB', 'ASP', 17.53), ('CE', 'MET', 'CG', 'ASP', 16.1), ('CE', 'MET', 'OD1', 'ASP', 15.35), ('CE', 'MET', 'OD2', 'ASP', 15.82)], [('O', 'MET', 'CB', 'ASP', 16.41), ('O', 'MET', 'CG', 'ASP', 14.9), ('O', 'MET', 'OD1', 'ASP', 14.29), ('O', 'MET', 'OD2', 'ASP', 14.44)], [('C', 'MET', 'CB', 'ASP', 17.25), ('C', 'MET', 'CG', 'ASP', 15.74), ('C', 'MET', 'OD1', 'ASP', 15.13), ('C', 'MET', 'OD2', 'ASP', 15.26)], [('CA', 'MET', 'CB', 'ASP', 17.0), ('CA', 'MET', 'CG', 'ASP', 15.48), ('CA', 'MET', 'OD1', 'ASP', 14.92), ('CA', 'MET', 'OD2', 'ASP', 14.94)], [('N', 'MET', 'CB', 'ASP', 16.34), ('N', 'MET', 'CG', 'ASP', 14.83), ('N', 'MET', 'OD1', 'ASP', 14.38), ('N', 'MET', 'OD2', 'ASP', 14.18)]]}
SER_HIS = { 
	'distances':
		[[9.09, 7.64, 7.36, 6.64, 6.14, 5.53], [8.29, 6.82, 6.56, 5.79, 5.32, 4.63]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 9.09), ('CB', 'SER', 'CG', 'HIS', 7.64), ('CB', 'SER', 'ND1', 'HIS', 7.36), ('CB', 'SER', 'CD2', 'HIS', 6.64), ('CB', 'SER', 'CE1', 'HIS', 6.14), ('CB', 'SER', 'NE2', 'HIS', 5.53)], [('OG', 'SER', 'CB', 'HIS', 8.29), ('OG', 'SER', 'CG', 'HIS', 6.82), ('OG', 'SER', 'ND1', 'HIS', 6.56), ('OG', 'SER', 'CD2', 'HIS', 5.79), ('OG', 'SER', 'CE1', 'HIS', 5.32), ('OG', 'SER', 'NE2', 'HIS', 4.63)]]}
SER_ASP = { 
	'distances':
		[[12.36, 10.93, 10.84, 10.03], [11.44, 9.97, 9.75, 9.18]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 12.36), ('CB', 'SER', 'CG', 'ASP', 10.93), ('CB', 'SER', 'OD1', 'ASP', 10.84), ('CB', 'SER', 'OD2', 'ASP', 10.03)], [('OG', 'SER', 'CB', 'ASP', 11.44), ('OG', 'SER', 'CG', 'ASP', 9.97), ('OG', 'SER', 'OD1', 'ASP', 9.75), ('OG', 'SER', 'OD2', 'ASP', 9.18)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(MET_SER, d, 'P_1ei9_3_1_2_22')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLN_HIS, d, 'P_1ei9_3_1_2_22')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(MET_GLN, d, 'P_1ei9_3_1_2_22')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_HIS, d, 'P_1ei9_3_1_2_22')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(SER_GLN, d, 'P_1ei9_3_1_2_22')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLN_ASP, d, 'P_1ei9_3_1_2_22')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(MET_HIS, d, 'P_1ei9_3_1_2_22')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(MET_ASP, d, 'P_1ei9_3_1_2_22')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(SER_HIS, d, 'P_1ei9_3_1_2_22')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(SER_ASP, d, 'P_1ei9_3_1_2_22')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'MET_SER' :  match1,
		'GLN_HIS' :  match2,
		'MET_GLN' :  match3,
		'ASP_HIS' :  match4,
		'SER_GLN' :  match5,
		'GLN_ASP' :  match6,
		'MET_HIS' :  match7,
		'MET_ASP' :  match8,
		'SER_HIS' :  match9,
		'SER_ASP' :  match10}